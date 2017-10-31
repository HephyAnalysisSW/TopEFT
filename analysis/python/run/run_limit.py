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
import TopEFT.tools.logger as logger
logger = logger.get_logger(args.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None )

from TopEFT.analysis.Setup              import Setup
from TopEFT.analysis.regions            import regionsA
from TopEFT.tools.resultsDB             import resultsDB
from TopEFT.analysis.getEstimates       import getEstimate
from TopEFT.tools.u_float               import u_float
from math                               import sqrt
from copy                               import deepcopy

setup = Setup()
setup.channels  = ['all']
setup.regions   = regionsA

# Define fake samples (yields from illia)
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
processes = [ WZ, TTX, TTW, TZQ, rare, nonprompt ]

setups = [setup]

##https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSYSignalSystematicsRun2
from TopEFT.tools.user           import combineReleaseLocation, analysis_results, results_directory, plot_directory
from TopEFT.tools.cardFileWriter import cardFileWriter
from TopEFT.analysis.getResults  import getResult, addResult


subDir = ''
baseDir = os.path.join(analysis_results, subDir)

limitDir    = os.path.join(baseDir, 'cardFiles', args.signal + args.extension)
overWrite   = (args.only is not None) or args.overwrite

def wrapper(s):
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
            for r in setup.regions:
                for channel in setup.channels:
                    niceName = ' '.join([channel, r.__str__()])
                    binname = 'Bin'+str(counter)
                    counter += 1
                    c.addBin(binname, [p.name for p in processes], niceName)

                    for p in processes:
                        name = p.name
                        expected = getEstimate(p, r, channel)#{"process":nam, "region":r, "lumi":35.9, "presel":"nLep==3&&isTTZ&&nJetGodd>2&&nBTag>0", "weightString":"weight", "channel":channel})
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

                    c.specifyObservation(binname, int(round((getEstimate(pseudoDataPriv, r, channel).val))))

                    #signalSetup = setup.sysClone()
                    signal = getEstimate(s, r, channel)#resultsCache.get({"process":s.name, "region":r, "lumi":35.9, "presel":"nLep==3&&isTTZ&&nJetGodd>2&&nBTag>0", "weightString":"weight", "channel":channel})
                    c.specifyExpectation(binname, 'signal', signal.val*xSecScale )
                    
                    if signal.val>0:
                        c.specifyUncertainty('PU',          binname, "signal", 1.01)
                        c.specifyUncertainty('JEC',         binname, "signal", 1.05)
                        c.specifyUncertainty('btag',        binname, "signal", 1.05)
                        c.specifyUncertainty('trigger',     binname, "signal", 1.04)
                        c.specifyUncertainty('leptonSF',    binname, "signal", 1.07)
                        c.specifyUncertainty('scale_sig',   binname, "signal", 1.30)
                        c.specifyUncertainty('PDF',         binname, "signal", 1.15)

                        uname = 'Stat_'+binname+'_signal'
                        c.addUncertainty(uname, 'lnN')
                        c.specifyUncertainty(uname, binname, 'signal', 1 + signal.sigma/signal.val )
                    else:
                        uname = 'Stat_'+binname+'_signal'
                        c.addUncertainty(uname, 'lnN')
                        c.specifyUncertainty(uname, binname, 'signal', 1 )

                    ## alternative signal model
                    #signal_ALT = getEstimate(s, r, channel)
                    #c.specifyExpectation(binname, 'signal_ALT', signal_ALT.val*xSecScale )
                    #
                    #if signal_ALT.val>0:
                    #    c.specifyUncertainty('PU',          binname, "signal_ALT", 1.01)
                    #    c.specifyUncertainty('JEC',         binname, "signal_ALT", 1.05)
                    #    c.specifyUncertainty('btag',        binname, "signal_ALT", 1.05)
                    #    c.specifyUncertainty('trigger',     binname, "signal_ALT", 1.04)
                    #    c.specifyUncertainty('leptonSF',    binname, "signal_ALT", 1.07)
                    #    c.specifyUncertainty('scale_sig',   binname, "signal_ALT", 1.30)
                    #    c.specifyUncertainty('PDF',         binname, "signal_ALT", 1.15)

                    #    uname = 'Stat_'+binname+'_signal_ALT'
                    #    c.addUncertainty(uname, 'lnN')
                    #    c.specifyUncertainty(uname, binname, 'signal_ALT', 1 + signal_ALT.sigma/signal_ALT.val )
                    #else:
                    #    uname = 'Stat_'+binname+'_signal_ALT'
                    #    c.addUncertainty(uname, 'lnN')
                    #    c.specifyUncertainty(uname, binname, 'signal_ALT', 1 )

                    
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

from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import allSignals

jobs = allSignals
jobs.append(TTZtoLLNuNu)

allJobs = [j.name for j in jobs]
#print "I have imported these signals:"
#for n in allJobs:
#    print n

if args.only is not None:
    wrapper(jobs[int(args.only)])
    exit(0)

results = map(wrapper, jobs)
results = [r for r in results if r]

