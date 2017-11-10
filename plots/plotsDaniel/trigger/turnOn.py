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
from TopEFT.tools.helpers         import deltaPhi, getObjDict, getVarValue
from TopEFT.tools.objectSelection import getFilterCut
from TopEFT.tools.cutInterpreter  import cutInterpreter
from TopEFT.tools.u_float         import u_float

from TopEFT.tools.user            import plot_directory

ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()

ROOT.gStyle.SetOptFit(0)
ROOT.gStyle.SetOptStat(0)


def turnon_func(x, par):

    halfpoint = par[0]
    width = max(par[1],1)
    plateau = par[2]

    #offset = par[3]
    #plateau = 1.0
    offset = 0

    pt = ROOT.TMath.Max(x[0],0.000001)

    arg = 0
    #print pt, halfpoint, width
    arg = (pt - halfpoint) / (width * ROOT.TMath.Sqrt(2))

    fitval = offset + plateau * 0.5 * (1 + ROOT.TMath.Erf(arg))
    #fitval = offset + plateau * TMath.Erfc(arg)

    return fitval




#postProcessing_directory = "TopEFT_PP_v10/trilep/"
#from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

from  TopEFT.samples.cmgTuples_MET_Data25ns_80X_03Feb_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_v1/singlelep/"
from  TopEFT.samples.cmgTuples_MET_Data25ns_92X_Run2017_12Sep2017_postProcessed import *


presel = "nlep>=1&&met_pt>20&&sqrt(2.*lep_pt[0]*met_pt*(1.-cos(lep_phi[0]-met_phi)))>20"

channels = {'eee':'nGoodElectrons==3','eemu':'nGoodElectrons==2&&nGoodMuons==1','emumu':'nGoodElectrons==1&&nGoodMuons==2','mumumu':'nGoodElectrons==0&&nGoodMuons==3', 'all':'(1)'}
channels = {'1e':'abs(lep_pdgId[0])==11', '1mu':'abs(lep_pdgId[0])==13', 'all':'(1)'}

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

colors  = {"singleLep": ROOT.kRed+1, "singleLep_addNonIso": ROOT.kOrange+1, "singleLep_addDiLep":ROOT.kBlue+1, "singleLep_addDiLep_addTriLep":ROOT.kGreen+1}
markers = {"singleLep": 20, "singleLep_addNonIso": 21, "singleLep_addDiLep": 22, "singleLep_addDiLep_addTriLep": 23}

binning = [0,10,20,30,40,50,60,70,80,100,120,150,200]

sample = MET_Run2016

for c in channels:
    print c
    h_total = {}
    h_trigg = {}
    tEff = {}

    for trigger in triggers.keys():
    
        #h_total     = ROOT.TH1F("total", "", *binning)
        #h_trigg     = ROOT.TH1F("trigger", "", *binning)
        
        baseline = '&&'.join([presel,channels[c]])
        trigger_sel = '&&'.join([presel,channels[c],triggers[trigger]])
        
        print baseline
        print trigger_sel

        h_total[trigger] = sample.get1DHistoFromDraw("lep_pt[0]", binning, selectionString=baseline, weightString=None, binningIsExplicit=True, addOverFlowBin='upper', isProfile=False)
        h_trigg[trigger] = sample.get1DHistoFromDraw("lep_pt[0]", binning, selectionString=trigger_sel, weightString=None, binningIsExplicit=True, addOverFlowBin='upper', isProfile=False)

        #sample.chain.Draw("lep_pt>>total", baseline)
        #sample.chain.Draw("lep_pt>>trigger", trigger_sel)

        h_ratio = h_trigg[trigger].Clone()
        h_ratio.Divide(h_total[trigger])

        tEff[trigger] = ROOT.TEfficiency(h_trigg[trigger],h_total[trigger])
        tEff[trigger].Draw()

        h_eff = h_total[trigger].Clone()
        h_eff.SetMaximum(1.05)
        h_eff.SetMinimum(0.0)
    
        xmin = h_ratio.GetXaxis().GetXmin()
        xmax = h_ratio.GetXaxis().GetXmax()

        fturn = ROOT.TF1("turnon",turnon_func,xmin,xmax,3)
        fturn.SetParNames('halfpoint','width','plateau')
        fturn.SetParLimits(0,0,10000)
        fturn.SetParLimits(1,0.1,10000)
        fturn.SetParLimits(2,0,1)

        fturn.SetLineColor(colors[trigger])
        fturn.SetLineWidth(2)

        gEff = tEff[trigger].GetPaintedGraph()

        expPlateau = min(h_ratio.GetMaximum(),0.99)
        expHalfP = max(h_ratio.GetBinCenter(h_ratio.FindFirstBinAbove(0.5)),0)
        expWidth = ROOT.TMath.Sqrt(expHalfP)

        #fturn.SetParameters(300,100,1)
        fturn.SetParameters(expHalfP,expWidth,expPlateau)

        ## do fit
        fitr = tEff[trigger].Fit(fturn,'S Q E EX0')#EX0
        

        #halfpoint = fitr.Value(0)
        #width = fitr.Value(1)
        #plateau = fitr.Value(2)

        #print 'Expected values: halfpoint = %5.2f, width = %5.2f, plateau = %5.2f' % (expHalfP, expWidth, expPlateau)
        #print 'Fit result: halfpoint = %5.2f, width = %5.2f, plateau = %5.2f' % (halfpoint, width, plateau)

    h_eff = h_total[triggers.keys()[0]].Clone()
    h_eff.SetMaximum(1.05)
    h_eff.SetMinimum(0.0)
    h_eff.GetXaxis().SetTitle("p_{T}(leading l) [GeV]")
    h_eff.GetYaxis().SetTitle("Efficiency")

    h_eff.GetXaxis().SetTitleSize(0.045)
    h_eff.GetXaxis().SetLabelSize(0.045)
    h_eff.GetXaxis().SetTitleOffset(1.3)
#    h_eff.GetXaxis().SetLabelOffset(0.04)

    h_eff.GetYaxis().SetTitleSize(0.045)
    h_eff.GetYaxis().SetLabelSize(0.045)
#    h_eff.GetYaxis().SetTitleOffset(0.14)


    can = ROOT.TCanvas("can","can", 700,700)
    
    h_eff.Draw()

    extraText = "Preliminary"
    latex1 = ROOT.TLatex()
    latex1.SetNDC()
    latex1.SetTextSize(0.04)
    latex1.SetTextAlign(11) # align right
    latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
    latex1.DrawLatex(0.72,0.96,"#bf{35.9fb^{-1}} (13TeV)")
    
    leg2 = ROOT.TLegend(0.50,0.45-0.04*len(triggers.keys()),0.90,0.45)
    leg2.SetFillColor(ROOT.kWhite)
    leg2.SetShadowColor(ROOT.kWhite)
    leg2.SetBorderSize(0)
    leg2.SetTextSize(0.035)


    for trigger in sorted(triggers.keys()):
        tEff[trigger].SetFillColor(0)
        tEff[trigger].SetMarkerColor(colors[trigger])
        tEff[trigger].SetLineColor(colors[trigger])
        tEff[trigger].SetMarkerStyle(markers[trigger])
        tEff[trigger].Draw("same")   
        
        niceName = "#bf{%s}"%trigger.replace("_"," ").replace("add","+ ").replace("singleLep","1l")
        
        leg2.AddEntry(tEff[trigger], niceName) 
    
    leg2.Draw()   
        
    plot_dir = os.path.join(plot_directory, "trigger", "Run2016_MET_2l", "turnOn", c)
    if not os.path.isdir(plot_dir): os.makedirs(plot_dir)
    for f in ['.png','.pdf','.root']:
        can.Print(plot_dir+"/%s_lep_pt_comp"%sample.name+f)


    h_eff.SetMaximum(1.0)
    h_eff.SetMinimum(0.8)
    h_eff.GetXaxis().SetTitle("p_{T}(leading l) [GeV]")
    h_eff.GetYaxis().SetTitle("Efficiency")

    h_eff.GetXaxis().SetTitleSize(0.045)
    h_eff.GetXaxis().SetLabelSize(0.045)
    h_eff.GetXaxis().SetTitleOffset(1.3)

    h_eff.GetYaxis().SetTitleSize(0.045)
    h_eff.GetYaxis().SetLabelSize(0.045)

    can = ROOT.TCanvas("can","can", 700,700)

    h_eff.Draw()

    extraText = "Preliminary"
    latex1 = ROOT.TLatex()
    latex1.SetNDC()
    latex1.SetTextSize(0.04)
    latex1.SetTextAlign(11) # align right
    latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
    latex1.DrawLatex(0.72,0.96,"#bf{35.9fb^{-1}} (13TeV)")

    for trigger in sorted(triggers.keys()):
        tEff[trigger].SetFillColor(0)
        tEff[trigger].SetMarkerColor(colors[trigger])
        tEff[trigger].SetLineColor(colors[trigger])
        tEff[trigger].SetMarkerStyle(markers[trigger])
        tEff[trigger].Draw("same")

        niceName = "#bf{%s}"%trigger.replace("_"," ").replace("add","+ ").replace("singleLep","1l")

    leg2.Draw()

    for f in ['.png','.pdf','.root']:
        can.Print(plot_dir+"/%s_lep_pt_comp_zoom"%sample.name+f)


