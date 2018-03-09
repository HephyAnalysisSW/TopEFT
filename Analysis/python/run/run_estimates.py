#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
(options, args) = parser.parse_args()

# Standard imports
import ROOT
import os
import sys
import pickle
import math

# Analysis
from TopEFT.Analysis.SetupHelpers import channels, allChannels
from TopEFT.Analysis.regions      import regionsE, noRegions, regionsReweight
from TopEFT.Tools.u_float      import u_float
from TopEFT.Analysis.Region       import Region

from TopEFT.Analysis.estimators         import *


#RootTools
from RootTools.core.standard import *

from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter

import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   options.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None)

allRegions = regionsE + noRegions

from TopEFT.Analysis.Setup              import Setup

setup                   = Setup(year=2016)
estimators = estimatorList(setup)
setup.estimators        = estimators.constructEstimatorList(["WZ", "TTX", "TTW", "TZQ", "rare", "nonprompt"])
setup.reweightRegions   = regionsReweight

# go orthogonal in Njet and Nbjet if needed
setupCR = setup.systematicClone(parameters={'nJets':(0,-1), 'nBTags':(0,0)})
setupCR.verbose     = True

setups = [setupCR]

data_directory = '/afs/hephy.at/data/rschoefbeck01/cmgTuples/'
postProcessing_directory = "TopEFT_PP_v14/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *


#signalReweighting = SignalReweighting( source_sample = source_gen, target_sample = s, cacheDir = reweightCache)

def wrapper(args):
        e,r,channel,setup = args
        res = e.cachedEstimate(r, channel, setup, save=True)
        return (e.uniqueKey(r, channel, setup), res )

jobs=[]

for setup in setups:
    signal      = MCBasedEstimate(name="TTZ", sample=setup.samples["TTZ"], cacheDir=setup.defaultCacheDir())
    observation = MCBasedEstimate(name="observation", sample=setup.samples["pseudoData"], cacheDir=setup.defaultCacheDir())
    for e in setup.estimators: e.initCache(setup.defaultCacheDir())
    for r in setup.regions:
        for channel in setup.channels:

            for e in setup.estimators:
                name = e.name.split('-')[0]
                jobs.append((e, r, channel, setup))
            
            jobs.append((observation, r, channel, setup))
            jobs.append((signal, r, channel, setup))



if options.noMultiThreading:
    results = map(wrapper, jobs)
else:
    from multiprocessing import Pool
    pool = Pool(processes=8)
    results = pool.map(wrapper, jobs)
    pool.close()
    pool.join()


















#from TopEFT.Analysis.run.getEstimates import getEstimate
##from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *
#
#data_directory = '/afs/hephy.at/data/rschoefbeck02/cmgTuples/'
#postProcessing_directory = "TopEFT_PP_v12/trilep/"
#from TopEFT.samples.cmgTuples_ttZ0j_Summer16_mAODv2_postProcessed import *
#
#data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
#postProcessing_directory = "TopEFT_PP_v12/dilep/"
#from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
#
#
#from TopEFT.Analysis.regions import *
#
#myRegions = regionsH
#
#for signal in allSignals:
#    for r in myRegions:
#        getEstimate(signal, r, "all", overwrite=True)
#
#mc = [TTZtoLLNuNu, WZ, TTX, TTW, TZQ, rare, nonprompt, pseudoData ]#, pseudoDataPriv]
#
#for sample in mc:
#    for r in myRegions:
#        getEstimate(sample, r, "all", overwrite=False)
