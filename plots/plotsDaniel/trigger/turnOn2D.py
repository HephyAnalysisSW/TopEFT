#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi
from RootTools.core.standard      import *
from TopEFT.tools.user            import plot_directory
from TopEFT.tools.helpers         import deltaPhi, getObjDict, getVarValue, writeObjToFile
from TopEFT.tools.objectSelection import getFilterCut
from TopEFT.tools.cutInterpreter  import cutInterpreter
from TopEFT.tools.u_float         import u_float

from TopEFT.tools.user            import plot_directory

ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()

ROOT.gStyle.SetOptFit(0)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat("1.2f")

from  TopEFT.samples.cmgTuples_MET_Data25ns_80X_03Feb_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_v1/singlelep/"
from  TopEFT.samples.cmgTuples_MET_Data25ns_92X_Run2017_12Sep2017_postProcessed import *

data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_v10/singlelep/"
from TopEFT.samples.cmgTuples_Summer16_1l_mAODv2_postProcessed import WJets, WJets_LO

presel = "nlep==2&&met_pt>20&&sqrt(2.*lep_pt[0]*met_pt*(1.-cos(lep_phi[0]-met_phi)))>20"

channels = {'eee':'nGoodElectrons==3','eemu':'nGoodElectrons==2&&nGoodMuons==1','emumu':'nGoodElectrons==1&&nGoodMuons==2','mumumu':'nGoodElectrons==0&&nGoodMuons==3', 'all':'(1)'}
channels = {'1e':'abs(lep_pdgId[0])==11', '1mu':'abs(lep_pdgId[0])==13'}

#channels = {'all':'(1)'}

# singleMu
singleMuTTZ         = ["HLT_SingleMuTTZ"] #isolated
singleMuTriggers    = ["HLT_IsoMu22", "HLT_IsoTkMu22", "HLT_IsoMu22_eta2p1", "HLT_IsoTkMu22_eta2p1", "HLT_IsoMu24", "HLT_IsoTkMu24"]
singleMuNoIso       = ["HLT_SingleMu_noniso"]

# singleEle
singleEleTTZ        = ["HLT_SingleEleTTZ"] #isolated
singleEleTriggers   = ["HLT_Ele27_WPTight_Gsf", "HLT_Ele25_eta2p1_WPTight_Gsf", "HLT_Ele27_eta2p1_WPLoose_Gsf"]
singleEleNoIso      = ["HLT_SingleEle_noniso"]

# multiLep
diMuTriggers        = ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ"," HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ"]
diEleTriggers       = ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"]
EMuTriggers         = ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL", "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ"]
trilepTriggers      = ["HLT_DiMu9_Ele9_CaloIdL_TrackIdL", "HLT_Mu8_DiEle12_CaloIdL_TrackIdL", "HLT_TripleMu_12_10_5", "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL"]

triggers_all = {
    "singleLep": "(%s)"%"||".join(singleMuTTZ+singleEleTTZ),
    "singleLep_addNonIso": "(%s)"%"||".join(singleMuTTZ+singleMuNoIso+singleEleTTZ+singleEleNoIso),
    "singleLep_addDiLep": "(%s)"%"||".join(singleMuTTZ+singleEleTTZ+diMuTriggers+diEleTriggers+EMuTriggers),
    "singleLep_addDiLep_addTriLep": "(%s)"%"||".join(singleMuTTZ+singleEleTTZ+diMuTriggers+diEleTriggers+EMuTriggers+trilepTriggers),
    "stopDilepMix": "((HLT_mumuIso||HLT_mumuNoiso)||(HLT_ee_DZ||HLT_ee_33||HLT_ee_33_MW)||(HLT_mue||HLT_mu30e30)||HLT_SingleMu_noniso||HLT_SingleEle_noniso)",
    "ttHMix": "(%s)"%"||".join(singleMuTriggers+singleEleTriggers+diMuTriggers+diEleTriggers+EMuTriggers+trilepTriggers),
    "ttHMix_no3l": "(%s)"%"||".join(singleMuTriggers+singleEleTriggers+diMuTriggers+diEleTriggers+EMuTriggers),
}


triggers_2016 = {
    "singleLep": "(%s)"%"||".join(singleMuTTZ+singleEleTTZ),
    "singleLep_addNonIso": "(%s)"%"||".join(singleMuTTZ+singleMuNoIso+singleEleTTZ+singleEleNoIso),
    "singleLep_addDiLep": "(%s)"%"||".join(singleMuTTZ+singleEleTTZ+diMuTriggers+diEleTriggers+EMuTriggers),
    "singleLep_addDiLep_addTriLep": "(%s)"%"||".join(singleMuTTZ+singleEleTTZ+diMuTriggers+diEleTriggers+EMuTriggers+trilepTriggers),
}

mu_17           = ["HLT_mu"]
mu_nonIso_17    = ["HLT_mu_nonIso"]
ele_17          = ["HLT_ele"]
ele_nonIso_17   = ["HLT_ele_nonIso"] # not there?

mumu_17         = ["HLT_mumu"]
ee_17           = ["HLT_ee"]
mue_17          = ["HLT_mue"]

mmm_17          = ["HLT_mmm"]
mme_17          = ["HLT_mme"]
mee_17          = ["HLT_mee"]
eee_17          = ["HLT_eee"]

triggers_2017 = {
    "singleLep": "(%s)"%"||".join(mu_17+ele_17),
    "singleLep_addNonIso": "(%s)"%"||".join(mu_17+mu_nonIso_17+ele_17),
    "singleLep_addDiLep": "(%s)"%"||".join(mu_17+ele_17+mumu_17+ee_17+mue_17),
    "singleLep_addDiLep_addTriLep": "(%s)"%"||".join(mu_17+ele_17+mumu_17+ee_17+mue_17+mmm_17+mme_17+mee_17+eee_17)
}

triggers = triggers_2016
sample = MET_Run2016
#sample = WJets_LO

colors  = {"singleLep": ROOT.kRed+1, "singleLep_addNonIso": ROOT.kOrange+1, "singleLep_addDiLep":ROOT.kBlue+1, "singleLep_addDiLep_addTriLep":ROOT.kGreen+1}
markers = {"singleLep": 20, "singleLep_addNonIso": 21, "singleLep_addDiLep": 22, "singleLep_addDiLep_addTriLep": 23}

binningMu   = ([10,15,20,25,40,60,80,100,200],[0,1.2,2.1,2.4])
binningE    = ([10,15,20,25,40,60,80,100,200],[0,1.479,2.5])

eta = "lep_eta[1]"
pt  = "lep_pt[1]"

for c in channels:
    print c
    h_total = {}
    h_trigg = {}
    tEff = {}

    if c == '1e':
        binning = binningE
    elif c == '1mu':
        binning = binningMu
    else:
        raise(NotImplementedError, "No binning implemented for channel %s"%c)
    
    for trigger in triggers.keys():
    
        #h_total     = ROOT.TH1F("total", "", *binning)
        #h_trigg     = ROOT.TH1F("trigger", "", *binning)
        
        baseline = '&&'.join([presel,channels[c]])
        trigger_sel = '&&'.join([presel,channels[c],triggers[trigger]])
        
        print baseline
        print trigger_sel

        h_total[trigger] = sample.get2DHistoFromDraw("abs(%s):%s"%(eta,pt), binning, selectionString=baseline, weightString=None, binningIsExplicit=True, isProfile=False) #no overflow
        h_trigg[trigger] = sample.get2DHistoFromDraw("abs(%s):%s"%(eta,pt), binning, selectionString=trigger_sel, weightString=None, binningIsExplicit=True, isProfile=False) #no overflow

        t_eff = ROOT.TEfficiency(h_trigg[trigger],h_total[trigger])

        h_ratio = h_trigg[trigger].Clone()
        h_ratio.SetName("eff")
        h_ratio.Divide(h_total[trigger])


        can = ROOT.TCanvas("can","can", 700,700)
        can.SetRightMargin(0.15)
        can.SetLogx()
        h_ratio.GetXaxis().SetNdivisions(712)
        h_ratio.GetXaxis().SetMoreLogLabels()
        h_ratio.GetXaxis().SetNoExponent()
        h_ratio.Draw("colz texte")

        #t_eff.Draw("colz same")
        h_eff = t_eff.CreateHistogram()
        for x in binning[0]:
            for y in binning[1]:
                x_bin = h_eff.GetXaxis().FindBin(x)
                y_bin = h_eff.GetYaxis().FindBin(y)
                n_bin = t_eff.FindFixBin(x,y)
                err = ( t_eff.GetEfficiencyErrorUp(n_bin) + t_eff.GetEfficiencyErrorLow(n_bin) ) / 2.
                h_eff.SetBinError(x_bin,y_bin,err)
        h_eff.Draw("colz texte same")
        #print h_eff.GetBinContent(4,4)
        #print h_eff.GetBinError(4,4)
        #raise(NotImplementedError, "just stop here")
        plot_dir = os.path.join(plot_directory, "trigger", "MET_2l", "efficiencies2D", c)
        if not os.path.isdir(plot_dir): os.makedirs(plot_dir)

        h_ratio.GetXaxis().SetTitle("p_{T}(leading l) [GeV]")
        h_ratio.GetYaxis().SetTitle("|#eta|(leading l)")

        h_ratio.GetXaxis().SetTitleSize(0.045)
        h_ratio.GetXaxis().SetLabelSize(0.045)
        h_ratio.GetXaxis().SetTitleOffset(1.3)

        h_ratio.GetYaxis().SetTitleSize(0.045)
        h_ratio.GetYaxis().SetLabelSize(0.045)

        extraText = "Preliminary"
        latex1 = ROOT.TLatex()
        latex1.SetNDC()
        latex1.SetTextSize(0.04)
        latex1.SetTextAlign(11) # align right
        latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
        latex1.DrawLatex(0.72,0.96,"#bf{35.9fb^{-1}} (13TeV)")

        filename = "%s_%s_%s_%s"%(sample.name,trigger, eta, pt)

        for f in ['.png','.pdf']:
            can.RedrawAxis()
            can.Print(plot_dir+"/%s"%filename+f)

        writeObjToFile(plot_dir+"/%s.root"%filename, h_ratio)


