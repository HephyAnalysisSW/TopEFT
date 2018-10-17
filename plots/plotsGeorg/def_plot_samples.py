# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *
from TopEFT.Tools.user import trainingFiles_directory as base_directory

def plot_samples_v2(version, year, leptonFlavour, trainingDate, isTestData, ptSelection, sampleSelection, sampleSize):

    #define paths and names
    #base_directory = trainingsFiles_directory
    file_directory = os.path.join(base_directory, version, str(year), leptonFlavour, ptSelection, sampleSelection)
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
        
    predict_directory = os.path.join('/afs/hephy.at/data/gmoertl01/DeepLepton/trainings', 'electrons' if leptonFlavour=='ele' else 'muons', str(trainingDate), sampleSelection+sizePattern+('Electron' if leptonFlavour=='ele' else 'Muon')+'Evaluation'+('TestData' if isTestData else 'TestDataIsTrainData'))

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

#old version
#def plot_samples_v2(version, year, leptonFlavour, trainingDate, isTestData, ptSelection, sampleSelection, sampleSize):
#
#    #define paths and names
#    base_directory = '/afs/hephy.at/data/gmoertl01/lepton/trainfiles/'
#    file_directory = os.path.join(base_directory, version, str(year), leptonFlavour, ptSelection, sampleSelection)
#    sample_texName = ('electrons_' if leptonFlavour=='ele' else 'muons_')+ptSelection+'_'+sampleSelection
#    texfileName    = ('' if sampleSize=='full' else sampleSize+'_')+('test_' if isTestData else 'train_')+leptonFlavour+'_std.txt' 
#    texfilePath    = os.path.join(file_directory, texfileName)
#    
#    predict_directory = os.path.join('/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/', 'electron' if leptonFlavour=='ele' else 'muon', str(trainingDate), 'evaluation' if sampleSize=='full' else sampleSize+'_evaluation', 'testdata' if isTestData else 'traindata')
#
#    #create FileList
#    if trainingDate==0:
#        with open(texfilePath,'r') as f:
#            FileList = f.read().splitlines()
#    else:
#        FileList = os.listdir(predict_directory)
#        if 'tree_association.txt' in FileList:
#            FileList.remove('tree_association.txt')
#        FileList = [filepath.replace('_predict.root', '.root') for filepath in FileList]
#
#    FileList = [filepath.replace(filepath, os.path.join(file_directory, filepath)) for filepath in FileList]
#    sample   = Sample.fromFiles( leptonFlavour, texName = sample_texName, files =FileList, treeName="tree")
#
#    if not trainingDate==0:
#        FilePredictList = os.listdir(predict_directory)
#        if 'tree_association.txt' in FilePredictList:
#            FilePredictList.remove('tree_association.txt')
#
#        FilePredictList = [filepath.replace(filepath, os.path.join(predict_directory, filepath)) for filepath in FilePredictList]
#
#        samplePredict = Sample.fromFiles( leptonFlavour+"_friend", texName = sample_texName+"_predict", files = FilePredictList, treeName="tree")
#        sample.addFriend(samplePredict, "tree")
#
#    samples={"leptonFlavour":leptonFlavour, "sample":sample, "trainingDate":trainingDate, "isTestData":isTestData}
#    
#    return samples

def histo_plot_variables(trainingDate):

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
    "lep_isPromptId/I",
    "lep_isNonPromptId/I",
    "lep_isFakeId/I",
    "lep_mvaTTH/F",
    "lep_mvaTTV/F",
    "nTrueInt/F",
    ]

    if not trainingDate==0: 
        variables.append("prob_lep_isPromptId/F")
        variables.append("prob_lep_isNonPromptId/F")
        variables.append("prob_lep_isFakeId/F")

    return variables

def roc_plot_variables():

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
    "lep_eInvMinusPInv/F",          #electrons (barrel: | |<0.0278,  endcap: | |<0.0158)                            #Electron 1/E - 1/p  (without absolute value!) for Leptons after the preselection : 0 at: 0x4108f90   
    "lep_lostHits/I",               #electrons (barrel: 1,           endcap: 1)                                     #Number of lost hits on inner track for Leptons after the preselection : 0 at: 0x4101ee0
    "lep_convVeto/I",               #electrons yes                                                                  #Conversion veto (always true for muons) for Leptons after the preselection : 0 at: 0x410e5c0
    "lep_hadronicOverEm/F",         #electrons                                                                      #Electron hadronicOverEm for Leptons after the preselection : 0 at: 0x4108990
    "lep_rho/F",                    #electrons                                                                      #rho for Leptons after the preselection : 0 at: 0x4117d20
    "lep_jetDR/F",                                                                         #(muons <=0.3)           #deltaR(lepton, nearest jet) for Leptons after the preselection : 0 at: 0x411ca70
    "lep_dxy/F",                                                                           #mouns                   #d_{xy} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410c4b0
    "lep_dz/F",                                                                            #mouns                   #d_{z} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410ca30
    "lep_isGlobalMuon/I",                                                                  #muons yes               #Muon is global for Leptons after the preselection : 0 at: 0x4106c30
    "lep_isPromptId/I",
    "lep_isNonPromptId/I",
    "lep_isFakeId/I",
    "prob_lep_isPromptId/F",
    "prob_lep_isNonPromptId/F",
    "prob_lep_isFakeId/F",
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

#define function to calculate eS and eB
def eS(p, rocdataset):
    ntruth=0.
    ntruthid=0.
    for data in rocdataset:
        if data[0]==1:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
    print ntruth, ntruthid
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

def drawObjectsSmall(isTestData, Flavour, Samples, ptSelection, RelIsoCut):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.025)
    tex.SetTextAlign(31) # align right
    lines = [
      (0.99, 0.93, '#bf{eff(IP+ID)=  POG: (POG ID+IP+relIso)/relIso, LeptonMVA: (MVA ID+relIso)/relIso, DeepLepton: (DL ID)/relIso}')
    ]
    return [tex.DrawLatex(*l) for l in lines]



def plot_plotList():
    plotList=[] #leptonType="Ele" or "Muo", plotDate="YYYYMMDD", isTraindata=1 or 0
    plotList.append(["Muo","20180809_std_PfAndSv",0,"std"])
    plotList.append(["Muo","20180809_std_PfAndSv",1,"std"])
    plotList.append(["Ele","20180808_std_PfAndSv",0,"std"])
    plotList.append(["Ele","20180808_std_PfAndSv",1,"std"])
    #plotList.append(["Muo","20180809_iso",0,"iso"])
    #plotList.append(["Muo","20180809_iso",1,"iso"])
    #plotList.append(["Ele","20180809_iso",0,"iso"])
    #plotList.append(["Ele","20180809_iso",1,"iso"])

    return plotList

def plot_samples(leptonType, plotDate, isTrainData):
 
    #define mixed QCD + TTJets samples for electorns and muons
    
    if leptonType=="Ele":

        sample_texName="Electrons_from_TTJets_and_QCD"
        
        if isTrainData:
            
            #Electron Train Files
            Files=[
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_a90000/","train_ele_50files.txt",
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/electron/"+plotDate+"/evaluation/traindata/"
            ]

        else:

            #Electron Test Files
            Files=[
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_a90000/","test_ele_50files.txt",
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/electron/"+plotDate+"/evaluation/testdata/"
            ]
    
    if leptonType=="Muo":

        sample_texName="Muons_from_TTJets_and_QCD"

        if isTrainData:

            #Muon Train Files
            Files=[
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_a90000/","train_muo.txt",
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/muon/"+plotDate+"/evaluation/traindata/"
            ]

        else:

            #Muon Test Files
            Files=[
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_a90000/","test_muo.txt",
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/muon/"+plotDate+"/evaluation/testdata/"
            ]

    #create FileList
    with open(Files[0]+Files[1],'r') as f:
        FileList = f.read().splitlines()
    with open(Files[0]+Files[1],'r') as f:
        FilePredictList = f.read().splitlines()
    FileList=[filepath.replace(filepath, Files[0]+filepath) for filepath in FileList]
    FilePredictList=[filepath.replace(filepath, Files[2]+filepath) for filepath in FilePredictList]
    FilePredictList=[filepath.replace(".root", "_predict.root") for filepath in FilePredictList]

    #Sample
    sample = Sample.fromFiles( leptonType, texName = sample_texName, files =FileList, treeName="tree")
    samplePredict = Sample.fromFiles( leptonType+"_friend", texName = sample_texName+"_predict", files = FilePredictList, treeName="tree")
    sample.addFriend(samplePredict, "tree")
    
    samples={"leptonType":leptonType, "sample":sample, "plotDate":plotDate, "isTrainData":isTrainData}
    print sample.files
    return samples

def plot_samples_iso(leptonType, plotDate, isTrainData):
 
    #define mixed QCD + TTJets samples for electorns and muons
    
    if leptonType=="Ele":

        sample_texName="Electrons_from_TTJets_and_QCD"
        
        if isTrainData:
            
            #Electron Train Files
            Files=[
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_isolation_a90000/","train_iso_ele.txt",
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/electron/"+plotDate+"/evaluation/traindata/"
            ]

        else:

            #Electron Test Files
            Files=[
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_isolation_a90000/","test_iso_ele.txt",
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/electron/"+plotDate+"/evaluation/testdata/"
            ]
    
    if leptonType=="Muo":

        sample_texName="Muons_from_TTJets_and_QCD"

        if isTrainData:

            #Muon Train Files
            Files=[
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_isolation_a90000/","train_iso_muo.txt",
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/muon/"+plotDate+"/evaluation/traindata/"
            ]

        else:

            #Muon Test Files
            Files=[
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_isolation_a90000/","test_iso_muo.txt",
            "/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/muon/"+plotDate+"/evaluation/testdata/"
            ]

    #create FileList
    with open(Files[0]+Files[1],'r') as f:
        FileList = f.read().splitlines()
    with open(Files[0]+Files[1],'r') as f:
        FilePredictList = f.read().splitlines()
    FileList=[filepath.replace(filepath, Files[0]+filepath) for filepath in FileList]
    FilePredictList=[filepath.replace(filepath, Files[2]+filepath) for filepath in FilePredictList]
    FilePredictList=[filepath.replace(".root", "_predict.root") for filepath in FilePredictList]

    #Sample
    sample = Sample.fromFiles( leptonType, texName = sample_texName, files =FileList, treeName="tree")
    samplePredict = Sample.fromFiles( leptonType+"_friend", texName = sample_texName+"_predict", files = FilePredictList, treeName="tree")
    sample.addFriend(samplePredict, "tree")
    
    samples={"leptonType":leptonType, "sample":sample, "plotDate":plotDate, "isTrainData":isTrainData}
    print samples.files
    return samples
