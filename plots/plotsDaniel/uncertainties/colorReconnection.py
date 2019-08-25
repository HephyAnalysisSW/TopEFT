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
from TopEFT.Analysis.SetupHelpers   import channel, trilepChannels, allTrilepChannels, singlelepChannels, allSinglelepChannels
from TopEFT.Analysis.regions        import regionsE, noRegions, btagRegions, regions4lB, regionsXSec, noRegionsB, regionsXSecB, regionsXSecC
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

setup16.lumi = 1

if options.regionsXSec:
    setup16.parameters.update({"nBTags":(0,-1), "nJets":(1,-1), 'mllMin':0})

# no triggers and filters
setup16.short = True

##Summer16 samples
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v20/singlelep/"
dirs = {}
dirs['TT_pow']                          = ['TT_pow']
dirs['TT_pow_QCDbasedCRTune_erdON']     = ['TT_pow_QCDbasedCRTune_erdON']
dirs['TT_pow_TuneCUETP8M2T4_erdON']     = ['TT_pow_TuneCUETP8M2T4_erdON']
dirs['TT_pow_GluonMoveCRTune']          = ['TT_pow_GluonMoveCRTune']
dirs['TT_pow_TuneCUETP8M2T4down']       = ['TT_pow_TuneCUETP8M2T4down']
dirs['TT_pow_TuneCUETP8M2T4_up']        = ['TT_pow_TuneCUETP8M2T4_up']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TT_pow                      = Sample.fromDirectory(name="TT_pow",                       treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow'])
TT_pow_QCDbasedCRTune_erdON = Sample.fromDirectory(name="TT_pow_QCDbasedCRTune_erdON",  treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow_QCDbasedCRTune_erdON'])
TT_pow_TuneCUETP8M2T4_erdON = Sample.fromDirectory(name="TT_pow_TuneCUETP8M2T4_erdON",  treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow_TuneCUETP8M2T4_erdON'])
TT_pow_GluonMoveCRTune      = Sample.fromDirectory(name="TT_pow_GluonMoveCRTune",       treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow_GluonMoveCRTune'])
TT_pow_TuneCUETP8M2T4_down  = Sample.fromDirectory(name="TT_pow_TuneCUETP8M2T4_down",   treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow_TuneCUETP8M2T4down'])
TT_pow_TuneCUETP8M2T4_up    = Sample.fromDirectory(name="TT_pow_TuneCUETP8M2T4_up",     treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow_TuneCUETP8M2T4_up'])


if options.regionsXSec:
    allRegions = regionsXSecC
else:
    allRegions = noRegions + regionsE + regions4lB
regions = allRegions if options.selectRegion is None else  [allRegions[options.selectRegion]]

#setupIncl = setup.systematicClone(parameters={'mllMin':0, 'nJets':(0,-1), 'nBTags':(0,-1), 'zWindow1':'allZ'})
#setupIncl = setup.systematicClone(parameters={'mllMin':0, 'nJets':(2,-1), 'nBTags':(1,-1), 'zWindow1':'onZ'})
#setup.verbose     = True

# use more inclusive selection in terms of lepton multiplicity in the future?

from TopEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TopEFT.Tools.user import analysis_results

cacheDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/colorReconnectionStudy/"

samples16 = [TT_pow, TT_pow_QCDbasedCRTune_erdON, TT_pow_TuneCUETP8M2T4_erdON, TT_pow_GluonMoveCRTune, TT_pow_TuneCUETP8M2T4_down, TT_pow_TuneCUETP8M2T4_up]#, TT_pow_TuneCUETP8M2T4_erdON]

estimates16 = []

for s in samples16:
    estimates16.append(MCBasedEstimate(name=s.name, sample=s ))
    estimates16[-1].initCache(cacheDir)

jobs = []

def wrapper(args):
    e, r, c, setup = args
    res = e.cachedEstimate(r, c, setup, save=True, overwrite=options.overwrite)
    return (e.uniqueKey(r, c, setup), res )

print regions

for r in noRegionsB:
    for c in [channel(1,0), channel(0,1)]:
        for e in estimates16:
            jobs.append((e, r, c, setup16))

for r in regions:
    for c in [channel(1,0), channel(0,1)]:
        logger.info("Working on 2016 results")
        for e in estimates16:
            jobs.append((e, r, c, setup16))
            #res = e.cachedEstimate(r, channel(-1,-1), setup16, save=True)
            #logger.info("Result: %s", res.val)

if options.noMultiThreading:
    results = map(wrapper, jobs)
else:
    from multiprocessing import Pool
    pool = Pool(processes=8)
    results = pool.map(wrapper, jobs)
    pool.close()
    pool.join()

print setup16.preselection("MC")

variations  = ["QCDbasedCRTune_erdON", "TuneCUETP8M2T4_erdON", "GluonMoveCRTune", "TuneCUETP8M2T4_down", "TuneCUETP8M2T4_up"]#, "TuneCUETP8M2T4_erdON"]
colors      = [ROOT.kRed+1, ROOT.kYellow+1, ROOT.kCyan+1, ROOT.kGreen+1, ROOT.kBlue+1, ROOT.kGray+2]


hists = {}
Nbins = len(regions)
for year in [2016]:
    hists[year] = {}
    for i, var in enumerate(variations):
        hists[year][var] = ROOT.TH1F("%s_%s"%(year,var),"%s_%s"%(year,var), Nbins, 0, Nbins)
        hists[year][var].style = styles.lineStyle(colors[i]-(year%2016), width=2)
        hists[year][var].legendText = "%s_%s"%(year,var)
        

for i, r in enumerate(regions):
    logger.info("Working on 2016 results")
    central_incl = estimates16[0].cachedEstimate(noRegionsB[0], channel(-1,-1), setup16)
    central = estimates16[0].cachedEstimate(r, channel(-1,-1), setup16)
    print r.cutString()
    print central
    for j,e in enumerate(estimates16[1:]):
        incl = e.cachedEstimate(noRegionsB[0], channel(-1,-1), setup16)
        norm = central_incl/incl
        res = norm * e.cachedEstimate(r, channel(-1,-1), setup16)
        #print "norm", central/norm
        #norm = central_incl/incl
        #res = res * central/norm
        #print (res-central)/central
        
        if central.val>0:
            hists[2016][variations[j]].SetBinContent(i+1, ((res-central)/central).val)
        else:
            hists[2016][variations[j]].SetBinContent(i+1, 0)

        #logger.info("Result: %s", res.val)

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
    line.SetLineStyle(2)
    #lines = [ (0, 0, 6, 0), (3, -0.1, 3, 0.1)  ]
    lines = [ (0, 0, 8, 0) ]#, (4, -0.1, 4, 0.1)  ]
    return [line.DrawLine(*l) for l in lines]

def drawBinNumbers(numberOfBins):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.03 )
    tex.SetTextAlign(23) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / numberOfBins
    #lines = [(min+(i+0.5)*diff, 0.05 ,  "N_{j} %s %i"%("#geq" if i==2 or i ==5 else "=", i%3 + 1)) for i in range(numberOfBins)]
    lines = [(min+(i+0.5)*diff, 0.05 ,  "N_{j} %s %i"%("#geq" if i==3 or i ==7 else "=", i%4 + 2)) for i in range(numberOfBins)]
    lines += [(0.3, 0.7, "N_{b}=1"), (0.7, 0.7, "N_{b}#geq2")]
    return [tex.DrawLatex(*l) for l in lines]

drawObjects = drawObjects( isData=False, lumi=round(35.9,0)) + drawZero() #+ drawBinNumbers(8)



plots_CR    =  [ [hists[2016]["QCDbasedCRTune_erdON"]], [hists[2016]["TuneCUETP8M2T4_erdON"]], [hists[2016]["GluonMoveCRTune"]]]
#plots_tune  =  [ [hists[2016]["TuneCUETP8M2T4_down"]], [hists[2016]["TuneCUETP8M2T4_up"]] ] 

for i in range(1,4):
    print hists[2016]["QCDbasedCRTune_erdON"].GetBinContent(i)



from TopEFT.Tools.user              import plot_directory

plotting.draw(
    Plot.fromHisto("CR_reweight",
                plots_CR,
                texX = "Signal Region",
                texY = "variation"
            ),
    plot_directory = os.path.join(plot_directory, "colorReconnection"),
    logX = False, logY = False, sorting = False,
    #legend = (0.74,0.80-0.010*8, 0.95, 0.80),
    legend = [ (0.15,0.9-0.03*sum(map(len, plots_CR)),0.9,0.9), 2],
    widths = {'x_width':700, 'y_width':600},
    yRange = (-0.1, 0.1),
    #yRange = (0.03, [0.001,0.5]),
    #ratio = {'yRange': (0.6, 1.4), 'drawObjects':boxes, 'texY':"#kappa"},
    drawObjects = drawObjects,
    copyIndexPHP = True,
)

#plotting.draw(
#    Plot.fromHisto("tune_v2",
#                plots_tune,
#                texX = "Signal Region",
#                texY = "variation"
#            ),
#    plot_directory = os.path.join(plot_directory, "tune"),
#    logX = False, logY = False, sorting = False,
#    #legend = (0.74,0.80-0.010*8, 0.95, 0.80),
#    legend = [ (0.15,0.9-0.03*sum(map(len, plots_tune)),0.9,0.9), 2],
#    widths = {'x_width':700, 'y_width':600},
#    yRange = (-0.1, 0.1),
#    #yRange = (0.03, [0.001,0.5]),
#    #ratio = {'yRange': (0.6, 1.4), 'drawObjects':boxes, 'texY':"#kappa"},
#    drawObjects = drawObjects,
#    copyIndexPHP = True,
#)


logger.info("All done.")

