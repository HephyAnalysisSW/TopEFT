#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option("--selectWeight",         dest="selectWeight",       default=None,                action="store",      help="select weight?")
parser.add_option("--PDFset",               dest="PDFset",              default="NNPDF30", choices=["NNPDF30", "PDF4LHC15_nlo_100"], help="select the PDF set")
parser.add_option("--selectRegion",         dest="selectRegion",          default=None, type="int",    action="store",      help="select region?")
parser.add_option("--sample",               dest='sample',  action='store', default='TTZ_NLO_16',    choices=["TTZ_LO_16", "TTZ_NLO_16", "TTZ_NLO_17", "WZ_pow_16"], help="which sample?")
parser.add_option("--small",                action='store_true', help="small?")
parser.add_option("--reducedPDF",           action='store_true', help="Don't use all PDF variations for tests?")
parser.add_option("--combine",              action='store_true', help="Combine results?")
parser.add_option("--noKeepNorm",           action='store_true', help="Keep the normalization = acceptance uncertainty only?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
parser.add_option('--overwrite',            dest="overwrite", default = False, action = "store_true", help="Overwrite existing output files, bool flag set to True  if used")
parser.add_option('--skipCentral',          dest="skipCentral", default = False, action = "store_true", help="Skip central weights")
parser.add_option('--btagWZ',               dest="btagWZ", default = False, action = "store_true", help="Get the uncertainties for b-tag extrapolation of WZ")
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
from TopEFT.Analysis.regions        import regionsE, noRegions, btagRegions, regions4lB, regionsXSec
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
postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *

## 2017 ##
postProcessing_directory = "TopEFT_PP_2017_mva_v20/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v20/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *

from TopEFT.Analysis.Setup          import Setup

setup16 = Setup(year=2016, nLeptons=3)
setup16.lumi = 1
setup16.parameters.update({"nBTags":(1,-1), "nJets":(3,-1)})

setup16.default_sys['reweight'].remove('reweightLeptonSFSyst_tight_3l')

# no triggers and filters
setup16.short = True

##Summer16 samples
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v21_CR/trilep/"
dirs = {}
dirs['TTZToLLNuNu']          = ['TTZToLLNuNu_ext']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TTZ_CR     = Sample.fromDirectory(name="TTZToLLNuNu", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}Z", directory=directories['TTZToLLNuNu'])

allRegions = noRegions + regionsE + regions4lB
regions = allRegions if options.selectRegion is None else  [allRegions[options.selectRegion]]

# use more inclusive selection in terms of lepton multiplicity in the future?

from TopEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TopEFT.Tools.user import analysis_results

cacheDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/CRReweight/"


estimate = MCBasedEstimate(name='TTZ', sample=TTZ_CR )
estimate.initCache(cacheDir)

jobs = []

def wrapper(args):
    e, r, c, setup = args
    res = e.cachedEstimate(r, c, setup, save=True, overwrite=options.overwrite)
    return (e.uniqueKey(r, c, setup), res )

print regions

for r in regions:
    for c in [channel(3,0), channel(2,1), channel(1,2), channel(0,3)]:
        logger.info("Working on 2016 results")
        jobs.append((estimate, r, c, setup16))
        jobs.append((estimate, r, c, setup16.systematicClone(sys={'reweight':['reweightCR']})))


if options.noMultiThreading:
    results = map(wrapper, jobs)
else:
    from multiprocessing import Pool
    pool = Pool(processes=8)
    results = pool.map(wrapper, jobs)
    pool.close()
    pool.join()

print setup16.preselection("MC")

variations  = ["CR"]
colors      = [ROOT.kRed+1, ROOT.kGreen+1, ROOT.kBlue+1, ROOT.kGray+2]


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
    central = estimate.cachedEstimate(r, channel(-1,-1), setup16)
    varied  = estimate.cachedEstimate(r, channel(-1,-1), setup16.systematicClone(sys={'reweight':['reweightCR']}))
    print abs(varied-central)/central
    hists[2016]["CR"].SetBinContent(i+1, ((varied-central)/central).val)
        

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


drawObjects = drawObjects( isData=False, lumi=round(35.9,0))



plots_fsr =  [ [hists[2016]["CR"]] ]


from TopEFT.Tools.user              import plot_directory

plotting.draw(
    Plot.fromHisto("reweightCR",
                plots_fsr,
                texX = "Signal Region"
            ),
    plot_directory = os.path.join(plot_directory, "colorReconnection"),
    logX = False, logY = False, sorting = False,
    #legend = (0.74,0.80-0.010*8, 0.95, 0.80),
    legend = [ (0.15,0.9-0.03*sum(map(len, plots_fsr)),0.9,0.9), 2],
    widths = {'x_width':700, 'y_width':600},
    yRange = (-0.2, 0.2),
    #yRange = (0.03, [0.001,0.5]),
    #ratio = {'yRange': (0.6, 1.4), 'drawObjects':boxes, 'texY':"#kappa"},
    drawObjects = drawObjects,
    copyIndexPHP = True,
)

logger.info("All done.")

