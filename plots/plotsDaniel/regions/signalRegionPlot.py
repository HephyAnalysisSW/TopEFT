'''
Get a signal region plot from the cardfiles
Prefit
Postfit to be added
'''

#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option("--selectWeight",         dest="selectWeight",       default=None,                action="store",      help="select weight?")
parser.add_option("--PDFset",               dest="PDFset",              default="NNPDF30", choices=["NNPDF30", "PDF4LHC15_nlo_100"], help="select the PDF set")
parser.add_option("--selectRegion",         dest="selectRegion",          default=None, type="int",    action="store",      help="select region?")
parser.add_option("--sample",               dest='sample',  action='store', default='TTZ_NLO_16',    choices=["TTZ_LO_16", "TTZ_NLO_16", "TTZ_NLO_17"], help="which sample?")
parser.add_option("--small",                action='store_true', help="small?")
parser.add_option("--combine",              action='store_true', help="Combine results?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
parser.add_option('--signal',               action="store_true")
parser.add_option('--overwrite',            dest="overwrite", default = False, action = "store_true", help="Overwrite existing output files, bool flag set to True  if used")
parser.add_option('--postFit',              dest="postFit", default = False, action = "store_true", help="Apply pulls?")
parser.add_option("--year",                 action='store',      default=2016, type="int", help='Which year?')
(options, args) = parser.parse_args()

# Standard imports
import ROOT
import os
import sys
import pickle
import math

# Analysis
from TopEFT.Analysis.regions        import regionsE, noRegions, regions4l
from TopEFT.Tools.u_float           import u_float
from TopEFT.Analysis.Region         import Region
from TopEFT.Tools.infoFromCards     import *
from TopEFT.Tools.user              import plot_directory
from TopEFT.samples.color           import color

from RootTools.core.standard import *
# logger
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   options.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None)

# regions like in the cards
regions = regionsE + regions4l

# processes (and names) like in the card
processes = ['signal', 'WZ', 'TTX', 'TTW', 'TZQ', 'rare', 'nonprompt','ZZ']

# uncertainties like in the card
uncertainties = ['PU', 'JEC', 'btag_heavy', 'btag_light', 'trigger', 'leptonSF', 'scale', 'scale_sig', 'PDF', 'nonprompt', 'WZ_xsec', 'ZZ_xsec', 'rare', 'ttX', 'tZq', 'Lumi']

Nbins = len(regions)

isData = True
if options.year == 2016:
    lumiStr = 35.9
elif options.year == 2017:
    lumiStr = 41.3
else:
    lumiStr = 77.2

cardName = "ewkDM_ttZ_ll"
#cardName_signal = "ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m1p200000"
cardName_signal = "ewkDM_ttZ_ll_DC2A_0p250000_DC2V_m0p250000"
#subDir = "nbtag0-njet1p"
subDir = ""
#cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_%s_xsec_shape_lowUnc/%s/ewkDM_dipoles/"%(options.year,subDir)
#cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_20167_xsec_shape_lowUnc/%s/ewkDM_currents/"%subDir
cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_%s_shape_lowUnc_allChannelsV7/%s/ewkDM_dipoles/"%(options.year,subDir)

#cardName = "ewkDM_ttZ_ll_DC1A_0p900000_DC1V_0p900000"
#cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_shape_lowUnc/ewkDM_currents/"
cardFile = "%s/%s.txt"%(cardDir, cardName)
cardFile_signal = "%s/%s.txt"%(cardDir, cardName_signal)

logger.info("Plotting from cardfile %s"%cardFile)

hists = {}
for process in processes + ['total'] + ['observed'] + ['BSM']:
    hists[process] = ROOT.TH1F(process,"", Nbins, 0, Nbins)


for i, r in enumerate(regions):
    binName             = "Bin%s"%i
    logger.info("Working on %s", binName)
    totalYield          = 0.
    backgroundYield     = 0.
    totalUncertainty    = 0.

    for p in processes:
        res      = getEstimateFromCard(cardFile, p, binName)
        if options.postFit:
            pYield      = applyAllNuisances(cardFile, p, res, binName, uncertainties)
            logger.info("Found following SF for process %s: %s"%(p, round(pYield.val/res.val,2)))
        else:
            pYield      = res
        # automatically get the stat uncertainty from card
        pError      = pYield.sigma**2
        if not p == "signal":
            backgroundYield += pYield
        totalYield += pYield

        if not options.postFit:
            for u in uncertainties:
                try:
                    unc = getPreFitUncFromCard(cardFile, p, u, binName)
                except:
                    logger.debug("No uncertainty %s for process %s"%(u, p))
                if unc > 0:
                    pError += (unc*pYield.val)**2

        
        totalUncertainty += pError

        hists[p].SetBinContent(i+1, pYield.val)
        hists[p].SetBinError(i+1,0)
        if p == "signal":
            hists[p].legendText = "ttZ"
        else:
            hists[p].legendText = p
        if not p == 'total':
           hists[p].style = styles.fillStyle( getattr(color, p), lineColor=getattr(color,p), errors=False )

    hists['total'].SetBinContent(i+1, totalYield.val)
    totalUncertainty = math.sqrt(totalUncertainty)
    hists['total'].SetBinError(i+1, totalUncertainty)
    if options.signal:
        hists['BSM'].SetBinContent(i+1, getEstimateFromCard(cardFile_signal, "signal", binName).val + backgroundYield.val)
        hists['BSM'].SetBinError(i+1, 0.1)
        hists['BSM'].legendText = "C_{1,A}=0, C_{1,V}=-1 "

for i, r in enumerate(regions):
    binName             = "Bin%s"%i
    hists['observed'].SetBinContent(i+1, getObservationFromCard(cardFile, binName).val)
    if not isData:
        hists['observed'].legendText = 'pseudo-data'
    else:
        hists['observed'].legendText = 'Data'
    

#hists['observed'].SetBinErrorOption(ROOT.TH1.kPoisson)
hists['observed'].style = styles.errorStyle( ROOT.kBlack, markerSize = 1. )

if options.signal:
    hists['BSM'].style = styles.lineStyle( ROOT.kRed+1, width=3, dashed=True)

boxes = []
ratio_boxes = []
for ib in range(1, 1 + hists['total'].GetNbinsX() ):
    val = hists['total'].GetBinContent(ib)
    if val<0: continue
    sys = hists['total'].GetBinError(ib)
    sys_rel = sys/val
    
    # uncertainty box in main histogram
    box = ROOT.TBox( hists['total'].GetXaxis().GetBinLowEdge(ib),  max([0.006, val-sys]), hists['total'].GetXaxis().GetBinUpEdge(ib), max([0.006, val+sys]) )
    box.SetLineColor(ROOT.kBlack)
    box.SetFillStyle(3444)
    box.SetFillColor(ROOT.kBlack)
    
    # uncertainty box in ratio histogram
    r_box = ROOT.TBox( hists['total'].GetXaxis().GetBinLowEdge(ib),  max(0.1, 1-sys_rel), hists['total'].GetXaxis().GetBinUpEdge(ib), min(1.9, 1+sys_rel) )
    r_box.SetLineColor(ROOT.kBlack)
    r_box.SetFillStyle(3444)
    r_box.SetFillColor(ROOT.kBlack)

    boxes.append( box )
    hists['total'].SetBinError(ib, 0)
    ratio_boxes.append( r_box )

def drawLabels( regions ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.028)
    tex.SetTextAngle(90)
    tex.SetTextAlign(12) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / len(regions)
    lines =  [(min+(3*i+0.90)*diff, 0.600,  r.texStringForVar('Z_pt'))   for i, r in enumerate(regions[:-3][::3])]
    return [tex.DrawLatex(*l) for l in lines] 

def drawLabels2( regions ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.028)
    tex.SetTextAngle(0)
    tex.SetTextAlign(12) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / len(regions)
    lines =  [(min+(3*i+0.90)*diff, 0.900,  "N_{l}=3")   for i, r in enumerate(regions[:-3][::3])]
    lines += [(min+(12+0.90)*diff, 0.900,  "N_{l}=4")]
    lines +=  [(min+(3*i+0.90)*diff, 0.860,  "N_{b-tag}#geq1")   for i, r in enumerate(regions[:-3][::3])]
    lines += [(min+(12+0.90)*diff, 0.860,  "N_{b-tag}#geq0")]
    lines +=  [(min+(3*i+0.90)*diff, 0.820,  "N_{j}#geq3")   for i, r in enumerate(regions[:-3][::3])]
    lines += [(min+(12+0.90)*diff, 0.820,  "N_{j}#geq2")]
    return [tex.DrawLatex(*l) for l in lines]


def drawDivisions(regions):
    min = 0.15
    max = 0.95
    diff = (max-min) / len(regions)
    lines = []
    lines2 = []
    line = ROOT.TLine()
#   line.SetLineColor(38)
    line.SetLineWidth(1)
    line.SetLineStyle(2)
    line1 = (min+3*diff,  0.013, min+3*diff, 0.93);
    line2 = (min+6*diff, 0.013, min+6*diff, 0.93);
    line3 = (min+9*diff, 0.013, min+9*diff, 0.93);
    line4 = (min+12*diff, 0.013, min+12*diff, 0.80-0.010*32-0.03);
    line5 = (min+12*diff, 0.80+0.03, min+12*diff, 0.93);
    return [line.DrawLineNDC(*l) for l in [line1, line2, line3, line4, line5]] + [tex.DrawLatex(*l) for l in lines] + [tex2.DrawLatex(*l) for l in lines2]


def drawBinNumbers(numberOfBins):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.13 )
    tex.SetTextAlign(23) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / numberOfBins
    lines = [(min+(i+0.5)*diff, 0.35 ,  str(i)) for i in range(numberOfBins)]
    return [tex.DrawLatex(*l) for l in lines]

def drawObjects( isData=False, lumi=36. ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Simulation') if not isData else (0.15, 0.95, 'CMS Preliminary'),
      (0.75, 0.95, '%sfb^{-1} (13 TeV)'%int(lumi) )
    ]
    return [tex.DrawLatex(*l) for l in lines]

def setBinLabels( hist ):
    for i in range(1, hist.GetNbinsX()+1):
        hist.GetXaxis().SetBinLabel(i, "%s"%i)

drawObjects = drawObjects( isData=isData, lumi=round(lumiStr,0)) + boxes + drawLabels( regions ) + drawLabels2( regions ) + drawDivisions( regions )# + drawBinNumbers( len(regions) )

bkgHists = []
for p in processes:
    if p is not "total" and p is not 'observed':
        bkgHists.append(hists[p])

for p in processes + ['total', 'observed', 'BSM']:
    setBinLabels(hists[p])

#histos =  bkgHists  + [hists["total"]]
if options.signal:
    plots = [ bkgHists, [hists['observed']], [hists['BSM']] ]
else:
    plots = [ bkgHists, [hists['observed']]]
if subDir:
    subDir = "%s_"%subDir

plotName = "%s%s_signalRegions_incl4lV7_%s"%(subDir,cardName,options.year)
if options.postFit:
    plotName += "_postFit"

plotting.draw(
    Plot.fromHisto(plotName,
                plots,
                texX = "Signal Region"
            ),
    plot_directory = os.path.join(plot_directory, "signalRegions"),
    logX = False, logY = True, sorting = True, 
    legend = (0.74,0.80-0.010*32, 0.95, 0.80),
    widths = {'x_width':700, 'y_width':600},
    yRange = (0.3,3000.),
    #yRange = (0.03, [0.001,0.5]),
    ratio = {'yRange': (0.6, 1.4), 'drawObjects':ratio_boxes} if not options.postFit else  {'yRange': (0.6, 1.4), 'drawObjects':ratio_boxes},
    drawObjects = drawObjects,
    copyIndexPHP = True,
)


#region_plot = Plot.fromHisto(name = "signalRegions", histos = histos, texX = "Region", texY = "Events" )
#plotting.draw( region_plot, \
#    plot_directory = os.path.join(plot_directory, "signalRegions"),
#    logX = False, logY = True,
#    sorting = False,
#    ratio = {},#ratio,
#    extensions = ["pdf", "png", "root","C"],
#    yRange = "auto",
#    widths = {'x_width':1000, 'y_width':700},
#    #drawObjects = drawObjects,
#    #legend = legend,
#    copyIndexPHP = True,
#    #canvasModifications = canvasModifications,
#    #histModifications = histModifications + ([lambda h: h.GetYaxis().SetNoExponent()] if (args.control and args.control=="TTZ") else []),
#    #ratioModifications = histModifications + [lambda h: h.GetXaxis().SetTitleOffset(5), lambda h: h.GetXaxis().SetTitleSize(30), lambda h: h.GetXaxis().SetLabelSize(0)],
#)




