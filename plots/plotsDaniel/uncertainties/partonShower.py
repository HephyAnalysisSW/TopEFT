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
setup17 = Setup(year=2017, nLeptons=1)

setup16.lumi = 1
setup17.lumi = 1

if options.btagWZ:
    setup16.parameters.update({"nBTags":(0,-1), "nJets":(1,-1)})
    setup17.parameters.update({"nBTags":(0,-1), "nJets":(1,-1)})

elif options.regionsXSec:
    setup16.parameters.update({"nBTags":(0,-1), "nJets":(2,-1), 'mllMin':0})
    setup17.parameters.update({"nBTags":(0,-1), "nJets":(2,-1), 'mllMin':0})

# no triggers and filters
setup16.short = True
setup17.short = True

##Summer16 samples
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v20/singlelep/"
dirs = {}
dirs['TT_pow']          = ['TT_pow']
dirs['TT_pow_fsrup']    = ['TT_pow_fsrup']
dirs['TT_pow_fsrdown']  = ['TT_pow_fsrdown']
dirs['TT_pow_isrup']    = ['TT_pow_isrup']
dirs['TT_pow_isrdown']  = ['TT_pow_isrdown']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TT_pow          = Sample.fromDirectory(name="TT_pow", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow'])
TT_pow_fsrup    = Sample.fromDirectory(name="TT_pow_fsrup", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow_fsrup'])
TT_pow_fsrdown  = Sample.fromDirectory(name="TT_pow_fsrdown", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow_fsrdown'])
TT_pow_isrup    = Sample.fromDirectory(name="TT_pow_isrup", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow_isrup'])
TT_pow_isrdown  = Sample.fromDirectory(name="TT_pow_isrdown", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}", directory=directories['TT_pow_isrdown'])

## Fall17 samples
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2017_mva_v20/singlelep/"
dirs = {}
dirs['TTSemi_pow']  = ['TTSemi_pow']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}
TTSemi_pow_17 = Sample.fromDirectory(name="TTSemi_pow_17", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}Z, Z#rightarrowll (NLO)", directory=directories['TTSemi_pow'])

if options.btagWZ:
    allRegions = btagRegions + noRegions
elif options.regionsXSec:
    allRegions = regionsXSec
else:
    allRegions = noRegions + regionsE + regions4lB
regions = allRegions if options.selectRegion is None else  [allRegions[options.selectRegion]]

#setupIncl = setup.systematicClone(parameters={'mllMin':0, 'nJets':(0,-1), 'nBTags':(0,-1), 'zWindow1':'allZ'})
#setupIncl = setup.systematicClone(parameters={'mllMin':0, 'nJets':(2,-1), 'nBTags':(1,-1), 'zWindow1':'onZ'})
#setup.verbose     = True

# use more inclusive selection in terms of lepton multiplicity in the future?

from TopEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TopEFT.Tools.user import analysis_results

PS_indices = range(1086, 1090)
PSweight_original = "abs(LHEweight_wgt[1080])"

cacheDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/partonShowerStudy/"

samples16 = [TT_pow, TT_pow_isrup, TT_pow_fsrup, TT_pow_isrdown, TT_pow_fsrdown]
samples17 = [TTSemi_pow_17]

estimates16 = []
estimates17 = []

for s in samples16:
    estimates16.append(MCBasedEstimate(name=s.name, sample=s ))
    estimates16[-1].initCache(cacheDir)

for s in samples17:
    estimates17.append(MCBasedEstimate(name=s.name, sample=s ))
    estimates17[-1].initCache(cacheDir)

jobs = []

def wrapper(args):
    e, r, c, setup = args
    res = e.cachedEstimate(r, c, setup, save=True, overwrite=options.overwrite)
    return (e.uniqueKey(r, c, setup), res )

print regions

for r in regions:
    for c in [channel(1,0), channel(0,1)]:
        logger.info("Working on 2016 results")
        for e in estimates16:
            jobs.append((e, r, c, setup16))
            #res = e.cachedEstimate(r, channel(-1,-1), setup16, save=True)
            #logger.info("Result: %s", res.val)
        logger.info("Working on 2017 results")
        for e in estimates17:
            jobs.append((e,r,c, setup17))
            #res = e.cachedEstimate(r, channel(-1,-1), setup17, save=True)
            #logger.info("Result: %s", res.val)
            for weight in PS_indices:
                jobs.append((e,r,c, setup17.systematicClone(sys={'reweight':['LHEweight_wgt[%s]/LHEweight_wgt[1080]'%weight]})))
                #res = e.cachedEstimate(r, channel(-1,-1), setup17.systematicClone(sys={'reweight':['LHEweight_wgt[%s]/LHEweight_wgt[1080]'%weight]}), save=True)
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

for r in regions:
    logger.info("Working on 2016 results")
    central = estimates16[0].cachedEstimate(r, channel(-1,-1), setup16)
    print r.cutString()
    print central
    for e in estimates16[1:]:
        res = e.cachedEstimate(r, channel(-1,-1), setup16)
        print (res-central)/central
        #logger.info("Result: %s", res.val)
    logger.info("Working on 2017 results")
    for e in estimates17:
        central = e.cachedEstimate(r, channel(-1,-1), setup17)
        print central
        #logger.info("Result: %s", res.val)
        for weight in PS_indices:
            res = e.cachedEstimate(r, channel(-1,-1), setup17.systematicClone(sys={'reweight':['LHEweight_wgt[%s]/LHEweight_wgt[1080]'%weight]}))
            print (res-central)/central
            #logger.info("Result: %s", res.val)
    
    



logger.info("All done.")

