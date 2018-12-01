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
argParser.add_argument("--filtering",        action='store_true', help="Use combined results?")
argParser.add_argument("--showPoints",        action='store_true', help="Show the points?")

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
        signals = [ x for x in ewkDM_currents if x.DC1A == -0.133 and x.DC1V != 0 ]
        x_var = 'DC1V'
        x_shift = 0.24
        y_par = 'C_{1,A}=-0.73'
    
    elif args.parameter == "DC1A":
        #signals = [ ewkDM_central ] + [ x for x in ewkDM_currents if x.DC1V == 0 and x.DC1A != 0 ]
        signals = [ x for x in ewkDM_currents if x.DC1V == -0.05 and x.DC1A != 0 ]
        x_var = 'DC1A'
        x_shift = -0.60
        y_par = 'C_{1,V}=0.19'

    elif args.parameter == "DC2V":
        signals = [ ewkDM_central ] + [ x for x in ewkDM_dipoles if x.DC2A == 0 and x.DC2V != 0 ]
        x_var = 'DC2V'
        x_shift = 0.
        y_par = ''

    elif args.parameter == "DC2A":
        signals = [ ewkDM_central ] + [ x for x in ewkDM_dipoles if x.DC2V == 0 and x.DC2A != 0 ]
        x_var = 'DC2A'
        x_shift = 0.
        y_par = ''

    else:
        raise NotImplementedError

elif args.model == "dim6top_LO":
    if args.parameter == "cpQM":
        signals = [ dim6top_central ] + [ x for x in dim6top_currents if x.cpt == 0.0 and x.cpQM != 0 ]
        #signals = [ x for x in dim6top_currents if x.cpt == -3.5 and x.cpQM != 0 ]
        x_var = 'cpQM'
        x_shift = 0.
        y_par = ''
    
    elif args.parameter == "cpt":
        signals = [ dim6top_central ] + [ x for x in dim6top_currents if x.cpQM == 0.0 and x.cpt != 0 ]
        #signals = [ x for x in dim6top_currents if x.cpQM == -4.0 and x.cpt != 0 ]
        x_var = 'cpt'
        x_shift = 0.
        y_par = ''
    
    elif args.parameter == "ctZ":
        signals = [ dim6top_central ] + [ x for x in dim6top_dipoles if x.ctZI == 0 and x.ctZ != 0 ]
        x_var = 'ctZ'
        x_shift = 0.
        y_par = ''
    
    elif args.parameter == "ctZI":
        signals = [ dim6top_central ] + [ x for x in dim6top_dipoles if x.ctZ == 0 and x.ctZI != 0 ]
        x_var = 'ctZI'
        x_shift = 0.
        y_par = ''
    
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
        #res = getResult(s)
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

for i,s in enumerate(signals):
    if resDB.contains({"signal":s.name}):
        res = resDB.getDicts({"signal":s.name})[-1]
        #res = getResult(s)
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
                print "bli"

            if not (s.var1 + x_shift in x) and not nll_value>50:
                print "bla", nll_value
                z.append(nll_value)
                x.append(s.var1 + x_shift)
                res_dic[round(s.var1 + x_shift,2)] = round(nll_value,3)

        else:
            print "No results for %s found"%s.name


## filter
print "Filtering"
z_sorted = sorted(z)
minimum = z.index(z_sorted[0])
#print z[minimum]
#z[minimum] = -(z_sorted[1]+z_sorted[2])/3
#print z[minimum]
for i,l in enumerate(z):
    if not i == minimum:
        if args.filtering:
            z[i] = z[i] - (z_sorted[1]+z_sorted[2])/3
        else:
            z[i] = z[i]

proc = "ttZ"

min_delta = findMinDelta(x_forRange)
x_min = min(x_forRange)
x_max = max(x_forRange)

print x_min, x_max

Nbins = int((x_max-x_min)/min_delta)

print Nbins

delta = (x_max-x_min)/Nbins


hist = ROOT.TH1F("NLL","", Nbins+1, x_min-delta/2, x_max+delta/2)
hist.SetStats(0)
hist.GetYaxis().SetRangeUser(0,26)

print "Best fit found for signal %s, %s"%bestFitPoint

if x_var == "DC1V":
    hist.GetXaxis().SetTitle("C_{1,V}")
elif x_var == "DC2V":
    hist.GetXaxis().SetTitle("C_{2,V}")
elif x_var == "cpQM":
#    hist.GetXaxis().SetTitle("c_{#varphiQ}^{-} #equiv C_{#varphiq}^{1(33)}-C_{#varphiq}^{3(33)}")
    hist.GetXaxis().SetTitle("c_{#varphiQ}^{-}/#Lambda^{2} (1/TeV^{2})")
elif x_var == "ctZ":
#    hist.GetXaxis().SetTitle("c_{tZ} #equiv Re{-s_{W}C_{uB}^{(33)}+c_{W}C_{uW}^{(33)}}")
    hist.GetXaxis().SetTitle("c_{tZ}/#Lambda^{2} (1/TeV^{2})")
elif x_var == "DC1A":
    hist.GetXaxis().SetTitle("C_{1,A}")
elif x_var == "DC2A":
    hist.GetXaxis().SetTitle("C_{2,A}")
elif x_var == "cpt":
#    hist.GetXaxis().SetTitle("c_{#varphit} #equiv C_{#varphiu}^{(33)}")
    hist.GetXaxis().SetTitle("c_{#varphit}/#Lambda^{2} (1/TeV^{2})")
elif x_var == "ctZI":
#    hist.GetXaxis().SetTitle("c_{tZ}^{[I]} #equiv Im{-s_{W}C_{uB}^{(33)}+c_{W}C_{uW}^{(33)}}")
    hist.GetXaxis().SetTitle("c_{tZ}^{[I]}/#Lambda^{2} (1/TeV^{2})")

#hist.GetYaxis().SetTitleOffset(1.0)
hist.GetYaxis().SetTitle("-2 #DeltalnL")
hist.GetYaxis().SetTitleOffset(1.2)
hist.SetStats(0)

#hist.Draw()

for x_val in res_dic.keys():
    if res_dic[x_val]>0:
        if args.filtering:
            hist.SetBinContent(hist.GetXaxis().FindBin(x_val), res_dic[x_val]-(z_sorted[1]+z_sorted[2])/3)
        else:
            hist.SetBinContent(hist.GetXaxis().FindBin(x_val), res_dic[x_val])#-(z_sorted[1]+z_sorted[2])/3)
    else:
        hist.SetBinContent(hist.GetXaxis().FindBin(x_val), 0.001)

#fun = ROOT.TF1("f_1", "[0] + [1]*x + [2]*x**2 +[4]*x**4", -50., 50.)
fun = ROOT.TF1("f_1", "[0] + [1]*x + [2]*x**2 + [3]*x**3 + [4]*x**4 +[5]*x**5 + [6]*x**6", x_min-delta/2, x_max+delta/2)
fun.SetLineColor(ROOT.kBlack)
fun.SetLineStyle(1)
#fun.SetLineWidth(2)

a = toGraph('NLL','NLL', len(x), x, z)

a.Fit(fun)

#fun.SetParameter(0,fun.GetParameter(0)-fun.GetMinimum())

funClone = fun.Clone()
parameters = [ funClone.GetParameter(x) for x in range(7) ]


bestFitX = fun.GetX(fun.GetMinimum(),x_min-delta/2,x_max+delta/2)
upper95 = fun.GetX(4,bestFitX,x_max)
lower95 = fun.GetX(4,x_min,bestFitX)
upper68 = fun.GetX(1,bestFitX,x_max)
lower68 = fun.GetX(1,x_min,bestFitX)

interval95 = ROOT.TF1("int_95", "[0] + [1]*x + [2]*x**2 + [3]*x**3 + [4]*x**4 +[5]*x**5 + [6]*x**6", lower95, upper95)
interval95.SetParameters(*parameters)

interval68 = ROOT.TF1("int_68", "[0] + [1]*x + [2]*x**2 + [3]*x**3 + [4]*x**4 +[5]*x**5 + [6]*x**6", lower68, upper68)
interval68.SetParameters(*parameters)

if args.prefit:
    postFix += "_prefit"
if args.useXSec:
    postFix += "_useXSec"
if args.useShape:
    postFix += "_useShape"
if args.expected:
    postFix += "_expected"
if args.smooth:
    #hist.Smooth(1,"k5b")
    postFix += "_smooth"
if args.inclusiveRegions:
    postFix += "inclusiveSR"

cans = ROOT.TCanvas("can_%s"%proc,"",700,700)

pads = ROOT.TPad("pad_%s"%proc,"",0.,0.,1.,1.)
pads.SetRightMargin(0.05)
pads.SetLeftMargin(0.14)
pads.SetTopMargin(0.15)
pads.Draw()
#pads.SetLogy()
pads.cd()


hist.Draw("AXIS")

#fun.SetFillColor(ROOT.kGreen)
fun.SetLineWidth(1503)
#fun.SetFillStyle(1111)
#fun.Draw("fsame")

interval95.SetFillColorAlpha(ROOT.kBlue-2,0.9)
interval95.SetLineColor(ROOT.kBlue-2)
interval95.SetFillStyle(1111)
interval95.Draw("f1same")

interval68.SetFillColorAlpha(ROOT.kGreen-2,0.9)
interval68.SetLineColor(ROOT.kGreen-2)
interval68.SetFillStyle(1111)
interval68.Draw("f1same")

fun.Draw("same")

if args.showPoints:
    hist.Draw("p same")

one = ROOT.TF1("one","[0]",x_min,x_max)
one.SetParameter(0,1)
one.SetLineColor(ROOT.kGray)

four = ROOT.TF1("four","[0]",x_min,x_max)
four.SetParameter(0,4)
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
    latex1.DrawLatex(0.14,0.96,'CMS #bf{#it{Preliminary}}')

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


leg = ROOT.TLegend(0.45,0.86,0.70,0.95)
leg.SetFillColor(ROOT.kWhite)
leg.SetShadowColor(ROOT.kWhite)
leg.SetBorderSize(0)
leg.SetTextSize(0.035)
leg.AddEntry(interval95, '#bf{95% C.L.}', 'f')
leg.AddEntry(interval68, '#bf{68% C.L.}', 'f')
leg.Draw()

leg2 = ROOT.TLegend(0.70,0.86,0.90,0.95)
leg2.SetFillColor(ROOT.kWhite)
leg2.SetShadowColor(ROOT.kWhite)
leg2.SetBorderSize(0)
leg2.SetTextSize(0.035)
leg2.AddEntry(SMpoint, '#bf{SM}', 'p')
leg2.AddEntry(None, '#bf{%s}'%y_par, '')
leg2.Draw()


plotDir = os.path.join( plot_directory,"NLL_plots_1D_%s/"%args.year )
if not os.path.isdir(plotDir):
    os.makedirs(plotDir)

args.year = "COMBINED" if args.combined else args.year

for e in [".png",".pdf",".root"]:
    cans.Print(plotDir+"%s_%s_%s_%s%s"%(args.model, args.parameter, setup.name, args.year, postFix)+e)

