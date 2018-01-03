import ROOT
import os
import shutil

from RootTools.core.standard    import *
from TopEFT.analysis.getResults import getResult
from TopEFT.Tools.user          import combineReleaseLocation, analysis_results, plot_directory
from functools import partial

from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--plot_directory',     action='store',      default='NLL_plots')
argParser.add_argument('--useBestFit', action='store_true', help="Use best fit value? Default is r=1")
args = argParser.parse_args()

def Eval(obj, x, params):
    return obj.Eval(x[0])

fitKey = "dNLL_postfit_r1" if not args.useBestFit else "dNLL_bestfit"

# get the absolute post fit NLL value of pure ttZ
ttZ_res = getResult(ewkDM_ttZ_ll_noH)
ttZ_NLL_abs = float(ttZ_res["NLL_prefit"]) + float(ttZ_res[fitKey])

print "Max Likelihood ttZ SM"
print ttZ_NLL_abs

signals = [ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767, ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767]
signals = [ewkDM_ttZ_ll_noH_DC2V_m0p25, ewkDM_ttZ_ll_noH_DC2V_m0p15, ewkDM_ttZ_ll_noH, ewkDM_ttZ_ll_noH_DC2V_0p05, ewkDM_ttZ_ll_noH_DC2V_0p10, ewkDM_ttZ_ll_noH_DC2V_0p20, ewkDM_ttZ_ll_noH_DC2V_0p30]

absNLL = []
for s in signals:
    res = getResult(s)
    absNLL.append(float(res["NLL_prefit"]) + float(res[fitKey]))

ttZ_NLL_abs = min(absNLL)

# get the delta NLL values for the signals, all w.r.t the (expected) global minimum of pure ttZ
NLL_list = []
for s in signals:
    res = getResult(s)
    print "Max Likelihood for %s:"%s.name
    print float(res["NLL_prefit"]) + float(res[fitKey])
    NLL_list.append(float(res["NLL_prefit"]) + float(res[fitKey]) - ttZ_NLL_abs )

# Create histogram and function to fit
hist = ROOT.TH1F("NLL","", 41,-1,1)
hist.SetStats(0)
#hist = ROOT.TGraph()

fun = ROOT.TF1("f_1", "[0] + [1]*x + [2]*x**2", -1., 1.)
#fun = ROOT.TF1("f_1", "[0] + [1]*x + [2]*x**2 +[4]*x**4", -1., 1.)
fun.SetLineColor(ROOT.kBlack)
fun.SetLineStyle(3)

# this needs to be automatized

x_values = [-0.25, -0.15, 0, 0.05, 0.10, 0.2, 0.3]
for i, x in enumerate(x_values):
    print x, 2*NLL_list[i]
    if NLL_list[i]<0.001: NLL_list[i]=0.001
    #hist.SetPoint(i+1, x, 2*NLL_list[i])
    b = hist.GetXaxis().FindBin(x)
    hist.SetBinContent(b, 2*NLL_list[i])
    hist.SetBinError(b, 0.1 * 2*NLL_list[i])
    ## impose symmetry:
    #hist.Fill(-x, 2*NLL_list[i])

# fit the function
hist.Fit(fun, "S")

#spline = ROOT.TSpline3("spline3", hist)
#fun = ROOT.TF1('f_1', partial(Eval, spline), hist.GetX()[0], hist.GetX()[hist.GetN() - 1], 1)
#fun.SetLineColor(ROOT.kBlack)
#fun.SetLineStyle(3)

#ROOT.gROOT.SetBatch(True)
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()

# plot stuff, add vertical lines at 1, 2, 3 sigma
can = ROOT.TCanvas("can","",700,700)

hist.SetMinimum(0)
hist.SetMaximum(30)
hist.GetXaxis().SetRangeUser(-0.3,0.3) 
hist.SetLineWidth(0)
hist.SetMarkerStyle(10)
#hist.GetYaxis().SetTitle("-2 log #frac{L(BSM)}{L(SM)}")
hist.GetYaxis().SetTitle("-2 #DeltalnL")
hist.GetYaxis().SetTitleOffset(1.5)
hist.GetXaxis().SetTitle("C_{2V}")
hist.Draw()

#fun.Draw("same")


one = ROOT.TF1("one","[0]",-1,1)
one.SetParameter(0,1)
one.SetLineColor(ROOT.kOrange)

four = ROOT.TF1("four","[0]",-1,1)
four.SetParameter(0,4)
four.SetLineColor(ROOT.kOrange+10)

nine = ROOT.TF1("nine","[0]",-1,1)
nine.SetParameter(0,9)
nine.SetLineColor(ROOT.kRed+1)

plus1   = ROOT.TLine(fun.GetX(1,0,1),0,fun.GetX(1,0,1),1) 
minus1  = ROOT.TLine(fun.GetX(1,-1,0),0,fun.GetX(1,-1,0),1) 
plus1.SetLineColor(ROOT.kOrange)
minus1.SetLineColor(ROOT.kOrange)

plus2   = ROOT.TLine(fun.GetX(4,0,1),0,fun.GetX(4,0,1),4) 
minus2  = ROOT.TLine(fun.GetX(4,-0.5,0),0,fun.GetX(4,-0.5,0),4)
plus2.SetLineColor(ROOT.kOrange+10)
minus2.SetLineColor(ROOT.kOrange+10)

#plus3   = ROOT.TLine(fun.GetX(9,0,1),0,fun.GetX(9,0,1),9) 
#minus3  = ROOT.TLine(fun.GetX(9,-1,0),0,fun.GetX(9,-1,0),9)
#plus3.SetLineColor(ROOT.kRed+1)
#minus3.SetLineColor(ROOT.kRed+1)

one.SetMarkerSize(0)
four.SetMarkerSize(0)

for l in [one, four, plus1, plus2, minus1, minus2]:
    l.SetLineStyle(2)
    l.SetLineWidth(2)
    l.Draw('same')


none = ROOT.TH1F()

leg = ROOT.TLegend(0.2,0.74,0.4,0.9)
leg.SetBorderSize(1)
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.SetTextSize(0.035)
leg.AddEntry(none,"#DeltaC_{1A} = 0.",'')
leg.AddEntry(none,"#DeltaC_{1V} = 0.",'')
leg.AddEntry(none,"C_{2A} = 0.",'')
if args.useBestFit:
    leg.AddEntry(none,"r = best fit",'')
else:
    leg.AddEntry(none,"r = 1",'')
leg.Draw()

leg2 = ROOT.TLegend(0.55,0.74,0.75,0.9)
leg2.SetBorderSize(1)
leg2.SetFillColor(0)
leg2.SetLineColor(0)
leg2.SetTextSize(0.035)
leg2.AddEntry(hist, "Pseudo-Data results")
leg2.AddEntry(fun, "Pol. fit")
leg2.AddEntry(one, "68 %")
leg2.AddEntry(four,"95 %")
leg2.Draw()

extraText = "Simulation"

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11) # align right
latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
latex1.DrawLatex(0.73,0.96,"#bf{35.9fb^{-1}} (13TeV)")

plot_dir = os.path.join(plot_directory,args.plot_directory)
if not os.path.isdir(plot_dir):
    os.makedirs(plot_dir)

plot_dir += '/NLL_pseudoDataPriv'
if args.useBestFit:
    plot_dir += '_bestFit'

filetypes = [".pdf",".png",".root"]

for f in filetypes:
    can.Print(plot_dir+f)


