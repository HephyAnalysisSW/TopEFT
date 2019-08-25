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
from TopEFT.Tools.user            import plot_directory
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.cutInterpreter  import cutInterpreter
from TopEFT.Tools.u_float         import u_float
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, writeObjToFile
from TopEFT.Tools.user            import plot_directory

from array import array

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--leg',                    action='store',         nargs='?',              choices=["E","M"],     default='E', help="electron or muon?")
    argParser.add_argument('--data',                   action='store_true',          help="run on data?")
    argParser.add_argument('--small',                  action='store_true',          help="small?")
    argParser.add_argument('--Run2017',                action='store_true',          help="2017 data?")

    return argParser

options = get_parser().parse_args()



ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()

ROOT.gStyle.SetPaintTextFormat("1.2f")

ROOT.gStyle.SetOptFit(0)
ROOT.gStyle.SetOptStat(0)

channel = options.leg # "M" or "E"
small = options.small

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

#postProcessing_directory = "TopEFT_PP_v12/dilep/"
#from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

#data_directory = '/afs/hephy.at/data/rschoefbeck01/cmgTuples/'
#postProcessing_directory = "TopEFT_PP_2017_v19/dilep/"
#from  TopEFT.samples.cmgTuples_Data25ns_92X_Run2017_postProcessed_trigger import *
#
#data_directory = '/afs/hephy.at/data/rschoefbeck01/cmgTuples/'
#postProcessing_directory = "TopEFT_PP_2017_v19/dilep/"
#from TopEFT.samples.cmgTuples_Summer17_mAODv2_postProcessed import *

data_directory = '/afs/hephy.at/data/rschoefbeck01/cmgTuples/'
postProcessing_directory = "TopEFT_PP_v14/dilep/"
from  TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *

data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_v14/dilep/"
from  TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

# presel for measuring efficiencies in single lep datasets
presel = "nlep==2&&nGoodElectrons==1&&nGoodMuons==1&&(lep_pdgId[0]*lep_pdgId[1])<0"

channels = {'all':'(1)'}

trigger_singleEle = ["HLT_Ele27_WPTight_Gsf", "HLT_Ele25_eta2p1_WPTight_Gsf", "HLT_Ele27_eta2p1_WPLoose_Gsf"]
trigger_singleMu  = ["HLT_IsoMu24", "HLT_IsoTkMu24"]

#trigger_singleEle_2017 = ["HLT_Ele35_WPTight_Gsf"]
trigger_singleEle_2017 = ["HLT_ele"]#, "HLT_ele_pre"]
trigger_singleMu_2017  = ["HLT_mu"]#["HLT_IsoMu27"]#, "HLT_IsoMu30"]


colors  = {"singleLep": ROOT.kRed+1, "singleLep_addNonIso": ROOT.kOrange+1, "singleLep_addDiLep":ROOT.kBlue+1, "singleLep_addDiLep_addTriLep":ROOT.kGreen+1, "SingleMu":ROOT.kRed+1, "SingleMuTTZ":ROOT.kBlue+1,"SingleEle":ROOT.kRed+1,"SingleEleTTZ":ROOT.kBlue+1}
markers = {"singleLep": 20, "singleLep_addNonIso": 21, "singleLep_addDiLep": 22, "singleLep_addDiLep_addTriLep": 23, "SingleMu":23, "SingleMuTTZ":22, "SingleEle":23, "SingleEleTTZ":22}

binning = [0,10,20,30,40,50,60,70,80,100,120,150,200,500]
binning = (len(binning)-1, array('d', binning))

#sample = MET_Run2016

if options.Run2017:
    lumi = 38.7
else:
    lumi = 35.9

if channel == "M":
    triggerLeg = "singleMuon"
    pdgId = 13
    #measure in singleEle data
    sample = ( SingleElectron_Run2016 if not options.Run2017 else SingleElectron_Run2017 ) if options.data else ( TTLep_pow if not options.Run2017 else TT_pow_17)
    #sample = WW_17
    triggers = trigger_singleEle if not options.Run2017 else trigger_singleEle_2017
    presel += "&&(%s)"%("||".join(triggers))
    binning2D = ([10,15,20,25,40,60,80,100,200,500],[0,1.2,2.1,2.4])
elif channel == "E":
    triggerLeg = "singleElectron"
    pdgId = 11
    #measure in singleMu data
    sample = ( SingleMuon_Run2016 if not options.Run2017 else SingleMuon_Run2017 ) if options.data else ( TTLep_pow if not options.Run2017 else TT_pow_17)
    #sample = WW_17
    triggers = trigger_singleMu if not options.Run2017 else trigger_singleMu_2017
    presel += "&&(%s)"%("||".join(triggers))
    binning2D = ([10,15,20,25,40,60,80,100,200,500],[0,1.479,2.5])

#sample = TTLep_pow

print "Getting events"

print sample.name
print triggers
print presel

if options.small:
    sample.reduceFiles(to=1)

s = sample.chain
s.Draw('>>eList',presel)
elist = ROOT.gDirectory.Get("eList")
number_events = elist.GetN()

print "Preparing Histograms"

sample.hist     = ROOT.TH1D("%s"%(sample.name),"", *binning)
sample.hist_ref = ROOT.TH1D("%s_%s"%(sample.name, "ref"),"", *binning)

print "Preparing 2D Histograms"

#get dummy 2d histograms
eta = "lep_eta[0]"
pt  = "lep_pt[0]"

binningArgs = (len(binning2D[0])-1, array('d', binning2D[0]), len(binning2D[1])-1, array('d', binning2D[1]))

sample.hist2D       = ROOT.TH2D("%s_2D"%(sample.name),"", *binningArgs) #sample.get2DHistoFromDraw("abs(%s):%s"%(eta,pt), binning2D, selectionString=presel+"&met_pt>1000", weightString=None, binningIsExplicit=True, isProfile=False)
sample.hist2D_ref   = ROOT.TH2D("%s_%s_2D"%(sample.name, "ref"),"", *binningArgs) #sample.get2DHistoFromDraw("abs(%s):%s"%(eta,pt), binning2D, selectionString=presel+"&met_pt>1000", weightString=None, binningIsExplicit=True, isProfile=False)

sample.hist2D.Reset()
sample.hist2D_ref.Reset()

print "Found %s events after preslection"%number_events

if small:
    number_events = 10000 # for test
    triggerLeg += '_small'

print "Looping over %s events"%number_events

passed = 0

for i in range(number_events):
    if i>0 and (i%10000)==0:
        print "Done with",i
    
    s.GetEntry(elist.GetEntry(i))
    
    m_index = -1
    if abs(s.lep_pdgId[0]) == pdgId: m_index = 0
    elif abs(s.lep_pdgId[1]) == pdgId: m_index = 1
    
    #print m_index, abs(s.lep_pdgId[0]), abs(s.lep_pdgId[1])
    if m_index < 0: print "weird"
    
    muon = {}
    electron = {}
    
    lep_pt = s.lep_pt[m_index]
    lep_eta = abs(s.lep_eta[m_index])
    if lep_pt > 500: lep_pt = 499.
    if channel == "M":
        if s.lep_matchedTrgObj1Mu[m_index]>0:
            sample.hist.Fill(lep_pt)
            sample.hist2D.Fill(lep_pt, lep_eta)
            passed += 1
    elif channel == "E":
        if s.lep_matchedTrgObj1El[m_index]>0:
            sample.hist.Fill(lep_pt)
            sample.hist2D.Fill(lep_pt, lep_eta)
            passed += 1
    sample.hist_ref.Fill(lep_pt)
    sample.hist2D_ref.Fill(lep_pt, lep_eta)

print float(passed)/number_events

h_ratio = sample.hist.Clone()
h_ratio.Divide(sample.hist_ref)

tEff = ROOT.TEfficiency(sample.hist, sample.hist_ref)
tEff.Draw()

h_eff = sample.hist_ref.Clone()
h_eff.SetMaximum(1.05)
h_eff.SetMinimum(0.0)
    
h_eff.GetXaxis().SetTitle("p_{T}(l) [GeV]")
h_eff.GetYaxis().SetTitle("Efficiency")

h_eff.GetXaxis().SetTitleSize(0.045)
h_eff.GetXaxis().SetLabelSize(0.045)
h_eff.GetXaxis().SetTitleOffset(1.3)

h_eff.GetYaxis().SetTitleSize(0.045)
h_eff.GetYaxis().SetLabelSize(0.045)
h_eff.GetXaxis().SetMoreLogLabels()
h_eff.GetXaxis().SetNoExponent()

h_eff.SetMarkerSize(0)
h_eff.SetLineWidth(0)

can = ROOT.TCanvas("can","can", 700,700)
can.SetLogx()

h_eff.Draw()

extraText = "Preliminary"
latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11) # align right
latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
latex1.DrawLatex(0.72,0.96,"#bf{%sfb^{-1}} (13TeV)"%lumi)

color  = ROOT.kOrange + 1
marker = 20

tEff.SetFillColor(0)
tEff.SetMarkerColor(color)
tEff.SetLineColor(color)
tEff.SetMarkerStyle(marker)
tEff.Draw("same")   

plot_dir = os.path.join(plot_directory, "trigger_TnP_2017", sample.name)
if not os.path.isdir(plot_dir): os.makedirs(plot_dir)
for f in ['.png','.pdf','.root']:
    can.Print(plot_dir+"/%s_lep_pt"%triggerLeg+f)


# 2D business
t_eff = ROOT.TEfficiency(sample.hist2D, sample.hist2D_ref)

h_ratio = sample.hist2D.Clone()
h_ratio.SetName("eff")
h_ratio.Divide(sample.hist2D_ref)


can = ROOT.TCanvas("can","can", 700,700)
can.SetRightMargin(0.15)
can.SetLogx()
h_ratio.GetXaxis().SetNdivisions(712)
h_ratio.GetXaxis().SetMoreLogLabels()
h_ratio.GetXaxis().SetNoExponent()
h_ratio.Draw("colz texte")

#t_eff.Draw("colz same")
h_eff = t_eff.CreateHistogram()
for x in binning2D[0]:
    for y in binning2D[1]:
        x_bin = h_eff.GetXaxis().FindBin(x)
        y_bin = h_eff.GetYaxis().FindBin(y)
        n_bin = t_eff.FindFixBin(x,y)
        err = ( t_eff.GetEfficiencyErrorUp(n_bin) + t_eff.GetEfficiencyErrorLow(n_bin) ) / 2.
        h_eff.SetBinError(x_bin,y_bin,err)



h_eff.Draw("colz texte same")
#print h_eff.GetBinContent(4,4)
#print h_eff.GetBinError(4,4)
#raise(NotImplementedError, "just stop here")

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
latex1.DrawLatex(0.72,0.96,"#bf{%sfb^{-1}} (13TeV)"%lumi)

filename = "%s_lep_pt_vs_lep_eta"%(triggerLeg)

for f in ['.png','.pdf']:
    can.RedrawAxis()
    can.Print(plot_dir+"/%s"%filename+f)

writeObjToFile(plot_dir+"/%s.root"%filename, h_ratio)


#    
#    leg2 = ROOT.TLegend(0.50,0.45-0.04*len(triggers.keys()),0.90,0.45)
#    leg2.SetFillColor(ROOT.kWhite)
#    leg2.SetShadowColor(ROOT.kWhite)
#    leg2.SetBorderSize(0)
#    leg2.SetTextSize(0.035)
#
#
#    for trigger in sorted(triggers.keys()):
#        color = colors[trigger] if trigger in colors.keys() else ROOT.kOrange+1
#        marker = markers[trigger] if trigger in markers.keys() else 20
#        tEff_muon[trigger].SetFillColor(0)
#        tEff_muon[trigger].SetMarkerColor(color)
#        tEff_muon[trigger].SetLineColor(color)
#        tEff_muon[trigger].SetMarkerStyle(marker)
#        tEff_muon[trigger].Draw("same")   
#        
#        niceName = "#bf{%s}"%trigger.replace("_"," ").replace("add","+ ").replace("singleLep","1l")
#        
#        leg2.AddEntry(tEff_muon[trigger], niceName) 
#    
#    leg2.Draw()   
#        
#    plot_dir = os.path.join(plot_directory, "trigger", sample.name, "turnOn", c)
#    if not os.path.isdir(plot_dir): os.makedirs(plot_dir)
#    for f in ['.png','.pdf','.root']:
#        can.Print(plot_dir+"/%s_muon_pt"%triggerLeg+f)
#
#
#    del can
#
#    can = ROOT.TCanvas("can","can", 700,700)
#    can.SetLogx()
#    h_eff.Draw()
#
#    extraText = "Preliminary"
#    latex1 = ROOT.TLatex()
#    latex1.SetNDC()
#    latex1.SetTextSize(0.04)
#    latex1.SetTextAlign(11) # align right
#    latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
#    latex1.DrawLatex(0.72,0.96,"#bf{35.9fb^{-1}} (13TeV)")
#
#    leg2 = ROOT.TLegend(0.50,0.45-0.04*len(triggers.keys()),0.90,0.45)
#    leg2.SetFillColor(ROOT.kWhite)
#    leg2.SetShadowColor(ROOT.kWhite)
#    leg2.SetBorderSize(0)
#    leg2.SetTextSize(0.035)
#
#
#    for trigger in sorted(triggers.keys()):
#        color = colors[trigger] if trigger in colors.keys() else ROOT.kOrange+1
#        marker = markers[trigger] if trigger in markers.keys() else 20
#        tEff_electron[trigger].SetFillColor(0)
#        tEff_electron[trigger].SetMarkerColor(color)
#        tEff_electron[trigger].SetLineColor(color)
#        tEff_electron[trigger].SetMarkerStyle(marker)
#        tEff_electron[trigger].Draw("same")
#
#        niceName = "#bf{%s}"%trigger.replace("_"," ").replace("add","+ ").replace("singleLep","1l")
#
#        leg2.AddEntry(tEff_electron[trigger], niceName)
#
#    leg2.Draw()
#
#    plot_dir = os.path.join(plot_directory, "trigger", sample.name, "turnOn", c)
#    if not os.path.isdir(plot_dir): os.makedirs(plot_dir)
#    for f in ['.png','.pdf','.root']:
#        can.Print(plot_dir+"/%s_electron_pt"%triggerLeg+f)

