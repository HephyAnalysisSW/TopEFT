#!/usr/bin/env python
'''
Combination on card file level
'''

import ROOT
import os
import argparse
from RootTools.core.Sample import Sample
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',       action='store',      default='INFO',         nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'],             help="Log level for logging")
argParser.add_argument("--signal",         action='store',      default='dipoles',       nargs='?', choices=["dipoles", "currents"], help="which signal scan?")
argParser.add_argument("--model",          action='store',      default='dim6top_LO',   nargs='?', choices=["dim6top_LO", "ewkDM"], help="which signal model?")
argParser.add_argument("--only",           action='store',      default=None,           nargs='?',                                                                                           help="pick only one signal point?")
argParser.add_argument("--useXSec",        action='store_true', help="Use the x-sec information?")
argParser.add_argument("--useShape",       action='store_true', help="Use the shape information?")
argParser.add_argument("--includeCR",      action='store_true', help="Do simultaneous SR and CR fit")
argParser.add_argument("--calcNuisances",  action='store_true', help="Extract the nuisances and store them in text files?")


args = argParser.parse_args()

## 2016
data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_2016_mva_v16/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *
postProcessing_directory = "TopEFT_PP_2016_mva_v16/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

## 2017
data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_2017_mva_v14/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v14/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *


# Logging
import TopEFT.Tools.logger as logger
logger = logger.get_logger(args.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None )

from math                               import sqrt
from copy                               import deepcopy


from TopEFT.Analysis.Setup              import Setup
from TopEFT.Analysis.SetupHelpers       import channel
from TopEFT.Analysis.regions            import regionsA, regionsE, regionsReweight, regionsReweight4l, regions4l, regions4lB
from TopEFT.Analysis.estimators         import *
from TopEFT.Analysis.DataObservation    import DataObservation
from TopEFT.Analysis.FakeEstimate       import FakeEstimate
from TopEFT.Analysis.run.SignalReweightingTemplate import *

from TopEFT.Tools.resultsDB             import resultsDB
from TopEFT.Tools.u_float               import u_float
from TopEFT.Tools.user                  import combineReleaseLocation, analysis_results, results_directory, plot_directory
from TopEFT.Tools.cardFileWriter        import cardFileWriter

# some fake setup
setup = Setup(2016, nLeptons=3)


def wrapper(s):

    logger.info("Now working on %s", s.name)

    c = cardFileWriter.cardFileWriter()
    c.releaseLocation = combineReleaseLocation
    cards = {}
    
    # get the seperated cards
    for year in [2016,2017]:
        
        subDir = ''
        cardDir = "regionsE_%s"%(year)
        if args.useXSec: cardDir += "_xsec"
        if args.useShape: cardDir += "_shape"
        cardDir += "_lowUnc"
        if args.includeCR: cardDir += "_SRandCR"

        baseDir = os.path.join(analysis_results)
        limitDir    = os.path.join(baseDir, 'cardFiles', cardDir, subDir, '_'.join([args.model, args.signal]))
        #resDB = resultsDB(limitDir+'/results.sq', "results", setup.resultsColumns)
        
        cardFileName = os.path.join(limitDir, s.name+'.txt')

        if not os.path.isfile(cardFileName):
            raise IOError("File %s doesn't exist!"%cardFileName)

        cards[year] = cardFileName
    
    limitDir = limitDir.replace('2017','COMBINED')
    
    # run combine and store results in sqlite database
    if not os.path.isdir(limitDir):
        os.makedirs(limitDir)
    resDB = resultsDB(limitDir+'/results.sq', "results", setup.resultsColumns)
    res = {"signal":s.name}

    overWrite = True

    if not overWrite and res.DB.contains(key):
        res = resDB.getDicts(key)[0]
        logger.info("Found result for %s, reusing", s.name)

    else:
        signalRegions = range(15,30)
        masks_2016 = ['mask_dc_2016_Bin'+str(i)+'=1' for i in signalRegions]
        masks_2017 = ['mask_dc_2017_Bin'+str(i)+'=1' for i in signalRegions]
    
        masks = ','.join(masks_2016+masks_2017)
        
        combinedCard = c.combineCards( cards )
        
        # We don't calculate limits here, but just in case we find a way how to do it, put placeholders here
        res.update({"exp":0, "obs":0, "exp1up":0, "exp2up":0, "exp1down":0, "exp2down":0})
        # Don't extract all the nuisances by default

        if args.calcNuisances:
            c.calcNuisances(combinedCard, masks=masks)

        nll = c.physicsModel(combinedCard, options="", normList=["WZ_norm","ZZ_norm"], masks=masks) # fastScan turns of profiling

        if nll["nll0"] > 0:
            res.update({"dNLL_postfit_r1":nll["nll"], "dNLL_bestfit":nll["bestfit"], "NLL_prefit":nll["nll0"]})
        else:
            res.update({"dNLL_postfit_r1":-999, "dNLL_bestfit":-999, "NLL_prefit":-999})
            logger.info("Fits failed, adding values -999 as results")
        logger.info("Adding results to database")
        resDB.add(res, nll['nll_abs'], overwrite=True)


    logger.info("Results stored in %s", limitDir)

#cardDir = "combination"
#if args.useXSec:
#    cardDir += "_xsec"
#if args.useShape:
#    cardDir += "_shape"
#
#baseDir = os.path.join(analysis_results)
#limitDir    = os.path.join(baseDir, 'cardFiles', cardDir, subDir, '_'.join([args.model, args.signal]))
#resDB = resultsDB(limitDir+'/results.sq', "results", setup.resultsColumns)



from TopEFT.samples.gen_fwlite_benchmarks import *
if args.model == "dim6top_LO":
    if args.signal == "dipoles":
        jobs = [dim6top_central] + dim6top_dipoles
    elif args.signal == "currents":
        jobs = [dim6top_central] + dim6top_currents
elif args.model == "ewkDM":
    if args.signal == "dipoles":
        jobs = [ewkDM_central] + ewkDM_dipoles
    elif args.signal == "currents":
        jobs = [ewkDM_central] + ewkDM_currents

allJobs = [j.name for j in jobs]

if args.only is not None:
    if args.only.isdigit():
        wrapper(jobs[int(args.only)])
    else:
        jobNames = [ x.name for x in jobs ]
        wrapper(jobs[jobNames.index(args.only)])
    exit(0)


