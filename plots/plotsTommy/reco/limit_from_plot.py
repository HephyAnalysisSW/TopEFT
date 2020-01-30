#!/usr/bin/env python
''' Make limit from plot 
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
ROOT.gROOT.LoadMacro("$CMSSW_BASE/src/StopsDilepton/tools/scripts/tdrstyle.C")
ROOT.setTDRStyle()
import array

from RootTools.core.standard      import *
from TopEFT.Tools.user            import plot_directory
from TopEFT.Tools.cardFileWriter import cardFileWriter
#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--input',     action='store',      default='./mlp1.root', help="Input file.")
argParser.add_argument('--output',    action='store',      default='./mlp1.txt', help="Output card file.")
argParser.add_argument('--refLumi',   action='store',      type=float, default=300, help="Lumi used in the input file.")
args = argParser.parse_args()

# Logger
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

# load histos
gDir    = ROOT.gDirectory
rFile   = ROOT.TFile.Open( args.input )
if rFile:
    # first & only TObject in file is the canvas
    try:
        canvas = rFile.Get(rFile.GetListOfKeys().At(0).GetName())
        histos = [ canvas.GetListOfPrimitives().At(i) for i in range(canvas.GetListOfPrimitives().GetSize()) ]
        histos = filter( lambda h: type(h)==ROOT.TH1F, histos)
    except:
        logger.error( "Could not load input file %s", args.input)
        sys.exit(-1)
else:
    logger.error( "Could not load input file %s", args.input)
    sys.exit(-1)

# nicer name
histos[0].SetName( "signal" )
for i_histo, histo in enumerate(histos[1:]):
    histo.SetName("bkg_%i"%i_histo)

# signal is first, the last histo is a copy 
logger.info( "Loaded %i histos from file %s", len(histos), args.input)
histos = histos[:-1]
# un-stack
for i_histo, histo in enumerate(histos[:-1]):
    histos[i_histo+1].Scale(-1)
    histo.Add( histos[i_histo+1] )
    histos[i_histo+1].Scale(-1)
    
# compute differences
h_signal, h_backgrounds = histos[0], histos[1:]

logger.info("Total signal %s %f", h_signal.GetName(), h_signal.Integral())
for i_h, h in enumerate(h_backgrounds):
    logger.info( "Total bkg %i %s: %f", i_h, h.GetName(), h.Integral() )

result = {}

lumi_factor = 136./300.
signal_strengths     = [0, 0.25, 0.5, 0.75, 1., 1.5, 2, 2.2]
for signal_strength in signal_strengths:
    c = cardFileWriter.cardFileWriter()


    bkg_sys         = 1.1
    bkg_shape_sys   = 1.1

    for i in range(len(h_backgrounds)):
        c.addUncertainty('bkg_sys_%i'%i, 'lnN')
        c.addUncertainty('bkg_shape_sys_%i'%i, 'lnN')

    c.addUncertainty('sig_sys', 'lnN')
    sig_sys         = 1.25

    for i_bin in range(1, 1+h_signal.GetNbinsX()):
        c.addBin('Bin'+str(i_bin), [h.GetName() for h in h_backgrounds], 'Bin'+str(i_bin))
        y_signal        = h_signal.GetBinContent(i_bin)
        y_backgrounds   = [ h.GetBinContent(i_bin) for h in h_backgrounds ]

        # Assume we observe the background
        c.specifyObservation('Bin'+str(i_bin), int(round(lumi_factor*(y_signal+sum(y_backgrounds)))))
        for i_h, h in enumerate(h_backgrounds):
            c.specifyExpectation('Bin'+str(i_bin), h.GetName(), lumi_factor*h.GetBinContent(i_bin))
            c.specifyUncertainty('bkg_sys_%i'%i_h,         'Bin'+str(i_bin),h.GetName(),bkg_sys)
            c.specifyUncertainty('bkg_shape_sys_%i'%i_h,   'Bin'+str(i_bin),h.GetName(),1+(bkg_shape_sys-1)*(i_bin)/(h_signal.GetNbinsX()))

        c.specifyExpectation('Bin'+str(i_bin), h_signal.GetName(), lumi_factor*signal_strength*h_signal.GetBinContent(i_bin))
        c.specifyUncertainty('sig_sys','Bin'+str(i_bin),h_signal.GetName(),sig_sys)
        

    c.addUncertainty('Lumi', 'lnN')
    c.specifyFlatUncertainty('Lumi', 1.03)

    c.writeToFile(args.output)
    result[signal_strength] = c.calcNLL(rm=False)

def getIntersections(func, level, x_min=0, x_max=4, stepsize=0.001):
    intersections = []
    x_val = x_min
    while x_val < x_max:
        x_val += stepsize
        intersection = func.GetX(level, x_val-stepsize, x_val)
        if (x_val-stepsize+stepsize/10000.) < intersection < (x_val-stepsize/10000.):
            intersections.append(intersection)
    return intersections

c1 = ROOT.TCanvas()
ROOT.gPad.SetRightMargin(0.15)

x  = array.array('d', signal_strengths )
y  = array.array('d', [-2*result[strength]['nll'] for strength in signal_strengths] )
g  = ROOT.TGraph(len(x),x,y)

#funStr = "[1]*(x-1)+[2]*(x-1)**2+[3]*(x-1)**4"
funStr = "[0]*(x-1)**2+[1]*(x-1)**3+[2]*(x-1)**4"
fun = ROOT.TF1("name", funStr, 0, signal_strengths[-1])
fun.SetTitle("")

g.Fit(fun)
parameters = [fun.GetParameter(i) for i in range(fun.GetNpar())]
fun.Draw("")
fun.SetLineColor(ROOT.kBlue-2)
fun.GetYaxis().SetRangeUser( 0, 50)

delta = 0.001
x_min, x_max  = min(signal_strengths), max(signal_strengths)

# find TF1 segments under threshold level**2
levels = [1, 2, 5]
intervals = {}
for level in levels:
    intersections = getIntersections(fun, level**2, x_min, x_max, delta/20.)
    intervals[level] = []
    for i,v in enumerate(intersections):
        if i > len(intersections)-2: break
        if fun.GetMinimum(intersections[i], intersections[i+1]) < 0.99:
            #intervals.append((intersections[i], intersections[i+1]))
            intervals[level].append(ROOT.TF1('', funStr, intersections[i], intersections[i+1]))
            intervals[level][-1].SetParameters(*parameters)

for interval in intervals[2]:
    interval.SetFillColorAlpha(ROOT.kYellow,0.9)
    interval.SetLineColor(ROOT.kOrange-2)
    interval.SetFillStyle(1111)
    interval.Draw("f1same")

for interval in intervals[1]:
    interval.SetFillColorAlpha(ROOT.kGreen+1,0.9)
    interval.SetLineColor(ROOT.kCyan-3)
    interval.SetFillStyle(1111)
    interval.Draw("f1same")

stuff = []

tex = ROOT.TLatex()
#tex.SetNDC()
tex.SetTextSize(0.03)
tex.SetTextColor(ROOT.kGray+2)
#tex.SetTextAngle(90)
tex.SetTextAlign(12) # align right

for level in [ 1, 2, 3, 4, 5 ]:
    l = ROOT.TLine(x_min, level**2, x_max, level**2)
    l.SetLineStyle( ROOT.kDashed )
    l.SetLineColor(ROOT.kGray+2)
    stuff.append(l)
    l.Draw("same")
    tex.DrawLatex(x_max*2.2/2.5, level**2+1, "%i#sigma"%level)
    tex.Draw()
    stuff.append(tex)

fun.GetYaxis().SetTitle("q")
fun.GetXaxis().SetTitle("#mu_{tWZ}")

fun.GetXaxis().SetLabelSize(0.04)
fun.GetYaxis().SetLabelSize(0.04)
fun.SetLineWidth(2)
fun.Draw("same")

c1.Print("/afs/hephy.at/user/r/rschoefbeck/www/etc/ll.png")
c1.Print("/afs/hephy.at/user/r/rschoefbeck/www/etc/ll.pdf")
c1.Print("/afs/hephy.at/user/r/rschoefbeck/www/etc/ll.root")
