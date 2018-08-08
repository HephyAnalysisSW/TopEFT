# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

def plot_plotList():
    plotList=[] #leptonType="Ele" or "Muo", plotDate="YYYYMMDD", isTraindata=1 or 0
    plotList.append(["Muo","20180802_std_PfAndSv",0,"std"])
    #plotList.append(["Muo","20180802_std_PfAndSv",1,"std"])
    plotList.append(["Ele","20180802_std_PfAndSv",0,"std"])
    #plotList.append(["Ele","20180802_std_PfAndSv",1,"std"])
    #plotList.append(["Muo","20180806_iso",0,"iso"])
    #plotList.append(["Muo","20180806_iso",1,"iso"])
    #plotList.append(["Ele","20180806_iso",0,"iso"])
    #plotList.append(["Ele","20180806_iso",1,"iso"])

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
    return samples

def histo_plot_variables():

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

    "lep_lostOuterHits/I",         
    "lep_lostHits/I", #lost inner hits
    "lep_innerTrackValidHitFraction/F",         

    "lep_jetDR/F",                 
    "lep_dxy/F",                   
    "lep_dz/F",                    
    "lep_edxy/F",                   
    "lep_edz/F",                    
    "lep_ip3d/F",
    "lep_sip3d/F",
    "lep_dxy_pf/F",                   
    "lep_dz_pf/F",                    
    "lep_dzAssociatedPV/F",
    "lep_hcalFraction/F",
    "lep_puppiWeight/F",
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
    #other Variables
    "lep_pdgId/I",
    "lep_mcMatchPdgId/I",
    "lep_mcMatchId/I",
    "lep_mcMatchAny/I",
    "lep_isPromptId/I",
    "lep_isNonPromptId/I",
    "lep_isFakeId/I",
    "prob_lep_isPromptId/F",
    "prob_lep_isNonPromptId/F",
    "prob_lep_isFakeId/F"
    ]

    return variables

def roc_plot_variables():

    # variables to read
    variables = [
    #"run/I",
    #"lumi/I",
    #"evt/l",
    #"lep_trackerHits/I",
    #"lep_innerTrackChi2/F",
    "lep_pdgId/I",
    #"lep_segmentCompatibility/F",
    #"lep_sigmaIEtaIEta/F",
    #"lep_mcMatchPdgId/I",
    #"lep_mcMatchId/I",
    #"lep_mcMatchAny/I",
    #"lep_mvaIdSpring16/F",
    "lep_mvaIdFall17noIso/F",
    "lep_pt/F",
    #"lep_relIso04/F",
    #
    #"lep_etaSc/F",                  #electrons (|etaSc|<=1.479 barrel cuts, |etaSc|>1.479 endcap cuts)              #Electron supercluster pseudorapidity for Leptons after the preselection : 0 at: 0x4109bd0
    #"lep_full5x5_sigmaIetaIeta/F",  #electrons (barrel: <0.0104,     endcap: <0.0305)                               #Electron full5x5_sigmaIetaIeta for Leptons after the preselection : 0 at: 0x411d5c0 
    #"lep_dEtaInSeed/F",             #electrons (barrel: | |<0.00353, endcap: | |<0.00567)                           #DeltaEta wrt ele SC seed for Leptons after the preselection : 0 at: 0x411e850
    #"lep_dPhiScTrkIn/F",            #electrons (barrel: | |<0.0499,  endcap: | |<0.0165)                            #Electron deltaPhiSuperClusterTrackAtVtx (without absolute value!) for Leptons after the preselection : 0 at: 0x41083f0
    "lep_relIso03/F",               #electrons (barrel: <0.0361,     endcap: <0.094)       #muons <0.1              #PF Rel Iso, R=0.3, pile-up corrected for Leptons after the preselection : 0 at: 0x410f640
    #"lep_eInvMinusPInv/F",          #electrons (barrel: | |<0.0278,  endcap: | |<0.0158)                            #Electron 1/E - 1/p  (without absolute value!) for Leptons after the preselection : 0 at: 0x4108f90   
    #"lep_lostOuterHits/I",          #electrons (barrel: 1,           endcap: 1)                                     #Number of lost hits on inner track for Leptons after the preselection : 0 at: 0x4101ee0
    #"lep_convVeto/I",               #electrons yes                                                                  #Conversion veto (always true for muons) for Leptons after the preselection : 0 at: 0x410e5c0
    #"lep_hadronicOverEm/F",         #electrons                                                                      #Electron hadronicOverEm for Leptons after the preselection : 0 at: 0x4108990
    #"lep_rho/F",                    #electrons                                                                      #rho for Leptons after the preselection : 0 at: 0x4117d20
    #"lep_jetDR/F",                                                                         #(muons <=0.3)           #deltaR(lepton, nearest jet) for Leptons after the preselection : 0 at: 0x411ca70
    #"lep_dxy/F",                                                                           #mouns                   #d_{xy} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410c4b0
    #"lep_dz/F",                                                                            #mouns                   #d_{z} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410ca30
    #"lep_isGlobalMuon/I",                                                                  #muons yes               #Muon is global for Leptons after the preselection : 0 at: 0x4106c30
    "lep_isPromptId/I",
    #"lep_isNonPromptId/I",
    #"lep_isFakeId/I",
    "prob_lep_isPromptId/F",
    #"prob_lep_isNonPromptId/F",
    #"prob_lep_isFakeId/F"
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
    return 0. if ntruth==0. else  ntruthid/ntruth

def eB(p, rocdataset):
    ntruth=0.
    ntruthid=0.
    for data in rocdataset:
        if not data[0]==1:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
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

