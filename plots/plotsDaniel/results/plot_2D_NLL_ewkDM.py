import ROOT
import os
import ctypes
import shutil
from functools                      import partial

from RootTools.core.standard        import *

## 2016
data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_2016_mva_v16/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *
postProcessing_directory = "TopEFT_PP_2016_mva_v16/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

## 2017
data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_2017_mva_v14/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v14/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *


from TopEFT.Tools.user              import combineReleaseLocation, analysis_results, plot_directory
from TopEFT.Tools.niceColorPalette  import niceColorPalette
from TopEFT.Tools.helpers           import getCouplingFromName
from TopEFT.Analysis.Setup          import Setup
from TopEFT.Tools.resultsDB             import resultsDB
from TopEFT.Tools.u_float               import u_float

from TopEFT.samples.gen_fwlite_benchmarks import *


# Plot style
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()
ROOT.gStyle.SetNumberContours(255)


import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--plot_directory',     action='store',      default='NLL_plots')
argParser.add_argument('--useBestFit', action='store_true', help="Use best fit value? Default is r=1")
argParser.add_argument('--smooth', action='store_true', help="Use histogram smoothing? Potentially dangerous (oversmoothing)!")
argParser.add_argument('--model', action='store', choices=["ewkDM", "dim6top_LO"], help="Which model?")
argParser.add_argument('--plane', action='store', choices=["currents", "dipoles"], default = "current", help="Current of dipole plane?")
argParser.add_argument("--useXSec",        action='store_true', help="Use the x-sec information?")
argParser.add_argument("--useShape",       action='store_true', help="Use the shape information?")
argParser.add_argument("--prefit",         action='store_true', help="Use pre-fit NLL?")
argParser.add_argument("--expected",         action='store_true', help="Use expected results?")
argParser.add_argument("--year",           action='store', default=2016, choices = [ '2016', '2017', '20167' ], help='Which year?')

args = argParser.parse_args()

year = int(args.year)

setup = Setup(year)

postFix = ""#"_fine_YR1"

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


# do the same stuff as in the analysis part

subDir = ''
baseDir = os.path.join(analysis_results, subDir)

cardDir = "regionsE_%s"%(year)
if args.useXSec:
    cardDir += "_xsec"
if args.useShape:
    cardDir += "_shape"
exp = "_expected" if args.expected else ''
cardDir += "_lowUnc_WZreweight%s_SRandCR"%exp

#/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_2016_xsec_shape_lowUnc_WZreweight_SRandCR/

limitDir    = os.path.join(baseDir, 'cardFiles', cardDir, subDir, '_'.join([args.model, args.plane]))

print limitDir
resDB = resultsDB(limitDir+'/results.sq', "results", setup.resultsColumns)

fitKey = "dNLL_postfit_r1" if not args.useBestFit else "dNLL_bestfit"


# get the absolute post fit NLL value of pure ttZ
if args.model == "ewkDM":
    ttZ_res = resDB.getDicts({"signal":ewkDM_central.name})[0]
elif args.model == "dim6top_LO":
    ttZ_res = resDB.getDicts({"signal":dim6top_central.name})[0]

if args.prefit:
    ttZ_NLL_abs = float(ttZ_res["NLL_prefit"])
else:
    ttZ_NLL_abs = float(ttZ_res["NLL_prefit"]) + float(ttZ_res[fitKey])

print "Max Likelihood ttZ SM"
print "{:10.2f}".format(ttZ_NLL_abs)

if args.model == "ewkDM":
    if args.plane == "currents":
        signals = [ ewkDM_central ] + [ x for x in ewkDM_currents ]
        x_var = 'DC1V'
        y_var = 'DC1A'
        #x_shift = 0.
        #y_shift = 0.
        x_shift = 0.24
        y_shift = -0.60
    
    elif args.plane == "dipoles":
        signals = [ ewkDM_central ] + [ x for x in ewkDM_dipoles ]
        x_var = 'DC2V'
        y_var = 'DC2A'
        x_shift = 0.
        y_shift = 0.

elif args.model == "dim6top_LO":
    if args.plane == "currents":
        signals = [ dim6top_central ] + [ x for x in dim6top_currents ]
        x_var = 'cpQM'
        y_var = 'cpt'
        x_shift = 0.
        y_shift = 0.
    
    elif args.plane == "dipoles":
        signals = [ dim6top_central ] + [ x for x in dim6top_dipoles ]
        x_var = 'ctZ'
        y_var = 'ctZI'
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

print "Searching for bestfit point"

bestNLL = 9999.
bestFitPoint = ('SM', x_shift, y_shift)

# scan all results to find best fit
for i,s in enumerate(signals):
    if resDB.contains({"signal":s.name}):
        res = resDB.getDicts({"signal":s.name})[0]
        #res = getResult(s)
        if type(res) == type({}):
            ttZ_NLL_abs_check = float(res["NLL_prefit"]) + float(res[fitKey])
            if ttZ_NLL_abs_check < ttZ_NLL_abs:
                ttZ_NLL_abs = ttZ_NLL_abs_check
                bestFitPoint = (s.name, s.var1 + x_shift, s.var2 + y_shift)
            #limit = float(res["NLL_prefit"]) + float(res[fitKey]) - ttZ_NLL_abs

print "Best fit found for signal %s, %s, %s"%bestFitPoint
print
print "{:>10}{:>10}{:>10}".format(x_var, y_var, "2*dNLL")

for i,s in enumerate(signals):
    if resDB.contains({"signal":s.name}):
        res = resDB.getDicts({"signal":s.name})[0]
        #res = getResult(s)
        print s.name
        if type(res) == type({}):
            if args.prefit:
                limit = float(res["NLL_prefit"]) - ttZ_NLL_abs
            else:
                limit = float(res["NLL_prefit"]) + float(res[fitKey]) - ttZ_NLL_abs

            if limit >= 0:
                # good result
                nll_value = 2*limit
            elif limit > -0.1 and limit < 0:
                # catch rounding errors
                nll_value = 0
            elif limit < -900:
                # if the fit failed, add a dummy value (these points should easily be excluded)
                nll_value = 100
            else:
                print "No good result found for %s, results is %s"%(s.name, limit)
                continue
            
            # Add results
            print "{:10.2f}{:10.2f}{:10.2f}".format(s.var1+x_shift, s.var2+y_shift, nll_value)
            if True:#s.var2 + y_shift > -0.9 and s.var1+x_shift<1.2:# and s.var1+x_shift>-0.9 and s.var1+x_shift<0.9:
            #if True:
                z.append(nll_value)
                x.append(s.var1 + x_shift)
                y.append(s.var2 + y_shift)
                res_dic[(round(s.var1 + x_shift,2), round(s.var2 + y_shift,2))] = round(nll_value,3)
            #else:
            #    print "Omitting..."
            #x.append(-1.06)
            #y.append(-0.9)
            #z.append(100)
            #
            #x.append(1.14)
            #y.append(-0.9)
            #z.append(100)
            #
            #x.append(-1.06)
            #y.append(0.9)
            #z.append(100)

            #x.append(1.14)
            #y.append(0.9)
            #z.append(100)

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

print "Best fit found for signal %s, %s, %s"%bestFitPoint
print

hist = a.GetHistogram().Clone()

#nxbins = 200
#nybins = 200

a.SetNpx(nxbins)
a.SetNpy(nybins)
hist = a.GetHistogram().Clone()


if x_var == "DC1V":
    hist.GetXaxis().SetTitle("C_{1,V}")
elif x_var == "DC2V":
    hist.GetXaxis().SetTitle("C_{2,V}")
elif x_var == "cpQM":
    hist.GetXaxis().SetTitle("c_{#varphiQ}^{-} #equiv C_{#varphiq}^{1(33)}-C_{#varphiq}^{3(33)}")
elif x_var == "ctZ":
    hist.GetXaxis().SetTitle("c_{tZ} #equiv Re{-s_{W}C_{uB}^{(33)}+c_{W}C_{uW}^{(33)}}")

hist.GetXaxis().SetNdivisions(505)
if y_var == "DC1A":
    hist.GetYaxis().SetTitle("C_{1,A}")
elif y_var == "DC2A":
    hist.GetYaxis().SetTitle("C_{2,A}")
elif y_var == "cpt":
    hist.GetYaxis().SetTitle("c_{#varphit} #equiv C_{#varphiu}^{(33)}")
elif y_var == "ctZI":
    hist.GetYaxis().SetTitle("c_{tZ}^{[I]} #equiv Im{-s_{W}C_{uB}^{(33)}+c_{W}C_{uW}^{(33)}}")

hist.GetYaxis().SetNdivisions(505)
hist.GetYaxis().SetTitleOffset(1.0)
hist.GetZaxis().SetTitle("-2 #DeltalnL")
hist.GetZaxis().SetTitleOffset(1.2)
hist.SetStats(0)
if args.prefit:
    postFix += "_prefit"
if args.useXSec:
    postFix += "_useXSec"
if args.useShape:
    postFix += "_useShape"
if args.expected:
    postFix += "_expected"
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
hist.SetMaximum(19.95) #19.95
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
latex1.DrawLatex(0.14,0.92,'#bf{%s model}'%args.model)
latex1.DrawLatex(0.6,0.96,'#bf{%.1f fb^{-1} MC (13TeV)}'%(setup.lumi/1e3))

#latex1.DrawLatex(0.14,0.94,'#bf{anomalous coupling model}')
#latex1.DrawLatex(0.6,0.94,'#bf{%.1f fb^{-1} MC (13TeV)}'%(setup.lumi['3mu']/1e3))

plotDir = os.path.join( plot_directory,"NLL_plots_2D_2016_data/" )
if not os.path.isdir(plotDir):
    os.makedirs(plotDir)

for e in [".png",".pdf",".root"]:
    cans.Print(plotDir+"%s_%s_%s_%s%s"%(args.model, args.plane, setup.name, args.year, postFix)+e)

if True:
    debug.Draw("ap0")
    cans.Print(plotDir+"%s_%s_%s_%s%s"%(args.model, args.plane, setup.name, args.year, postFix+"_grid")+'.png')

