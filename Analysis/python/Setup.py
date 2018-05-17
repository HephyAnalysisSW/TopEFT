'''
Setup for 2l/3l/4l ttV selections.
Can use different lepton IDs, cuts etc for different channels.
Still missing:
- most of the 2l channel cuts/selections
- additional cuts for 4l channel (dl mass etc)
'''

#Standard import
import copy

# RootTools
from RootTools.core.standard import *

# Logging
import logging
logger = logging.getLogger(__name__)

#user specific
from TopEFT.Tools.user import analysis_results
from TopEFT.Tools.helpers import getObjFromFile

##define samples
# 2016
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
# 2017
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *


from TopEFT.Analysis.SystematicEstimator import jmeVariations, metVariations
from TopEFT.Analysis.SetupHelpers import getZCut, channel, trilepChannels, quadlepChannels
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.triggerSelector import triggerSelector
from TopEFT.Analysis.regions import *

#to run on data
dataLumi2016        = Run2016.lumi
dataLumi2017        = 41290
dataLumi201617      = dataLumi2016 + dataLumi2017
dataLumi20161718    = 150000
dataHighLumi        = 3e6

#10/fb to run on MC
#lumi = {c:10000 for c in channels}
#lumi = dataLumi201678
lumi = dataLumi2016

#Define defaults here
zMassRange          = 10
default_mllMin      = 0
default_zWindow1    = "onZ"
default_zWindow2    = "offZ"
default_nJets       = (3, -1)   # written as (min, max)
default_nBTags      = (1, -1)
default_metMin      = 0


#default_sys = {'weight':'weight', 'reweight':['reweightPU36fb', 'reweightBTagDeepCSV_SF', 'reweightTrigger', 'reweightLeptonTrackingSF'], 'selectionModifier':None}
default_parameters   = {
            'mllMin':        default_mllMin,
            'metMin':        default_metMin,
            'zWindow1':      default_zWindow1,
            'zWindow2':      default_zWindow2,
            'zMassRange':    zMassRange,
            'nJets':         default_nJets,
            'nBTags':        default_nBTags,
        }

class Setup:
    def __init__(self, year=2017, nLeptons=3, nonprompt=False):
        self.name       = "defaultSetup"
        self.channels   = [channel(-1,-1)]
        self.resultsFile= 'calculatedLimits_%s.db'%self.name
        self.year       = year
        self.nLeptons   = nLeptons
        
        if nLeptons == 2:
            self.tight_ID    = "tight_SS"
            self.FO_ID       = "FO_SS"
        elif nLeptons == 3:
            self.tight_ID    = "tight_3l"
            self.FO_ID       = "FO_3l"
        elif nLeptons == 4:
            self.tight_ID    = "tight_4l"
            self.FO_ID       = "FO_4l"
        else:
            raise NotImplementedError("Can't handle 0,1,5,.. lepton cases")

        self.nonprompt  = nonprompt
        self.leptonId = self.FO_ID if self.nonprompt else self.tight_ID

        self.default_sys = {'weight':'weight', 'reweight':['reweightPU36fb', 'reweightBTagDeepCSV_SF'], 'selectionModifier':None} # 'reweightTrigger_%s'%self.leptonId, 'reweightLeptonTrackingSF_%s'%self.leptonId

        self.resultsColumns     = ['signal', 'exp', 'obs', 'exp1up', 'exp1down', 'exp2up', 'exp2down', 'NLL_prefit', 'dNLL_postfit_r1', 'dNLL_bestfit']
        self.uncertaintyColumns = ["region", "channel", "PDFset"]

        self.analysis_results = analysis_results
        self.prefixes         = []
        self.externalCuts     = []

        #Default cuts and requirements. Those three things below are used to determine the key in the cache!
        self.parameters   = copy.deepcopy(default_parameters)
        self.sys          = self.default_sys 
        if year == 2017:
            self.lumi         = dataLumi2017
            self.dataLumi     = dataLumi2017
        elif year == 2016:
            self.lumi         = dataLumi2016
            self.dataLumi     = dataLumi2016
        elif year == 20167:
            self.lumi         = dataLumi201617
            self.dataLumi     = dataLumi201617
        elif year == "run2":
            self.lumi         = dataLumi20161718
            self.dataLumi     = dataLumi20161718
        elif year == "HLLHC":
            self.lumi         = dataHighLumi
            self.dataLumi     = dataHighLumi

        self.genSelection = "Sum$(GenJet_pt>30)>=3&& abs(Z_mass-91.2)<10&&(abs(Z_daughterPdg)==11 || abs(Z_daughterPdg)==13 || abs(Z_daughterPdg)==15 )"

        # Data
        if year == 2017:
            data = Run2017
        else:
            data = Run2016

        # MC
        if year == 2017:
            TTZSample           = TTZtoLLNuNu_17
            WZSample            = WZ_amcatnlo_17 # no powheg yet
            TTXSample           = TTX_17
            TTWSample           = TTW_17
            TZQSample           = TZQ_17
            ZZSample            = ZZ
            rareSample          = rare_17
            rare_noZZSample     = rare_noZZ
            nonpromptSample     = nonpromptMC_17
            pseudoDataSample    = pseudoData_17
            ttbarSample         = TTLep_pow_17
        else:
            ## use 2016 samples as default (we do combine on card file level)
            TTZSample           = TTZtoLLNuNu
            WZSample            = WZ_powheg # might update to powheg?
            TTXSample           = TTX
            TTWSample           = TTW
            TZQSample           = TZQ
            ZZSample            = ZZ
            rareSample          = rare
            rare_noZZSample     = rare_noZZ
            nonpromptSample     = nonpromptMC
            pseudoDataSample    = pseudoData
            ttbarSample         = TTLep_pow


        # removed the channel dependence.
        self.samples = {
            'TTZ':          TTZSample,
            'WZ' :          WZSample,
            'TTX' :         TTXSample,
            'TTW' :         TTWSample,
            'TZQ' :         TZQSample,
            'rare':         rareSample,
            'ZZ':           ZZSample,
            'rare_noZZ':    rare_noZZSample,
            'nonprompt':    nonpromptSample,
            'ttbar':        ttbarSample,
            'pseudoData':   pseudoDataSample,
            'Data' :        data,
            }
        
    def prefix(self):
        return '_'.join(self.prefixes+[self.preselection('MC')['prefix']])

    def defaultCacheDir(self):
        return os.path.join(self.analysis_results, self.prefix(), 'cacheFiles')

    #Clone the setup and optinally modify the systematic variation
    def defaultClone(self):
        '''Clone setup and change systematics to default'''

        res            = copy.copy(self)
        res.sys        = copy.deepcopy(self.default_sys)
        res.parameters = copy.deepcopy(default_parameters)

        return res

    #Clone the setup and optinally modify the systematic variation
    def systematicClone(self, sys=None, parameters=None):
        '''Clone setup and change systematic if provided'''

        res            = copy.copy(self)
        res.sys        = copy.deepcopy(self.sys)
        res.parameters = copy.deepcopy(self.parameters)

        if sys:
            for k in sys.keys():
                if k=='remove':
                    for i in sys[k]:
                      res.sys['reweight'].remove(i)
                elif k=='reweight':
                    res.sys[k] = list(set(res.sys[k]+sys[k])) #Add with unique elements
                    for upOrDown in ['Up','Down']:
                      if 'reweightPU36fb'+upOrDown                              in res.sys[k]: res.sys[k].remove('reweightPU36fb')
                      if 'reweightTrigger_%s'%self.leptonId+upOrDown            in res.sys[k]: res.sys[k].remove('reweightTrigger_%s'%self.leptonId)
                      if 'reweightBTagDeepCSV_SF_b_'+upOrDown                   in res.sys[k]: res.sys[k].remove('reweightBTagDeepCSV_SF')
                      if 'reweightBTagDeepCSV_SF_l_'+upOrDown                   in res.sys[k]: res.sys[k].remove('reweightBTagDeepCSV_SF')
                      if 'reweightLeptonTrackingSF_%s'%self.leptonId+upOrDown   in res.sys[k]: res.sys[k].remove('reweightLeptonTrackingSF_%s'%self.leptonId)
                      if 'reweightLeptonSF_%s'%self.leptonId+upOrDown           in res.sys[k]: res.sys[k].remove('reweightLeptonSF_%s'%self.leptonId)
                else:
                    res.sys[k] = sys[k] # if sys[k] else res.sys[k]

        if parameters:
            for k in parameters.keys():
                res.parameters[k] = parameters[k]


        return res

    def defaultParameters(self, update={}):
        assert type(update)==type({}), "Update arguments with key arg dictionary. Got this: %r"%update
        res = copy.deepcopy(self.parameters)
        res.update(update)
        return res

    def weightString(self):
        return "*".join([self.sys['weight']] + (self.sys['reweight'] if self.sys['reweight'] else []))

    def preselection(self, dataMC , nElectrons=-1, nMuons=-1, isFastSim = False, short=False):
        '''Get preselection  cutstring.'''
        return self.selection(dataMC, nElectrons=nElectrons, nMuons=nMuons, isFastSim = isFastSim, short=short, hadronicSelection = False, **self.parameters)

    def selection(self, dataMC,
                        mllMin, metMin, zWindow1, zWindow2, zMassRange,
                        nJets, nBTags,
                        nElectrons=-1, nMuons=-1,
                        hadronicSelection = False,  isFastSim = False, short=False):
        '''Define full selection
           dataMC: 'Data' or 'MC'
           nElectrons, nMuons: Number of E and M. -1: all
           zWindow: offZ, onZ, or allZ
           hadronicSelection: whether to return only the hadronic selection
           isFastSim: adjust filter cut etc. for fastsim
        '''
        
        nLeptons = self.nLeptons
        # Get the right channel and do sanity checks
        if nElectrons < 0 and nMuons < 0:
            # this should be the new "all" case. Just 
            pass
        else:
            if nElectrons + nMuons != nLeptons: raise NotImplementedError("Electrons and Muons don't add up!")

        #Consistency checks
        if self.sys['selectionModifier']:
          assert self.sys['selectionModifier'] in jmeVariations+metVariations+['genMet'], "Don't know about systematic variation %r, take one of %s"%(self.sys['selectionModifier'], ",".join(jmeVariations + ['genMet']))
        assert dataMC in ['Data','MC'],                                                   "dataMC = Data or MC, got %r."%dataMC

        #Postfix for variables (only for MC and if we have a jme variation)
        sysStr = ""
        metStr = ""
        if dataMC == "MC" and self.sys['selectionModifier'] in jmeVariations: sysStr = "_" + self.sys['selectionModifier']
        if dataMC == "MC" and self.sys['selectionModifier'] in metVariations: metStr = "_" + self.sys['selectionModifier']

        res={'cuts':[], 'prefixes':[]}

        if nJets and not (nJets[0]==0 and nJets[1]<0):
            assert nJets[0]>=0 and (nJets[1]>=nJets[0] or nJets[1]<0), "Not a good nJets selection: %r"%nJets
            njetsstr = "nJetSelected"+sysStr+">="+str(nJets[0])
            prefix   = "nJets"+str(nJets[0])
            if nJets[1]>=0:
                njetsstr+= "&&"+"nJetSelected"+sysStr+"<="+str(nJets[1])
                if nJets[1]!=nJets[0]: prefix+=str(nJets[1])
            else:
                prefix+='p'
            res['cuts'].append(njetsstr)
            res['prefixes'].append(prefix)

        if nBTags and not (nBTags[0]==0 and nBTags[1]<0):
            assert nBTags[0]>=0 and (nBTags[1]>=nBTags[0] or nBTags[1]<0), "Not a good nBTags selection: %r"% nBTags
            nbtstr = "nBTag"+sysStr+">="+str(nBTags[0])
            prefix = "nbtag"+str(nBTags[0])
            if nBTags[1]>=0:
                nbtstr+= "&&nBTag"+sysStr+"<="+str(nBTags[1])
                if nBTags[1]!=nBTags[0]: prefix+=str(nBTags[1])
            else:
                prefix+='p'
            res['cuts'].append(nbtstr)
            res['prefixes'].append(prefix)

        if metMin and metMin>0:
          res['cuts'].append('met_pt'+sysStr+metStr+'>='+str(metMin))
          res['prefixes'].append('met'+str(metMin))

        if not hadronicSelection:
            if mllMin and mllMin>0:
              res['cuts'].append('Z_mass>='+str(mllMin))
              res['prefixes'].append('mll'+str(mllMin))

            if nMuons >= 0 and nElectrons >= 0:
                chStr = "(nMuons_%s==%i&&nElectrons_%s==%i)"%(self.leptonId, nMuons, self.leptonId, nElectrons)
            else:
                # this is for the 'all' channel
                if not self.nonprompt:
                    chStr = "nLeptons_%s==%i"%(self.leptonId, nLeptons)
                else:
                    chStr = "nLeptons_%s>=%i"%(self.leptonId, nLeptons)

            #Z window

            # two different cases: Z_mass for 3l, Z1_mass_4l and Z2_mass_4l for 4l
            if nLeptons == 3:
                res['cuts'].append(getZCut(zWindow1, "Z_mass", zMassRange))
                if not self.nonprompt: res['cuts'].append("Z_fromTight>0")
            elif nLeptons == 4:
                res['cuts'].append(getZCut(zWindow1, "Z1_mass_4l", zMassRange))
                if nMuons%2 == 0:
                    logger.info("Z window 2 off Z, nMuons %s", nMuons)
                    res['cuts'].append(getZCut("offZ", "Z2_mass_4l", zMassRange))
                else:
                    logger.info("Z window 2 all Z, nMuons %s", nMuons)
                    res['cuts'].append(getZCut("allZ", "Z2_mass_4l", zMassRange))
            # no Z-mass cut for 2l case

            res['cuts'].append(chStr)

            if not self.nonprompt:
                res['cuts'].append('nLeptons_%s==%i'%(self.leptonId, nLeptons))
            else:
                res['cuts'].append('nLeptons_%s>=%i'%(self.leptonId, nLeptons))

            if nLeptons==2:
                raise NotImplementedError("Not yet thought about SS selection")
            elif nLeptons==3:
                lep_pt = "(lep_%s*(lep_pt - lep_ptCorr) + lep_ptCorr)"%self.tight_ID
                leptonSelection = [\
                    "Sum$(%s>40&&lep_%s>0)>0"%(lep_pt, self.leptonId),\
                    "Sum$(%s>20&&lep_%s>0)>1"%(lep_pt, self.leptonId),\
                    "Sum$(%s>10&&lep_%s>0)>2"%(lep_pt, self.leptonId),\
                                  ]
                res['cuts'].append("&&".join(leptonSelection))
                res['cuts'].append("!(nLeptons_tight_4l>=4)") # make sure to remove full overlap with 4l. This is enought, what is below shouldn't be necessary.
                if self.nonprompt: res['cuts'].append("nLeptons_tight_3l<3")
                ## need to veto 4l events to remove overlap
                #baseline4l = Setup(self.year, nLeptons=4)
                #baseline4l.parameters.update({'nJets':(2,-1), 'nBTags':(0,-1), 'zMassRange':20})
                #for c in quadlepChannels:
                #    res['cuts'].append("!(%s)"%baseline4l.preselection(dataMC, nElectrons=c.nE, nMuons=c.nM, short=True)['cut'])
            elif nLeptons==4:
                res['cuts'].append("Sum$(lep_pt>40&&lep_%s>0)>0 && Sum$(lep_pt>10&&lep_%s>0)>3"%(self.leptonId, self.leptonId)) #check if this is good enough
                res['cuts'].append("min_dl_mass>12&&totalLeptonCharge==0")
            else:
                raise NotImplementedError("nLeptons has to be 2 or 3 or 4. That's already more than enough to think about.")

        # Need a better solution for the Setups for different eras
        if self.year == 20167: self.year = 2016 #FIXME since we use 2016 MC for now
        if not short: res['cuts'].append(getFilterCut(isData=(dataMC=='Data'), isFastSim=isFastSim, year = self.year))
        # apply triggers in MC
        if not dataMC == 'Data':
            tr = triggerSelector(self.year)
            if not short: res['cuts'].append(tr.getSelection("MC"))
        res['cuts'].extend(self.externalCuts)
        
        return {'cut':"&&".join(res['cuts']), 'prefix':'-'.join(res['prefixes']), 'weightStr': ( self.weightString() if dataMC == 'MC' else 'weight')}
