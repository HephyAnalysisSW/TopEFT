#!/usr/bin/env python
import ROOT
import os
import argparse
from RootTools.core.Sample import Sample
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',       action='store',      default='INFO',         nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'],             help="Log level for logging")
argParser.add_argument("--signal",         action='store',      default='dipoles',       nargs='?', choices=["dipoles", "currents"], help="which signal scan?")
argParser.add_argument("--model",          action='store',      default='dim6top_LO',   nargs='?', choices=["dim6top_LO", "ewkDM"], help="which signal model?")
argParser.add_argument("--only",           action='store',      default=None,           nargs='?',                                                                                           help="pick only one signal point?")
argParser.add_argument("--scale",          action='store',      default=1.0,            type=float,nargs='?',                                                                                help="scaling all yields")
argParser.add_argument("--overwrite",      action='store_true', default = False,        help="Overwrite existing output files")
argParser.add_argument("--useXSec",        action='store_true', help="Use the x-sec information?")
argParser.add_argument("--useShape",       action='store_true', help="Use the shape information?")
argParser.add_argument("--statOnly",       action='store_true', help="Use only statistical uncertainty?")
argParser.add_argument("--controlRegion",  action='store',      default='', choices = ['', 'nbtag0-njet3p', 'nbtag1p-njet02', 'nbtag1p-njet2', 'nbtag0-njet02', 'nbtag0-njet0p', 'nbtag0-njet1p', 'nbtag0-njet2p'], help="Use any CRs cut?")
argParser.add_argument("--includeCR",      action='store_true', help="Do simultaneous SR and CR fit")
argParser.add_argument("--calcNuisances",  action='store_true', help="Extract the nuisances and store them in text files?")
argParser.add_argument("--unblind",        action='store_true', help="Unblind? Currently also correlated with controlRegion option for safety.")
argParser.add_argument("--include4l",      action='store_true', help="Include 4l regions?")
argParser.add_argument("--year",           action='store',      type=int, default=2016, choices = [ 2016, 2017, 20167 ], help='Which year?')


args = argParser.parse_args()


# Logging
import TopEFT.Tools.logger as logger
logger = logger.get_logger(args.logLevel, logFile = None )
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None )

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

year = int(args.year)

cardDir = "regionsE_%s"%(year)
if args.useXSec:
    cardDir += "_xsec"
if args.useShape:
    cardDir += "_shape"
cardDir += "_lowUnc"

## 2l setup ##
# not yet part of the game

## 3l setup ##
setup3l                 = Setup(year, nLeptons=3)
estimators3l            = estimatorList(setup3l)
setup3l.estimators      = estimators3l.constructEstimatorList(["WZ", "TTX", "TTW", "ZG", "rare", "ZZ"])#, "nonprompt"])
setup3l.reweightRegions = regionsReweight
setup3l.channels        = [channel(-1,-1)] # == 'all'
setup3l.regions         = regionsE
setup3l.year            = year

## 3l NP setup ##
setup3l_NP              = Setup(year, nLeptons=3, nonprompt=True)
setup3l_NP.channels     = [channel(-1,-1)] # == 'all'
setup3l_NP.regions      = regionsE

## 4l setup ##
setup4l                 = Setup(year=year, nLeptons=4)
setup4l.parameters.update({'nJets':(1,-1), 'nBTags':(1,-1), 'zMassRange':20, 'zWindow2':"offZ"})
estimators4l            = estimatorList(setup4l)
setup4l.estimators      = estimators4l.constructEstimatorList(["ZZ", "rare","TTX"])
setup4l.reweightRegions = regionsReweight4l
setup4l.channels        = [channel(-1,-1)] # == 'all'
setup4l.regions         = regions4lB
setup4l.year            = year

## CR setups ##
setup3l_CR              = setup3l.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,0)})
setup3l_NP_CR           = setup3l_NP.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,0)})
setup4l_CR              = setup4l.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,-1), 'zWindow2':"onZ"})

## define list of setups ##
setups = []
if args.includeCR:
    setups += [\
        (setup3l_CR, setup3l_NP_CR),
        (setup4l_CR, 0)
            ]
    cardDir += "_SRandCR"

setups += [\
    (setup3l, setup3l_NP),
    (setup4l, 0)
        ]


subDir = ''
baseDir = os.path.join(analysis_results, subDir)

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
elif year == 20167:
    PDFset = "NNPDF30"
    TTZ_sample = "TTZ_NLO"
    logger.info("Will use PDF and scale uncertainties based on 2016.")

# always use PDF4LHC set for now, only included in Fall17
TTZ_sample = "TTZ_NLO_17"
PDFset = "PDF4LHC15_nlo_100"

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
        c.addUncertainty('PartonShower','lnN')
        c.addUncertainty('nonprompt',   'lnN')
        c.addUncertainty('WZ_xsec',     'lnN')
        c.addUncertainty('WZ_bb',       'lnN')
        c.addUncertainty('ZZ_xsec',     'lnN')
        c.addUncertainty('rare',        'lnN')
        c.addUncertainty('ttX',         'lnN')
        #c.addUncertainty('tZq',         'lnN')

        c.addRateParameter('WZ', 1, '[0,2]')
        c.addRateParameter('ZZ', 1, '[0,2]')
        # others as well?

        for setupPair in setups:
            
            # extract the nominal and nonprompt setup from the pair
            setup, setupNP = setupPair
            
            signal      = MCBasedEstimate(name="TTZ", sample=setup.samples["TTZ"], cacheDir=setup.defaultCacheDir())
            #nonprompt   = FakeEstimate(name="nonPromptDD", sample=setup.samples["Data"], setup=setupNP, cacheDir=setup.defaultCacheDir())
            if args.unblind or (setup == setup3l_CR) or (setup == setup4l_CR):
                observation = DataObservation(name="Data", sample=setup.samples["Data"], cacheDir=setup.defaultCacheDir())
                logger.info("Using data!")
                print setup.year
            else:
                observation = MCBasedEstimate(name="observation", sample=setup.samples["pseudoData"], cacheDir=setup.defaultCacheDir())
                logger.info("Using pseudo-data!")
                print setup.year
            for e in setup.estimators: e.initCache(setup.defaultCacheDir())

            for r in setup.regions:
                for channel in setup.channels:
                    niceName = ' '.join([channel.name, r.__str__()])
                    binname = 'Bin'+str(counter)
                    counter += 1
                    c.addBin(binname, [e.name.split('-')[0] for e in setup.estimators]+["nonPromptDD"], niceName)
                    #c.addBin(binname, 'nonPromptDD', niceName)

                    for e in setup.estimators:
                        name = e.name.split('-')[0]
                        expected = e.cachedEstimate(r, channel, setup)
                        c.specifyExpectation(binname, name, round(expected.val,3) if expected.val > 0 else 0.01)

                        if not args.statOnly:
                            c.specifyUncertainty('PU',          binname, name, 1+round(e.PUSystematic( r, channel, setup).val,3)) #1.01 
                            if not name.count('nonprompt'):
                                c.specifyUncertainty('JEC',         binname, name, 1+round(e.JECSystematic( r, channel, setup).val,3)) #1.03 #1.05
                                c.specifyUncertainty('btag_heavy',  binname, name, 1+round(e.btaggingSFbSystematic(r, channel, setup).val,3)) #1.03 #1.05 before
                                c.specifyUncertainty('btag_light',  binname, name, 1+round(e.btaggingSFlSystematic(r, channel, setup).val,3)) #1.03 #1.05 before
                                c.specifyUncertainty('trigger',     binname, name, 1+round(e.triggerSystematic(r, channel, setup).val,3))
                                c.specifyUncertainty('leptonSF',    binname, name, 1+round(e.leptonSFSystematic(r, channel, setup).val,3))
                                c.specifyUncertainty('scale',       binname, name, 1.01) 
                                c.specifyUncertainty('PDF',         binname, name, 1.01)

                            if name.count('ZZ'):      c.specifyUncertainty('ZZ_xsec',     binname, name, 1.20) #1.20
                            if name.count('WZ'):
                                c.specifyUncertainty('WZ_xsec',     binname, name, 1.10)
                                if setup == setup3l:
                                    c.specifyUncertainty('WZ_bb',     binname, name, 1.08)
                            
                            if name.count('nonprompt'):    c.specifyUncertainty('nonprompt',   binname, name, 1.30)
                            if name.count('rare'):    c.specifyUncertainty('rare',        binname, name, 1.50)
                            if name.count('TTX'):     c.specifyUncertainty('ttX',         binname, name, 1.10) #1.15
                            #if name.count('TZQ'):     c.specifyUncertainty('tZq',         binname, name, 1.10) #1.15


                        #MC bkg stat (some condition to neglect the smaller ones?)
                        uname = 'Stat_'+binname+'_'+name
                        c.addUncertainty(uname, 'lnN')
                        if expected.val > 0:
                            c.specifyUncertainty(uname, binname, name, round(1+expected.sigma/expected.val,3) )
                        else:
                            c.specifyUncertainty(uname, binname, name, 1.01 )
                    
                    c.addUncertainty('Stat_'+binname+'_nonprompt', 'lnN')
                    #if setup.nLeptons == 3:
                    #    np = nonprompt.cachedEstimate(r, channel, setupNP)
                    #    c.specifyUncertainty('Stat_'+binname+'_nonprompt',   binname, "nonPromptDD", round(1+np.sigma/np.val,3))
                    #else:
                    #    np = u_float(0.)
                    #    c.specifyUncertainty('Stat_'+binname+'_nonprompt',   binname, "nonPromptDD", 1.01)
                    
                    # only get NP for 3l channel
                    
                    if setup.nLeptons == 3 and setupNP:
                        nonprompt   = FakeEstimate(name="nonPromptDD", sample=setup.samples["Data"], setup=setupNP, cacheDir=setup.defaultCacheDir())
                        np = nonprompt.cachedEstimate(r, channel, setupNP)
                        if np.val < 0.01:
                            np = u_float(0.01,0.)
                        c.specifyExpectation(binname, 'nonPromptDD', round(np.val,3)) 
                        c.specifyUncertainty('Stat_'+binname+'_nonprompt',   binname, "nonPromptDD", round(1+np.sigma/np.val,3))
                        c.specifyUncertainty('nonprompt',   binname, "nonPromptDD", 1.30)
                    else:
                        c.specifyExpectation(binname, 'nonPromptDD', 0.)
                    
                    if args.unblind or (setup == setup3l_CR) or (setup == setup4l_CR):
                        obs = observation.cachedObservation(r, channel, setup)
                    else:
                        obs = observation.cachedEstimate(r, channel, setup)
                    c.specifyObservation(binname, int(round(obs.val,0)))

                    if args.useShape:
                        logger.info("Using 2D reweighting method for shapes")
                        if args.model == "dim6top_LO":
                            source_gen = dim6top_central
                        elif args.model == "ewkDM":
                            source_gen = ewkDM_central

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
                            c.specifyUncertainty('PU',          binname, "signal", 1+round(e.PUSystematic( r, channel, setup).val,3))
                            c.specifyUncertainty('JEC',         binname, "signal", 1+round(e.JECSystematic( r, channel, setup).val,3)) #1.05
                            c.specifyUncertainty('btag_heavy',  binname, "signal", 1+round(e.btaggingSFbSystematic(r, channel, setup).val,3)) #1.05
                            c.specifyUncertainty('btag_light',  binname, "signal", 1+round(e.btaggingSFlSystematic(r, channel, setup).val,3)) #1.05
                            c.specifyUncertainty('trigger',     binname, "signal", 1+round(e.triggerSystematic(r, channel, setup).val,3))
                            c.specifyUncertainty('leptonSF',    binname, "signal", 1+round(e.leptonSFSystematic(r, channel, setup).val,3))
                            # This doesn't get the right uncertainty in CRs. However, signal doesn't matter there anyway.
                            #c.specifyUncertainty('scale_sig',   binname, "signal", round(scale_cache.get({"region":r, "channel":channel, "PDFset":None}).val,3) + 1)
                            #c.specifyUncertainty('PDF',         binname, "signal", round(PDF_cache.get({"region":r, "channel":channel, "PDFset":PDFset}).val,3) + 1)
                            c.specifyUncertainty('scale_sig',   binname, "signal", 1.05) #1.30
                            c.specifyUncertainty('PDF',         binname, "signal", 1.04) #1.15
                            c.specifyUncertainty('PartonShower',binname, "signal", 1.04)

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
    
    #print limitDir
    if not os.path.isdir(limitDir):
        os.makedirs(limitDir)
    resDB = resultsDB(limitDir+'/results.sq', "results", setup.resultsColumns)
    res = {"signal":s.name}
    if not overWrite and res.DB.contains(key):
        res = resDB.getDicts(key)[0]
        logger.info("Found result for %s, reusing", s.name)
    else:
        # We don't calculate limits here, but just in case we find a way how to do it, put placeholders here
        res.update({"exp":0, "obs":0, "exp1up":0, "exp2up":0, "exp1down":0, "exp2down":0})
        # Don't extract all the nuisances by default
        if args.calcNuisances:
            c.calcNuisances(cardFileName, masking=range(15,30))
        # extract the NLL
        nll = c.physicsModel(cardFileName, options="", normList=["WZ_norm","ZZ_norm"], masking=range(15,30)) # fastScan turns of profiling
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

results = map(wrapper, jobs)
results = [r for r in results if r]

