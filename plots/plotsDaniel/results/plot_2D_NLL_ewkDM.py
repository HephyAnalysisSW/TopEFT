import ROOT
import os
import ctypes
import shutil
from functools                      import partial

from RootTools.core.standard        import *

from TopEFT.Analysis.run.getResults import getResult
from TopEFT.Tools.user              import combineReleaseLocation, analysis_results, plot_directory
from TopEFT.Tools.niceColorPalette  import niceColorPalette
from TopEFT.Tools.helpers           import getCouplingFromName
from TopEFT.Analysis.Setup          import Setup

from TopEFT.samples.gen_fwlite_benchmarks import *


setup = Setup()

# Plot style
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()
ROOT.gStyle.SetNumberContours(255)


import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--plot_directory',     action='store',      default='NLL_plots')
argParser.add_argument('--useBestFit', action='store_true', help="Use best fit value? Default is r=1")
argParser.add_argument('--smooth', action='store_true', help="Use histogram smoothing? Potentially dangerous (oversmoothing)!")
argParser.add_argument('--plane', action='store', choices=["current", "dipole"], default = "current", help="Current of dipole plane?")
args = argParser.parse_args()

postFix = "_fine"

def Eval(obj, x, params):
    return obj.Eval(x[0])

def toGraph2D(name,title,length,x,y,z):
    result = ROOT.TGraph2D(length)
    debug = ROOT.TGraph()
    result.SetName(name)
    result.SetTitle(title)
    for i in range(length):
        result.SetPoint(i, x[i], y[i], z[i])
        debug.SetPoint(i, x[i], y[i])
    c = ROOT.TCanvas()
    result.Draw()
    debug.Draw()
    del c
    #res = ROOT.TGraphDelaunay(result)
    return result,debug


fitKey = "dNLL_postfit_r1" if not args.useBestFit else "dNLL_bestfit"

# get the absolute post fit NLL value of pure ttZ
ttZ_res = getResult(ewkDM_central)
#ttZ_res = getResult(dim6top_LO_ttZ_ll_cpQM_0p00_cpt_0p00)
ttZ_NLL_abs = float(ttZ_res["NLL_prefit"]) + float(ttZ_res[fitKey])

print "Max Likelihood ttZ SM"
print "{:10.2f}".format(ttZ_NLL_abs)

# load all samples, omit the 1/1 point
#signals = [ x for x in allSamples_dim6top if not x.name.startswith('dim6top_LO_ttZ_ll_ctZ_1p00_ctZI_1p00') ]

if args.plane == "current":
    signals = [ ewkDM_central ] + [ x for x in ewkDM_currents ]
    x_var = 'DC1V'
    y_var = 'DC1A'
    #x_shift = 0.
    #y_shift = 0.
    x_shift = 0.24
    y_shift = -0.60

elif args.plane == "dipole":
    signals = [ ewkDM_central ] + [ x for x in ewkDM_dipoles ]
    x_var = 'DC2V'
    y_var = 'DC2A'
    x_shift = 0.
    y_shift = 0.

print "Number of results", len(signals)

var1_values = []
var2_values = []

for s in signals:
    s.var1 = getCouplingFromName(s.name, x_var)
    s.var2 = getCouplingFromName(s.name, y_var)
    if s.var1 != 0.0 and (s.var1+x_shift) not in var1_values:
        var1_values.append(s.var1 + x_shift)
    if s.var2 != 0.0 and (s.var2+y_shift) not in var2_values:
        var2_values.append(s.var2 + y_shift)


var1_values = sorted(var1_values)
var2_values = sorted(var2_values)

x_min = var1_values[0] - (abs(var1_values[0]) - abs(var1_values[1])) / 2
x_max = var1_values[-1] + (abs(var1_values[-1]) - abs(var1_values[-2])) / 2
nbins_x = len(var1_values)
bin_size_x = (x_max - x_min) / nbins_x

y_min = var2_values[0] - (abs(var2_values[0]) - abs(var2_values[1])) / 2
y_max = var2_values[-1] + (abs(var2_values[-1]) - abs(var2_values[-2])) / 2
nbins_y = len(var2_values)
bin_size_y = (y_max - y_min) / nbins_y


x = []
y = []
z = []

res_dic = {}

print "{:>10}{:>10}{:>10}".format(x_var, y_var, "2*dNLL")

for i,s in enumerate(signals):
    res = getResult(s)
    print s.name
    if type(res) == type({}):
        limit = float(res["NLL_prefit"]) + float(res[fitKey]) - ttZ_NLL_abs

        if limit >= 0:
            # good result
            nll_value = 2*limit
        elif limit > -0.01 and limit < 0:
            # catch rounding errors
            nll_value = 0
        elif limit < -900:
            #continue
            # if the fit failed, add a dummy value (these points should easily be excluded)
            nll_value = 100
        else:
            print "No good result found for %s, results is %s"%(s.name, limit)
            continue
        
        # Add results
        print "{:10.2f}{:10.2f}{:10.2f}".format(s.var1+x_shift, s.var2+y_shift, nll_value)
        if s.var2 + y_shift > -0.8 and s.var1+x_shift>-0.9 and s.var1+x_shift<0.9:
            z.append(nll_value)
            x.append(s.var1 + x_shift)
            y.append(s.var2 + y_shift)
            res_dic[(round(s.var1 + x_shift,2), round(s.var2 + y_shift,2))] = round(nll_value,3)
        else:
            print "Omitting..."
    else:
        print "No results for %s found"%s.name

proc = "ttZ"

#print res_dic

multiplier = 3

a,debug = toGraph2D(proc, proc, len(x), x,y,z)#res_dic)
nxbins = max(1, min(500, nbins_x*multiplier))
nybins = max(1, min(500, nbins_y*multiplier))

print "Number of bins on x-axis: %s"%nxbins
print "Number of bins on y-axis: %s"%nybins


hist = a.GetHistogram().Clone()

#nxbins = 200
#nybins = 200

a.SetNpx(nxbins)
a.SetNpy(nybins)
hist = a.GetHistogram().Clone()


if x_var == "DC1V":
    hist.GetXaxis().SetTitle("C_{1,V}")
else:
    hist.GetXaxis().SetTitle("#DeltaC_{2,V}")
hist.GetXaxis().SetNdivisions(505)
if y_var == "DC1A":
    hist.GetYaxis().SetTitle("C_{1,A}")
else:
    hist.GetYaxis().SetTitle("#DeltaC_{2,A}")
hist.GetYaxis().SetNdivisions(505)
hist.GetYaxis().SetTitleOffset(1.0)
hist.GetZaxis().SetTitle("-2 #DeltalnL")
hist.GetZaxis().SetTitleOffset(1.2)
hist.SetStats(0)
if args.smooth:
    hist.Smooth()
    postFix += "_smooth"

cans = ROOT.TCanvas("can_%s"%proc,"",700,700)

#contours = {'ttZ': [-0.1,0.,1.,4.]}
contours = {'ttZ': [1.,4.]}
drawContours = True
if drawContours:
    histsForCont = hist.Clone()
    c_contlist = ((ctypes.c_double)*(len(contours[proc])))(*contours[proc])
    histsForCont.SetContour(len(c_contlist),c_contlist)
    histsForCont.Draw("contzlist")
    cans.Update()
    conts = ROOT.gROOT.GetListOfSpecials().FindObject("contours")
    #cont_m2 = conts.At(0).Clone()
    #cont_m1 = conts.At(1).Clone()
    cont_p1 = conts.At(0).Clone()
    cont_p2 = conts.At(1).Clone()

pads = ROOT.TPad("pad_%s"%proc,"",0.,0.,1.,1.)
pads.SetRightMargin(0.20)
pads.SetLeftMargin(0.14)
pads.SetTopMargin(0.11)
pads.Draw()
pads.cd()

hist.GetZaxis().SetRangeUser(0,4.95)
hist.SetMaximum(79.95) #19.95
hist.SetMinimum(0.)
#hist.GetZaxis().SetRangeUser(0,4.95)

hist.Draw("colz")

if drawContours:
    for conts in [cont_p2]:
        for cont in conts:
            cont.SetLineColor(ROOT.kRed)
            cont.SetLineWidth(2)
            cont.SetLineStyle(7)
            cont.Draw("same")
    for conts in [cont_p1]:
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
latex1.DrawLatex(0.14,0.92,'#bf{ewkDM model}')
latex1.DrawLatex(0.6,0.96,'#bf{%.1f fb^{-1} MC (13TeV)}'%(setup.lumi['3mu']/1e3))


plotDir = os.path.join( plot_directory,"NLL_plots_2D/" )
if not os.path.isdir(plotDir):
    os.makedirs(plotDir)

for e in [".png",".pdf",".root"]:
    cans.Print(plotDir+"ewkDM_%s_%s%s"%(args.plane, setup.name, postFix)+e)

debug.Draw("ap0")
cans.Print(plotDir+"ewkDM_%s_%s%s"%(args.plane, setup.name, postFix+"_grid")+'.png')

