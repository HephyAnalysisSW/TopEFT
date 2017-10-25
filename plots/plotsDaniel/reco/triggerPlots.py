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

#ROOT.gROOT.SetBatch(True)
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()

postProcessing_directory = "TopEFT_PP_v4/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

signal  = [ TTZtoLLNuNu ]
bkg     = [ TTW, WZ ]#, TTX, rare ]

presel = "nlep==3&&lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10&&Z_mass>0&&abs(Z_mass-91.2)<10"

channels = {'eee':'nGoodElectrons==3','eemu':'nGoodElectrons==2&&nGoodMuons==1','emumu':'nGoodElectrons==1&&nGoodMuons==2','mumumu':'nGoodElectrons==0&&nGoodMuons==3', 'all':'(1)'}
#channels = {'all':'(1)'}

btag = "nBTag"

regions = [\
            "njet==2&&%s==0"%btag,
            "njet==3&&%s==0"%btag,
            "njet>=4&&%s==0"%btag,
            "njet==2&&%s==1"%btag,
            "njet==3&&%s==1"%btag,
            "njet>=4&&%s==1"%btag,
            "njet==2&&%s>=2"%btag,
            "njet==3&&%s>=2"%btag,
            "njet>=4&&%s>=2"%btag,
            ]

nReg = len(regions)

singleMuTriggers    = ["HLT_IsoMu22", "HLT_IsoTkMu22", "HLT_IsoMu22_eta2p1", "HLT_IsoTkMu22_eta2p1", "HLT_IsoMu24", "HLT_IsoTkMu24"]
singleEleTriggers   = ["HLT_Ele27_WPTight_Gsf", "HLT_Ele25_eta2p1_WPTight_Gsf", "HLT_Ele27_eta2p1_WPLoose_Gsf"]
diMuTriggers        = ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ"," HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ"]
diEleTriggers       = ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"]
EMuTriggers         = ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL", "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ"]
trilepTriggers      = ["HLT_DiMu9_Ele9_CaloIdL_TrackIdL", "HLT_Mu8_DiEle12_CaloIdL_TrackIdL", "HLT_TripleMu_12_10_5", "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL"]

#triggers = {"singleLep": "(HLT_SingleEleTTZ||HLT_SingleMuTTZ)"}
triggers = {"stopDilepMix": "((HLT_mumuIso||HLT_mumuNoiso)||(HLT_ee_DZ||HLT_ee_33||HLT_ee_33_MW)||(HLT_mue||HLT_mu30e30)||HLT_SingleMu_noniso||HLT_SingleEle_noniso)"}
triggers = {"ttHMix": "(%s)"%"||".join(singleMuTriggers+singleEleTriggers+diMuTriggers+diEleTriggers+EMuTriggers+trilepTriggers)}
triggers = {"ttHMix_no3l": "(%s)"%"||".join(singleMuTriggers+singleEleTriggers+diMuTriggers+diEleTriggers+EMuTriggers)}

for trigger in triggers:
    for c in channels:
        print c
    
        h_total     = ROOT.TH1F("total", "", nReg, 0, nReg)
        h_trigg     = ROOT.TH1F("trigger", "", nReg, 0, nReg)
        h_ratio     = ROOT.TH1F("eff", "", nReg, 0, nReg)
        h_ratio.Sumw2()
    
    
        for j, r in enumerate(regions):
            num = u_float(0)
            denom = u_float(0)
            for i, sample in enumerate(signal + bkg):
                print sample.name
                val = sample.getYieldFromDraw('&&'.join([presel,channels[c],r]), "weight*35.9")
                trig = sample.getYieldFromDraw('&&'.join([presel,channels[c],r, triggers[trigger]]), "weight*35.9")
                print j, val, trig
                num += u_float(val)
                denom += u_float(trig)
    
            h_total.SetBinContent(j+1, num.val)
            h_total.SetBinError(j+1, num.sigma)
            h_trigg.SetBinContent(j+1, denom.val)
            h_trigg.SetBinError(j+1, denom.sigma)        
            
    
        h_ratio = h_trigg.Clone()
        h_ratio.Divide(h_total)
        h_ratio.SetMaximum(1.04)
        h_ratio.SetMinimum(0.90)
    
        
        can = ROOT.TCanvas("can","can", 700,700)
    
        h_ratio.GetXaxis().SetTitle("region")
        h_ratio.GetYaxis().SetTitle("efficiency")
    
        #h_ratio.GetXaxis().SetTitleSize(0.13)
        #h_ratio.GetXaxis().SetLabelSize(0.11)
        #h_ratio.GetXaxis().SetLabelOffset(0.02)
        #h_ratio.GetYaxis().SetTitleSize(0.145)
        #h_ratio.GetYaxis().SetLabelSize(0.13)
        #h_ratio.GetYaxis().SetTitleOffset(0.32)
        h_ratio.GetYaxis().SetNdivisions(506)
        h_ratio.Draw("e1p")   
        
        extraText = "Preliminary"
        latex1 = ROOT.TLatex()
        latex1.SetNDC()
        latex1.SetTextSize(0.04)
        latex1.SetTextAlign(11) # align right
        latex1.DrawLatex(0.10,0.955,'CMS #bf{#it{'+extraText+'}}')
        latex1.DrawLatex(0.72,0.955,"#bf{35.9fb^{-1}} (13TeV)")
        
        plot_dir = os.path.join(plot_directory, "regionPlot", "ttZ", "trigger", c)
        if not os.path.isdir(plot_dir): os.makedirs(plot_dir)
        for f in ['.png','.pdf','.root']:
            can.Print(plot_dir+"/regions_%s"%trigger+f)
