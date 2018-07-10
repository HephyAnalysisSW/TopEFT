# Standard imports
import ROOT
import os
from array import array
from copy import deepcopy
import math

# RootTools
from RootTools.core.standard import *

# User specific 
from TopEFT.Tools.user import plot_directory
plot_directory_=os.path.join(plot_directory, 'DeepLepton')
plot_directory=plot_directory_

#define mixed QCD + TTJets samples for electorns and muons
PlotTrainData=1  #1=true, 0=false
ElectronDate='20180703'
MuonDate='20180704'
logY=1

#Electron Train Files
EleTrainFiles=[
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_a90000/","train_ele_file1to70.txt",
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/"+ElectronDate+"/electron/evaluation/traindata/"
]
with open(EleTrainFiles[0]+EleTrainFiles[1],'r') as f:
    EleTrainFileList = f.read().splitlines()
with open(EleTrainFiles[0]+EleTrainFiles[1],'r') as f:
    EleTrainFilePredictList = f.read().splitlines()
EleTrainFileList=[filepath.replace(filepath, EleTrainFiles[0]+filepath) for filepath in EleTrainFileList]
EleTrainFilePredictList=[filepath.replace(filepath, EleTrainFiles[2]+filepath) for filepath in EleTrainFilePredictList]
EleTrainFilePredictList=[filepath.replace(".root", "_predict.root") for filepath in EleTrainFilePredictList]

#Electron Test Files
EleTestFiles=[
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_a90000/","train_ele_file1to70.txt",
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/"+ElectronDate+"/electron/evaluation/traindata/"
]
with open(EleTestFiles[0]+EleTestFiles[1],'r') as f:
    EleTestFileList = f.read().splitlines()
with open(EleTestFiles[0]+EleTestFiles[1],'r') as f:
    EleTestFilePredictList = f.read().splitlines()
EleTestFileList=[filepath.replace(filepath, EleTestFiles[0]+filepath) for filepath in EleTestFileList]
EleTestFilePredictList=[filepath.replace(filepath, EleTestFiles[2]+filepath) for filepath in EleTestFilePredictList]
EleTestFilePredictList=[filepath.replace(".root", "_predict.root") for filepath in EleTestFilePredictList]

#Muon Train Files
MuoTrainFiles=[
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_a90000/","train_muo.txt",
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/"+MuonDate+"/muon/evaluation/traindata/"
]
with open(MuoTrainFiles[0]+MuoTrainFiles[1],'r') as f:
    MuoTrainFileList = f.read().splitlines()
with open(MuoTrainFiles[0]+MuoTrainFiles[1],'r') as f:
    MuoTrainFilePredictList = f.read().splitlines()
MuoTrainFileList=[filepath.replace(filepath, MuoTrainFiles[0]+filepath) for filepath in MuoTrainFileList]
MuoTrainFilePredictList=[filepath.replace(filepath, MuoTrainFiles[2]+filepath) for filepath in MuoTrainFilePredictList]
MuoTrainFilePredictList=[filepath.replace(".root", "_predict.root") for filepath in MuoTrainFilePredictList]

#Muon Test Files
MuoTestFiles=[
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/preprocessing/trainsamples_a90000/","test_muo.txt",
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DeepLepton/"+MuonDate+"/muon/evaluation/testdata/"
]
with open(MuoTestFiles[0]+MuoTestFiles[1],'r') as f:
    MuoTestFileList = f.read().splitlines()
with open(MuoTestFiles[0]+MuoTestFiles[1],'r') as f:
    MuoTestFilePredictList = f.read().splitlines()
MuoTestFileList=[filepath.replace(filepath, MuoTestFiles[0]+filepath) for filepath in MuoTestFileList]
MuoTestFilePredictList=[filepath.replace(filepath, MuoTestFiles[2]+filepath) for filepath in MuoTestFilePredictList]
MuoTestFilePredictList=[filepath.replace(".root", "_predict.root") for filepath in MuoTestFilePredictList]


#Electron Sample
sampleEle = Sample.fromFiles( "Ele", texName = "Electrons_from_TTJets_and_QCD", files =(EleTrainFileList if PlotTrainData else EleTestFileList), treeName="tree")
sampleElePredict = Sample.fromFiles( "Ele_friend", texName = "Electrons_from_TTJets_and_QCD_predict", files = (EleTrainFilePredictList if PlotTrainData else EleTestFilePredictList), treeName="tree")
sampleEle.addFriend(sampleElePredict, "tree")

#Muon Sample
sampleMuo = Sample.fromFiles( "Muo", texName = "Muons_from_TTJets_and_QCD", files = [MuoTrainFileList[0]], treeName="tree")
sampleMuoPredict = Sample.fromFiles( "Muo_friend", texName = "Muons_from_TTJets_and_QCD_predict", files = [MuoTrainFilePredictList[0]], treeName="tree")
#sampleMuo = Sample.fromFiles( "Muo", texName = "Muons_from_TTJets_and_QCD", files = (MuoTrainFileList if PlotTrainData else MuoTestFileList), treeName="tree")
#sampleMuoPredict = Sample.fromFiles( "Muo_friend", texName = "Muons_from_TTJets_and_QCD_predict", files = (MuoTrainFilePredictList if PlotTrainData else MuoTestFilePredictList), treeName="tree")
sampleMuo.addFriend(sampleMuoPredict, "tree")


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
#"lep_relIso03/F",               #electrons (barrel: <0.0361,     endcap: <0.094)       #muons <0.1              #PF Rel Iso, R=0.3, pile-up corrected for Leptons after the preselection : 0 at: 0x410f640
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


#define plot structure
leptonFlavourList=[]
#leptonFlavourList.append({"Name":"Electron", "ShortName":"ele", "pdgId":11, "sample":sampleEle})
leptonFlavourList.append({"Name":"Muon", "ShortName":"muo", "pdgId":13, "sample":sampleMuo})

MVAList=[]
MVAList.append({"Name":"MVA_Fall17noIso", "Var":"lep_mvaIdFall17noIso", "plotColor":ROOT.kGray, "lineWidth":1})
MVAList.append({"Name":"DeepLeptonSummer18", "Var":"prob_lep_isPromptId", "plotColor":ROOT.kRed, "lineWidth":2})

binnedList=[]
binnedList.append({"Name":"pt", "VarName":"|pt|", "Var":"lep_pt", "abs":1, "cuts":[0, 250], "bins":50})

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


for leptonFlavour in leptonFlavourList:
    if leptonFlavour["Name"]=="Muon":
        MVAList=[]
        MVAList.append({"Name":"DeepLeptonSummer18", "Var":"prob_lep_isPromptId", "plotColor":ROOT.kRed, "lineWidth":2})
    
    for binVar in binnedList:

        colorList=[]
        lineWidthList=[]
        
        #Initialize Mulitgraph
        c=ROOT.TCanvas()
        c.SetLogy()
        mg=ROOT.TMultiGraph()
        g=[]
        ng=0

        for MVA in MVAList:
            
            colorList.append(MVA["plotColor"])
            lineWidthList.append(MVA["lineWidth"])

            # reader class
            readerData=[[] for i in xrange(binVar["bins"])]
            reader = leptonFlavour["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
            reader.start()
            while reader.run():
                if abs(reader.event.lep_pdgId)==leptonFlavour["pdgId"]:
                    cut_val = getattr(reader.event, binVar["Var"]) 
                    if cut_val >= binVar["cuts"][0] and cut_val <  binVar["cuts"][1]:
                        j=int(math.ceil(cut_val/(binVar["cuts"][1]-binVar["cuts"][0])*binVar["bins"]))-1
                        readerData[j].append([reader.event.lep_isPromptId, getattr(reader.event, MVA["Var"])])
                        #print "j=%i, pt=%f" %(j, reader.event.lep_pt)
                        #print "i=%i,j=%i,  pt=%f" %(i,j, reader.event.lep_pt)
            
            j=0
            x=array('d')
            y=array('d')
            for dataset in readerData:
                #print j+1, len(dataset)
                j += 1
                prange=[pval*0.001 for pval in range(950,1000)]
                for pval in prange:
                    xval=eB(pval,dataset)
                    p=pval 
                    #print pval, xval
                    if xval<=0.01:
                        break
                if not len(dataset)==0:
                    x.append(j*5)
                    y.append(eS(p,dataset))

            #Draw Graphs
            n=len(x)
            g.append(ROOT.TGraph(n,x,y))
            gname=(MVA["Name"]+": "+binVar["Var"]+", "+"eB<=0.01")
            g[ng].SetName(gname)
            g[ng].SetTitle(gname)
            g[ng].SetLineColor(colorList[ng])
            g[ng].SetLineWidth(lineWidthList[ng])
            g[ng].SetMarkerColor(colorList[ng])
            #g[ng].SetMarkerStyle( 5 )
            g[ng].SetFillStyle(0)
            g[ng].SetFillColor(0)
            g[ng].SetMarkerSize(0)
            g[ng].Draw("C")
            #nmaxtext.DrawLatex(x[nmax],y[nmax],"mvaId=%1.2f" %p[nmax])
            mg.Add(g[ng])
            ng += 1

        #Draw Multigraph
        mg.Draw("AC")
        mg.SetTitle(leptonFlavour["sample"].texName+(" - TrainData" if PlotTrainData else " - TestData"))
        mg.GetXaxis().SetTitle('pt')
        mg.GetYaxis().SetTitle('eS')
        #mg.GetYaxis().SetRangeUser(0.0,1.0)
        c.BuildLegend()
        directory=(os.path.join(plot_directory, ElectronDate if leptonFlavour["Name"]=="Electron" else MuonDate, leptonFlavour["Name"]))
        if not os.path.exists(directory):
            os.makedirs(directory)
        c.Print(os.path.join(directory, 'roc_binned_'+binVar["Name"]+'.png'))
