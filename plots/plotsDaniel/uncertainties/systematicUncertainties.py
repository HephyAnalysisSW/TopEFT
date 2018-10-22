#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option("--selectRegion",         dest="selectRegion",          default=None, type="int",    action="store",      help="select region?")
parser.add_option("--small",                action='store_true', help="small?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
parser.add_option('--overwrite',            dest="overwrite", default = False, action = "store_true", help="Overwrite existing output files, bool flag set to True  if used")
parser.add_option('--regionsXSec',          dest="regionsXSec", default = False, action = "store_true", help="Use nJet and nBTag binning")
(options, args) = parser.parse_args()

# Standard imports
import ROOT
import os
import sys
import pickle
import math

# Analysis
from TopEFT.Analysis.SetupHelpers       import channel, trilepChannels, allTrilepChannels, singlelepChannels, allSinglelepChannels
from TopEFT.Analysis.regions            import noRegions, regionsA, regionsE, regionsReweight, regionsReweight4l, regions4l, regions4lB
from TopEFT.Analysis.estimators         import *
from TopEFT.Analysis.DataObservation    import DataObservation
from TopEFT.Analysis.FakeEstimate       import FakeEstimate
from TopEFT.Analysis.run.SignalReweightingTemplate import *
from TopEFT.Analysis.run.WZReweightingTemplate import *
from TopEFT.Tools.u_float           import u_float
from TopEFT.Tools.resultsDB         import resultsDB
from TopEFT.Analysis.Region         import Region

#RootTools
from RootTools.core.standard import *

from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter

import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   options.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None)

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"

## 2016 ##
postProcessing_directory = "TopEFT_PP_2016_mva_v20/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2016_mva_v20/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *

## 2017 ##
postProcessing_directory = "TopEFT_PP_2017_mva_v20/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v20/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *

from TopEFT.Analysis.Setup          import Setup

setup16 = Setup(year=2016, nLeptons=1)
colors      = [ROOT.kRed+1, ROOT.kGreen+1, ROOT.kBlue+1, ROOT.kGray+2]

setup16.lumi = 1

signal      = MCBasedEstimate(name="TTZ", sample=setup16.samples["TTZ"], cacheDir=setup16.defaultCacheDir())

TTZ_sample      = "TTZ_NLO_17"
PDFset          = "PDF4LHC15_nlo_100"
PDF_cacheDir    = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/PDF_%s/"%PDFset
PDF_cache       = resultsDB(PDF_cacheDir+TTZ_sample+'_unc.sq', "PDF", ["region", "channel", "PDFset"])
scale_cache     = resultsDB(PDF_cacheDir+TTZ_sample+'_unc.sq', "scale", ["region", "channel", "PDFset"])
PS_cache        = resultsDB(PDF_cacheDir+TTZ_sample+'_unc.sq', "PSscale", ["region", "channel", "PDFset"])

if options.regionsXSec:
    setup16.parameters.update({"nBTags":(0,-1), "nJets":(2,-1), 'mllMin':0})

# no triggers and filters
setup16.short = True

##Summer16 samples

allRegions = regionsE + regions4lB
regions = allRegions

hists = {}
Nbins = len(regions)
for i, var in enumerate(["PDF","scale","PSscale"]):
    hists[var] = ROOT.TH1F(var, var, Nbins, 0, Nbins)
    hists[var].style = styles.lineStyle(colors[i], width=2)
    hists[var].legendText = var
        

for i, r in enumerate(regions):
    logger.info("Working on 2016 results")

    hists["PDF"].SetBinContent(i+1, PDF_cache.get({"region":r, "channel":'all', "PDFset":"PDF4LHC15_nlo_100"}).val)
    hists["PDF"].GetXaxis().SetBinLabel(i+1, "%i"%(i+1))
    hists["scale"].SetBinContent(i+1, scale_cache.get({"region":r, "channel":'all', "PDFset":"scale"}).val)
    hists["PSscale"].SetBinContent(i+1, PS_cache.get({"region":r, "channel":'all', "PDFset":"PSscale"}).val-1)
    

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

def drawZero():
    lines = []
    line = ROOT.TLine()
#   line.SetLineColor(38)
    line.SetLineWidth(1)
    line.SetLineStyle(1)
    lines = [ (12, 0., 12, 0.15)  ]
    return [line.DrawLine(*l) for l in lines]

def drawLabelsLower( regions ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextFont(42)
    tex.SetTextAngle(0)
    tex.SetTextAlign(23) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / len(regions)

    lines  = [(min+6*diff, 0.80, "N_{b}=0"),        (min+13.5*diff, 0.80, "N_{b}#geq0"),      (min+21*diff, 0.80, "N_{b}#geq1"),      (min+28.5*diff, 0.80, "N_{b}#geq1")]
    lines += [(min+6*diff, 0.85, "N_{jet}#geq1"),   (min+13.5*diff, 0.85, "N_{jet}#geq0"),    (min+21*diff, 0.85, "N_{jet}#geq3"),    (min+28.5*diff, 0.85, "N_{jet}#geq1")]
    lines += [(min+6*diff, 0.90, "N_{lep}=3"),      (min+13.5*diff, 0.90, "N_{lep}=4"),       (min+21*diff, 0.90, "N_{lep}=3"),       (min+28.5*diff, 0.90, "N_{lep}=4")]

    return [tex.DrawLatex(*l) for l in lines]


def drawLabels( regions ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.028)
    if len(regions)>12:
        tex.SetTextAngle(90)
    else:
        tex.SetTextAngle(0)
    tex.SetTextAlign(12) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / len(regions)
    y_pos = 0.50 if len(regions)>12 else 0.85
    x_pos = 0.90 if len(regions)>12 else 0.25
    if len(regions) > 12:
        lines =  [(min+(3*i+x_pos)*diff, y_pos,  r.texStringForVar('Z_pt'))   for i, r in enumerate(regions[:-3][::3])]
    else:
        lines =  [(min+(3*i+x_pos)*diff, y_pos,  r.texStringForVar('Z_pt'))   for i, r in enumerate(regions[::3])]
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
    lines = [ (min+3*i*diff,  0.1, min+3*i*diff, 0.75) if min+3*i*diff<0.74 else (min+3*i*diff,  0.1, min+3*i*diff, 0.75) for i in range(1,10) ]
    return [line.DrawLineNDC(*l) for l in lines] + [tex.DrawLatex(*l) for l in []] + [tex2.DrawLatex(*l) for l in lines2]

drawObjects = drawObjects( isData=False, lumi=round(35.9,0)) + drawZero() + drawLabelsLower(regions) + drawLabels(regions) + drawDivisions(regions)



plots_CR    =  [ [hists["PDF"]], [hists["scale"]], [hists["PSscale"]] ]




from TopEFT.Tools.user              import plot_directory

plotting.draw(
    Plot.fromHisto("syst",
                plots_CR,
                texX = "Signal region",
                texY = "syst. uncertainty"
            ),
    plot_directory = os.path.join(plot_directory, "systematicUncertainties"),
    logX = False, logY = False, sorting = False,
    #legend = (0.74,0.80-0.010*8, 0.95, 0.80),
    legend = [ (0.15,0.9-0.03*sum(map(len, plots_CR)),0.9,0.9), 2],
    widths = {'x_width':700, 'y_width':600},
    yRange = (0.0, 0.15),
    #yRange = (0.03, [0.001,0.5]),
    #ratio = {'yRange': (0.6, 1.4), 'drawObjects':boxes, 'texY':"#kappa"},
    drawObjects = drawObjects,
    copyIndexPHP = True,
)


logger.info("All done.")

