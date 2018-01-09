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
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, writeObjToFile, getObjFromFile
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.cutInterpreter  import cutInterpreter
from TopEFT.Tools.u_float         import u_float

from array import array

from TopEFT.Tools.user            import plot_directory

postProcessing_directory = "TopEFT_PP_v14/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *


ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()

ROOT.gStyle.SetOptFit(0)
ROOT.gStyle.SetOptStat(0)

#presel = "nlep==3&&lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10&&Z_mass>0&&abs(Z_mass-91.2)<10"
presel = "nlep==3&&lep_pt[0]>40&&Z_mass>0"

channels = {'eee':'nGoodElectrons==3','eemu':'nGoodElectrons==2&&nGoodMuons==1','emumu':'nGoodElectrons==1&&nGoodMuons==2','mumumu':'nGoodElectrons==0&&nGoodMuons==3', 'all':'(1)'}

#channels = {'eee':'nGoodElectrons==3'}

#triggers_2016 = ["singleLep","singleLep_addNonIso"]
triggers_2017 = ["singleLep"]

colors  = {"MET_Run2017": ROOT.kRed+1,  "MET_Run2016": ROOT.kOrange+1,  "WJets": ROOT.kBlue+1,  "WJets_LO": ROOT.kGreen+1,  "SL_Run2017": ROOT.kRed+1,  "tt_Summer17": ROOT.kBlue+1}
markers = {"MET_Run2017": 20,           "MET_Run2016": 21,              "WJets": 22,            "WJets_LO": 23,             "SL_Run2017": 20,           "tt_Summer17": 22}


#triggers_2016 = {
#    "singleLep": "(%s)"%"||".join(singleMuTTZ+singleEleTTZ),
#    "singleLep_addNonIso": "(%s)"%"||".join(singleMuTTZ+singleMuNoIso+singleEleTTZ+singleEleNoIso),
#}

triggers = triggers_2017

efficiencies = {}

for c in ['e', 'mu']:
    efficiencies[c] = {}
    #for m in ["MET_Run2017", "MET_Run2016", "WJets", "WJets_LO"]:
    for m in ["SL_Run2017", "tt_Summer17"]:
        efficiencies[c][m] = {}
        for t in triggers:
            #efficiencies[c][m][t] = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/MET_1l/efficiencies2D/1%s/%s_%s.root"%(c,m,t), "eff")
            if m == "SL_Run2017" and c == "e":
                effDir, effFile = "SingleMuon_Run2017", "singleElectron_lep_pt_vs_lep_eta"
            if m == "SL_Run2017" and c == "mu":
                effDir, effFile = "SingleElectron_Run2017", "singleMuon_lep_pt_vs_lep_eta"
            if m == "tt_Summer17" and c == "e":
                effDir, effFile = "TT_pow_17", "singleElectron_lep_pt_vs_lep_eta"
            if m == "tt_Summer17" and c == "mu":
                effDir, effFile = "TT_pow_17", "singleMuon_lep_pt_vs_lep_eta"
                
            efficiencies[c][m][t] = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger_TnP_2017/%s/%s.root"%(effDir, effFile), "eff")

def getEfficiency(pt, eta, pdgId, trigger, measurement):
    if abs(pdgId) == 11:
        eff_map = efficiencies['e'][measurement][trigger]
    elif abs(pdgId) == 13:
        eff_map = efficiencies['mu'][measurement][trigger]
    else:
        raise(NotImplementedError, "Don't know what to do with pdgId %s"%pdgId)

    return eff_map.GetBinContent(eff_map.GetXaxis().FindBin(pt), eff_map.GetYaxis().FindBin(abs(eta)))

binning = [10,15,20,25,40,60,80,100,200]
binning = (len(binning)-1, array('d', binning))

for trigger in triggers:
    print "Working on trigger %s"%trigger
    for c in channels:
        print "... on channel %s"%c
        for sample in [TTZtoLLNuNu]:
            print "... on sample %s"%sample.name
            incl_cut    = '&&'.join([presel,channels[c]])
            
            s = sample.chain
            
            s.Draw('>>eList',incl_cut)
            elist = ROOT.gDirectory.Get("eList")
            number_events = elist.GetN()

            sample.hists = {}
            sample.hist_ref = {}
            # Define hists for the different measurements
            for i in range(3):
                sample.hists[i] = { m:ROOT.TH1F("%s_%s_%s_%s"%(sample.name, trigger, c, m),"", *binning) for m in ["SL_Run2017", "tt_Summer17"] }#["MET_Run2017", "MET_Run2016", "WJets"] }
                sample.hist_ref[i] = ROOT.TH1F("%s_%s_%s"%(sample.name, "ref", c),"", *binning)

            print "Gonna loop over %s events"%number_events
            if number_events > 1e5:
                print "This will take some time"

            for i in range(number_events):
                if i>0 and (i%10000)==0:
                    print "Done with",i
                s.GetEntry(elist.GetEntry(i))
                w = s.weight
                
                for m in ["SL_Run2017", "tt_Summer17"]:#["MET_Run2017", "MET_Run2016", "WJets"]:
                    effs = []
                    for l in range(3):
                        effs.append(getEfficiency(s.lep_pt[l], s.lep_eta[l], s.lep_pdgId[l], trigger, m))
                        #print s.lep_pt[l], s.lep_eta[l], s.lep_pdgId[l], trigger, m
                        #print getEfficiency(s.lep_pt[l], s.lep_eta[l], s.lep_pdgId[l], trigger, m)
                    eff = 1 - ( (1-effs[0]) * (1-effs[1]) * (1-effs[2]) )
                    #eff = reduce(lambda x, y: x*y, effs)
                    for j in range(3):
                    #print s.lep_pt[0], w, w*eff, eff
                        pt = s.lep_pt[j] if s.lep_pt[j]<200 else 199.
                        sample.hists[j][m].Fill(pt, w*eff)

                for j in range(3):
                    pt = s.lep_pt[j] if s.lep_pt[j]<200 else 199.
                    sample.hist_ref[j].Fill(pt, w)
            
            for j in range(3):
                sample.teffs = {}

                can = ROOT.TCanvas("can","can", 700,700)
                first = True
                
                leg2 = ROOT.TLegend(0.42,0.45-0.04*4,0.90,0.45)
                leg2.SetFillColor(ROOT.kWhite)
                leg2.SetShadowColor(ROOT.kWhite)
                leg2.SetBorderSize(0)
                leg2.SetTextSize(0.035)

                sample.hist_ref[j].SetMaximum(1.05)
                sample.hist_ref[j].SetMinimum(0.8)
                sample.hist_ref[j].SetMarkerSize(0)
                sample.hist_ref[j].SetLineWidth(0)
                sample.hist_ref[j].GetXaxis().SetTitle("p_{T}(l_{%s}) [GeV]"%(j+1))
                sample.hist_ref[j].GetYaxis().SetTitle("Efficiency")

                sample.hist_ref[j].Draw()

                leg2.AddEntry(sample.hist_ref[j], "3l eff using 1l eff map from:")
                for m in ["SL_Run2017", "tt_Summer17"]:#["MET_Run2017", "MET_Run2016", "WJets"]:
                    sample.teffs[m] = ROOT.TEfficiency(sample.hists[j][m],sample.hist_ref[j])
                    sample.teffs[m].SetFillColor(0)
                    sample.teffs[m].SetMarkerColor(colors[m])
                    sample.teffs[m].SetLineColor(colors[m])
                    sample.teffs[m].SetMarkerStyle(markers[m])

                    niceName = m.replace("_Run", " ").replace("Jets", "+jets (MC)")
                    if "Single" in niceName: niceName += " (data)"
                    leg2.AddEntry(sample.teffs[m], niceName)

                    if first and False:
                        sample.teffs[m].Draw()
                        first = False
                    else:
                        sample.teffs[m].Draw("same")

                leg2.Draw()

                extraText = "Preliminary"
                latex1 = ROOT.TLatex()
                latex1.SetNDC()
                latex1.SetTextSize(0.04)
                latex1.SetTextAlign(11) # align right
                latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
                latex1.DrawLatex(0.72,0.96,"#bf{35.9fb^{-1}} (13TeV)")


                plot_dir = os.path.join(plot_directory, "trigger_TnP_2017", "SingleLep", "efficiency", trigger, c)
                if not os.path.isdir(plot_dir): os.makedirs(plot_dir)

                for f in ['.png','.pdf','.root']:
                    can.Print(plot_dir+"/lep_pt_%s_%s"%(j,sample.name)+f)


                #sample.hists[m].Divide(sample.hist_ref)
                #sample.hists[m].SetLineColor()
                #sample.hists[m].SetLineWidth(2)

            
            

            #sample.hist = ROOT.TH1F(sample.name, "", nReg, 0, nReg)
            #sample.hist.SetFillColor(sample.color)




