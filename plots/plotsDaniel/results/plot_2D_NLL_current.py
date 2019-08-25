import ROOT
import os
import ctypes
import shutil

from RootTools.core.standard    import *
from TopEFT.Analysis.run.getResults import getResult
from TopEFT.Tools.user          import combineReleaseLocation, analysis_results, plot_directory
from functools import partial
from TopEFT.Tools.niceColorPalette import niceColorPalette

from TopEFT.Analysis.Setup import Setup

setup = Setup()

# Plot style
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()
ROOT.gStyle.SetNumberContours(255)


#from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *
from TopEFT.samples.gen_fwlite_benchmarks import *

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--plot_directory',     action='store',      default='NLL_plots')
argParser.add_argument('--useBestFit', action='store_true', help="Use best fit value? Default is r=1")
args = argParser.parse_args()

def Eval(obj, x, params):
    return obj.Eval(x[0])

def toGraph2D(name,title,length,x,y,z):
    result = ROOT.TGraph2D(length)
    result.SetName(name)
    result.SetTitle(title)
    for i in range(length):
        result.SetPoint(i,x[i],y[i],z[i])
    h = result.GetHistogram()
    h.SetMinimum(min(z))
    h.SetMaximum(max(z))
    c = ROOT.TCanvas()
    result.Draw()
    del c
    #res = ROOT.TGraphDelaunay(result)
    return result


fitKey = "dNLL_postfit_r1" if not args.useBestFit else "dNLL_bestfit"

# get the absolute post fit NLL value of pure ttZ
#ttZ_res = getResult(ewkDM_ttZ_ll_noH)
ttZ_res = getResult(dim6top_LO_ttZ_ll_cpQM_0p00_cpt_0p00)
ttZ_NLL_abs = float(ttZ_res["NLL_prefit"]) + float(ttZ_res[fitKey])

print "Max Likelihood ttZ SM"
print ttZ_NLL_abs

# load all samples, omit the 1/1 point
#signals = [ x for x in allSamples_dim6top if not x.name.startswith('dim6top_LO_ttZ_ll_ctZ_1p00_ctZI_1p00') ]
signals = [ x for x in dim6top_currents ]


ctZ_values = []
ctZi_values = []

for s in signals:
    s.ctZ   = float(s.name.split('_')[5].replace('p','.').replace('m','-'))
    if not (s.ctZ in ctZ_values):
        ctZ_values.append(s.ctZ)
    s.ctZi  = float(s.name.split('_')[7].replace('p','.').replace('m','-'))
    if not (s.ctZi in ctZi_values):
        ctZi_values.append(s.ctZi)


ctZ_values = sorted(ctZ_values)
ctZi_values = sorted(ctZi_values)

x_min = ctZ_values[0] - (abs(ctZ_values[0]) - abs(ctZ_values[1])) / 2
x_max = ctZ_values[-1] + (abs(ctZ_values[-1]) - abs(ctZ_values[-2])) / 2
nbins_x = len(ctZ_values)
bin_size_x = (x_max - x_min) / nbins_x

y_min = ctZi_values[0] - (abs(ctZi_values[0]) - abs(ctZi_values[1])) / 2
y_max = ctZi_values[-1] + (abs(ctZi_values[-1]) - abs(ctZi_values[-2])) / 2
nbins_y = len(ctZi_values)
bin_size_y = (y_max - y_min) / nbins_y


x = []
y = []
z = []

for i,s in enumerate(signals):
    res = getResult(s)
    if type(res) == type({}):
        limit = float(res["NLL_prefit"]) + float(res[fitKey]) - ttZ_NLL_abs
        if limit >= 0:
            print s.name, round(2*limit,2)
            z.append(2*limit)
            x.append(s.ctZ)
            y.append(s.ctZi)
        elif limit > -0.01 and limit < 0:
            print s.name, 0
            z.append(0)
            x.append(s.ctZ)
            y.append(s.ctZi)
        else:
            print "No good result found for %s, results is %s"%(s.name, limit)
    else:
        print "No results for %s found"%s.name

proc = "ttZ"

a = toGraph2D(proc, proc, len(x), x, y, z)
nxbins = max(1, min(500, nbins_x*3))
nybins = max(1, min(500, nbins_y*3))

a.SetNpx(nxbins)
a.SetNpy(nybins)
hist = a.GetHistogram().Clone()
hist.GetXaxis().SetTitle("C_{pQM}")
hist.GetXaxis().SetNdivisions(505)
hist.GetYaxis().SetTitle("C_{pt}")
hist.GetYaxis().SetNdivisions(505)
hist.GetYaxis().SetTitleOffset(1.0)
hist.GetZaxis().SetTitle("-2 #DeltalnL")
hist.GetZaxis().SetTitleOffset(1.2)
hist.SetStats(0)
hist.Smooth()

cans = ROOT.TCanvas("can_%s"%proc,"",700,700)

contours = {'ttZ': [-0.1,0.,1.,4.]}
drawContours = True
if drawContours:
    histsForCont = hist.Clone()
    c_contlist = ((ctypes.c_double)*(len(contours[proc])))(*contours[proc])
    histsForCont.SetContour(len(c_contlist),c_contlist)
    histsForCont.Draw("contzlist")
    cans.Update()
    conts = ROOT.gROOT.GetListOfSpecials().FindObject("contours")
    cont_m2 = conts.At(0).Clone()
    cont_m1 = conts.At(1).Clone()
    cont_p1 = conts.At(2).Clone()
    cont_p2 = conts.At(3).Clone()

pads = ROOT.TPad("pad_%s"%proc,"",0.,0.,1.,1.)
pads.SetRightMargin(0.20)
pads.SetLeftMargin(0.14)
pads.SetTopMargin(0.11)
pads.Draw()
pads.cd()

hist.SetMaximum(99.95) #1.95
hist.SetMinimum(0.)


hist.Draw("colz")

if drawContours:
    for conts in [cont_m1, cont_p1]:
        for cont in conts:
            cont.SetLineColor(ROOT.kRed)
            cont.SetLineWidth(2)
            cont.SetLineStyle(7)
            cont.Draw("same")
    for conts in [cont_m2, cont_p2]:
        for cont in conts:
            cont.SetLineColor(ROOT.kOrange)
            cont.SetLineWidth(2)
            cont.SetLineStyle(7)
            cont.Draw("same")

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11)

latex1.DrawLatex(0.14,0.96,'CMS #bf{#it{Simulation}}')
latex1.DrawLatex(0.14,0.92,'#bf{dim6top_LO model}')
print setup.lumi['3mu']/1e3
latex1.DrawLatex(0.6,0.96,'#bf{%s fb^{-1} MC (13TeV)}'%(setup.lumi['3mu']/1e3))


plotDir = os.path.join( plot_directory,"NLL_plots_2D/" )
if not os.path.isdir(plotDir):
    os.makedirs(plotDir)

for e in [".png",".pdf",".root"]:
    cans.Print(plotDir+"dim6top_LO_current_%s"%setup.name+e)

