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
    def __init__(self, name, sample, cacheDir=None):
        super(FakeEstimate, self).__init__(name, cacheDir=cacheDir)
        self.sample = sample
        self.dataMC = "Data" if sample.isData else "MC"
        self.magicNumber = 0.85
        muFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/muFR_all.root")
        elFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/elFR_all.root")
        self.muMap = getObjFromFile(muFile, "passed")
        self.elMap = getObjFromFile(elFile, "passed")
        
    def _estimate(self, region, channel, setup):

        ''' Concrete implementation of abstract method 'estimate' as defined in Systematic
        '''

        logger.debug( "MC prediction for %s channel %s" %(self.name, channel) )

        if channel.name == 'all':
            #if setup.nLeptons == 3: channels = trilepChannels
            #elif setup.nLeptons == 4: channels = quadlepChannels
            ## 'all' is the total of all contributions
            #return sum([self.cachedEstimate(region, c, setup) for c in channels])

        #else:

            # estimate fake contribution from events with exactly three loose leptons, and less than 3 tight leptons
            # take loose leptons with same pT requirements like analysis leptons
            
            tmpSample = self.sample
            
            variables = map( TreeVariable.fromString, ["Z_pt/F", "cosThetaStar/F", "weight/F", "met_pt/F", "Z_mass/F", "nJetSelected/I", "nBTag/I", 'Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I', 'nonZ_l2_index/I', 'reweightPU36fb/F', 'reweightBTagDeepCSV_SF/F' ] )
            variables += [VectorTreeVariable.fromString('lep[pt/F,ptCorr/F,eta/F,phi/F,FO_3l/I,tight_3l/I,FO_SS/I,tight_SS/I,jetPtRatiov2/F,pdgId/I]')]

            tmpSample.setSelectionString([setup.preselection(self.dataMC, nElectrons=channel.nE, nMuons=channel.nM)['cut'], region.cutString()])
            print tmpSample.selectionString
            reader = tmpSample.treeReader( variables = variables )
            reader.start()
            fakeYield = u_float(0)
            while reader.run():
                FR = 1.
                nLep = len([ l for l in reader.event.lep_pt if l > 0])
                lep = [getObjDict(reader.event, "lep"+'_', ["pt", "ptCorr", "eta", "phi", "FO_3l", "FO_SS", "tight_3l", "tight_SS", "pdgId","jetPtRatiov2"], i) for i in range(nLep) ]

                # get the relevant leptons
                lep = [ l for l in lep if l[setup.leptonId] ]
                
                # get tight and loose separately
                looseNotTight   = [ l for l in lep if not l[setup.tight_ID] ]
                tight           = [ l for l in lep if l[setup.tight_ID] ]
                nLooseNotTight  = len( looseNotTight )
                nTight          = len( tight )
                print nTight, nLooseNotTight
               
                if len(lep) > setup.nLeptons:
                    print "Doing gymastics"
                    # Do the combinatorics
                    looseCombinations = itertools.combinations(looseNotTight, setup.nLeptons - nTight)
                    allCombinations = [ (tight + list(x)) for x in looseCombinations ]
                    print allCombinations
                else:
                    allCombinations = lep

                for comb in allCombinations:
                    nLooseNotTight = 0
                    for l in lep:
                        if l[setup.tight_ID]:
                            continue
                        else:
                            if abs(l['pdgId']) == 11: FRmap = self.elMap
                            elif abs(l['pdgId']) == 13: FRmap = self.muMap
                            else: raise NotImplementedError
                            ptCorrected = l['ptCorr'] if l['ptCorr'] < 99 else 99.
                            FR_from_map = FRmap.GetBinContent(FRmap.FindBin(ptCorrected, abs(l['eta'])))
                            FR *= FR_from_map
                            nLooseNotTight += 1

                    FR *= (-1)**(nLooseNotTight+1)
                    allweights = [setup.sys['weight']] + setup.sys['reweight']
                    weights = [ getattr( reader.event, w ) for w in allweights ]
                    weight = reduce(mul, weights, 1)
                    fakeYield += ( reader.event.weight * FR * setup.lumi/1000. )

            #print fakeYield 
            #raise NotImplementedError
            return fakeYield

            #preSelection = setup.preselection('MC', channel=channel)
            #cut = "&&".join([region.cutString(setup.sys['selectionModifier']), preSelection['cut']])
            #weight = preSelection['weightStr']

            #logger.debug( "Using cut %s and weight %s"%(cut, weight) )
            #return setup.lumi[channel]/1000.*u_float(**self.sample[channel].getYieldFromDraw(selectionString = cut, weightString = weight) )

