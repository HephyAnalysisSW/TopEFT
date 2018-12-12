import ROOT
import os
import ctypes
import shutil
from functools                      import partial

from RootTools.core.standard        import *

## 2016
data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *
postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

## 2017
data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *


from TopEFT.Tools.user              import combineReleaseLocation, analysis_results, plot_directory
from TopEFT.Tools.niceColorPalette  import niceColorPalette, redColorPalette
from TopEFT.Tools.helpers           import getCouplingFromName
from TopEFT.Analysis.Setup          import Setup
from TopEFT.Tools.resultsDB             import resultsDB
from TopEFT.Tools.u_float               import u_float

from TopEFT.samples.gen_fwlite_benchmarks import *


# Plot style
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--plot_directory',  action='store',      default='NLL_plots')
argParser.add_argument('--useBestFit',      action='store_true', help="Use best fit value? Default is r=1")
argParser.add_argument("--combined",        action='store_true', help="Use combined results?")
argParser.add_argument('--smooth',          action='store_true', help="Use histogram smoothing? Potentially dangerous (oversmoothing)!")
argParser.add_argument('--model',           action='store', choices=["ewkDM", "dim6top_LO"], help="Which model?")
argParser.add_argument('--parameter',       action='store', choices=["DC1A", "DC1V", "DC2A","DC2V", "ctZ","ctZI","cpt","cpQM"], default = None, help="Which parameter to scan?")
argParser.add_argument("--useXSec",         action='store_true', help="Use the x-sec information?")
argParser.add_argument("--useShape",        action='store_true', help="Use the shape information?")
argParser.add_argument("--prefit",          action='store_true', help="Use pre-fit NLL?")
argParser.add_argument("--expected",        action='store_true', help="Use expected results?")
argParser.add_argument("--inclusiveRegions", action='store_true', help="Use inclusive signal regions?")
argParser.add_argument("--unblinded",       action='store_true', help="Use unblinded results?")
argParser.add_argument("--year",            action='store', default=2016, choices = [ '2016', '2017', '20167' ], help='Which year?')
argParser.add_argument("--showPoints",      action='store_true', help="Show the points?")
argParser.add_argument("--profiling",       action='store_true', help="Show the points?")
argParser.add_argument("--subdir",          action='store', default="NLL_plots_1D_final", help="Show the points?")
argParser.add_argument("--sigma",           action='store_true', help="Use sigma levels?")
args = argParser.parse_args()

year = int(args.year)

setup = Setup(year)

postFix = ""#"_fine_YR1"

def Eval(obj, x, params):
    return obj.Eval(x[0])

def toGraph(name,title,length,x,z):
    result = ROOT.TGraph(length)
    result.SetName(name)
    result.SetTitle(title)
    for i in range(length):
        result.SetPoint(i, x[i], z[i])
    c = ROOT.TCanvas()
    result.Draw()
    del c
    #res = ROOT.TGraphDelaunay(result)
    return result

def findMinDelta(l):
    minDelta = 999
    l = sorted(l)
    for i,x in enumerate(l):
        if i>(len(l)-2): break
        minDelta = (l[i+1]-x) if (l[i+1]-x)<minDelta else minDelta
    return minDelta

def getCouplingsFromSample(sample):
    couplings = ["DC1A", "DC1V", "DC2A","DC2V", "ctZ","ctZI","cpt","cpQM"]
    l = []
    for c in couplings:
        val = getCouplingFromName(sample.name, c)
        if val:
            l.append((c, val))
        else:
            l.append((c, 0))
    return l

def setCouplingValues(samples):
    for x in samples:
        couplings = getCouplingsFromSample(x)
        if len(couplings)>0:
            for c,val in couplings:
                setattr(x, c, val)

def profiling(samples, coupling, couplingZ):
    # get the list of samples, filter and return profiled list of NLL

    print "Profiling"
    # get coupling values
    couplingValues = []
    for s in samples:
        val = getattr(s, coupling)
        if val not in couplingValues and abs(val) != 3.5 and abs(val) != 7.0:# and abs(val) != 10.5 :
            couplingValues.append(val)
    
    totalMin = 9999
    points = []
    for c in sorted(couplingValues):
        tmp = []
        for s in samples:
            print s.name
            print c, getattr(s, couplingZ)
            if getattr(s, coupling) == c:
                if resDB.contains({"signal":s.name}):
                    print "Adding a point"
                    res = resDB.getDicts({"signal":s.name})[-1]
                    res = float(res["NLL_prefit"]) + float(res["dNLL_postfit_r1"])
                    if res > 0:
                        tmp.append(res)
        min_tmp = min(tmp)
        points.append((c, min_tmp))
        if min_tmp < totalMin: totalMin = min_tmp
    
    newPoints = []
    for p in points:
        newPoints.append((p[0], p[1] - totalMin))
        #p[1] = p[1] - totalMin

    return newPoints

setCouplingValues(dim6top_dipoles + dim6top_currents + ewkDM_dipoles + ewkDM_currents)
###### need to remove doubles

# do the same stuff as in the analysis part

subDir = ''
baseDir = os.path.join(analysis_results, subDir)

if not args.inclusiveRegions:
    cardDir = "regionsE_%s"%(year) if not args.combined else "regionsE_COMBINED"
else:
    cardDir = "inclusiveRegions_%s"%(year) if not args.combined else "inclusiveRegions_COMBINED"

if args.useXSec:
    cardDir += "_xsec"
if args.useShape:
    cardDir += "_shape"
exp = "_expected" if args.expected else ''

#cardDir += "_lowUnc%s"%exp
cardDir += "_lowUnc%s_SRandCR"%exp

#regionsE_COMBINED_xsec_shape_lowUnc_expected_SRandCR
#regionsE_2017_xsec_shape_lowUnc_expected_SRandCR

#/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_2016_xsec_shape_lowUnc_WZreweight_SRandCR/

plane = "currents" if args.parameter in ["DC1V","DC1A","cpt","cpQM"] else "dipoles"

limitDir    = os.path.join(baseDir, 'cardFiles', cardDir, subDir, '_'.join([args.model, plane]))

print limitDir
resDB = resultsDB(limitDir+'/results.sq', "results", setup.resultsColumns)

fitKey = "dNLL_postfit_r1" if not args.useBestFit else "dNLL_bestfit"


# get the absolute post fit NLL value of pure ttZ
if args.model == "ewkDM":
    ttZ_res = resDB.getDicts({"signal":ewkDM_central.name})[-1]
elif args.model == "dim6top_LO":
    ttZ_res = resDB.getDicts({"signal":dim6top_central.name})[-1]

if args.prefit:
    ttZ_NLL_abs = float(ttZ_res["NLL_prefit"])
else:
    ttZ_NLL_abs = float(ttZ_res["NLL_prefit"]) + float(ttZ_res[fitKey])

print "Max Likelihood ttZ SM"
print "{:10.2f}".format(ttZ_NLL_abs)

if args.model == "ewkDM":
    if args.parameter == "DC1V":
        #signals = [ ewkDM_central ] + [ x for x in ewkDM_currents if x.DC1A == 0 and x.DC1V != 0 ]
        if args.profiling:
            signals = [ ewkDM_central ] + ewkDM_currents
        else:
            if args.expected or True:
                signals = [ ewkDM_central ] + [ x for x in ewkDM_currents if x.DC1A == 0 and x.DC1V != 0 ]
            else:
                signals = [ x for x in ewkDM_currents if x.DC1A == -0.133 and x.DC1V != 0 ]
        x_var = 'DC1V'
        z_var = 'DC1A'
        x_shift = 0.24
        if args.expected or True:
            y_par = 'C_{1,A}=-0.60'
        else:
            y_par = 'C_{1,A}=-0.73'
        allowedIntervals = []
        indirectConstraints = []
    
    elif args.parameter == "DC1A":
        #signals = [ ewkDM_central ] + [ x for x in ewkDM_currents if x.DC1V == 0 and x.DC1A != 0 ]
        if args.expected or True:
            signals = [ ewkDM_central ] + [ x for x in ewkDM_currents if x.DC1V == 0 and x.DC1A != 0 ]
        else:
            signals = [ x for x in ewkDM_currents if x.DC1V == -0.05 and x.DC1A != 0 ]
        x_var = 'DC1A'
        x_shift = -0.60
        if args.expected or True:
            y_par = 'C_{1,V}=0.24'
        else:
            y_par = 'C_{1,V}=0.19'
        allowedIntervals = []
        indirectConstraints = []

    elif args.parameter == "DC2V":
        signals = [ ewkDM_central ] + [ x for x in ewkDM_dipoles if x.DC2A == 0 and x.DC2V != 0 ]
        x_var = 'DC2V'
        x_shift = 0.
        y_par = ''
        allowedIntervals = []
        indirectConstraints = []

    elif args.parameter == "DC2A":
        signals = [ ewkDM_central ] + [ x for x in ewkDM_dipoles if x.DC2V == 0 and x.DC2A != 0 ]
        x_var = 'DC2A'
        x_shift = 0.
        y_par = ''
        allowedIntervals = []
        indirectConstraints = []

    else:
        raise NotImplementedError

elif args.model == "dim6top_LO":
    if args.parameter == "cpQM":
        if args.profiling:
            signals = dim6top_currents
        else:
            signals = [ dim6top_central ] + [ x for x in dim6top_currents if x.cpt == 0.0 and x.cpQM != 0 ]
        x_var = 'cpQM'
        z_var = 'cpt'
        x_shift = 0.
        y_par = ''
        allowedIntervals = []
        indirectConstraints = [(-3.4, 7.5)]
    
    elif args.parameter == "cpt":
        if args.profiling:
            signals = dim6top_currents
        else:
            signals = [ dim6top_central ] + [ x for x in dim6top_currents if x.cpQM == 0.0 and x.cpt != 0 ]
        x_var = 'cpt'
        z_var = 'cpQM'
        x_shift = 0.
        y_par = ''
        if args.expected:
            allowedIntervals = [(-20.2, 4.0)]
        else:
            allowedIntervals = [(-22.2, -13.0), (-3.2, 6.0)]
        indirectConstraints = [(-2.5, 7.0)]
    
    elif args.parameter == "ctZ":
        signals = [ dim6top_central ] + [ x for x in dim6top_dipoles if x.ctZI == 0 and x.ctZ != 0 ]
        x_var = 'ctZ'
        x_shift = 0.
        y_par = ''
        allowedIntervals = []
        indirectConstraints = []
    
    elif args.parameter == "ctZI":
        signals = [ dim6top_central ] + [ x for x in dim6top_dipoles if x.ctZ == 0 and x.ctZI != 0 ]
        x_var = 'ctZI'
        x_shift = 0.
        y_par = ''
        allowedIntervals = []
        indirectConstraints = []

    
    else:
        raise NotImplementedError

else:
    raise NotImplementedError

print "Number of results", len(signals)

var1_values = []

for s in signals:
    s.var1 = getCouplingFromName(s.name, x_var)
    if s.var1 != 0.0 and (s.var1+x_shift) not in var1_values:
        var1_values.append(s.var1 + x_shift)

var1_values = sorted(var1_values)

x           = []
x_forRange  = []
z           = []

res_dic = {}

print "Searching for bestfit point"

bestNLL = 9999.

SMPoint = ('SM', x_shift)
bestFitPoint = ('SM', x_shift)

# scan all results to find best fit
for i,s in enumerate(signals):
    if resDB.contains({"signal":s.name}):
        res = resDB.getDicts({"signal":s.name})[-1]
        if type(res) == type({}):
            ttZ_NLL_abs_check = float(res["NLL_prefit"]) + float(res[fitKey])
            if ttZ_NLL_abs_check < ttZ_NLL_abs and ttZ_NLL_abs_check>0.1:
                ttZ_NLL_abs = ttZ_NLL_abs_check
                bestFitPoint = (s.name, s.var1 + x_shift)
            #limit = float(res["NLL_prefit"]) + float(res[fitKey]) - ttZ_NLL_abs

if args.expected: bestFitPoint = SMPoint

print "Best fit found for signal %s, %s"%bestFitPoint
print
print "{:>10}{:>10}".format(x_var, "2*dNLL")


if args.profiling:
    points = profiling(signals, x_var, z_var)

    for p, c in points:
        nll_value = 2*c
        if not nll_value > 20:
            z.append(nll_value)
            x.append(p + x_shift)
            res_dic[round(p + x_shift,2)] = round(nll_value,3)
        if not (p + x_shift in x_forRange) and not nll_value>20:
            x_forRange.append(p + x_shift)

else:
    for i,s in enumerate(signals):
        if resDB.contains({"signal":s.name}):
            res = resDB.getDicts({"signal":s.name})[-1]
            print s.name
            if type(res) == type({}):
                if args.prefit:
                    limit = float(res["NLL_prefit"]) - ttZ_NLL_abs
                else:
                    limit = float(res["NLL_prefit"]) + float(res[fitKey]) - ttZ_NLL_abs
    
                if limit >= 0.0:
                    # good result
                    nll_value = 2*limit
                elif limit > -0.1 and limit < 0:
                    # catch rounding errors
                    print limit
                    nll_value = 0
                elif limit < -900:
                    # if the fit failed, add a dummy value (these points should easily be excluded)
                    nll_value = 100
                else:
                    print limit
                    print "No good result found for %s, results is %s"%(s.name, limit)
                    continue
                
                # Add results
                print "{:10.2f}{:10.2f}".format(s.var1+x_shift, nll_value)
    
                if not (s.var1 + x_shift in x) and not nll_value>50:
                    x_forRange.append(s.var1 + x_shift)
    
                if not (s.var1 + x_shift in x) and not nll_value>50:
                    z.append(nll_value)
                    x.append(s.var1 + x_shift)
                    res_dic[round(s.var1 + x_shift,2)] = round(nll_value,3)
    
            else:
                print "No results for %s found"%s.name

proc = "ttZ"
y_max = 26

min_delta = findMinDelta(x_forRange)
x_min = min(x_forRange)
x_max = max(x_forRange)

Nbins = int((x_max-x_min)/min_delta)

delta = (x_max-x_min)/Nbins

hist = ROOT.TH1F("NLL","", (Nbins+1)*10, x_min-delta/2., x_max+delta/2.)
hist.SetStats(0)
hist.GetYaxis().SetRangeUser(0,y_max)

print "Best fit found for signal %s, %s"%bestFitPoint

if x_var == "DC1V":
    hist.GetXaxis().SetTitle("C_{1,V}")
elif x_var == "DC2V":
    hist.GetXaxis().SetTitle("C_{2,V}")
elif x_var == "cpQM":
    hist.GetXaxis().SetTitle("c_{#varphiQ}^{-}/#Lambda^{2} (1/TeV^{2})")
elif x_var == "ctZ":
    hist.GetXaxis().SetTitle("c_{tZ}/#Lambda^{2} (1/TeV^{2})")
elif x_var == "DC1A":
    hist.GetXaxis().SetTitle("C_{1,A}")
elif x_var == "DC2A":
    hist.GetXaxis().SetTitle("C_{2,A}")
elif x_var == "cpt":
    hist.GetXaxis().SetTitle("c_{#varphit}/#Lambda^{2} (1/TeV^{2})")
elif x_var == "ctZI":
    hist.GetXaxis().SetTitle("c_{tZ}^{[I]}/#Lambda^{2} (1/TeV^{2})")

hist.GetYaxis().SetTitle("-2 #DeltalnL")
hist.GetYaxis().SetTitleOffset(1.2)
hist.SetStats(0)

for x_val in res_dic.keys():
    if res_dic[x_val]>0:
        hist.SetBinContent(hist.GetXaxis().FindBin(x_val), res_dic[x_val])
    else:
        hist.SetBinContent(hist.GetXaxis().FindBin(x_val), 0.001)

bfb = [bestFitPoint[1]]*5
funStr = "[0]*(x-{})**2 + [1]*(x-{})**3 + [2]*(x-{})**4 + [3]*(x-{})**5 + [4]*(x-{})**6".format(*bfb)

fun = ROOT.TF1("f_1", funStr, x_min-delta/2, x_max+delta/2)
fun.SetLineColor(ROOT.kBlack)
fun.SetLineStyle(1)
fun.SetNpx(1000)
a = toGraph('NLL','NLL', len(x), x, z)

a.Fit(fun)

funClone = fun.Clone()
parameters = [ funClone.GetParameter(x) for x in range(5) ]


bestFitX = fun.GetX(fun.GetMinimum(),x_min-delta/2,x_max+delta/2)

# Get the intervals. Curve sketch not straight forward in ROOT.

def getIntersections(func, level, x_min, x_max, stepsize):
    intersections = []
    x_val = x_min
    while x_val < x_max:
        x_val += stepsize
        intersection = func.GetX(level, x_val-stepsize, x_val)
        if (x_val-stepsize+stepsize/10000.) < intersection < (x_val-stepsize/10000.):
            intersections.append(intersection)

    return intersections



intervals68 = []
intersections = getIntersections(fun, 1, x_min, x_max, delta/20.)
for i,v in enumerate(intersections):
    if i > len(intersections)-2: break
    if fun.GetMinimum(intersections[i], intersections[i+1]) < 0.99:
        intervals68.append((intersections[i], intersections[i+1]))

intervals95 = []
intersections = getIntersections(fun, 4, x_min, x_max, delta/20.)
for i,v in enumerate(intersections):
    if i > len(intersections)-2: break
    if fun.GetMinimum(intersections[i], intersections[i+1]) < 3.99:
        intervals95.append((intersections[i], intersections[i+1]))


intervals95_f = []
for interval in intervals95:
    intervals95_f.append(ROOT.TF1('', funStr, interval[0], interval[1]))
    intervals95_f[-1].SetParameters(*parameters)

intervals68_f = []
for interval in intervals68:
    intervals68_f.append(ROOT.TF1('', funStr, interval[0], interval[1]))
    intervals68_f[-1].SetParameters(*parameters)

boxes = []
lines = []
if args.model == 'dim6top_LO':
    for interval in allowedIntervals:
        lines.append(ROOT.TLine(interval[0], 0, interval[0], y_max))
        lines.append(ROOT.TLine(interval[1], 0, interval[1], y_max))
        boxes.append(ROOT.TBox(interval[0]-2*min_delta, 0, interval[0], y_max))
        boxes.append(ROOT.TBox(interval[1], 0, interval[1]+2*min_delta, y_max))

for box in boxes:
    box.SetLineColor(ROOT.kGray+1)
    box.SetFillColor(ROOT.kGray+1)
    box.SetFillStyle(3005)
    box.SetLineWidth(2)
for line in lines:
    line.SetLineColor(ROOT.kGray+1)
    line.SetLineWidth(2)


boxesIndirect = []
linesIndirect = []
if args.model == 'dim6top_LO':
    for interval in indirectConstraints:
        linesIndirect.append(ROOT.TLine(interval[0], 0, interval[0], y_max))
        linesIndirect.append(ROOT.TLine(interval[1], 0, interval[1], y_max))
        boxesIndirect.append(ROOT.TBox(interval[0]-2*min_delta, 0, interval[0], y_max))
        boxesIndirect.append(ROOT.TBox(interval[1], 0, interval[1]+2*min_delta, y_max))

for box in boxesIndirect:
    box.SetLineColor(ROOT.kRed-9)
    box.SetFillColor(ROOT.kRed-9)
    box.SetFillStyle(3004)
    box.SetLineWidth(2)
for line in linesIndirect:
    line.SetLineColor(ROOT.kRed-9)
    line.SetLineWidth(2)



if args.prefit:
    postFix += "_prefit"
if args.useXSec:
    postFix += "_useXSec"
if args.useShape:
    postFix += "_useShape"
if args.expected:
    postFix += "_expected"
if args.smooth:
    postFix += "_smooth"
if args.inclusiveRegions:
    postFix += "inclusiveSR"
if args.profiling:
    postFix += "_profiled"

cans = ROOT.TCanvas("can_%s"%proc,"",700,700)

pads = ROOT.TPad("pad_%s"%proc,"",0.,0.,1.,1.)
pads.SetRightMargin(0.05)
pads.SetLeftMargin(0.14)
pads.SetTopMargin(0.15)
pads.Draw()
pads.cd()


hist.Draw("AXIS")
fun.SetLineWidth(1503)

for interval in intervals95_f:
    interval.SetFillColorAlpha(ROOT.kBlue-2,0.9)
    interval.SetLineColor(ROOT.kBlue-2)
    interval.SetFillStyle(1111)
    interval.Draw("f1same")

for interval in intervals68_f:
    interval.SetFillColorAlpha(ROOT.kGreen-2,0.9)
    interval.SetLineColor(ROOT.kGreen-2)
    interval.SetFillStyle(1111)
    interval.Draw("f1same")

fun.Draw("same")

for box in boxes:
    box.Draw("same")
for line in lines:
    line.Draw("same")
for box in boxesIndirect:
    box.Draw("same")
for line in linesIndirect:
    line.Draw("same")


if args.showPoints:
    hist.Draw("p same")

one = ROOT.TF1("one","[0]",x_min,x_max)
if args.sigma:
    one.SetParameter(0,1)
else:
    one.SetParameter(0,0.989)

one.SetLineColor(ROOT.kGray)

four = ROOT.TF1("four","[0]",x_min,x_max)
if args.sigma:
    four.SetParameter(0,4)
else:
    four.SetParameter(0, 3.84)
four.SetLineColor(ROOT.kGray)

nine = ROOT.TF1("nine","[0]",-10,10)
nine.SetParameter(0,9)
nine.SetLineColor(ROOT.kRed+1)

plus1   = ROOT.TLine(fun.GetX(1,0,x_max),0,fun.GetX(1,0,x_max),1)
minus1  = ROOT.TLine(fun.GetX(1,x_min,0),0,fun.GetX(1,x_min,0),1)
plus1.SetLineColor(ROOT.kOrange)
minus1.SetLineColor(ROOT.kOrange)

plus2   = ROOT.TLine(fun.GetX(4,0,x_max),0,fun.GetX(4,0,x_max),4)
minus2  = ROOT.TLine(fun.GetX(4,x_min,0),0,fun.GetX(4,x_min,0),4)
plus2.SetLineColor(ROOT.kOrange+10)
minus2.SetLineColor(ROOT.kOrange+10)

one.SetMarkerSize(0)
four.SetMarkerSize(0)

for l in [one, four]:#, plus1, plus2, minus1, minus2]:
    l.SetLineStyle(2)
    l.SetLineWidth(2)
    l.Draw('same')

SMpoint = ROOT.TGraph(1)
SMpoint.SetName("SMpoint")
BFpoint = ROOT.TGraph(1)
BFpoint.SetName("BFpoint")

SMpoint.SetPoint(0, SMPoint[1], hist.GetMaximum()/100.)
#BFpoint.SetPoint(0, bestFitPoint[1], hist.GetMaximum()/100.)
BFpoint.SetPoint(0, bestFitX, hist.GetMaximum()/100.)

SMpoint.SetMarkerStyle(23)
SMpoint.SetMarkerSize(2)
SMpoint.SetMarkerColor(ROOT.kRed+2)
BFpoint.SetMarkerStyle(22)
BFpoint.SetMarkerSize(2)
BFpoint.SetMarkerColor(ROOT.kBlue+2)

SMpoint.Draw("p same")
#BFpoint.Draw("p same")

#fun.Draw("same")
if args.showPoints:
    hist.Draw("p same")

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.035)
latex1.SetTextAlign(11)

if not args.unblinded:
    latex1.DrawLatex(0.14,0.96,'CMS #bf{#it{Simulation}}')
else:
    latex1.DrawLatex(0.14,0.96,'CMS')# #bf{#it{Preliminary}}')

if args.model == "ewkDM":
    latex1.DrawLatex(0.14,0.91,'#bf{anomalous}')
    latex1.DrawLatex(0.14,0.87,'#bf{coupling model}')
else:
    latex1.DrawLatex(0.14,0.91,'#bf{top EFT}')
    latex1.DrawLatex(0.14,0.87,'#bf{model}')

if args.combined:
    setup.lumi = 35900+41600

if not args.unblinded:
    latex1.DrawLatex(0.6,0.96,'#bf{%.1f fb^{-1} MC (13TeV)}'%(setup.lumi/1e3))
else:
    latex1.DrawLatex(0.7,0.96,'#bf{%.1f fb^{-1} (13TeV)}'%(setup.lumi/1e3))


leg = ROOT.TLegend(0.60,0.86,0.80,0.95)
leg.SetFillColor(ROOT.kWhite)
leg.SetShadowColor(ROOT.kWhite)
leg.SetBorderSize(0)
leg.SetTextSize(0.035)
if args.sigma:
    leg.AddEntry(intervals95_f[0], '#bf{2#sigma}', 'f')
    leg.AddEntry(intervals68_f[0], '#bf{1#sigma}', 'f')
else:
    leg.AddEntry(intervals95_f[0], '#bf{95% C.L.}', 'f')
    leg.AddEntry(intervals68_f[0], '#bf{68% C.L.}', 'f')

leg.Draw()

leg2 = ROOT.TLegend(0.80,0.86,0.90,0.95)
leg2.SetFillColor(ROOT.kWhite)
leg2.SetShadowColor(ROOT.kWhite)
leg2.SetBorderSize(0)
leg2.SetTextSize(0.035)
leg2.AddEntry(SMpoint, '#bf{SM}', 'p')
leg2.AddEntry(None, '#bf{%s}'%y_par, '')
leg2.Draw()

leg3 = ROOT.TLegend(0.35,0.86,0.60,0.95)
leg3.SetFillColor(ROOT.kWhite)
leg3.SetShadowColor(ROOT.kWhite)
leg3.SetBorderSize(0)
leg3.SetTextSize(0.035)
if indirectConstraints:
    leg3.AddEntry(boxesIndirect[0], '#bf{Indirect}', 'f')
if allowedIntervals:
    leg3.AddEntry(boxes[0], '#bf{Prev. CMS}', 'f')
else:
    leg3.AddEntry(None, '', '')
#leg3.AddEntry(None, '#bf{%s}'%y_par, '')
leg3.Draw()


hist.Draw("AXIS same")

plotDir = os.path.join( plot_directory, args.subdir+'/' )
if not os.path.isdir(plotDir):
    os.makedirs(plotDir)

args.year = "COMBINED" if args.combined else args.year

for e in [".png",".pdf",".root"]:
    cans.Print(plotDir+"%s_%s_%s_%s%s"%(args.model, args.parameter, setup.name, args.year, postFix)+e)


print "68% interval"
print intervals68

print "95% interval";
print intervals95

