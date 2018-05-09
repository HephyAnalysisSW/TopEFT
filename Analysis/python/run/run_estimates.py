#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
parser.add_option("--controlRegion",  action='store', default='', choices = ['', 'nbtag0-njet3p', 'nbtag1p-njet02', 'nbtag1p-njet2', 'nbtag0-njet02', 'nbtag0-njet0p', 'nbtag0-njet1p', 'nbtag0-njet2p'], help="Use any CRs cut?")
parser.add_option("--sample", action='store', default='WZ', choices = ["WZ", "TTX", "TTW", "TZQ", "rare", "nonprompt", "pseudoData", "TTZ", "Data"], help="Choose which sample to run the estimates for")
parser.add_option("--year",            action='store',      default=2016, choices = [ '2016', '2017', '20167' ], help='Which year?')
parser.add_option("--skipSystematics", action='store_true', help="Don't run the systematic variations")
parser.add_option("--overwrite", action='store_true', help="Overwrite?")
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
from TopEFT.Analysis.DataObservation    import DataObservation


#RootTools
from RootTools.core.standard import *

from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter

## 2016
postProcessing_directory = "TopEFT_PP_2016_mva_v2/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

## 2017
postProcessing_directory = "TopEFT_PP_2017_mva_v3/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *

import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   options.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None)

allRegions = regionsE + noRegions

from TopEFT.Analysis.Setup              import Setup
year                    = int(options.year)
setup                   = Setup(year=year, nLeptons=3)
estimators              = estimatorList(setup)
setup.estimators        = estimators.constructEstimatorList(["WZ", "TTX", "TTW", "TZQ", "rare", "nonprompt"])
setup.reweightRegions   = regionsReweight
setup.channels          = [channel(-1,-1)]

# go orthogonal in Njet and Nbjet if needed
if options.controlRegion:
    if options.controlRegion == 'nbtag0-njet3p':
        setup = setup.systematicClone(parameters={'nJets':(3,-1), 'nBTags':(0,0)})
    elif options.controlRegion == 'nbtag0-njet2p':
        setup = setup.systematicClone(parameters={'nJets':(2,-1), 'nBTags':(0,0)})
    elif options.controlRegion == 'nbtag1p-njet02':
        setup = setup.systematicClone(parameters={'nJets':(0,2), 'nBTags':(1,-1)})
    elif options.controlRegion == 'nbtag1p-njet2':
        setup = setup.systematicClone(parameters={'nJets':(2,2), 'nBTags':(1,-1)})
    elif options.controlRegion == 'nbtag0-njet02':
        setup = setup.systematicClone(parameters={'nJets':(0,2), 'nBTags':(0,0)})
    elif options.controlRegion == 'nbtag0-njet0p':
        setup = setup.systematicClone(parameters={'nJets':(0,-1), 'nBTags':(0,0)})
    elif options.controlRegion == 'nbtag0-njet1p':
        setup = setup.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,0)})
    else:
        raise NotImplementedError

setup.verbose = True
#setupCR = setup.systematicClone(parameters={'nJets':(0,-1), 'nBTags':(0,0)})

reweights = ["reweightBTagDeepCSV_SF_b_Up", "reweightBTagDeepCSV_SF_b_Down", "reweightBTagDeepCSV_SF_l_Up", "reweightBTagDeepCSV_SF_l_Down", "reweightPU36fbUp", "reweightPU36fbDown"]
modifiers = ['JECUp', 'JECDown', 'JERUp', 'JERDown']

setups = [setup]

setup4l = Setup(year=year, nLeptons=4)

if (options.sample not in ["Data", "pseudoData"]) and not (options.skipSystematics):
    for r in reweights:
        setups.append(setup.systematicClone(sys={"reweight":[r]}))
    for m in modifiers:
        setups.append(setup.systematicClone(sys={"selectionModifier":m}))

#signalReweighting = SignalReweighting( source_sample = source_gen, target_sample = s, cacheDir = reweightCache)

def wrapper(args):
        e,r,channel,setup = args
        res = e.cachedEstimate(r, channel, setup, save=True, overwrite=options.overwrite)
        return (e.uniqueKey(r, channel.name, setup), res )

jobs=[]

if options.sample not in ["Data", "TTZ", "pseudoData"]:
    estimators = estimators.constructEstimatorList([options.sample]) if options.sample else estimators.constructEstimatorList(["WZ", "TTX", "TTW", "TZQ", "rare", "nonprompt"])
else:
    estimators = []

logger.info("Starting estimates for sample %s", setup.samples[options.sample]['3mu'].name)

for setup in setups:

    signal      = MCBasedEstimate(name="TTZ", sample=setup.samples["TTZ"], cacheDir=setup.defaultCacheDir())
    data        = DataObservation(name="Data", sample=setup.samples["Data"], cacheDir=setup.defaultCacheDir())
    observation = MCBasedEstimate(name="observation", sample=setup.samples["pseudoData"], cacheDir=setup.defaultCacheDir())
    for e in estimators: e.initCache(setup.defaultCacheDir())

    for r in setup.regions:
        for channel in setup.channels:

            if options.sample == "Data":
                jobs.append((data, r, channel, setup))
            elif options.sample == "TTZ":
                jobs.append((signal, r, channel, setup))
            elif options.sample == "pseudoData":
                jobs.append((observation, r, channel, setup))
            else:
                for e in estimators:
                    name = e.name.split('-')[0]
                    jobs.append((e, r, channel, setup))


if options.sample == "TTZ":
    for setup in [setups[0]]:
        for rr in setup.reweightRegions:
            jobs.append((signal, rr, channel, setup))



if options.noMultiThreading:
    results = map(wrapper, jobs)
else:
    from multiprocessing import Pool
    pool = Pool(processes=8)
    results = pool.map(wrapper, jobs)
    pool.close()
    pool.join()


