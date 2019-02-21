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
parser.add_option('--controlRegion',        dest="controlRegion", default = False, action = "store_true", help="Control regions?")
parser.add_option('--regionsXSec',          dest="regionsXSec", default = False, action = "store_true", help="Use nJet and nBTag binning")
(options, args) = parser.parse_args()

# Standard imports
import ROOT
import os
import sys
import pickle
import math

# Analysis
from TopEFT.Analysis.SetupHelpers   import channel, trilepChannels, allTrilepChannels, allQuadlepChannels, quadlepChannels
from TopEFT.Analysis.regions        import regionsE, noRegions, btagRegions, regions4lB, regionsXSec, regionsXSecD
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
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *

from TopEFT.Analysis.Setup          import Setup

year = 2017
setup3l = Setup(year=year, nLeptons=3)
if options.btagWZ:
    setup3l.parameters.update({"nBTags":(0,-1), "nJets":(1,-1)})
elif options.regionsXSec:
    setup3l.parameters.update({"nBTags":(0,-1), "nJets":(1,-1)})

setup4l = Setup(year=year, nLeptons=4)
setup4l.parameters.update({'nJets':(1,-1), 'nBTags':(1,-1), 'zMassRange':20, 'zWindow2':"offZ"})

##Fixed samples
data_directory = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
dirs = {}
dirs['WZTo3LNu_fxfx']   = ['WZTo3LNu_fxfx']
dirs['TZQToLL']         = ['TZQToLL']
dirs['TTZToLLNuNu_amc'] = ['TTZToLLNuNu_amc']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

WZTo3LNu_fxfx_nom   = Sample.fromDirectory(name="WZTo3LNu_fxfx_nom", treeName="Events", isData=False, color=color.TTJets, texName="WZ", directory=directories['WZTo3LNu_fxfx'])
TZQToLL_nom         = Sample.fromDirectory(name="TZQToLL_nom", treeName="Events", isData=False, color=color.TTJets, texName="tZq", directory=directories['TZQToLL'])
TTZToLLNuNu_amc_nom = Sample.fromDirectory(name="TTZToLLNuNu_amc_nom", treeName="Events", isData=False, color=color.TTJets, texName="ttZ", directory=directories['TTZToLLNuNu_amc'])

##FEBug samples
data_directory = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep_FEBug/"
dirs = {}
dirs['WZTo3LNu_fxfx']   = ['WZTo3LNu_fxfx']
dirs['TZQToLL']         = ['TZQToLL']
dirs['TTZToLLNuNu_amc'] = ['TTZToLLNuNu_amc']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

WZTo3LNu_fxfx_FEBug   = Sample.fromDirectory(name="WZTo3LNu_fxfx_FEBug", treeName="Events", isData=False, color=color.TTJets, texName="WZ", directory=directories['WZTo3LNu_fxfx'])
TZQToLL_FEBug         = Sample.fromDirectory(name="TZQToLL_FEBug", treeName="Events", isData=False, color=color.TTJets, texName="tZq", directory=directories['TZQToLL'])
TTZToLLNuNu_amc_FEBug = Sample.fromDirectory(name="TTZToLLNuNu_amc_FEBug", treeName="Events", isData=False, color=color.TTJets, texName="ttZ", directory=directories['TTZToLLNuNu_amc'])

if options.regionsXSec:
    allRegions = noRegions + regionsXSecD
else:
    allRegions = noRegions + regionsE + regions4lB
regions = allRegions if not options.selectRegion else  [allRegions[options.selectRegion]]

#setupIncl = setup.systematicClone(parameters={'mllMin':0, 'nJets':(0,-1), 'nBTags':(0,-1), 'zWindow1':'allZ'})
setupIncl3l = setup3l.systematicClone(parameters={'mllMin':0, 'nJets':(2,-1), 'nBTags':(1,-1), 'zWindow1':'onZ'})
setupIncl4l = setup4l.systematicClone(parameters={'mllMin':0, 'nJets':(1,-1), 'nBTags':(1,-1), 'zWindow1':'onZ'})
setupCR3l = setup3l.systematicClone(parameters={'mllMin':0, 'nJets':(1,-1), 'nBTags':(0,0), 'zWindow1':'onZ'})
setupCR4l = setup4l.systematicClone(parameters={'mllMin':0, 'nJets':(1,-1), 'nBTags':(0,-1), 'zWindow1':'onZ'})
#setup.verbose     = True

# use more inclusive selection in terms of lepton multiplicity in the future?

from TopEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TopEFT.Tools.user import analysis_results

results = {}

cacheDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/FEBug/"

#TZQToLL_nom#WZTo3LNu_fxfx_nom#TTZToLLNuNu_amc_nom
sample_nom = WZTo3LNu_fxfx_nom
#TZQToLL_FEBug#WZTo3LNu_fxfx_FEBug#TTZToLLNuNu_amc_FEBug
sample_FEBug = WZTo3LNu_fxfx_FEBug

estimate_nom = MCBasedEstimate(name=sample_nom.name, sample=sample_nom )
estimate_nom.initCache(cacheDir)

estimate_FEBug = MCBasedEstimate(name=sample_FEBug.name, sample=sample_FEBug )
estimate_FEBug.initCache(cacheDir)


## Results DB for scale and PDF uncertainties

FE_cache = resultsDB(cacheDir+sample_nom.name+'_unc.sq', "PDF", ["region", "channel"])

def wrapper(args):
        e, r, c, setup = args
        res = e.cachedEstimate(r, c, setup, save=True, overwrite=options.overwrite)
        return (e.uniqueKey(r, c, setup), res )

jobs=[]

# remove all so to avoid unnecessary concurrency. All will be calculated as sum of the individual channels later
seperateChannels3l = allTrilepChannels
allTrilepChannelNames = [ c.name for c in allTrilepChannels ]
seperateChannels3l.pop(allTrilepChannelNames.index('all'))

seperateChannels4l = allQuadlepChannels
allQuadlepChannelNames4l = [ c.name for c in allQuadlepChannels ]
seperateChannels4l.pop(allQuadlepChannelNames4l.index('all'))

estimates = [estimate_nom,estimate_FEBug]

for estimate in estimates:
    if not options.skipCentral:
        # First run over seperate channels
        jobs.append((estimate, noRegions[0], channel(-1,-1), setupIncl3l))
        jobs.append((estimate, noRegions[0], channel(-1,-1), setupIncl4l))
        for c in seperateChannels3l:
            jobs.append((estimate, noRegions[0], c, setupIncl3l))
        for c in seperateChannels4l:
            jobs.append((estimate, noRegions[0], c, setupIncl4l))
    
    
    if not options.combine:
        for region in regions:
            seperateChannels = seperateChannels4l if region in regions4lB else seperateChannels3l
            for c in seperateChannels:
            #for region in regions:
                if options.controlRegion:
                    setup = setupCR4l if region in regions4lB else setupCR3l
                else:
                    setup = setup4l if region in regions4lB else setup3l

                jobs.append((estimate, region, c, setup))
        
        logger.info("Created %s jobs",len(jobs))
    
        if options.noMultiThreading: 
            results = map(wrapper, jobs)
        else:
            from multiprocessing import Pool
            pool = Pool(processes=8)
            results = pool.map(wrapper, jobs)
            pool.close()
            pool.join()
    
    logger.info("All done with the estimates.")


if options.combine:
    for c in [channel(-1,-1)]:#allChannels:

        for region in regions:
            if options.controlRegion:
                setup = setupCR4l if region in regions4lB else setupCR3l
            else:
                setup = setup4l if region in regions4lB else setup3l
            logger.info("Region: %s", region)

            res_nom = estimate_nom.cachedEstimate(region, c, setup)
            res_FEBug = estimate_FEBug.cachedEstimate(region, c, setup)

            if res_nom.val>0:
                print (res_nom-res_FEBug)/res_nom
            else:
                print 0

