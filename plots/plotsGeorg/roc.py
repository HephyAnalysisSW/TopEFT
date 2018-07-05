# Standard imports
import ROOT
import os
from array import array

# RootTools
from RootTools.core.standard import *

# User specific 
from TopEFT.Tools.user import plot_directory
plot_directory_=os.path.join(plot_directory, 'roc_plots')
plot_directory=plot_directory_

#define mixed QCD + TTJets samples for electorns and muons
sampleEle = Sample.fromFiles( "mixedEle", texName = "mixedElectronsFrom_TTJets_and_QCD", files = [
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/trainsamples_a90000/trainfile_ele_1.root"
], treeName="tree")
sampleElePredict = Sample.fromFiles( "mixedEle_friend", texName = "mixedElectronsFrom_TTJets_and_QCD_predict", files = [
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/data_deepLepton/20180703/Evaluation_2x2epochs_trainfiles_a90k/TestLeptonEvaluation/trainfile_ele_1_predict.root"
], treeName="tree")
#n=1
#for i in xrange(500,n):
#    sampleEle.files.append("/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/trainsamples_a90000/trainfile_ele_"+str(i)+".root")
#    sampleElePredict.files.append("/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/data_deepLepton/20180703/Evaluation_2x2epochs_trainfiles_a90k/TestLeptonEvaluation/trainfile_ele_"+str(i)+"_predict.root")
sampleEle.addFriend(sampleElePredict, "tree")

sampleMuo = Sample.fromFiles( "mixedMuo", texName = "mixedMuonsFrom_TTJets_and_QCD", files = [
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/trainsamples_a90000/trainfile_muo_11.root"
], treeName="tree")
sampleMuoPredict = Sample.fromFiles( "mixedMuo_friend", texName = "mixedMuonsFrom_TTJets_and_QCD_predict", files = [
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/data_deepLepton/20180704/MuonEvaluationTestData/trainfile_muo_11_predict.root"
], treeName="tree")

#fileNoList=[13,14,16,17,18,1,22,25,27,28,31,33,35,38,39,3,40,43,47,48,4,52,53,54,57,60,61,62,63,64,65,66,68,72,74,75,76,77,80]
#for fileNo in fileNoList:
#    sampleMuo.files.append("/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/trainsamples_a90000/trainfile_muo_"+str(fileNo)+".root")
#    sampleMuoPredict.files.append("/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/data_deepLepton/20180704/MuonEvaluationTestData/trainfile_muo_"+str(fileNo)+"_predict.root")

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
#"lep_pt/F",
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


logY=1

#define plot structure
leptonList=[]
#leptonList.append({"Name":"Electron", "ShortName":"ele", "pdgId":11, "sample":sampleEle})
leptonList.append({"Name":"Muon", "ShortName":"muo", "pdgId":13, "sample":sampleMuo})

MVAList=[]
#MVAList.append({"Name":"MVA_Fall17noIso", "Var":"lep_mvaIdFall17noIso", "plotColor":[ROOT.kGray,ROOT.kGray+1,ROOT.kGray+2,ROOT.kGray+3,ROOT.kGray+4], "lineWidth":1})
MVAList.append({"Name":"DeepLeptonSummer18", "Var":"prob_lep_isPromptId", "plotColor":[ROOT.kRed,ROOT.kRed+1,ROOT.kRed+2,ROOT.kRed+3,ROOT.kRed+4], "lineWidth":2})

cutList=[]
cutList.append({"Name":"relIso", "VarName":"relIso03", "Var":"lep_relIso03", "abs":0, "cuts":[0.1,0.2,0.3,0.4,0.5], "operator":"<="})
#cutList.append({"Name":"pt", "VarName":"|pt|", "Var":"lep_pt", "abs":1, "cuts":[25], "operator":">="})

colorList=[]
lineWidthList=[]
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

for lepton in leptonList:
    for var in cutList:
        rocdata=[]
        pdata=[]
        xdata=[]
        ydata=[]
        nmaxdata=[]
        plotLegend=[]
        for MVA in MVAList:
            i=0
            for cut in var["cuts"]:
                legendString=MVA["Name"]+" |pdgId|="+str(lepton["pdgId"])+", "+var["VarName"]+var["operator"]+str(cut)
                plotLegend.append(legendString)
                colorList.append(MVA["plotColor"][i])
                lineWidthList.append(MVA["lineWidth"])
                rocdata.append([])
                i += 1

        # reader class
        reader = lepton["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
        # loop
        reader.start()

        while reader.run():
            j=0
            for MVA in MVAList:
                for cut in var["cuts"]:
                    if abs(reader.event.lep_pdgId)==lepton["pdgId"]:
                        if eval(str(eval('reader.event.'+var["Var"]))+var["operator"]+str(cut)):
                            rocdata[j].append([reader.event.lep_isPromptId, eval('reader.event.'+MVA["Var"])])            
                            #print "pdgId %i, pt %f" %(reader.event.lep_pdgId, reader.event.lep_pt)
                    j += 1

        #calculate eS and eB
        for rocdataset in rocdata:
            p=array('d')
            x=array('d')
            y=array('d')

            npmin=-100
            npmax=100
            nmax=0
            xymax=0.
            for np in xrange(npmin,npmax,1):
                i=np-npmin
                p.append(np/100.)
                x.append(eS(p[i], rocdataset))
                y.append(eB(p[i], rocdataset)) if logY else y.append(1-eB(p[i], rocdataset))
                #if ((x[i]*y[i])>xymax):
                #    xymax=x[i]*y[i]
                #    nmax=i
                #print p[i], x[i], y[i]
            #print "maximum at: ", p[nmax], x[nmax], y[nmax]
            pdata.append(p)
            xdata.append(x)
            ydata.append(y)
            #nmaxdata.append(nmax)

        #Draw TGraph
        c=ROOT.TCanvas()
        c.SetLogy()
        mg=ROOT.TMultiGraph()
        g=[]
        #nmaxtext=ROOT.TLatex()
        for i in xrange(len(rocdata)):
            p=pdata[i]
            x=xdata[i]
            y=ydata[i]
            gname=plotLegend[i]
            #nmax=nmaxdata[i]
            n=len(x)
            g.append(ROOT.TGraph(n,x,y))
            g[i].SetName(gname)
            g[i].SetTitle(gname)
            g[i].SetLineColor(colorList[i])
            g[i].SetLineWidth(lineWidthList[i])
            g[i].SetMarkerColor(colorList[i])
            #g[i].SetMarkerStyle( 5 )
            g[i].SetFillStyle(0)
            g[i].SetMarkerSize(0)
            g[i].Draw("ACP")
            #nmaxtext.DrawLatex(x[nmax],y[nmax],"mvaId=%1.2f" %p[nmax])
            mg.Add(g[i])
        mg.Draw("ACP")
        mg.SetTitle(lepton["sample"].texName)
        mg.GetXaxis().SetTitle('eS')
        mg.GetXaxis().SetLimits(0.597, 1.003)
        mg.GetYaxis().SetTitle('eB' if logY else '1-eB')
        mg.GetYaxis().SetRangeUser(0.0009, 1.01) if logY else mg.GetYaxis().SetLimits(0.0, 1.0)
        c.BuildLegend(0.12,0.90,0.5,0.7) if logY else c.BuildLegend()
        if not os.path.exists(plot_directory):
            os.makedirs(plot_directory)
        c.Print(os.path.join(plot_directory, lepton["sample"].texName+lepton["Name"]+var["Name"]+'_log_roc_plot.png')) if logY else c.Print(os.path.join(plot_directory, lepton["sample"].texName+lepton["Name"]+var["Name"]+'_lin_roc_plot.png'))
