#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option("--selectWeight",         dest="selectWeight",       default=None,                action="store",      help="select weight?")
parser.add_option("--PDFset",               dest="PDFset",              default="NNPDF30", choices=["NNPDF30", "PDF4LHC15_nlo_100"], help="select the PDF set")
parser.add_option("--selectRegion",         dest="selectRegion",          default=None, type="int",    action="store",      help="select region?")
parser.add_option("--sample",               dest='sample',  action='store', default='TTZ_NLO_16',    choices=["TTZ_LO_16", "TTZ_NLO_16", "TTZ_NLO_17", "WZ_pow_16"], help="which sample?")
parser.add_option("--small",                action='store_true', help="small?")
parser.add_option("--combine",              action='store_true', help="Combine results?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
parser.add_option('--overwrite',            dest="overwrite", default = False, action = "store_true", help="Overwrite existing output files, bool flag set to True  if used")
parser.add_option('--skipCentral',          dest="skipCentral", default = False, action = "store_true", help="Skip central weights")
parser.add_option('--btagWZ',               dest="btagWZ", default = False, action = "store_true", help="Get the uncertainties for b-tag extrapolation of WZ")
(options, args) = parser.parse_args()

# Standard imports
import ROOT
import os
import sys
import pickle
import math

# Analysis
from TopEFT.Analysis.SetupHelpers   import channel, trilepChannels, allTrilepChannels
from TopEFT.Analysis.regions        import regionsE, noRegions, btagRegions
from TopEFT.Tools.u_float           import u_float 
from TopEFT.Tools.resultsDB         import resultsDB
from TopEFT.Analysis.Region         import Region 
from TopEFT.Analysis.Setup          import Setup

#RootTools
from RootTools.core.standard import *

from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter

import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   options.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None)

year = 2017 if options.sample.count("17") else 2016
setup = Setup(year=year, nLeptons=3)
if options.btagWZ:
    setup.parameters.update({"nBTags":(0,-1), "nJets":(1,-1)})


##Summer16 samples
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v4/trilep/"
dirs = {}
dirs['TTZ_LO']          = ["TTZ_LO"]
dirs['TTZToLLNuNu_ext'] = ['TTZToLLNuNu_ext']
dirs['WZTo3LNu_comb']   = ['WZTo3LNu_comb']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

#TTZ_LO_16   = Sample.fromDirectory(name="TTZ_LO", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}Z (LO)", directory=directories['TTZ_LO'])
TTZ_NLO_16  = Sample.fromDirectory(name="TTZ_NLO", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}Z, Z#rightarrowll (NLO)", directory=directories['TTZToLLNuNu_ext'])
WZ_pow_16   = Sample.fromDirectory(name="WZ_pow", treeName="Events", isData=False, color=color.TTJets, texName="WZ (powheg)", directory=directories['WZTo3LNu_comb'])

## Fall17 samples
#data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
#postProcessing_directory = "TopEFT_PP_2017_Fall17_v3/trilep/"
data_directory = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2017_mva_v3/trilep/"
dirs = {}
dirs['TTZToLLNuNu'] = ['TTZToLLNuNu_amc']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}
TTZ_NLO_17 = Sample.fromDirectory(name="TTZ_NLO_17", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}Z, Z#rightarrowll (NLO)", directory=directories['TTZToLLNuNu'])


if options.sample == "TTZ_LO_16":
    sample = TTZ_LO_16
elif options.sample == "TTZ_NLO_16":
    sample = TTZ_NLO_16
elif options.sample == "TTZ_NLO_17":
    sample = TTZ_NLO_17
elif options.sample == "WZ_pow_16":
    sample = WZ_pow_16
if options.small:
    sample.reduceFiles( to = 1 )

if options.btagWZ:
    allRegions = btagRegions + noRegions
else:
    allRegions = regionsE + noRegions
regions = allRegions if not options.selectRegion else  [allRegions[options.selectRegion]]

setupIncl = setup.systematicClone(parameters={'mllMin':0, 'nJets':(0,-1), 'nBTags':(0,-1), 'zWindow1':'allZ'})
setup.verbose     = True

# use more inclusive selection in terms of lepton multiplicity in the future?

from TopEFT.Analysis.MCBasedEstimate import MCBasedEstimate
from TopEFT.Tools.user import analysis_results

'''
check all PDF sets that are available. will only implement parts for now.
'''

PDFset = options.PDFset
#PDFset = "NNPDF30"

scale_indices = [1,2,3,4,6,8]
LHEweight_original = 'abs(LHEweight_original)' # should be similar to genWeight

if options.sample == "TTZ_NLO_16":
    if PDFset == "NNPDF30":
        PDFType         = "replicas"
        centralWeight   = "genWeight" # sample produced with NNPDF30, so no central LHEweight saved apart from genWeight
        PDF_indices     = range(9,109)
        aS_indices      = [109,110]
    else:
        raise NotImplementedError

elif options.sample == "TTZ_NLO_17":
    if PDFset == "NNPDF31":
        raise NotImplementedError
    elif PDFset == "NNPDF30":
        PDFType         = "replicas"
        centralWeight   = "abs(LHEweight_wgt[972])"
        PDF_indices     = range(973,1073)
        aS_indices      = [1073, 1074]
    elif PDFset == "PDF4LHC15_nlo_100":
        PDFType         = "hessian"
        centralWeight   = "abs(LHEweight_wgt[475])"
        PDF_indices     = range(476,576)
        aS_indices      = [576, 577]
    else:
        raise NotImplementedError

elif options.sample == "WZ_pow_16":
    if PDFset == "NNPDF30":
        PDFType         = "replicas"
        centralWeight   = "genWeight" # sample produced with NNPDF30, so no central LHEweight saved apart from genWeight
        PDF_indices     = range(9,109)
        aS_indices      = [109,110]
    else:
        # CT10nlo and MMHT2014nlo68clas118 also included
        raise NotImplementedError

else:
    raise NotImplementedError


# central weights here should cancel out, but are necessary to not change the sign for NLO samples
if not options.selectWeight:
    scale_variations= [ "abs(LHEweight_wgt[%i])"%(i) for i in scale_indices ]
    PDF_variations  = [ "abs(LHEweight_wgt[%i])"%(i) for i in PDF_indices ]
    aS_variations   = [ "abs(LHEweight_wgt[%i])"%(i) for i in aS_indices ]
    variations      = scale_variations + PDF_variations + aS_variations
else:
    variations  = [ "abs(LHEweight_wgt[%s])"%(options.selectWeight) ]

results = {}

scale_systematics = {}

cacheDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/PDF_%s/"%(PDFset)

estimate = MCBasedEstimate(name=sample.name, sample=sample )
estimate.initCache(cacheDir)

## Results DB for scale and PDF uncertainties

PDF_cache = resultsDB(cacheDir+sample.name+'_unc.sq', "PDF", ["region", "channel", "PDFset"])
scale_cache = resultsDB(cacheDir+sample.name+'_unc.sq', "scale", ["region", "channel", "PDFset"])


'''
Recommendation from arxiv:1510.03865
for MC sets sort the obtained values e.g. in a list, then calculate
delta(PDF)sigma = (sigma[84] - sigma[16])/2
which gives the 68% CL
'''

def wrapper(args):
        r, c, setup = args
        res = estimate.cachedEstimate(r, c, setup, save=True, overwrite=options.overwrite)
        return (estimate.uniqueKey(r, c, setup), res )

jobs=[]

# remove all so to avoid unnecessary concurrency. All will be calculated as sum of the individual channels later
seperateChannels = allTrilepChannels
allTrilepChannelNames = [ c.name for c in allTrilepChannels ]
seperateChannels.pop(allTrilepChannelNames.index('all'))

if not options.skipCentral:
    # First run over seperate channels
    jobs.append((noRegions[0], channel(-1,-1), setupIncl))
    for var in variations:
        for c in seperateChannels:
            jobs.append((noRegions[0], c, setupIncl.systematicClone(sys={'reweight':[var]})))

## then one can sum up over all (currently done in the combine step)
#for var in variations:
#    jobs.append((noRegions[0], "all", setupIncl.systematicClone(sys={'reweight':[var]})))


if not options.combine:
    for c in seperateChannels:
        for region in regions:
            jobs.append((region, c, setup))
            for var in variations:
                jobs.append((region, c, setup.systematicClone(sys={'reweight':[var]})))
    
    logger.info("Created %s jobs",len(jobs))

    if options.noMultiThreading: 
        results = map(wrapper, jobs)
    else:
        from multiprocessing import Pool
        pool = Pool(processes=8)
        results = pool.map(wrapper, jobs)
        pool.close()
        pool.join()
    
    logger.info("All done.")

if options.combine:
    for c in ['all']:#allChannels:
    
        for region in regions:
            
            scales = []
            deltas = []
            delta_squared = 0
            # central yield inclusive and in region
            sigma_incl_central  = estimate.cachedEstimate(noRegions[0], 'all', setupIncl.systematicClone(sys={'reweight':[LHEweight_original]}))
            sigma_incl_centralWeight = estimate.cachedEstimate(noRegions[0], 'all', setupIncl.systematicClone(sys={'reweight':[centralWeight]}))
            sigma_central       = estimate.cachedEstimate(region, c, setup.systematicClone(sys={'reweight':[LHEweight_original]}))
            sigma_centralWeight = estimate.cachedEstimate(region, c, setup.systematicClone(sys={'reweight':[centralWeight]}))

            for var in scale_variations:
                simga_incl_reweight = estimate.cachedEstimate(noRegions[0], 'all', setupIncl.systematicClone(sys={'reweight':[var]}))
                norm = sigma_incl_central/simga_incl_reweight
                
                sigma_reweight  = estimate.cachedEstimate(region, c, setup.systematicClone(sys={'reweight':[var]}))
                sigma_reweight_acc = sigma_reweight * norm
                
                unc = abs( ( sigma_reweight_acc - sigma_central) / sigma_central )
                scales.append(unc.val)
            
            scale_rel = max(scales)

            for var in PDF_variations:
                # calculate x-sec noramlization
                simga_incl_reweight = estimate.cachedEstimate(noRegions[0], 'all', setupIncl.systematicClone(sys={'reweight':[var]}))
                norm = sigma_incl_central/simga_incl_reweight
                norm_centralWeight = sigma_incl_central/sigma_incl_centralWeight

                sigma_reweight  = estimate.cachedEstimate(region, c, setup.systematicClone(sys={'reweight':[var]}))
                sigma_reweight_acc = sigma_reweight * norm

                ## For replicas, just get a list of all sigmas, sort it and then get the 68% interval
                deltas.append(sigma_reweight_acc.val)
                ## recommendation for hessian is to have delta_sigma = sum_k=1_N( (sigma_k - sigma_0)**2 )
                ## so I keep the norm for both sigma_k and sigma_0 to obtain the acceptance uncertainty. Correct?
                delta_squared += ( sigma_reweight.val - sigma_centralWeight.val )**2
            
            deltas = sorted(deltas)

            # calculate uncertainty
            if PDFType == "replicas":
                # get the 68% interval
                upper = len(deltas)*84/100-1
                lower = len(deltas)*16/100 - 1
                delta_sigma = (deltas[upper]-deltas[lower])/2
            elif PDFType == "hessian":
                delta_sigma = math.sqrt(delta_squared)

            # recommendation is to multiply uncertainty by 1.5
            deltas_as = []
            for var in aS_variations:
                simga_incl_reweight = estimate.cachedEstimate(noRegions[0], 'all', setupIncl.systematicClone(sys={'reweight':[var]}))
                norm = sigma_incl_central/simga_incl_reweight
                
                sigma_reweight  = estimate.cachedEstimate(region, c, setup.systematicClone(sys={'reweight':[var]}))
                sigma_reweight_acc = sigma_reweight * norm

                deltas_as.append(sigma_reweight_acc.val)

            scale = 1.5 if PDFset.count("NNPDF") else 1.0
            delta_sigma_alphaS = scale * ( deltas_as[0] - deltas_as[1] ) / 2.

            # add alpha_s and PDF in quadrature
            delta_sigma_total = math.sqrt( delta_sigma_alphaS**2 + delta_sigma**2 )

            # make it relative wrt central value in region
            delta_sigma_rel = delta_sigma_total/sigma_central.val

            logger.info("Calculated PDF and alpha_s uncertainties for region %s in channel %s"%(region, c.name))
            logger.info("Central x-sec: %s", sigma_central)
            logger.info("Delta x-sec using PDF variations: %s", delta_sigma)
            logger.info("Delta x-sec using alpha_S variations: %s", delta_sigma_alphaS)
            logger.info("Delta x-sec total: %s", delta_sigma_total)
            logger.info("Relative uncertainty: %s", delta_sigma_rel)
            logger.info("Relative scale uncertainty: %s", scale_rel)
            
            # Store results
            PDF_cache.add({"region":region, "channel":c, "PDFset":options.PDFset}, delta_sigma_rel, overwrite=True)
            scale_cache.add({"region":region, "channel":c, "PDFset":None}, scale_rel, overwrite=True)

            print region, c.name
            PDF_cache.get({"region":region, "channel":c, "PDFset":options.PDFset})
            scale_cache.get({"region":region, "channel":c, "PDFset":None})
