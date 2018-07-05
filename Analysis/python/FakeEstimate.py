# Logging
import logging
import os
import itertools
logger = logging.getLogger(__name__)

from TopEFT.Analysis.Region import Region
from TopEFT.Tools.u_float import u_float
from TopEFT.Analysis.SystematicEstimator import SystematicEstimator
from TopEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TopEFT.Analysis.SetupHelpers import channel, trilepChannels, quadlepChannels

from operator import mul

from RootTools.core.standard import *
from TopEFT.Tools.helpers import getObjDict, getCollection, getObjFromFile

class FakeEstimate(SystematicEstimator):
    def __init__(self, name, sample, setup, cacheDir=None):
        super(FakeEstimate, self).__init__(name, cacheDir=cacheDir)
        self.sample = sample
        self.dataMC = "Data" if sample.isData else "MC"
        self.magicNumber = 0.85
        if sample.isData:
            if setup.year == 2017:
                muFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/fakerate_mu_data_2017.root")
                elFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/fakerate_el_data_2017.root")
            elif setup.year == 2016:
                muFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/fakerate_mu_data_2016.root")
                elFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/fakerate_el_data_2016.root")
            else:
                raise NotImplementedError
        else:
            if setup.year == 2017:
            # FR maps from ttbar MC
                muFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/muFR_all.root")
                elFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/elFR_all.root")
            elif setup.year == 2016:
                # this should be another root file
                muFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/muFR_all.root")
                elFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/elFR_all.root")
            else:
                raise NotImplementedError
        self.muMap = getObjFromFile(muFile, "passed")
        self.elMap = getObjFromFile(elFile, "passed")
        
    def _estimate(self, region, channel, setup):
        if not setup.nonprompt:
            raise (NotImplementedError, "Need a nonprompt setup")

        ''' Concrete implementation of abstract method 'estimate' as defined in Systematic
        '''

        logger.info( "Prediction for %s channel %s" %(self.name, channel) )

        if channel.name == 'all':
            # estimate fake contribution from events with at least three loose leptons, and less than 3 tight leptons
            # take loose leptons with same pT requirements like analysis leptons
            
            tmpSample = self.sample
            
            variables = map( TreeVariable.fromString, ["run/I", "lumi/I", "evt/I", "Z_pt/F", "cosThetaStar/F", "weight/F", "met_pt/F", "Z_mass/F", "nJetSelected/I", "nBTag/I", 'Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I', 'nonZ_l2_index/I', "nLeptons_FO_3l/I", "nLeptons_tight_3l/I", "nLeptons_tight_4l/I"])
            if not self.sample.isData:
                logger.info("Adding weights to be read.")
                variables += map( TreeVariable.fromString, ['reweightPU36fb/F', 'reweightBTagDeepCSV_SF/F' ] )
            variables += [VectorTreeVariable.fromString('lep[pt/F,ptCorr/F,eta/F,phi/F,FO_3l/I,tight_3l/I,FO_SS/I,tight_SS/I,jetPtRatiov2/F,pdgId/I]')]

            tmpSample.setSelectionString([setup.preselection(self.dataMC, nElectrons=channel.nE, nMuons=channel.nM)['cut'], region.cutString()])
            reader = tmpSample.treeReader(allBranchesActive=True, variables = variables )
            reader.start()
            fakeYield = u_float(0)
            
            nEvents =  u_float(tmpSample.getYieldFromDraw())
            logger.info("Runing over %s events.", nEvents.val)
            
            while reader.run():
                nLep = len([ l for l in reader.event.lep_pt if l > 0])
                lep = [getObjDict(reader.event, "lep"+'_', ["pt", "ptCorr", "eta", "phi", "FO_3l", "FO_SS", "tight_3l", "tight_SS", "pdgId","jetPtRatiov2"], i) for i in range(nLep) ]

                # get the relevant leptons
                lep = [ l for l in lep if l[setup.leptonId] ]
                
                # get tight and loose separately
                looseNotTight   = [ l for l in lep if not l[setup.tight_ID] ]
                tight           = [ l for l in lep if l[setup.tight_ID] ]
                nLooseNotTight  = len( looseNotTight )
                nTight          = len( tight )
                
                # Really get ALL possible combinations.
                allCombinations = itertools.combinations(tight+looseNotTight, setup.nLeptons)
                for comb in allCombinations:
                    FR = 1.
                    nLooseNotTight = 0
                    for l in comb:
                        if l[setup.tight_ID]:
                            continue
                        else:
                            if abs(l['pdgId']) == 11: FRmap = self.elMap
                            elif abs(l['pdgId']) == 13: FRmap = self.muMap
                            else: raise NotImplementedError
                            # we run out of stats in data at higher pt, hence we cut at a lower value
                            ptCut = 45. if self.sample.isData else 99.
                            ptCorrected = l['ptCorr'] if l['ptCorr'] < ptCut else (ptCut-1)
                            FR_from_map = FRmap.GetBinContent(FRmap.FindBin(ptCorrected, abs(l['eta'])))
                            if self.sample.isData:
                                FR *= FR_from_map/(1-FR_from_map)
                            else:
                                FR *= FR_from_map
                            nLooseNotTight += 1

                    FR *= (-1)**(nLooseNotTight+1)

                    allweights = [setup.sys['weight']] + setup.sys['reweight']

                    if self.sample.isData:
                        weight = 1
                    else:
                        weights = [ getattr( reader.event, w ) for w in allweights ]
                        weight = reduce(mul, weights, 1)

                    fakeYield += ( weight * FR )
            # apply the statistical uncertainty to the result
            result = u_float(0.) if nEvents.val==0 else u_float(fakeYield, (nEvents.sigma/nEvents.val)*fakeYield )
            return result if self.sample.isData else (result * setup.lumi/1000.) 

