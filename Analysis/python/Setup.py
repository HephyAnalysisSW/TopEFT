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
from TopEFT.Analysis.SetupHelpers import getZCut, channels, allChannels
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Analysis.regions import *

#to run on data
dataLumi2016 = {'3mu':Run2016.lumi, '3e':Run2016.lumi, '2mu1e':Run2016.lumi, '2e1mu':Run2016.lumi}
lumi1617 = Run2016.lumi + 41290
dataLumi20167 = {'3mu':lumi1617, '3e':lumi1617, '2mu1e':lumi1617, '2e1mu':lumi1617}
dataLumi2017 = {'3mu':41290, '3e':41290, '2mu1e':41290, '2e1mu':41290}
dataLumi201678 = {'3mu':150000, '3e':150000, '2mu1e':150000, '2e1mu':150000}

dataHighLumi = {'3mu':3e6, '3e':3e6, '2mu1e':3e6, '2e1mu':3e6}

#10/fb to run on MC
#lumi = {c:10000 for c in channels}
#lumi = dataLumi201678
lumi = dataLumi2016

#Define defaults here
zMassRange          = 10
default_mllMin      = 0
default_zWindow     = "onZ"
default_nJets       = (3, -1)   # written as (min, max)
default_nBTags      = (1, -1)
default_metMin      = 0


default_sys = {'weight':'weight', 'reweight':['reweightPU36fb', 'reweightBTagDeepCSV_SF', 'reweightTrigger', 'reweightLeptonTrackingSF'], 'selectionModifier':None}
default_parameters   = {
            'mllMin':        default_mllMin,
            'metMin':        default_metMin,
            'zWindow':       default_zWindow,
            'nJets':         default_nJets,
            'nBTags':        default_nBTags,
        }

class Setup:
    def __init__(self, year=2017):
        self.name       = "defaultSetup"
        self.channels   = ["all"]
        self.regions    = regionsE
        self.resultsFile= 'calculatedLimits_%s.db'%self.name
        self.year       = year

        self.resultsColumns     = ['signal', 'exp', 'obs', 'exp1up', 'exp1down', 'exp2up', 'exp2down', 'NLL_prefit', 'dNLL_postfit_r1', 'dNLL_bestfit']
        self.uncertaintyColumns = ["region", "channel", "PDFset"]

        self.analysis_results = analysis_results
        self.zMassRange       = zMassRange
        self.prefixes         = []
        self.externalCuts     = []

        #Default cuts and requirements. Those three things below are used to determine the key in the cache!
        self.parameters   = default_parameters 
        self.sys          = default_sys 
        if year == 2017:
            self.lumi         = dataLumi2017
            self.dataLumi     = dataLumi2017
        elif year == 2016:
            self.lumi         = dataLumi2016
            self.dataLumi     = dataLumi2016
        elif year == 20167:
            self.lumi         = dataLumi20167
            self.dataLumi     = dataLumi20167
        elif year == "run2":
            self.lumi         = dataLumi201678
            self.dataLumi     = dataLumi201678
        elif year == "HLLHC":
            self.lumi         = dataHighLumi
            self.dataLumi     = dataHighLumi

        self.genSelection = "Sum$(GenJet_pt>30)>=3&& abs(Z_mass-91.2)<10&&(abs(Z_daughterPdg)==11 || abs(Z_daughterPdg)==13 || abs(Z_daughterPdg)==15 )"

        # defining seperate samples. should not be necessary, but just for the sake of sanity. Add switch for eras
        if year == 2017:
            MMM = Run2017
            EEE = Run2017
            MME = Run2017
            EEM = Run2017
        else:
            ## use 2016 samples as default (we do combine on card file level)
            MMM = Run2016
            EEE = Run2016 
            MME = Run2016
            EEM = Run2016

        # MC
        if year == 2017:
            TTZSample           = TTZtoLLNuNu_17
            WZSample            = WZ_amcatnlo_17 # no powheg yet
            TTXSample           = TTX_17
            TTWSample           = TTW_17
            TZQSample           = TZQ_17
            rareSample          = rare_17
            nonpromptSample     = nonprompt_17
            pseudoDataSample    = pseudoData_17
        else:
            ## use 2016 samples as default (we do combine on card file level)
            TTZSample           = TTZtoLLNuNu
            WZSample            = WZ_powheg # might update to powheg?
            TTXSample           = TTX
            TTWSample           = TTW
            TZQSample           = TZQ
            rareSample          = rare
            nonpromptSample     = nonprompt
            pseudoDataSample    = pseudoData


        self.samples = {
        'TTZ':          {c:TTZSample        for c in channels},
        'WZ' :          {c:WZSample         for c in channels},
        'TTX' :         {c:TTXSample        for c in channels},
        'TTW' :         {c:TTWSample        for c in channels},
        'TZQ' :         {c:TZQSample        for c in channels},
        'rare':         {c:rareSample       for c in channels},
        'nonprompt':    {c:nonpromptSample  for c in channels},
        'pseudoData':   {c:pseudoDataSample for c in channels},
        'Data'   :    {'3mu':   MMM,
                       '3e':    EEE,
                       '2mu1e': MME,
                       '2e1mu': EEM},
        }
        
    def prefix(self):
        return '_'.join(self.prefixes+[self.preselection('MC')['prefix']])

    def defaultCacheDir(self):
        return os.path.join(self.analysis_results, self.prefix(), 'cacheFiles')

    #Clone the setup and optinally modify the systematic variation
    def defaultClone(self):
        '''Clone setup and change systematics to default'''

        res            = copy.copy(self)
        res.sys        = copy.deepcopy(default_sys)
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
                      if 'reweightPU36fb'+upOrDown                  in res.sys[k]: res.sys[k].remove('reweightPU36fb')
                      if 'reweightTrigger'+upOrDown                 in res.sys[k]: res.sys[k].remove('reweightTrigger')
                      if 'reweightBTagDeepCSV_SF_b_'+upOrDown       in res.sys[k]: res.sys[k].remove('reweightBTagDeepCSV_SF')
                      if 'reweightBTagDeepCSV_SF_l_'+upOrDown       in res.sys[k]: res.sys[k].remove('reweightBTagDeepCSV_SF')
                      if 'reweightLeptonTrackingSF'+upOrDown        in res.sys[k]: res.sys[k].remove('reweightLeptonTrackingSF')
                      if 'reweightLeptonSF'+upOrDown                in res.sys[k]: res.sys[k].remove('reweightLeptonSF')
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

    def preselection(self, dataMC , channel='all', isFastSim = False):
        '''Get preselection  cutstring.'''
        return self.selection(dataMC, channel = channel, isFastSim = isFastSim, hadronicSelection = False, **self.parameters)

    def selection(self, dataMC,
                        mllMin, metMin, zWindow,
                        nJets, nBTags,
                        channel = 'all', hadronicSelection = False,  isFastSim = False):
        '''Define full selection
           dataMC: 'Data' or 'MC'
           channel: all, EE, MuMu or EMu
           zWindow: offZ, onZ, or allZ
           hadronicSelection: whether to return only the hadronic selection
           isFastSim: adjust filter cut etc. for fastsim
        '''
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

            presel_2l     = "(nGoodLeptons>=2)"  
            presel3mu     = "(nGoodMuons==3&&nGoodElectrons==0)"
            presel2mu1e   = "(nGoodMuons==2&&nGoodElectrons==1)"
            presel2e1mu   = "(nGoodMuons==1&&nGoodElectrons==2)"
            presel3e      = "(nGoodMuons==0&&nGoodElectrons==3)"
            allPresels    = [presel3mu,presel2mu1e,presel2e1mu,presel3e]

            #Z window
            assert zWindow in ['offZ', 'onZ', 'allZ'], "zWindow must be one of onZ, offZ, allZ. Got %r"%zWindow
            if zWindow == 'onZ':                     res['cuts'].append(getZCut(zWindow, self.zMassRange))
            if zWindow == 'offZ' and channel!="EMu": res['cuts'].append(getZCut(zWindow, self.zMassRange))  # Never use offZ when in emu channel, use allZ instead

            #lepton channel
            assert channel in allChannels+["2l_incl"], "channel must be one of "+",".join(allChannels)+". Got %r."%channel

            if channel=="3mu":        chStr = presel3mu
            elif channel=="2mu1e":    chStr = presel2mu1e
            elif channel=="2e1mu":    chStr = presel2e1mu
            elif channel=="3e":       chStr = presel3e
            elif channel=="2l_incl":  chStr = presel_2l
            elif channel=="all":      chStr = "("+'||'.join(allPresels)+')'

            res['cuts'].append(chStr)

            if channel is not "2l_incl":
                res['cuts'].append('nlep==3')

                res['cuts'].append("lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10")


        # Need a better solution for the Setups for different eras
        if self.year == 20167: self.year = 2016 #FIXME since we use 2016 MC for now
        res['cuts'].append(getFilterCut(isData=(dataMC=='Data'), isFastSim=isFastSim, year = self.year))
        res['cuts'].extend(self.externalCuts)
        
        return {'cut':"&&".join(res['cuts']), 'prefix':'-'.join(res['prefixes']), 'weightStr': ( self.weightString() if dataMC == 'MC' else 'weight')}
