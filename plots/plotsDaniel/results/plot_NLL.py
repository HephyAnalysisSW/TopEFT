import ROOT
import os
import shutil

from RootTools.core.standard    import *
from TopEFT.analysis.getResults import getResult
from TopEFT.tools.user          import combineReleaseLocation, analysis_results, plot_directory

from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--plot_directory',     action='store',      default='NLL_plots')
argParser.add_argument('--useBestFit', action='store_true', help="Use best fit value? Default is r=1")
args = argParser.parse_args()

fitKey = "dNLL_postfit_r1" if not args.useBestFit else "dNLL_bestfit"

ttZ_res = getResult(ewkDM_ttZ_ll)
ttZ_NLL_abs = float(ttZ_res["NLL_prefit"]) + float(ttZ_res[fitKey])

signals = [ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767, ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767]

NLL_list = []

for s in signals:
    res = getResult(s)
    NLL_list.append(float(res["NLL_prefit"]) + float(res[fitKey]) - ttZ_NLL_abs )

hist = ROOT.TH1F("NLL","", 21,-1,1)
hist.SetStats(0)
fun = ROOT.TF1("f_1", "[0] + [1]*x + [2]*x**2", -1., 1.)
fun.SetLineColor(ROOT.kBlue)

hist.Fill(0,0.001)
hist.Fill(-0.1767, 2*NLL_list[0])
hist.Fill(0.1767, 2*NLL_list[1])

hist.Fit(fun, "S")

#ROOT.gROOT.SetBatch(True)
ROOT.gROOT.LoadMacro('../../../../RootTools/plot/scripts/tdrstyle.C')
ROOT.setTDRStyle()


can = ROOT.TCanvas("can","",700,700)

hist.SetMinimum(0)
hist.SetMaximum(30)
hist.GetXaxis().SetRangeUser(-0.3,0.3) 
hist.SetLineWidth(0)
hist.SetMarkerStyle(4)
hist.GetYaxis().SetTitle("-2#DeltaNLL")
hist.GetXaxis().SetTitle("C_{2V}")
hist.Draw()



one = ROOT.TF1("one","[0]",-1,1)
one.SetParameter(0,1)
one.SetLineWidth(2)
one.SetLineColor(ROOT.kGray+1)
one.SetLineStyle(3)
one.Draw('same')

four = ROOT.TF1("four","[0]",-1,1)
four.SetParameter(0,4)
four.SetLineWidth(2)
four.SetLineColor(ROOT.kGray+2)
four.SetLineStyle(3)
four.Draw('same')

nine = ROOT.TF1("nine","[0]",-1,1)
nine.SetParameter(0,9)
nine.SetLineWidth(2)
nine.SetLineColor(ROOT.kGray+3)
nine.SetLineStyle(3)
nine.Draw('same')


#leg_size = 0.04 * 4
#
#
#leg = ROOT.TLegend(0.2,0.9-leg_size,0.4,0.9)
#leg.SetBorderSize(1)
#leg.SetFillColor(0)
#leg.SetLineColor(0)
#leg.SetTextSize(0.035)
#
#leg.AddEntry(exp,"Expected",'l')
#leg.AddEntry(obs,"Observed",'l')
#leg.AddEntry(exp1Sigma,"Exp #pm 1 #sigma",'f')
#leg.AddEntry(exp2Sigma,"Exp #pm 2 #sigma",'f')
#leg.Draw()

none = ROOT.TH1F()


extraText = "Preliminary"

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11) # align right
latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{'+extraText+'}}')
latex1.DrawLatex(0.73,0.96,"#bf{35.9fb^{-1}} (13TeV)")

plot_dir = os.path.join(plot_directory,args.plot_directory)
if not os.path.isdir(plot_dir):
    os.makedirs(plot_dir)

plot_dir += '/NLL_first'
if args.useBestFit:
    plot_dir += '_bestFit'

filetypes = [".pdf",".png",".root"]

for f in filetypes:
    can.Print(plot_dir+f)


