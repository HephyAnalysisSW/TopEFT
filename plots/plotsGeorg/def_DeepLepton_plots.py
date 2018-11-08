# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *
from TopEFT.Tools.user import trainingFiles_directory as base_directory

####################################
### definitions for plot scripts ###
####################################

#arg parser
def get_parser():
    ''' Argument parser for DeepLepton plot scripts.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for DeepLepton plot scripts")

    argParser.add_argument('--version',         action='store', type=str, choices=['v1', 'v2', 'v3', 'v3_small'],      required = True, help="Version for output directory")
    argParser.add_argument('--year',            action='store', type=int, choices=[2016,2017],                         required = True, help="Which year?")
    argParser.add_argument('--flavour',         action='store', type=str, choices=['ele','muo'],                       required = True, help="Which Flavour?")
    argParser.add_argument('--trainingDate',    action='store', type=int, default=0,                                                    help="Which Training Date? 0 for no Training Date.")
    argParser.add_argument('--isTestData',      action='store', type=int, choices=[0,1,99],                            required = True, help="0 for testdata, 1 for traindata, 99 for selective list of trainfiles specified in trainfiles")
    argParser.add_argument('--ptSelection',     action='store', type=str, choices=['pt_10_to_inf','pt_15_to_inf'],     required = True, help="Which pt selection?")
    argParser.add_argument('--sampleSelection', action='store', type=str, choices=['DYvsQCD_sorted', 'DYvsQCD_sorted_looseId', 'TTJets_sorted'], required = True, help="Which sample selection?")
    argParser.add_argument('--trainingType',    action='store', type=str, choices=['std','iso'],                       required = True, help="Standard or Isolation Training?")
    argParser.add_argument('--sampleSize',      action='store', type=str, choices=['small','medium','large','full'],   required = True, help="small sample or full sample?")

    argParser.add_argument('--binned',          action='store', type=str, choices=['pt','eta','nTrueInt'], default='pt',                 help="Which variable for binning?")
    argParser.add_argument('--eBbins',          action='store', type=int, choices=[1,5,10,25,50], default=50,                            help="Calculate eB for how many bins?")

    argParser.add_argument('--predictionPath',  action='store', type=str, default='',                                                   help="if isTestData 99, path to prediction files?")
    argParser.add_argument('--testDataPath',    action='store', type=str, default='',                                                   help="if isTestData 99, path to test files?")

    #argParser.add_argument('--nJobs',        action='store', type=int,    nargs='?',         default=1,                   help="Maximum number of simultaneous jobs.")
    #argParser.add_argument('--job',          action='store', type=int,                       default=0,                   help="Run only job i")

    return argParser


#preselection:
def lep_preselection(leptonFlavour):
    if leptonFlavour == 'muo':
        loose_id = "abs(lep_pdgId)==13&&lep_pt>5&&abs(lep_eta)<2.4&&lep_miniRelIso<0.4&&lep_sip3d<8&&abs(lep_dxy)<0.05&&abs(lep_dz)<0.1&&lep_pfMuonId&&lep_mediumMuonId"
    else:
        loose_id = ""
    return loose_id


#get samples for plots and add prediction branches as friend tree
def plot_samples(version, year, leptonFlavour, trainingDate, isTestData, ptSelection, sampleSelection, sampleSize, predictionPath, testDataPath):

    #define paths and names
    #base_directory = trainingsFiles_directory
    file_directory = testDataPath if (isTestData==99 and testDataPath!='') else os.path.join(base_directory, version, str(year), leptonFlavour, ptSelection, sampleSelection)
    sample_texName = ('electrons_' if leptonFlavour=='ele' else 'muons_')+ptSelection+'_'+sampleSelection
    texfileName    = ('' if sampleSize=='full' else sampleSize+'_')+('test_' if isTestData else 'train_')+leptonFlavour+'_std.txt' 
    texfilePath    = os.path.join(file_directory, texfileName)
    
    if sampleSize == 'full':
        sizePattern = '_'
    elif sampleSize =='small':
        sizePattern = '_Small'
    elif sampleSize =='medium':
        sizePattern = '_Medium'
    elif sampleSize =='large':
        sizePattern = '_Large'
        
    predict_directory = predictionPath if isTestData==99 else os.path.join('/afs/hephy.at/data/gmoertl01/DeepLepton/trainings', 'electrons' if leptonFlavour=='ele' else 'muons', str(trainingDate), sampleSelection+sizePattern+('Electron' if leptonFlavour=='ele' else 'Muon')+'Evaluation'+('TestData' if isTestData else 'TestDataIsTrainData'))

    #create FileList
    if trainingDate==0:
        with open(texfilePath,'r') as f:
            FileList = f.read().splitlines()
    else:
        FileList = os.listdir(predict_directory)
        if 'tree_association.txt' in FileList:
            FileList.remove('tree_association.txt')
        FileList = [filepath.replace('_predict.root', '.root') for filepath in FileList]

    #limit length of FileList, to save time for plot processing
    #if len(FileList)>50:
    #    del FileList[50:]

    FileList = [filepath.replace(filepath, os.path.join(file_directory, filepath)) for filepath in FileList]
    sample   = Sample.fromFiles( leptonFlavour, texName = sample_texName, files =FileList, treeName="tree")

    if not trainingDate==0:
        FilePredictList = os.listdir(predict_directory)
        if 'tree_association.txt' in FilePredictList:
            FilePredictList.remove('tree_association.txt')

        FilePredictList = [filepath.replace(filepath, os.path.join(predict_directory, filepath)) for filepath in FilePredictList]

        samplePredict = Sample.fromFiles( leptonFlavour+"_friend", texName = sample_texName+"_predict", files = FilePredictList, treeName="tree")
        sample.addFriend(samplePredict, "tree")

    samples={"leptonFlavour":leptonFlavour, "sample":sample, "trainingDate":trainingDate, "isTestData":isTestData}
    
    return samples

#variables for histogram plots
def histo_plot_variables(trainingDate, version):

    variables = [
    "run/I",
    "lumi/I",
    "evt/l",
    "lep_trackerHits/I",
    #Training Variables
    "lep_pt/F",
    "lep_eta/F",
    "lep_phi/F",
    "lep_rho/F",                   
    "lep_innerTrackChi2/F",
    
    "lep_relIso03/F",             
    "lep_relIso04/F",             
    "lep_miniRelIso/F",             
    "lep_chargedHadRelIso03/F",
    "lep_chargedHadRelIso04/F",
    "lep_miniRelIsoNeutral/F",
    "lep_miniRelIsoCharged/F",

    "lep_lostHits/I", #lost inner hits
    "lep_innerTrackValidHitFraction/F",         
    "lep_trackerLayers/I", 
    "lep_pixelLayers/I", 
    "lep_trackerHits/I", 
    "lep_lostOuterHits/I",
    "lep_jetBTagCSV/F", 
    "lep_jetBTagDeepCSV/F", 
    "lep_jetBTagDeepCSVCvsB/F", 
    "lep_jetBTagDeepCSVCvsL/F",

    "lep_jetDR/F",                 
    "lep_dxy/F",                   
    "lep_dz/F",                    
    "lep_edxy/F",                   
    "lep_edz/F",                    
    "lep_ip3d/F",
    "lep_sip3d/F",
    #"lep_dxy_pf/F",                   
    #"lep_dz_pf/F",                    
    #"lep_dzAssociatedPV/F",
    #"lep_hcalFraction/F",
    #"lep_puppiWeight/F",
    "lep_EffectiveArea03/F",
    "lep_jetPtRatiov1/F",
    "lep_jetPtRatiov2/F",
    "lep_jetPtRelv1/F",
    "lep_jetPtRelv2/F",
    "lep_ptErrTk/F",

    "npfCand_neutral/I",
    "npfCand_charged/I",
    "npfCand_photon/I",
    "npfCand_electron/I",
    "npfCand_muon/I",

    "pfCand_neutral[pt_ptRelSorted/F]",
    "pfCand_charged[pt_ptRelSorted/F]",
    "pfCand_photon[pt_ptRelSorted/F]",
    "pfCand_electron[pt_ptRelSorted/F]",
    "pfCand_muon[pt_ptRelSorted/F]",

    #Electron specific
    "lep_etaSc/F",                
    "lep_sigmaIEtaIEta/F",
    "lep_full5x5_sigmaIetaIeta/F",
    "lep_dEtaInSeed/F",           
    "lep_dPhiScTrkIn/F",
    "lep_dEtaScTrkIn/F",
    "lep_eInvMinusPInv/F",        
    "lep_convVeto/I",              
    "lep_hadronicOverEm/F",        
    "lep_r9/F",
    "lep_mvaIdFall17noIso/F",
    "lep_mvaIdSpring16/F",
    #Muon specific
    "lep_segmentCompatibility/F",
    "lep_muonInnerTrkRelErr/F",
    "lep_isGlobalMuon/I",          
    "lep_chi2LocalPosition/F",
    "lep_chi2LocalMomentum/F",
    "lep_globalTrackChi2/F",
    "lep_glbTrackProbability/F",
    "lep_caloCompatibility/F",
    "lep_trkKink/F",
    #other Variables
    "lep_pdgId/I",
    "lep_mcMatchPdgId/I",
    "lep_mcMatchId/I",
    "lep_mcMatchAny/I",
    "lep_mediumMuonId/I",
    "lep_pfMuonId/I",
    "lep_isPromptId"+("" if version=='v1' else "_Training")+"/I",
    "lep_isNonPromptId"+("" if version=='v1' else "_Training")+"/I",
    "lep_isFakeId"+("" if version=='v1' else "_Training")+"/I",
    "lep_mvaTTH/F",
    "lep_mvaTTV/F",
    "nTrueInt/F",
    ]

    if not trainingDate==0:
        variables.append("prob_lep_isPromptId"+("" if version=='v1' else "_Training")+"/F")
        variables.append("prob_lep_isNonPromptId"+("" if version=='v1' else "_Training")+"/F")
        variables.append("prob_lep_isFakeId"+("" if version=='v1' else "_Training")+"/F")

    return variables

#variables for roc plots
def roc_plot_variables(version):

    # variables to read
    variables = [
    "lep_pdgId/I",
    "lep_mvaIdFall17noIso/F",
    "lep_pt/F",
    "lep_etaSc/F",                  #electrons (|etaSc|<=1.479 barrel cuts, |etaSc|>1.479 endcap cuts)              #Electron supercluster pseudorapidity for Leptons after the preselection : 0 at: 0x4109bd0
    "lep_full5x5_sigmaIetaIeta/F",  #electrons (barrel: <0.0104,     endcap: <0.0305)                               #Electron full5x5_sigmaIetaIeta for Leptons after the preselection : 0 at: 0x411d5c0 
    "lep_dEtaInSeed/F",             #electrons (barrel: | |<0.00353, endcap: | |<0.00567)                           #DeltaEta wrt ele SC seed for Leptons after the preselection : 0 at: 0x411e850
    "lep_dPhiScTrkIn/F",            #electrons (barrel: | |<0.0499,  endcap: | |<0.0165)                            #Electron deltaPhiSuperClusterTrackAtVtx (without absolute value!) for Leptons after the preselection : 0 at: 0x41083f0
    "lep_relIso03/F",               #electrons (barrel: <0.0361,     endcap: <0.094)       #muons <0.1              #PF Rel Iso, R=0.3, pile-up corrected for Leptons after the preselection : 0 at: 0x410f640
    "lep_eInvMinusPInv/F",          #electrons (barrel: | |<0.0278,  endcap: | |<0.0158)                            #Electron 1/E - 1/p  (without absolute value!) ff version='v1' else "_Training")+"or Leptons after the preselection : 0 at: 0x4108f90   
    "lep_lostHits/I",               #electrons (barrel: 1,           endcap: 1)                                     #Number of lost hits on inner track for Leptons after the preselection : 0 at: 0x4101ee0
    "lep_convVeto/I",               #electrons yes                                                                  #Conversion veto (always true for muons) for Leptons after the preselection : 0 at: 0x410e5c0
    "lep_hadronicOverEm/F",         #electrons                                                                      #Electron hadronicOverEm for Leptons after the preselection : 0 at: 0x4108990
    "lep_rho/F",                    #electrons                                                                      #rho for Leptons after the preselection : 0 at: 0x4117d20
    "lep_jetDR/F",                                                                         #(muons <=0.3)           #deltaR(lepton, nearest jet) for Leptons after the preselection : 0 at: 0x411ca70
    "lep_dxy/F",                                                                           #mouns                   #d_{xy} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410c4b0
    "lep_dz/F",                                                                            #mouns                   #d_{z} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410ca30
    "lep_isGlobalMuon/I",                                                                  #muons yes               #Muon is global for Leptons after the preselection : 0 at: 0x4106c30
    "lep_sip3d/F",
    "lep_isPromptId"+("" if version=='v1' else "_Training")+"/I",
    "lep_isNonPromptId"+("" if version=='v1' else "_Training")+"/I",
    "lep_isFakeId"+("" if version=='v1' else "_Training")+"/I",
    "prob_lep_isPromptId"+("" if version=='v1' else "_Training")+"/F",
    "prob_lep_isNonPromptId"+("" if version=='v1' else "_Training")+"/F",
    "prob_lep_isFakeId"+("" if version=='v1' else "_Training")+"/F",
    "lep_tightId/I",
    "lep_mediumMuonId/I",
    "lep_pfMuonId/I",
    "lep_eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz/I",
    "lep_mvaTTH/F",
    "lep_mvaTTV/F",
    "lep_eta/F",
    "nTrueInt/F",
    ]

    return variables

#functions to calculate eS and eB
def eS(p, rocdataset):
    ntruth=0.
    ntruthid=0.
    for data in rocdataset:
        if data[0]==1:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
    #print ntruth, ntruthid
    return 0. if ntruth==0. else  ntruthid/ntruth

def eB(p, rocdataset):
    ntruth=0.
    ntruthid=0.
    for data in rocdataset:
        if not data[0]==1:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
    #print ntruth, ntruthid
    return 0. if ntruth==0. else ntruthid/ntruth

## define classes
#def isPrompt(lepton):
#    return abs(lepton.lep_mcMatchId) in [6,23,24,25,37]
#
#def isNonPrompt(lepton):
#    return not isPrompt(lepton) and abs(lepton.lep_mcMatchAny) in [4, 5]
#
#def isFake(lepton):
#    return not isPrompt(lepton) and not ( abs(lepton.lep_mcMatchAny) in [4, 5] )


#POG Ids
def getEleWPs(etaSc, selectPOGId):
    WPs_barrel={
    "full5x5_sigmaIetaIeta": [0.0115, 0.011, 0.00998, 0.00998],
    "abs(dEtaInSeed)": [0.00749, 0.00477, 0.00311, 0.00308],
    "abs(dPhiIn)": [0.228, 0.222, 0.103, 0.0816],
    "H/E": [0.356, 0.298, 0.253, 0.0414],
    "abs(1/E-1/p)": [0.299, 0.241, 0.134, 0.0129],
    "missingInnerHits": [2, 1, 1, 1],
    "conversionVeto": [1, 1, 1, 1]
    }

    WPs_endCap={
    "full5x5_sigmaIetaIeta": [0.037, 0.0314, 0.0298, 0.0292],
    "abs(dEtaInSeed)": [0.00895, 0.00868, 0.00609, 0.00605],
    "abs(dPhiIn)": [0.213, 0.213, 0.045, 0.0394],
    "H/E": [0.211, 0.101, 0.0878, 0.0641],
    "abs(1/E-1/p)": [ 0.15, 0.14, 0.13, 0.0129],
    "missingInnerHits": [3, 1, 1, 1],
    "conversionVeto": [1, 1, 1, 1]
    }

    selectDict = {'veto': 0, 'loose': 1, 'medium': 2, 'tight': 3}
    varList = ["full5x5_sigmaIetaIeta", "abs(dEtaInSeed)", "abs(dPhiIn)", "H/E", "abs(1/E-1/p)", "missingInnerHits", "conversionVeto"]
    WPs={}
    for var in varList:
        WPs.update({var: WPs_barrel[var][selectDict[selectPOGId]] if abs(etaSc)<=1.479 else WPs_endCap[var][selectDict[selectPOGId]]})
    return WPs


def getElePOGId(leptonVarDict):
    
    selectList = ['veto', 'loose', 'medium', 'tight']
    selectDict = {'veto': 1, 'loose': 2, 'medium': 3, 'tight': 4}
    POGId=0
    for selectPOGId in selectList:
        WPs = getEleWPs(leptonVarDict["etaSc"], selectPOGId)
        if  leptonVarDict["full5x5_sigmaIetaIeta"] <  WPs["full5x5_sigmaIetaIeta"] \
        and leptonVarDict["abs(dEtaInSeed)"]       <  WPs["abs(dEtaInSeed)"] \
        and leptonVarDict["abs(dPhiIn)"]           <  WPs["abs(dPhiIn)"] \
        and leptonVarDict["H/E"]                   <  WPs["H/E"] \
        and leptonVarDict["abs(1/E-1/p)"]          <  WPs["abs(1/E-1/p)"] \
        and leptonVarDict["missingInnerHits"]      <= WPs["missingInnerHits"] \
        and leptonVarDict["conversionVeto"]        == WPs["conversionVeto"]:
            POGId=selectDict[selectPOGId]
    return POGId

def passIso(cutValIso, valIso):
    Id=0
    if valIso < cutValIso:
        Id=1
    return Id

def passIP(pdgId, etaSc, dxy, dz):
    dxyCutMuon   = 0.05
    dzCutMuon    = 0.1
    dxyCutBarrel = 0.05
    dzCutBarrel  = 0.1
    dxyCutEndCap = 0.1
    dzCutEndCap  = 0.2

    Id=0
    if abs(pdgId)==11:
        if abs(etaSc)<=1.479 and abs(dxy)<dxyCutBarrel and abs(dz)<dzCutBarrel:
            Id=1
        if abs(etaSc)>1.479 and abs(dxy)<dxyCutEndCap and abs(dz)<dzCutEndCap:
            Id=1
    if abs(pdgId)==13:
        if abs(dxy)<dxyCutMuon and abs(dz)<dzCutMuon:
            Id=1
    return Id   
    
#POG Ids incl relIso
def getEleWPsIso(etaSc, selectPOGId):
    WPs_barrel={
    "full5x5_sigmaIetaIeta": [0.0115, 0.011, 0.00998, 0.00998],
    "abs(dEtaInSeed)": [0.00749, 0.00477, 0.00311, 0.00308],
    "abs(dPhiIn)": [0.228, 0.222, 0.103, 0.0816],
    "H/E": [0.356, 0.298, 0.253, 0.0414],
    "abs(1/E-1/p)": [0.299, 0.241, 0.134, 0.0129],
    "missingInnerHits": [2, 1, 1, 1],
    "conversionVeto": [1, 1, 1, 1],
    "relIso": [0.175, 0.0994, 0.0695, 0.0588]
    }

    WPs_endCap={
    "full5x5_sigmaIetaIeta": [0.037, 0.0314, 0.0298, 0.0292],
    "abs(dEtaInSeed)": [0.00895, 0.00868, 0.00609, 0.00605],
    "abs(dPhiIn)": [0.213, 0.213, 0.045, 0.0394],
    "H/E": [0.211, 0.101, 0.0878, 0.0641],
    "abs(1/E-1/p)": [ 0.15, 0.14, 0.13, 0.0129],
    "missingInnerHits": [3, 1, 1, 1],
    "conversionVeto": [1, 1, 1, 1],
    "relIso": [0.159, 0.107, 0.0821, 0.0571]
    }

    selectDict = {'veto': 0, 'loose': 1, 'medium': 2, 'tight': 3}
    varList = ["full5x5_sigmaIetaIeta", "abs(dEtaInSeed)", "abs(dPhiIn)", "H/E", "abs(1/E-1/p)", "missingInnerHits", "conversionVeto", "relIso"]
    WPs={}
    for var in varList:
        WPs.update({var: WPs_barrel[var][selectDict[selectPOGId]] if abs(etaSc)<=1.479 else WPs_endCap[var][selectDict[selectPOGId]]})
    return WPs


def getElePOGIdIso(leptonVarDict):
    
    selectList = ['veto', 'loose', 'medium', 'tight']
    selectDict = {'veto': 1, 'loose': 2, 'medium': 3, 'tight': 4}
    POGId=0
    for selectPOGId in selectList:
        WPs = getEleWPsIso(leptonVarDict["etaSc"], selectPOGId)
        if  leptonVarDict["full5x5_sigmaIetaIeta"] <  WPs["full5x5_sigmaIetaIeta"] \
        and leptonVarDict["abs(dEtaInSeed)"]       <  WPs["abs(dEtaInSeed)"] \
        and leptonVarDict["abs(dPhiIn)"]           <  WPs["abs(dPhiIn)"] \
        and leptonVarDict["H/E"]                   <  WPs["H/E"] \
        and leptonVarDict["abs(1/E-1/p)"]          <  WPs["abs(1/E-1/p)"] \
        and leptonVarDict["missingInnerHits"]      <= WPs["missingInnerHits"] \
        and leptonVarDict["conversionVeto"]        == WPs["conversionVeto"]\
        and leptonVarDict["relIso"]                <  WPs["relIso"]:
            POGId=selectDict[selectPOGId]
    return POGId

#Helper Box in plots
def drawObjects(isTestData, Flavour, Samples, ptSelection, RelIsoCut):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(31) # align right
    lines = [
      (0.22, 0.97, '#it{CMS preliminary} '),
      (1.03, 0.97, ('Electron ' if Flavour=="ele" else 'Muon ')+('TestData' if isTestData else 'TrainData')+' ('+Samples+')'+' , '+ptSelection+('' if RelIsoCut=='' else ', relIso<='+str(RelIsoCut))),
    ]
    return [tex.DrawLatex(*l) for l in lines]

def drawObjectsSmall(preselection):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.019)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.01, 0.93, '#bf{preselcetion: '+preselection+'}')
    ]
    return [tex.DrawLatex(*l) for l in lines]

