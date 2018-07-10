# Standard imports
import ROOT
import os
from array import array
from copy import deepcopy

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



#define plot structure
leptonFlavourList=[]
#leptonFlavourList.append({"Name":"Electron", "ShortName":"ele", "pdgId":11, "sample":sampleEle})
leptonFlavourList.append({"Name":"Muon", "ShortName":"muo", "pdgId":13, "sample":sampleMuo})

MVAList=[]
MVAList.append({"Name":"MVA_Fall17noIso", "Var":"lep_mvaIdFall17noIso", "plotColor":[ROOT.kGray,ROOT.kGray+1,ROOT.kGray+2,ROOT.kGray+3,ROOT.kGray+4], "lineWidth":1})
MVAList.append({"Name":"DeepLeptonSummer18", "Var":"prob_lep_isPromptId", "plotColor":[ROOT.kRed,ROOT.kRed+1,ROOT.kRed+2,ROOT.kRed+3,ROOT.kRed+4], "lineWidth":2})

pt_cuts=[]
pt_cuts.append({"Name":"pt15to25","lower_limit":15, "upper_limit":25})
pt_cuts.append({"Name":"pt>25","lower_limit":25, "upper_limit":1000})

cutList=[]
cutList.append({"Name":"relIso", "VarName":"relIso03", "Var":"lep_relIso03", "cuts":[0.1,0.2,0.3,0.4,0.5], "operator":"<="})

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

#loop over Leptons, MVAs and Cuts

for leptonFlavour in leptonFlavourList:
    if leptonFlavour["Name"]=="Muon":
        MVAList=[]
        MVAList.append({"Name":"DeepLeptonSummer18", "Var":"prob_lep_isPromptId", "plotColor":[ROOT.kRed,ROOT.kRed+1,ROOT.kRed+2,ROOT.kRed+3,ROOT.kRed+4], "lineWidth":2})

    for pt_cut in pt_cuts:
    
        for var in cutList:
            readerdata=[]
            plotLegend=[]
            
            colorList=[]
            lineWidthList=[]
            
            #Draw TGraph
            c=ROOT.TCanvas()
            if logY: c.SetLogy()
            mg=ROOT.TMultiGraph()
            g=[]
            ng=0
             
            for MVA in MVAList:
                i=0
                for cut in var["cuts"]:
                    legendString=MVA["Name"]+" |pdgId|="+str(leptonFlavour["pdgId"])+", "+var["VarName"]+var["operator"]+str(cut)
                    plotLegend.append(legendString)
                    colorList.append(MVA["plotColor"][i])
                    lineWidthList.append(MVA["lineWidth"])
                    readerdata.append([])
                    i += 1

            # reader class
            reader = leptonFlavour["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
            # loop
            reader.start()

            while reader.run():
                j=0
                for MVA in MVAList:
                    for cut in var["cuts"]:
                        if abs(reader.event.lep_pdgId)==leptonFlavour["pdgId"] and (reader.event.lep_pt>=pt_cut["lower_limit"] and reader.event.lep_pt<=pt_cut["upper_limit"]):
                            if (getattr(reader.event,var["Var"]) <= cut if var["operator"]=="<=" else getattr(reader.event,var["Var"]) >= cut):
                                readerdata[j].append([reader.event.lep_isPromptId, getattr(reader.event, MVA["Var"])])            
                                #print "pdgId %i, pt %f" %(reader.event.lep_pdgId, reader.event.lep_pt)
                        j += 1

            #calculate eS and eB
            for dataset in readerdata:
                p=array('d')
                x=array('d')
                y=array('d')

                prange=[pval*0.01 for pval in xrange(-100,100)]
                for pval in prange:
                    x.append(eS(pval, dataset))
                    y.append(eB(pval, dataset)) if logY else y.append(1-eB(pval, dataset))

                gname=plotLegend[ng]
                n=len(x)
                g.append(ROOT.TGraph(n,x,y))
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
            mg.Draw("AC")
            mg.SetTitle(pt_cut["Name"]+" "+leptonFlavour["sample"].texName+(" - TrainData" if PlotTrainData else " - TestData"))
            mg.GetXaxis().SetTitle('eS')
            mg.GetXaxis().SetLimits(0.597, 1.003)
            mg.GetYaxis().SetTitle('eB' if logY else '1-eB')
            mg.GetYaxis().SetRangeUser(0.0009, 1.01) if logY else mg.GetYaxis().SetLimits(0.0, 1.0)
            #c.BuildLegend(0.12,0.90,0.5,0.7) if logY else c.BuildLegend()
            c.BuildLegend()
            directory=(os.path.join(plot_directory, ElectronDate if leptonFlavour["Name"]=="Electron" else MuonDate, leptonFlavour["Name"]))
            if not os.path.exists(directory):
                os.makedirs(directory)
            c.Print(os.path.join(directory, 'roc_'+pt_cut["Name"]+'_cut_'+var["Name"]+'.png'))
