#!/usr/bin/env python
import ROOT
import os
import argparse
from RootTools.core.Sample import Sample
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',       action='store', default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'],             help="Log level for logging")
argParser.add_argument("--signal",         action='store', default='dipole',          nargs='?', choices=["dipoles", "currents"], help="which signal scan?")
argParser.add_argument("--model",         action='store', default='dim6top_LO',          nargs='?', choices=["dim6top_LO", "ewkDM"], help="which signal model?")
argParser.add_argument("--only",           action='store', default=None,            nargs='?',                                                                                           help="pick only one signal point?")
argParser.add_argument("--scale",          action='store', default=1.0, type=float, nargs='?',                                                                                           help="scaling all yields")
argParser.add_argument("--overwrite",      default = False, action = "store_true", help="Overwrite existing output files")
argParser.add_argument("--popFromSR",      default = False, action = "store", help="Remove one signal region?")
argParser.add_argument("--useXSec",        action='store_true', help="Use the x-sec information?")
argParser.add_argument("--useShape",       action='store_true', help="Use the shape information?")
argParser.add_argument("--statOnly",       action='store_true', help="Use only statistical uncertainty?")
argParser.add_argument("--controlRegion",  action='store', default='', choices = ['', 'nbtag0-njet3p', 'nbtag1p-njet02', 'nbtag1p-njet2', 'nbtag0-njet02', 'nbtag0-njet0p'], help="Use any CRs cut?")
argParser.add_argument("--unblind",        action='store_true', help="Unblind? Currently also correlated with controlRegion option for safety.")
argParser.add_argument("--year",           action='store', default=2016, choices = [ '2016', '2017' ], help='Which year?')

args = argParser.parse_args()


# Logging
import TopEFT.Tools.logger as logger
logger = logger.get_logger(args.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None )

data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_v20/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *

postProcessing_directory = "TopEFT_PP_v20/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

from math                               import sqrt
from copy                               import deepcopy


from TopEFT.Analysis.Setup              import Setup
from TopEFT.Analysis.regions            import regionsA, regionsE, regionsReweight
from TopEFT.Analysis.estimators         import *
from TopEFT.Analysis.DataObservation    import DataObservation
from TopEFT.Analysis.run.SignalReweightingTemplate import *

from TopEFT.Tools.resultsDB             import resultsDB
from TopEFT.Tools.u_float               import u_float
from TopEFT.Tools.user                  import combineReleaseLocation, analysis_results, results_directory, plot_directory
from TopEFT.Tools.cardFileWriter        import cardFileWriter

year = int(args.year)
setup                   = Setup(year)

subDir = ''
baseDir = os.path.join(analysis_results, subDir)

if args.controlRegion:
    subDir = args.controlRegion
    if args.controlRegion == 'nbtag0-njet3p':
        setup = setup.systematicClone(parameters={'nJets':(3,-1), 'nBTags':(0,0)})
    elif args.controlRegion == 'nbtag1p-njet02':
        setup = setup.systematicClone(parameters={'nJets':(0,2), 'nBTags':(1,-1)})
    elif args.controlRegion == 'nbtag1p-njet2':
        setup = setup.systematicClone(parameters={'nJets':(2,2), 'nBTags':(1,-1)})
    elif args.controlRegion == 'nbtag0-njet02':
        setup = setup.systematicClone(parameters={'nJets':(0,2), 'nBTags':(0,0)})
    elif args.controlRegion == 'nbtag0-njet0p':
        setup = setup.systematicClone(parameters={'nJets':(0,-1), 'nBTags':(0,0)})
    else:
        raise NotImplementedError
else:
    subDir = ''

estimators = estimatorList(setup)
setup.estimators        = estimators.constructEstimatorList(["WZ", "TTX", "TTW", "TZQ", "rare", "nonprompt"])
setup.reweightRegions   = regionsReweight
#setup.regions           = regionsE #already defined in Setup

setups = [setup]

cardDir = "regionsE_%s"%(year)
if args.useXSec:
    cardDir += "_xsec"
if args.useShape:
    cardDir += "_shape"
cardDir += "_lowUnc"

limitDir    = os.path.join(baseDir, 'cardFiles', cardDir, subDir, '_'.join([args.model, args.signal]))
overWrite   = (args.only is not None) or args.overwrite

reweightCache = os.path.join( results_directory, 'SignalReweightingTemplate' )


from TopEFT.Generation.Configuration import Configuration
from TopEFT.Generation.Process       import Process
from TopEFT.Tools.u_float         import u_float

config = Configuration( model_name = args.model )

modification_dict = {"process":"ttZ_ll"}

if args.model == "dim6top_LO":
    # This is for the fine scan (should be merged)
    xsecDB = "/afs/hephy.at/data/rschoefbeck02/TopEFT/results/xsec_DBv2.db"
    # This is for the coarse scan
    xsecDB_Backup = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/xsec_DBv2.db"
    if args.signal == "dipoles":
        nonZeroCouplings = ["ctZ","ctZi"]
    elif args.signal == "currents":
        nonZeroCouplings = ["cpQM", "cpt"]
    # for safety, set all couplings to 0.
    modification_dict["ctZ"]    = 0.
    modification_dict["ctZi"]   = 0.
    modification_dict["cpQM"]   = 0.
    modification_dict["cpt"]    = 0.


elif args.model == "ewkDM":
    xsecDB = "/afs/hephy.at/data/rschoefbeck02/TopEFT/results/xsec_DBv2.db"
    # Just in case
    xsecDB_Backup = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/xsec_DBv2.db"
    if args.signal == "dipoles":
        nonZeroCouplings = ["DC2A","DC2V"]
    elif args.signal == "currents":
        nonZeroCouplings = ["DC1A", "DC1V"]
    # for safety, set all couplings to 0.
    modification_dict["DC1A"]   = 0.
    modification_dict["DC1V"]   = 0.
    modification_dict["DC2A"]   = 0.
    modification_dict["DC2V"]   = 0.


logger.info("Using model %s in plane: %s", args.model, args.signal)

logger.info("Will scan the following coupling values: %s and %s", nonZeroCouplings[0], nonZeroCouplings[1])

p = Process(process = "ttZ_ll", nEvents = 5000, config = config, xsec_cache=xsecDB)

xsec_central = p.xsecDB.get(modification_dict)

if year == 2016:
    PDFset = "NNPDF30"
    TTZ_sample = "TTZ_NLO"
elif year == 2017:
    PDFset = "NNPDF30"
    TTZ_sample = "TTZ_NLO_17"
    raise NotImplementedError

PDF_cacheDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/PDF_%s/"%PDFset
PDF_cache   = resultsDB(PDF_cacheDir+TTZ_sample+'_unc.sq', "PDF", ["region", "channel", "PDFset"])
scale_cache = resultsDB(PDF_cacheDir+TTZ_sample+'_unc.sq', "scale", ["region", "channel", "PDFset"])

#print PDF_cache.get({'region':regionsE[0], "channel":

logger.info("Found SM x-sec of %s", xsec_central)

def getCouplingFromName(name, coupling):
    name = name.lower()
    coupling = coupling.lower()
    if coupling in name:
        l = name.split('_')
        return float(l[l.index(coupling)+1].replace('p','.').replace('m','-'))
    else:
        return 0.
    

def wrapper(s):
    
    logger.info("Now working on %s", s.name)
    xSecScale = 1
    c = cardFileWriter.cardFileWriter()
    c.releaseLocation = combineReleaseLocation

    ## Make it less likely that database write access is concurrent
    #if "worker" in os.path.expandvars("$HOSTNAME") or True:
    #    import random
    #    import time
    #    waitTime = random.random()*20
    #    logger.info("Waiting for %s seconds to avoid database problems.", waitTime)
    #    time.sleep(waitTime)

    for coup in nonZeroCouplings:
        try:
            modification_dict[coup] = getCouplingFromName(s.name, coup)
            logger.info("The following coupling is set to non-zero value: %s: %s", coup, modification_dict[coup])
        except ValueError:
            logger.info("The following coupling is kept at zero: %s: %s", coup, modification_dict[coup])
            continue
    try:
        p = Process(process = "ttZ_ll", nEvents = 5000, config = config, xsec_cache=xsecDB)
        xsec = p.xsecDB.get(modification_dict)
    except IndexError:
        logger.info("Looking into backup DB for x-sec")
        p = Process(process = "ttZ_ll", nEvents = 5000, config = config, xsec_cache=xsecDB_Backup)
        xsec = p.xsecDB.get(modification_dict)
    logger.info("Found modified x-sec of %s", xsec)
    
    cardFileName = os.path.join(limitDir, s.name+'.txt')
    if not os.path.exists(cardFileName) or overWrite:
        counter=0
        c.reset()
        c.addUncertainty('PU',          'lnN')
        c.addUncertainty('JEC',         'lnN')
        c.addUncertainty('btag_heavy',  'lnN')
        c.addUncertainty('btag_light',  'lnN')
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
            if args.unblind and args.controlRegion:
                observation = DataObservation(name="Data", sample=setup.samples["Data"], cacheDir=setup.defaultCacheDir())
            else:
                observation = MCBasedEstimate(name="observation", sample=setup.samples["pseudoData"], cacheDir=setup.defaultCacheDir())
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
                        c.specifyExpectation(binname, name, round(expected.val,3) if expected.val > 0 else 0.01)

                        if expected.val>0:
                            if not args.statOnly:
                                c.specifyUncertainty('PU',          binname, name, e.PUSystematic( r, channel, setup).val) #1.01 
                                c.specifyUncertainty('JEC',         binname, name, e.JECSystematic( r, channel, setup).val) #1.03 #1.05
                                c.specifyUncertainty('btag_heavy',  binname, name, e.btaggingSFbSystematic(r, channel, setup).val) #1.03 #1.05 before
                                c.specifyUncertainty('btag_light',  binname, name, e.btaggingSFlSystematic(r, channel, setup).val) #1.03 #1.05 before
                                c.specifyUncertainty('trigger',     binname, name, 1.03) #1.04
                                c.specifyUncertainty('leptonSF',    binname, name, 1.05) #1.07
                                c.specifyUncertainty('scale',       binname, name, 1.01) 
                                c.specifyUncertainty('PDF',         binname, name, 1.01)

                                if name.count('ZZ'):      c.specifyUncertainty('ZZ_xsec',     binname, name, 1.20) #1.20
                                if name.count('WZ'):      c.specifyUncertainty('WZ_xsec',     binname, name, 1.10) #1.20
                                if name.count('nonprompt'):    c.specifyUncertainty('nonprompt',   binname, name, 1.30)
                                if name.count('rare'):    c.specifyUncertainty('rare',        binname, name, 1.50)
                                if name.count('TTX'):     c.specifyUncertainty('ttX',         binname, name, 1.10) #1.15
                                if name.count('TZQ'):     c.specifyUncertainty('tZq',         binname, name, 1.10) #1.15


                            #MC bkg stat (some condition to neglect the smaller ones?)
                            uname = 'Stat_'+binname+'_'+name
                            c.addUncertainty(uname, 'lnN')
                            c.specifyUncertainty(uname, binname, name, round(1+expected.sigma/expected.val,3) )

                    obs = observation.cachedEstimate(r, channel, setup)
                    c.specifyObservation(binname, int(round(obs.val,0)))

                    if args.useShape:
                        logger.info("Using 2D reweighting method for shapes")
                        if args.model == "dim6top_LO":
                            source_gen = dim6top_central
                        elif args.model == "ewkDM":
                            source_gen = ewkDM_central
                        #target_gen = s

                        signalReweighting = SignalReweighting( source_sample = source_gen, target_sample = s, cacheDir = reweightCache)
                        f = signalReweighting.cachedReweightingFunc( setup.genSelection )
                        sig = signal.reweight2D(r, channel, setup, f)
                    else:
                        sig = signal.cachedEstimate(r, channel, setup)

                    xSecMod = 1
                    if args.useXSec:
                        xSecMod = xsec.val/xsec_central.val
                    
                    logger.info("x-sec is multiplied by %s",xSecMod)
                    
                    c.specifyExpectation(binname, 'signal', round(sig.val*xSecScale * xSecMod, 3) )
                    
                    if sig.val>0:
                        if not args.statOnly:
                            c.specifyUncertainty('PU',          binname, "signal", e.PUSystematic( r, channel, setup).val)
                            c.specifyUncertainty('JEC',         binname, "signal", e.JECSystematic( r, channel, setup).val) #1.05
                            c.specifyUncertainty('btag_heavy',  binname, "signal", e.btaggingSFbSystematic(r, channel, setup).val) #1.05
                            c.specifyUncertainty('btag_light',  binname, "signal", e.btaggingSFlSystematic(r, channel, setup).val) #1.05
                            c.specifyUncertainty('trigger',     binname, "signal", 1.03) #1.04
                            c.specifyUncertainty('leptonSF',    binname, "signal", 1.05) #1.07
                            # This doesn't get the right uncertainty in CRs. However, signal doesn't matter there anyway.
                            c.specifyUncertainty('scale_sig',   binname, "signal", round(scale_cache.get({"region":r, "channel":channel, "PDFset":None}).val,3) + 1)
                            c.specifyUncertainty('PDF',         binname, "signal", round(PDF_cache.get({"region":r, "channel":channel, "PDFset":PDFset}).val,3) + 1)
                            #c.specifyUncertainty('scale_sig',   binname, "signal", 1.10) #1.30
                            #c.specifyUncertainty('PDF',         binname, "signal", 1.05) #1.15

                        uname = 'Stat_'+binname+'_signal'
                        c.addUncertainty(uname, 'lnN')
                        c.specifyUncertainty(uname, binname, 'signal', round(1 + sig.sigma/sig.val,3) )
                    else:
                        uname = 'Stat_'+binname+'_signal'
                        c.addUncertainty(uname, 'lnN')
                        c.specifyUncertainty(uname, binname, 'signal', 1 )

                    
        c.addUncertainty('Lumi', 'lnN')
        c.specifyFlatUncertainty('Lumi', 1.026)
        cardFileName = c.writeToFile(cardFileName)
    else:
        logger.info("File %s found. Reusing.",cardFileName)
    
    res = {}
    
    resDB = resultsDB(limitDir+'/results.sq', "results", setup.resultsColumns)
    res = {"signal":s.name}
    if not overWrite and res.DB.contains(key):
        res = resDB.getDicts(key)[0]
        logger.info("Found result for %s, reusing", s.name)
    else:
        # calculate the limit
        #limit = c.calcLimit(cardFileName)#, options="--run blind")
        res.update({"exp":0, "obs":0, "exp1up":0, "exp2up":0, "exp1down":0, "exp2down":0})
        c.calcNuisances(cardFileName)
        # extract the NLL
        nll = c.calcNLL(cardFileName, options="--fastScan")
        if nll["nll0"] > 0:
            res.update({"dNLL_postfit_r1":nll["nll"], "dNLL_bestfit":nll["bestfit"], "NLL_prefit":nll["nll0"]})
        else:
            res.update({"dNLL_postfit_r1":-999, "dNLL_bestfit":-999, "NLL_prefit":-999})
            logger.info("Fits failed, adding values -999 as results")
        logger.info("Adding results to database")
        resDB.add(res, nll['nll_abs'], overwrite=True)

    print
    print "NLL results:"
    print "{:>15}{:>15}{:>15}".format("Pre-fit", "Post-fit r=1", "Best fit")
    print "{:15.2f}{:15.2f}{:15.2f}".format(float(res["NLL_prefit"]), float(res["NLL_prefit"])+float(res["dNLL_postfit_r1"]), float(res["NLL_prefit"])+float(res["dNLL_bestfit"]))
    
    #if res: 
    #    try:
    #        print "Result: %r obs %5.3f exp %5.3f -1sigma %5.3f +1sigma %5.3f"%(s.name, res['-1.000'], res['0.500'], res['0.160'], res['0.840'])
    #        return sConfig, res
    #    except:
    #        print "Problem with limit: %r" + str(res)
    #        return None


from TopEFT.samples.gen_fwlite_benchmarks import *
#jobs = allSamples_dim6top
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
        print jobNames[145]
        print len(jobs)
        #try:
        wrapper(jobs[jobNames.index(args.only)])
        #except ValueError:
        #    logger.info("Couldn't find sample %s", args.only)
    exit(0)

results = map(wrapper, jobs)
results = [r for r in results if r]

