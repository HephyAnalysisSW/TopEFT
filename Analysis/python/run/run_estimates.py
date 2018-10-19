#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
parser.add_option("--controlRegion",  action='store', default='', choices = ['', 'nbtag0-njet1p-3l', 'nbtag0p-njet1p-4l'], help="Use any CRs cut?")
parser.add_option("--sample", action='store', default='WZ', choices = ["WZ", "TTX", "XG", "rare", "nonprompt", "pseudoData", "TTZ", "Data", "ZZ"], help="Choose which sample to run the estimates for")
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
import copy

# Analysis
from TopEFT.Analysis.SetupHelpers import *
from TopEFT.Analysis.regions      import regionsE, noRegions, regionsReweight, regions4l, regionsReweight4l, regions4lB
from TopEFT.Tools.u_float      import u_float
from TopEFT.Analysis.Region       import Region

from TopEFT.Analysis.estimators         import *
from TopEFT.Analysis.DataObservation    import DataObservation
from TopEFT.Analysis.FakeEstimate       import FakeEstimate

#RootTools
from RootTools.core.standard import *

from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter

## 2016
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *
postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

## 2017
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
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
setup.estimators        = estimators.constructEstimatorList(["WZ", "TTX", "XG", "rare", "ZZ"])
setup.reweightRegions   = regionsReweight
setup.channels          = [channel(-1,-1)]
setup.regions           = noRegions + regionsE

setupNP                 = Setup(year=year, nLeptons=3, nonprompt=True)
setupNP.channels          = [channel(-1,-1)]
setupNP.regions           = noRegions + regionsE

setup.verbose = True
#setupCR = setup.systematicClone(parameters={'nJets':(0,-1), 'nBTags':(0,0)})

#reweights = ["reweightBTagDeepCSV_SF_b_Up", "reweightBTagDeepCSV_SF_b_Down", "reweightBTagDeepCSV_SF_l_Up", "reweightBTagDeepCSV_SF_l_Down", "reweightPU36fbUp", "reweightPU36fbDown"]
#reweights3l = reweights + ["reweightTriggerDown_tight_3l", "reweightTriggerUp_tight_3l", "reweightLeptonSFDown_tight_3l", "reweightLeptonSFUp_tight_3l"]
#reweights4l = reweights + ["reweightTriggerDown_tight_4l", "reweightTriggerUp_tight_4l", "reweightLeptonSFDown_tight_4l", "reweightLeptonSFUp_tight_4l"]
reweights = ["reweightBTagDeepCSV_SF_b_Up", "reweightBTagDeepCSV_SF_b_Down", "reweightBTagDeepCSV_SF_l_Up", "reweightBTagDeepCSV_SF_l_Down", "reweightPU36fbUp", "reweightPU36fbDown"]
reweights3l = reweights + ["reweightTriggerDown_tight_3l", "reweightTriggerUp_tight_3l", "reweightLeptonSFSystDown_tight_3l", "reweightLeptonSFSystUp_tight_3l", "reweightEleSFStatDown_tight_3l", "reweightEleSFStatUp_tight_3l", "reweightMuSFStatDown_tight_3l", "reweightMuSFStatUp_tight_3l", "reweightLeptonTrackingSFDown_tight_3l", "reweightLeptonTrackingSFUp_tight_3l"]
reweights4l = reweights + ["reweightTriggerDown_tight_4l", "reweightTriggerUp_tight_4l", "reweightLeptonSFSystDown_tight_4l", "reweightLeptonSFSystUp_tight_4l", "reweightEleSFStatDown_tight_4l", "reweightEleSFStatUp_tight_4l", "reweightMuSFStatDown_tight_4l", "reweightMuSFStatUp_tight_4l", "reweightLeptonTrackingSFDown_tight_4l", "reweightLeptonTrackingSFUp_tight_4l"]
modifiers = ['JECUp', 'JECDown', 'JERUp', 'JERDown']

## 4l setup ##
setup4l                   = Setup(year=year, nLeptons=4)
setup4l.parameters.update({'nJets':(1,-1), 'nBTags':(1,-1), 'zMassRange':20, 'zWindow2':'offZ'})
estimators4l              = estimatorList(setup4l)
setup4l.estimators        = estimators4l.constructEstimatorList(["ZZ", "rare"])
setup4l.reweightRegions   = regionsReweight4l
setup4l.channels          = [channel(-1,-1)]
setup4l.regions           = noRegions + regions4lB

## 4l control region setup
# to be added now

setup_CR = setup.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,0)})
setupNP_CR = setupNP.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,0)})
setup4l_CR = setup4l.systematicClone(parameters={'nJets':(0,-1), 'nBTags':(0,-1), 'zWindow2':"onZ"})

# control region setups. go orthogonal in Njet and Nbjet if needed
if options.controlRegion:
    if options.controlRegion == 'nbtag0-njet1p-3l':
        setup_CR = setup.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,0)})
        setupNP_CR = setupNP.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,0)})
    elif options.controlRegion == 'nbtag0p-njet1p-4l':
        setup4l_CR = setup4l.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,-1), 'zWindow2':"onZ"})
    else:
        raise NotImplementedError


# only run over 3l/4l when necessary
if not options.controlRegion:
    if not options.sample in ["nonprompt"]:
        setups = [setup, setup_CR]
        if options.sample in ["ZZ","rare","TTX","TTZ","Data","pseudoData"]:
            setups += [setup4l, setup4l_CR]
    else:
        setups = [setupNP, setupNP_CR]
else:
    if not options.sample in ["nonprompt"]:
        setups = [setup_CR] if '3l' in options.controlRegion else [setup4l_CR]
    else:
        setups = [setupNP_CR]

#
#if options.sample in []:
#    setups = [setup4l]
#elif options.sample in ["WZ", "TTX", "TTW", "TZQ"]:
#    setups = [setup]
#elif options.sample in ["nonprompt"]:
#    setups = [setupNP]
#else:
#    # rare, ZZ, nonprompt, pseudodata, TTZ run in all SRs
#    setups = [setup, setup4l]

######### only for now ###############
#setups = [setup]

allSetups = [ copy.deepcopy(s) for s in setups ]

if (options.sample not in ["Data", "pseudoData", "nonprompt"]) and not (options.skipSystematics):
    for s in setups:
        reweights = reweights3l if s.nLeptons == 3 else reweights4l
        for r in reweights:
        #for s in setups:
            allSetups.append(s.systematicClone(sys={"reweight":[r]}))
    for m in modifiers:
        for s in setups:
            allSetups.append(s.systematicClone(sys={"selectionModifier":m}))

#signalReweighting = SignalReweighting( source_sample = source_gen, target_sample = s, cacheDir = reweightCache)

def wrapper(args):
        e,r,channel,setup = args
        res = e.cachedEstimate(r, channel, setup, save=True, overwrite=options.overwrite)
        return (e.uniqueKey(r, channel, setup), res )

jobs=[]

if options.sample not in ["Data", "TTZ", "pseudoData", "nonprompt"]:
    estimators = estimators.constructEstimatorList([options.sample]) if options.sample else estimators.constructEstimatorList(["WZ", "TTX", "TTW", "TZQ", "rare"])
else:
    estimators = []

logger.info("Starting estimates for sample %s", setup.samples[options.sample].name)

for setup in allSetups:

    signal      = MCBasedEstimate(name="TTZ_%s"%year, sample=setup.samples["TTZ"], cacheDir=setup.defaultCacheDir())
    data        = DataObservation(name="Data_%s"%year, sample=setup.samples["Data"], cacheDir=setup.defaultCacheDir())
    observation = MCBasedEstimate(name="observation_%s"%year, sample=setup.samples["pseudoData"], cacheDir=setup.defaultCacheDir())
    nonprompt   = FakeEstimate(name="nonPromptDD_%s"%year, sample=setup.samples["Data"], setup=setup, cacheDir=setup.defaultCacheDir())

    estimatorsC = [ copy.deepcopy(e) for e in estimators ]
    for e in estimatorsC: e.initCache(setup.defaultCacheDir())

    logger.info("Cache for setup %s is located in %s", setup, setup.defaultCacheDir())
    for r in setup.regions:
        for channel in setup.channels:
            if options.sample == "Data":
                jobs.append((data, r, channel, setup))
            elif options.sample == "TTZ":
                jobs.append((signal, r, channel, setup))
            elif options.sample == "pseudoData":
                jobs.append((observation, r, channel, setup))
            elif options.sample == "nonprompt":
                jobs.append((nonprompt, r, channel, setup))
            else:
                setup.short = True if options.sample == 'ZG' and year == 2017 else False
                for e in estimatorsC:
                    #name = e.name.split('-')[0]
                    jobs.append((e, r, channel, setup))


if options.sample == "TTZ":
    for setup in [allSetups[0]]:
        for rr in setup.reweightRegions:
            jobs.append((signal, rr, channel, setup))

logger.info("Created %s jobs", len(jobs))


if options.noMultiThreading:
    results = map(wrapper, jobs)
else:
    from multiprocessing import Pool
    pool = Pool(processes=8)
    results = pool.map(wrapper, jobs)
    pool.close()
    pool.join()

logger.info("Done.")
