#!/usr/bin/env python
import ROOT
import os
import argparse
from RootTools.core.Sample import Sample
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',       action='store', default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'],             help="Log level for logging")
argParser.add_argument("--signal",         action='store', default='ewkDM',          nargs='?', choices=["ewkDM"], help="which signal?")
argParser.add_argument("--only",           action='store', default=None,            nargs='?',                                                                                           help="pick only one masspoint?")
argParser.add_argument("--scale",          action='store', default=1.0, type=float, nargs='?',                                                                                           help="scaling all yields")
argParser.add_argument("--overwrite",      default = False, action = "store_true", help="Overwrite existing output files")
argParser.add_argument("--popFromSR",      default = False, action = "store", help="Remove one signal region?")
argParser.add_argument("--extension",      default = '', action = "store", help="Extension to dir name?")

args = argParser.parse_args()


# Logging
import TopEFT.Tools.logger as logger
logger = logger.get_logger(args.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None )

from TopEFT.Analysis.Setup              import Setup
from TopEFT.Analysis.regions            import regionsA, regionsE, regionsReweight
from TopEFT.Analysis.estimators         import *
from TopEFT.Tools.resultsDB             import resultsDB
from TopEFT.Analysis.run.getEstimates   import getEstimate
from TopEFT.Tools.u_float               import u_float
from math                               import sqrt
from copy                               import deepcopy

setup                   = Setup()
#setup.channels          = ['all'] #already defined in Setup
setup.estimators        = constructEstimatorList(["WZ", "TTX", "TTW", "TZQ", "rare", "nonprompt"])
setup.reweightRegions   = regionsReweight
#setup.regions           = regionsE #already defined in Setup

# Define fake samples (yields from illia)
data_directory = '/afs/hephy.at/data/rschoefbeck01/cmgTuples/'
postProcessing_directory = "TopEFT_PP_v14/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

setups = [setup]

##https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSYSignalSystematicsRun2
from TopEFT.Tools.user           import combineReleaseLocation, analysis_results, results_directory, plot_directory
from TopEFT.Tools.cardFileWriter import cardFileWriter
from TopEFT.Analysis.run.getResults  import getResult, addResult

from TopEFT.Analysis.run.SignalReweightingTemplate import *

subDir = ''
baseDir = os.path.join(analysis_results, subDir)

limitDir    = os.path.join(baseDir, 'cardFiles', setup.name, args.signal + args.extension)
overWrite   = (args.only is not None) or args.overwrite

reweightCache = os.path.join( results_directory, 'SignalReweightingTemplate' )

def wrapper(s):
    
    logger.info("Now working on %s", s.name)
    xSecScale = 1
    c = cardFileWriter.cardFileWriter()
    c.releaseLocation = combineReleaseLocation

    cardFileName = os.path.join(limitDir, s.name+'.txt')
    if not os.path.exists(cardFileName) or overWrite:
        counter=0
        c.reset()
        c.addUncertainty('PU',          'lnN')
        c.addUncertainty('JEC',         'lnN')
        c.addUncertainty('btag',        'lnN')
        c.addUncertainty('trigger',     'lnN')
        c.addUncertainty('leptonSF',    'lnN')
        c.addUncertainty('scale',       'lnN')
        c.addUncertainty('scale_sig',   'lnN')
        c.addUncertainty('PDF',         'lnN')
        c.addUncertainty('nonprompt',   'lnN')
        c.addUncertainty('WZ_xsec',     'lnN')
        c.addUncertainty('ZZ_xsec',     'lnN')
        c.addUncertainty('rare',        'lnN')
        c.addUncertainty('ttX',         'lnN')
        c.addUncertainty('tZq',         'lnN')


        for setup in setups:
            signal      = MCBasedEstimate(name="TTZ", sample=setup.samples["TTZ"], cacheDir=setup.defaultCacheDir())
            observation = MCBasedEstimate(name="observation", sample=setup.samples["pseudoData"], cacheDir=setup.defaultCacheDir())
            #observation = DataObservation(name='Data', sample=setup.sample['pseudoData'], cacheDir=setup.defaultCacheDir())
            for e in setup.estimators: e.initCache(setup.defaultCacheDir())

            for r in setup.regions:
                for channel in setup.channels:
                    niceName = ' '.join([channel, r.__str__()])
                    binname = 'Bin'+str(counter)
                    counter += 1
                    c.addBin(binname, [e.name.split('-')[0] for e in setup.estimators], niceName)

                    for e in setup.estimators:
                        name = e.name.split('-')[0]
                        expected = e.cachedEstimate(r, channel, setup)
                        c.specifyExpectation(binname, name, expected.val)

                        if expected.val>0:
                            c.specifyUncertainty('PU',          binname, name, 1.01)
                            c.specifyUncertainty('JEC',         binname, name, 1.05)
                            c.specifyUncertainty('btag',        binname, name, 1.05)
                            c.specifyUncertainty('trigger',     binname, name, 1.04)
                            c.specifyUncertainty('leptonSF',    binname, name, 1.07)
                            c.specifyUncertainty('scale',       binname, name, 1.01)
                            c.specifyUncertainty('PDF',         binname, name, 1.01)

                            if name.count('ZZ'):      c.specifyUncertainty('ZZ_xsec',     binname, name, 1.20)
                            if name.count('WZ'):      c.specifyUncertainty('WZ_xsec',     binname, name, 1.20)
                            if name.count('nonprompt'):    c.specifyUncertainty('nonprompt',   binname, name, 1.30)
                            if name.count('rare'):    c.specifyUncertainty('rare',        binname, name, 1.50)
                            if name.count('TTX'):     c.specifyUncertainty('ttX',         binname, name, 1.15)
                            if name.count('TZQ'):     c.specifyUncertainty('tZq',         binname, name, 1.15)


                            #MC bkg stat (some condition to neglect the smaller ones?)
                            uname = 'Stat_'+binname+'_'+name
                            c.addUncertainty(uname, 'lnN')
                            c.specifyUncertainty(uname, binname, name, 1+expected.sigma/expected.val )

                    obs = observation.cachedEstimate(r, channel, setup)
                    c.specifyObservation(binname, int(round(obs.val,0)))

                    source_gen = dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p00
                    target_gen = s

                    signalReweighting = SignalReweighting( source_sample = source_gen, target_sample = s, cacheDir = reweightCache)
                    f = signalReweighting.cachedReweightingFunc( setup.genSelection )
                    
                    sig = signal.reweight2D(r, channel, setup, f)
                    c.specifyExpectation(binname, 'signal', sig.val*xSecScale )
                    
                    if sig.val>0:
                        c.specifyUncertainty('PU',          binname, "signal", 1.01)
                        c.specifyUncertainty('JEC',         binname, "signal", 1.05)
                        c.specifyUncertainty('btag',        binname, "signal", 1.05)
                        c.specifyUncertainty('trigger',     binname, "signal", 1.04)
                        c.specifyUncertainty('leptonSF',    binname, "signal", 1.07)
                        c.specifyUncertainty('scale_sig',   binname, "signal", 1.30)
                        c.specifyUncertainty('PDF',         binname, "signal", 1.15)

                        uname = 'Stat_'+binname+'_signal'
                        c.addUncertainty(uname, 'lnN')
                        c.specifyUncertainty(uname, binname, 'signal', 1 + sig.sigma/sig.val )
                    else:
                        uname = 'Stat_'+binname+'_signal'
                        c.addUncertainty(uname, 'lnN')
                        c.specifyUncertainty(uname, binname, 'signal', 1 )

                    
        c.addUncertainty('Lumi', 'lnN')
        c.specifyFlatUncertainty('Lumi', 1.026)
        cardFileName = c.writeToFile(cardFileName)
    else:
        print "File %s found. Reusing."%cardFileName
    
    res = {}
    
    if getResult(s) and not overWrite:
        res = getResult(s)
        print "Found result for %s, reusing"%s.name
    else:
        # calculate the limit
        limit = c.calcLimit(cardFileName)#, options="--run blind")
        res.update({"exp":limit['0.500'], "obs":limit['-1.000'], "exp1up":limit['0.840'], "exp2up":limit['0.975'], "exp1down":limit['0.160'], "exp2down":limit['0.025']})
        # run the checks
        c.calcNuisances(cardFileName)
        # extract the NLL
        nll = c.calcNLL(cardFileName)
        res.update({"dNLL_postfit_r1":nll["nll"], "dNLL_bestfit":nll["bestfit"], "NLL_prefit":nll["nll0"]})
        addResult(s, res, nll['nll_abs'], overwrite=True)
        
    print "NLL results:"
    print "{:>15}{:>15}{:>15}".format("Pre-fit", "Post-fit r=1", "Best fit")
    print "{:15.2f}{:15.2f}{:15.2f}".format(float(res["NLL_prefit"]), float(res["NLL_prefit"])+float(res["dNLL_postfit_r1"]), float(res["NLL_prefit"])+float(res["dNLL_bestfit"]))
    
    if xSecScale != 1:
        for k in res:
            res[k] *= xSecScale
    
    #if res: 
    #    try:
    #        print "Result: %r obs %5.3f exp %5.3f -1sigma %5.3f +1sigma %5.3f"%(s.name, res['-1.000'], res['0.500'], res['0.160'], res['0.840'])
    #        return sConfig, res
    #    except:
    #        print "Problem with limit: %r" + str(res)
    #        return None


from TopEFT.samples.gen_fwlite_benchmarks import *
jobs = allSamples_dim6top

allJobs = [j.name for j in jobs]
#print "I have imported these signals:"
#for n in allJobs:
#    print n

if args.only is not None:
    wrapper(jobs[int(args.only)])
    exit(0)

results = map(wrapper, jobs)
results = [r for r in results if r]

