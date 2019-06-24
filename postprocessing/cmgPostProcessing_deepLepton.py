#!/usr/bin/env python

# standard imports
import ROOT
import sys
import os
import copy
import random
import subprocess
import datetime
import shutil
import uuid

from array import array
from operator import mul
from math import sqrt, atan2, sin, cos, cosh, isnan

# RootTools
from RootTools.core.standard import *

# User specific
import TopEFT.Tools.user as user

# Tools for systematics
from TopEFT.Tools.helpers                    import closestOSDLMassToMZ, checkRootFile, writeObjToFile, deltaR, bestDRMatchInCollection, deltaPhi, mZ, cosThetaStar, getGenZ, getGenPhoton, getSortedZCandidates, getMinDLMass
from TopEFT.Tools.addJERScaling              import addJERScaling
from TopEFT.Tools.objectSelection_deepLepton import getLeptons, muonSelector, eleSelector, lepton_branches_data, lepton_branches_mc
from TopEFT.Tools.objectSelection_deepLepton import getGoodBJets, getGoodJets, isBJet, isAnalysisJet, getGoodPhotons, getGenPartsAll, getAllJets
from TopEFT.Tools.overlapRemovalTTG          import getTTGJetsEventType
from TopEFT.Tools.puProfileCache             import puProfile

from TopEFT.Tools.WeightInfo                 import WeightInfo
from TopEFT.Tools.HyperPoly                  import HyperPoly

from TopEFT.Tools.mt2Calculator              import mt2Calculator
from TopEFT.Tools.genMatch                   import getGenMatch
from TopEFT.Tools.user                       import results_directory
mt2Calc = mt2Calculator()

# for syncing
import TopEFT.Tools.sync as sync

#MC tools
from TopEFT.Tools.mcTools import GenSearch, B_mesons, D_mesons, B_mesons_abs, D_mesons_abs
genSearch = GenSearch()

# central configuration
targetLumi = 1000 #pb-1 Which lumi to normalize to

logChoices      = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET', 'SYNC']
triggerChoices  = ['mumu', 'ee', 'mue', 'mu', 'e', 'e_for_mu']

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--logLevel',                    action='store',         nargs='?',              choices=logChoices,     default='INFO',                     help="Log level for logging")
    argParser.add_argument('--overwrite',                   action='store_true',                                                                                        help="Overwrite existing output files, bool flag set to True  if used")
    argParser.add_argument('--samples',                     action='store',         nargs='*',  type=str,                           default=['WZTo3LNu'],               help="List of samples to be post-processed, given as CMG component name")
    argParser.add_argument('--triggerSelection',            action='store_true',                                                                                        help="Trigger selection?")
    argParser.add_argument('--eventsPerJob',                action='store',         nargs='?',  type=int,                           default=30000000,                   help="Maximum number of events per job (Approximate!).") # mul by 100
    argParser.add_argument('--nJobs',                       action='store',         nargs='?',  type=int,                           default=1,                          help="Maximum number of simultaneous jobs.")
    argParser.add_argument('--job',                         action='store',                     type=int,                           default=0,                          help="Run only job i")
    argParser.add_argument('--minNJobs',                    action='store',         nargs='?',  type=int,                           default=1,                          help="Minimum number of simultaneous jobs.")
    argParser.add_argument('--fileBasedSplitting',          action='store_true',                                                                                        help="Split njobs according to files")
    argParser.add_argument('--dataDir',                     action='store',         nargs='?',  type=str,                           default="/a/b/c",                   help="Name of the directory where the input data is stored (for samples read from Heppy).")
    argParser.add_argument('--targetDir',                   action='store',         nargs='?',  type=str,                           default=user.postprocessing_output_directory, help="Name of the directory the post-processed files will be saved")
    argParser.add_argument('--processingEra',               action='store',         nargs='?',  type=str,                           default='TopEFT_PP_v4',             help="Name of the processing era")
    argParser.add_argument('--skim',                        action='store',         nargs='?',  type=str,                           default='dilepTiny',                help="Skim conditions to be applied for post-processing")
    argParser.add_argument('--LHEHTCut',                    action='store',         nargs='?',  type=int,                           default=-1,                         help="LHE cut.")
    argParser.add_argument('--sync',                        action='store_true',                                                                                        help="Run syncing.")
    argParser.add_argument('--small',                       action='store_true',                                                                                        help="Run the file on a small sample (for test purpose), bool flag set to True if used")
    argParser.add_argument('--FEBug',                       action='store_true',                                                                                        help="Modify jets according to JME Formula Evaluator bug")
    argParser.add_argument('--theano',                      action='store_true',                                                                                        help="Use theano?")
    argParser.add_argument('--deepLepton',                  action='store_true',                                                                                        help="Add deep lepton MVA?")
    argParser.add_argument('--skipGenMatching',             action='store_true',                                                                                        help="skip matched genleps??")
    argParser.add_argument('--keepLHEWeights',              action='store_true',                                                                                        help="Keep LHEWeights?")
    argParser.add_argument('--keepPhotons',                 action='store_true',                                                                                        help="Keep photon information?")
    argParser.add_argument('--remakeTTVLeptonMVA',          action='store_true',                                                    default=True,                       help="Remake TTV lepton MVA?")
    argParser.add_argument('--skipSystematicVariations',    action='store_true',                                                                                        help="Don't calulcate BTag, JES and JER variations.")
    argParser.add_argument('--doTopPtReweighting',          action='store_true',                                                                                        help="Top pt reweighting?")
    argParser.add_argument('--doCRReweighting',             action='store_true',                                                                                        help="color reconnection reweighting?")
    argParser.add_argument('--forceProxy',                  action='store_true',                                                                                        help="Don't check certificate")
    argParser.add_argument('--year',                        action='store',                     type=int,   choices=[2016,2017],    required = True,                    help="Which year?")
    argParser.add_argument('--addReweights',                action='store_true',                                                                                        help="Add reweights for sample EFT reweighting?")
    argParser.add_argument('--interpolationOrder',          action='store',         nargs='?',  type=int,                           default=2,                          help="Interpolation order for EFT weights.")

    return argParser

options = get_parser().parse_args()

# Logging
import TopEFT.Tools.logger as logger
logFile = '/tmp/%s_%s_%s_njob%s.txt'%(options.skim, '_'.join(options.samples), os.environ['USER'], str(0 if options.nJobs==1 else options.job) )
logger  = logger.get_logger(options.logLevel, logFile = logFile, add_sync_level = options.sync)

import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None )

# Flags 
isDiLep     =   options.skim.lower().startswith('dilep')
isTriLep    =   options.skim.lower().startswith('trilep')
isQuadLep   =   options.skim.lower().startswith('quadlep')
isSingleLep =   options.skim.lower().startswith('singlelep')
isInclusive =   options.skim.lower().count('inclusive') 
isTiny      =   options.skim.lower().count('tiny') 

writeToDPM = options.targetDir == '/dpm/'

# Skim condition
skimConds = []
if isDiLep:
    #skimConds.append( "Sum$(LepGood_pt>10&&abs(LepGood_eta)<2.5) + Sum$(LepOther_pt>10&&abs(LepOther_eta)<2.5)>=2" )
    skimConds.append( "(Sum$(LepGood_pt>5&&abs(LepGood_eta)<2.5) + Sum$(LepOther_pt>5&&abs(LepOther_eta)<2.5))>=2" )
if isTriLep:
    skimConds.append( "Sum$(LepGood_pt>10&&abs(LepGood_eta)<2.5&&LepGood_miniRelIso<0.4) + Sum$(LepOther_pt>10&&abs(LepOther_eta)<2.5&&LepOther_miniRelIso<0.4)>=2 && Sum$(LepOther_pt>10&&abs(LepOther_eta)<2.5)+Sum$(LepGood_pt>10&&abs(LepGood_eta)<2.5)>=3" )
#    skimConds.append( "( run==%s&&lumi==%s&&evt==%s )"%(283052, 75, 124332542) )
if isQuadLep:
    skimConds.append( "Sum$(LepGood_pt>10&&abs(LepGood_eta)<2.5&&LepGood_miniRelIso<0.4) + Sum$(LepOther_pt>10&&abs(LepOther_eta)<2.5&&LepOther_miniRelIso<0.4)>=3 && Sum$(LepOther_pt>10&&abs(LepOther_eta)<2.5)+Sum$(LepGood_pt>10&&abs(LepGood_eta)<2.5)>=4" )
if isSingleLep:
    skimConds.append( "Sum$(LepGood_pt>20&&abs(LepGood_eta)<2.5) + Sum$(LepOther_pt>20&&abs(LepOther_eta)<2.5)>=1" )
if isInclusive:
    #skimConds = ["(evt==49567738&&lumi==66691)"]
    skimConds = ["(1)"]

maxN = 100 if options.small else None
from TopEFT.samples.helpers import fromHeppySample

if options.year==2016:
    MCgeneration = "Summer16"
else:
    MCgeneration = "Fall17"
    
if options.sync:
    from TopEFT.samples.sync import *
    samples = map( eval, options.samples ) 
else:
    if options.deepLepton: #FIXME
        #force_sample_map = "lepton_2016_data_heppy_mapper" if any( [ "Run" in s for s in options.samples] ) else "lepton_2016_mc_heppy_mapper"
        if any( [ "Run" in s for s in options.samples] ):
            force_sample_map = "full_events_2016_data_heppy_mapper"
        elif any( [ "SMS_T2tt_dM_10to80" in s for s in options.samples] ):
            force_sample_map = "signal_SMS_T2tt_dM_10to80_heppy_mapper"
        else: 
            force_sample_map = "full_events_2016_mc_heppy_mapper"
            #force_sample_map = "test_heppy_mapper"
    else:
        force_sample_map = None
    samples = [ fromHeppySample(s, data_path = options.dataDir, force_sample_map = force_sample_map, maxN = maxN, MCgeneration=MCgeneration, forceProxy=options.forceProxy) for s in options.samples ]
    #print(options.samples)
    #print(samples[0].files)
    logger.debug("Reading from CMG tuples: %s", ",".join(",".join(s.files) for s in samples) )
    
if len(samples)==0:
    logger.info( "No samples found. Was looking for %s. Exiting" % options.samples )
    sys.exit(-1)

isData = False not in [s.isData for s in samples]
isMC   = True not in [s.isData for s in samples]

# Check that all samples which are concatenated have the same x-section.
assert isData or len(set([s.heppy.xSection for s in samples]))==1, "Not all samples have the same xSection: %s !"%(",".join([s.name for s in samples]))
assert isMC or len(samples)==1, "Don't concatenate data samples"

xSection = samples[0].heppy.xSection if isMC else None

# Trigger selection
from TopEFT.Tools.triggerSelector import triggerSelector
ts           = triggerSelector(options.year)
triggerCond  = ts.getSelection(options.samples[0] if isData else "MC")
treeFormulas = {"triggerDecision": {'string':triggerCond} }
if isData and options.triggerSelection:
    logger.info("Sample will have the following trigger skim: %s"%triggerCond)
    skimConds.append( triggerCond )

# Trigger SF
from TopEFT.Tools.triggerEfficiency          import triggerEfficiency
triggerSF = triggerEfficiency(options.year)

# Tracking SF
from TopEFT.Tools.leptonTrackingEfficiency import leptonTrackingEfficiency
leptonTrackingSF = leptonTrackingEfficiency(options.year)

# Lepton SF
from TopEFT.Tools.leptonSF import leptonSF as leptonSF_
# get different lepton SF reader & store this extra Id information
# extra_lep_ids = ['FO_4l', 'FO_3l', 'FO_2l', 'FO_1l', 'FO_SS', 'tight_4l', 'tight_3l', 'tight_2l', 'tight_1l','tight_SS']
extra_lep_ids = ['FO_4l', 'FO_3l', 'FO_SS', 'tight_4l', 'tight_3l', 'tight_SS']
tight_lep_ids = [ x for x in extra_lep_ids if 'tight' in x ]
leptonSF = {tight_id:leptonSF_(year=options.year, ID=tight_id) for tight_id in tight_lep_ids }

#Samples: combine if more than one
if len(samples)>1:
    sample_name =  samples[0].name+"_comb"
    logger.info( "Combining samples %s to %s.", ",".join(s.name for s in samples), sample_name )
    sample = Sample.combine(sample_name, samples, maxN = maxN)
    # Clean up
    for s in samples:
        sample.clear()
elif len(samples)==1:
    sample = samples[0]
else:
    raise ValueError( "Need at least one sample. Got %r",samples )

try:
    xsec = sample.xsec
    nEvents = sample.nEvents
    lumiweight1fb = xsec * 1000. / nEvents
except:
    pass

if options.fileBasedSplitting:
    len_orig = len(sample.files)
    sample = sample.split( n=options.nJobs, nSub=options.job)
    if sample is None:  
        logger.info( "No such sample. nJobs %i, job %i numer of files %i", options.nJobs, options.job, len_orig )
        sys.exit(0)
    logger.info( "fileBasedSplitting: Run over %i/%i files for job %i/%i."%(len(sample.files), len_orig, options.job, options.nJobs))
    logger.debug( "fileBasedSplitting: Files to be run over:\n%s", "\n".join(sample.files) )
if isMC:
    from TopEFT.Tools.puReweighting import getReweightingFunction
    if options.year == 2016:
        nTrueInt36fb_puRW        = getReweightingFunction(data="PU_2016_36000_XSecCentral", mc="Summer16")
        nTrueInt36fb_puRWDown    = getReweightingFunction(data="PU_2016_36000_XSecDown",    mc="Summer16")
        nTrueInt36fb_puRWUp      = getReweightingFunction(data="PU_2016_36000_XSecUp",      mc="Summer16")
    elif options.year == 2017:
        # keep the weight name for now. Should we update to a more general one?
        puProfiles = puProfile( source_sample = samples[0] )
        mcHist = puProfiles.cachedTemplate( selection="( 1 )", weight='genWeight', overwrite=False ) # use genWeight for amc@NLO samples. No problems encountered so far
        nTrueInt36fb_puRW        = getReweightingFunction(data="PU_2017_42400_XSecCentral", mc=mcHist)
        nTrueInt36fb_puRWDown    = getReweightingFunction(data="PU_2017_42400_XSecDown",    mc=mcHist)
        nTrueInt36fb_puRWUp      = getReweightingFunction(data="PU_2017_42400_XSecUp",      mc=mcHist)

# top pt reweighting
# Decision based on sample name -> whether TTJets or TTLep is in the sample name
isTT = sample.name.startswith("TTJets") or sample.name.startswith("TTLep") or sample.name.startswith("TT_pow") or sample.name.startswith("TTZ")
doTopPtReweighting = isTT and options.doTopPtReweighting
if doTopPtReweighting:
    from TopEFT.Tools.topPtReweighting import getUnscaledTopPairPtReweightungFunction, getTopPtDrawString, getTopPtsForReweighting
    logger.info( "Sample will have top pt reweighting." )
    topPtReweightingFunc = getUnscaledTopPairPtReweightungFunction(selection = "dilep")
    # Compute x-sec scale factor on unweighted events
    selectionString = "&&".join(skimConds)
    topScaleF = sample.getYieldFromDraw( selectionString = selectionString, weightString = getTopPtDrawString(selection = "dilep"))
    topScaleF = topScaleF['val']/float(sample.chain.GetEntries(selectionString))
    logger.info( "Found topScaleF %f", topScaleF )
else:
    topScaleF = 1
    logger.info( "Sample will NOT have top pt reweighting. topScaleF=%f",topScaleF )

if options.doCRReweighting:
    from TopEFT.Tools.colorReconnectionReweighting import getCRWeight, getCRDrawString
    logger.info( "Sample will have CR reweighting." )
    selectionString = "&&".join(skimConds)
    #norm = sample.getYieldFromDraw( selectionString = selectionString, weightString = "genWeight" )
    norm = float(sample.chain.GetEntries(selectionString))
    CRScaleF = sample.getYieldFromDraw( selectionString = selectionString, weightString = getCRDrawString() )
    CRScaleF = CRScaleF['val']/norm#['val']
    logger.info(" Using norm: %s"%norm )
    logger.info(" Found CRScaleF: %s"%CRScaleF)
else:
    CRScaleF = 1
    logger.info( "Sample will NOT have CR reweighting. CRScaleF=%f",CRScaleF )

# systematic variations
addSystematicVariations = (not isData) and (not options.skipSystematicVariations)
if addSystematicVariations:
    # B tagging SF
    from TopEFT.Tools.btagEfficiency import btagEfficiency
    
    # CSVv2
    if options.year == 2016:
        effFile         = '$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/TTLep_pow_Moriond17_2j_2l_CSVv2_eta.pkl'
        sfFile          = '$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/CSVv2_Moriond17_B_H.csv'
    elif options.year == 2017:
        effFile         = '$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/TTLep_pow_Fall17_2j_2l_CSVv2_eta.pkl'
        sfFile          = '$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/CSVv2_94XSF_V2_B_F.csv'
    btagEff_CSVv2   = btagEfficiency( effFile = effFile, sfFile = sfFile, fastSim = False )

    # DeepCSV
    if options.year == 2016:
        effFile         = '$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/TTLep_pow_Moriond17_2j_2l_deepCSV_eta.pkl'
        sfFile          = '$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/DeepCSV_Moriond17_B_H.csv'
    elif options.year == 2017:
        effFile         = '$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/TTLep_pow_Fall17_2j_2l_deepCSV_eta.pkl'
        sfFile          = '$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/DeepCSV_94XSF_V3_B_F.csv'
    btagEff_DeepCSV = btagEfficiency( effFile = effFile, sfFile = sfFile, fastSim = False )

# LHE cut (DY samples)
if options.LHEHTCut>0:
    sample.name+="_lheHT"+str(options.LHEHTCut)
    logger.info( "Adding upper LHE cut at %f", options.LHEHTCut )
    skimConds.append( "lheHTIncoming<%f"%options.LHEHTCut )

# output directory (store temporarily when running on dpm)
if writeToDPM:
    # Allow parallel processing of N threads on one worker
    directory = os.path.join('/tmp/%s'%os.environ['USER'], str(uuid.uuid4()), options.processingEra)
    if not os.path.exists( directory ):
        os.makedirs( directory )
    from TopEFT.Tools.user import dpm_directory as user_dpm_directory
else:
    directory  = os.path.join(options.targetDir, options.processingEra) 

postfix = '_small' if options.small else ''

if options.FEBug:
    from JetMET.JetCorrector.jetCorrectors_17Nov2017 import Fall17_17Nov17_V11_MC, Fall17_17Nov17_V24_MC
    if not ( options.year == 2017 and isMC):
        raise NotImplementedError( "Can do this only for 2017 MC" ) 

    postfix += '_FEBug'

output_directory = os.path.join( directory, options.skim+postfix, sample.name )

if os.path.exists(output_directory) and options.overwrite:
    if options.nJobs > 1:
        logger.warning( "NOT removing directory %s because nJobs = %i", output_directory, options.nJobs )
    else:
        logger.info( "Output directory %s exists. Deleting.", output_directory )
        shutil.rmtree(output_directory)

try:    #Avoid trouble with race conditions in multithreading
    os.makedirs(output_directory)
    logger.info( "Created output directory %s.", output_directory )
except:
    pass

if options.remakeTTVLeptonMVA:
    from TopEFT.Tools.leptonMVA import leptonMVA
    mva = leptonMVA(options.year)

if isTiny:
    #branches to be kept for data and MC
    branchKeepStrings_DATAMC = \
       ["run", "lumi", "evt", "isData", "rho", "nVert",
        "met_pt", "met_phi", "met_chsPt", "met_chsPhi",
        "Flag_*", "HLT_*",
        # "LepGood_eta", "LepGood_etaSc", "LepGood_pt","LepGood_phi", "LepGood_dxy", "LepGood_dz","LepGood_tightId", "LepGood_pdgId",
        # "LepGood_mediumMuonId", "LepGood_miniRelIso", "LepGood_relIso03", "LepGood_sip3d", "LepGood_mvaIdSpring15", "LepGood_convVeto", "LepGood_lostHits", "LepGood_eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz"
        ]

    #branches to be kept for MC samples only
    branchKeepStrings_MC = [ \
        "nTrueInt", "genWeight", "xsec", "met_genPt", "met_genPhi", "lheHTIncoming", "nIsr"
    ]

    #branches to be kept for data only
    branchKeepStrings_DATA = [ ]
else:
    #branches to be kept for data and MC
    branchKeepStrings_DATAMC = [\
        "run", "lumi", "evt", "isData", "rho", "nVert",
        "met_pt", "met_phi","met_Jet*", "met_Unclustered*", "met_sumEt", "met_rawPt","met_rawPhi", "met_rawSumEt", "met_caloPt", "met_caloPhi",
        "Flag_*","HLT_*",
        # "nDiscJet", "DiscJet_*",
        # "nJetFailId", "JetFailId_*",
        # "nLepGood", "LepGood_*",
        # "nLepOther", "LepOther_*",
        "nTauGood", "TauGood_*",

    ]

    #branches to be kept for MC samples only
    branchKeepStrings_MC = [\
        "nTrueInt", "genWeight", "xsec", "met_gen*", "lheHTIncoming",
        "ngenPartAll","genPartAll_*","ngenLep","genLep_*"
    ]

    #branches to be kept for data only
    branchKeepStrings_DATA = [ ]

if options.keepPhotons:
    branchKeepStrings_DATAMC += [
        "ngamma", "gamma_idCutBased", "gamma_hOverE", "gamma_r9", "gamma_sigmaIetaIeta", "gamma_chHadIso04", "gamma_chHadIso", "gamma_phIso",
        "gamma_neuHadIso", "gamma_relIso", "gamma_pdgId", "gamma_pt", "gamma_eta", "gamma_phi", "gamma_mass",
        "gamma_chHadIsoRC04", "gamma_chHadIsoRC"
    ]
    branchKeepStrings_MC += [
        "gamma_mcMatchId", "gamma_mcPt", "gamma_genIso04", "gamma_genIso03", "gamma_drMinParton"
    ]

if options.keepLHEWeights:
    branchKeepStrings_MC+=["nLHEweight", "LHEweight_id", "LHEweight_wgt", "LHEweight_original"]

if isSingleLep:
    branchKeepStrings_DATAMC += ['HLT_*']
if options.deepLepton:
    branchKeepStrings_DATAMC += ['nDL_*', 'DL_*']
# Load reweight pickle file if supposed to keep weights. 
extra_variables = []
if options.addReweights and isMC:

    # Determine coefficients for storing in vector
    # Sort Ids wrt to their position in the card file

    weightInfo = WeightInfo( sample.reweight_pkl )

    # weights for the ntuple
    rw_vector       = TreeVariable.fromString( "rw[w/F,"+",".join(w+'/F' for w in weightInfo.variables)+"]")
    rw_vector.nMax  = weightInfo.nid
    extra_variables.append(rw_vector)

    # coefficients for the weight parametrization
    param_vector      = TreeVariable.fromString( "p[C/F]" )
    param_vector.nMax = HyperPoly.get_ndof(weightInfo.nvar, options.interpolationOrder)
    hyperPoly         = HyperPoly( options.interpolationOrder )
    extra_variables.append(param_vector)
    extra_variables.append(TreeVariable.fromString( "chi2_ndof/F"))

# Jet variables to be read from chain
jetCorrInfo = ['corr/F', 'corr_JECUp/F', 'corr_JECDown/F'] if addSystematicVariations else []
if isMC:
    if isTiny:
        jetMCInfo = ['mcPt/F', 'hadronFlavour/I', 'mcMatchId/I']
    else:
        jetMCInfo = ['mcMatchFlav/I', 'partonId/I', 'partonMotherId/I', 'mcPt/F', 'mcFlavour/I', 'hadronFlavour/I', 'mcMatchId/I']
else:
    jetMCInfo = []

if sample.isData:
    lumiScaleFactor=None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_DATA
    from FWCore.PythonUtilities.LumiList import LumiList
    # Apply golden JSON
    if options.year == 2016:
        json = '$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    elif options.year == 2017:
        json = '$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
    if hasattr( sample, 'heppy'): sample.heppy.json = json
    lumiList = LumiList(os.path.expandvars(json))
    logger.info( "Loaded json %s", json )
else:
    lumiScaleFactor = xSection*targetLumi/float(sample.normalization) if xSection is not None else None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_MC

jetVars = ['pt/F', 'rawPt/F', 'eta/F', 'phi/F', 'id/I', 'btagCSV/F', 'btagDeepCSV/F', 'area/F', 'DFb/F', 'DFbb/F'] + jetCorrInfo + jetMCInfo
if options.year == 2016: jetVars += ['id16/I']
jetVarNames = [x.split('/')[0] for x in jetVars]
genLepVars      = ['pt/F', 'phi/F', 'eta/F', 'pdgId/I', 'index/I', 'lepGood2MatchIndex/I', 'n_t/I','n_W/I', 'n_B/I', 'n_D/I', 'n_tau/I']
genLepVarNames  = [x.split('/')[0] for x in genLepVars]

read_variables = map(TreeVariable.fromString, ['met_pt/F', 'met_phi/F', 'run/I', 'lumi/I', 'evt/l', 'nVert/I', 'rho/F'] )
if options.keepPhotons:
    read_variables += [ TreeVariable.fromString('ngamma/I'),
                        VectorTreeVariable.fromString('gamma[pt/F,eta/F,phi/F,mass/F,idCutBased/I,pdgId/I]') ]

new_variables = [ 'weight/F', 'triggerDecision/I']
new_variables+= [ 'jet[%s]'% ( ','.join(jetVars) ) ]

lepton_branches_read  = lepton_branches_mc if isMC else lepton_branches_data
if sync or options.remakeTTVLeptonMVA: 
    lepton_branches_read  += ',trackMult/F,miniRelIsoCharged/F,miniRelIsoNeutral/F,jetPtRelv2/F,jetPtRelv1/F,jetPtRatiov2/F,jetPtRatiov1/F,relIso03/F,jetBTagDeepCSV/F,segmentCompatibility/F,mvaIdSpring16/F,eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz/I,mvaIdFall17noIso/F'
if options.deepLepton:                 
    lepton_branches_read  += ',r9/F,dEtaInSeed/F,edxy/F,edz/F,ip3d/F,sip3d/F,innerTrackChi2/F,innerTrackValidHitFraction/F,ptErrTk/F,rho/F,jetDR/F,trackerLayers/I,pixelLayers/I,trackerHits/I,lostHits/I,lostOuterHits/I,glbTrackProbability/F,isGlobalMuon/I,chi2LocalPosition/F,chi2LocalMomentum/F,globalTrackChi2/F,trkKink/F,caloCompatibility/F,nStations/F'
    read_variables.append( VectorTreeVariable.fromString('DL_pfCand_neutral[pt/F,eta/F,phi/F,dxy_pf/F,dz_pf/F,puppiWeight/F,fromPV/F,selectedLeptons_mask/I]', nMax=200 )) # default nMax is 100
    read_variables.append( VectorTreeVariable.fromString('DL_pfCand_charged[pt/F,eta/F,phi/F,dxy_pf/F,dz_pf/F,puppiWeight/F,dzAssociatedPV/F,fromPV/F,selectedLeptons_mask/I]', nMax=500 )) # default nMax is 100
    read_variables.append( VectorTreeVariable.fromString('DL_pfCand_photon[pt/F,eta/F,phi/F,dxy_pf/F,dz_pf/F,puppiWeight/F,fromPV/F,selectedLeptons_mask/I]', nMax=200 )) # default nMax is 100
    read_variables.append( VectorTreeVariable.fromString('DL_pfCand_electron[pt/F,eta/F,phi/F,dxy_pf/F,dz_pf/F,pdgId/I,selectedLeptons_mask/I]', nMax=50 )) # default nMax is 100
    read_variables.append( VectorTreeVariable.fromString('DL_pfCand_muon[pt/F,eta/F,phi/F,dxy_pf/F,dz_pf/F,pdgId/I,selectedLeptons_mask/I]', nMax=50 )) # default nMax is 100
    read_variables.append( VectorTreeVariable.fromString('DL_SV[pt/F,eta/F,phi/F,chi2/F,ndof/F,dxy/F,edxy/F,ip3d/F,eip3d/F,sip3d/F,cosTheta/F,jetPt/F,jetEta/F,jetDR/F,maxDxyTracks/F,secDxyTracks/F,maxD3dTracks/F,secD3dTracks/F,selectedLeptons_mask/I]', nMax=200 )) # default nMax is 100
    read_variables.extend( map( TreeVariable.fromString, ["nDL_pfCand_neutral/I", "nDL_pfCand_charged/I", "nDL_pfCand_photon/I", "nDL_pfCand_electron/I", "nDL_pfCand_muon/I", "nDL_SV/I"]) )
# For the moment store all the branches that we read
lepton_branches_store = lepton_branches_read+',mvaTTV/F,cleanEle/I,ptCorr/F,isGenPrompt/I'

extra_mu_selector  = {lep_id:muonSelector(lep_id, year = options.year) for lep_id in extra_lep_ids}
extra_ele_selector = {lep_id:eleSelector(lep_id, year = options.year) for lep_id in extra_lep_ids}
for lep_id in extra_lep_ids: lepton_branches_store+=',%s/I'%(lep_id)

if options.deepLepton:

    if options.theano:
        # Theano config
        import uuid, os
        theano_compile_dir = '/afs/hephy.at/data/%s01/theano_compile_tmp/%s'%( os.environ['USER'], str(uuid.uuid4()) )
        if not os.path.exists( theano_compile_dir ):
            os.makedirs( theano_compile_dir )
        #os.environ['THEANO_FLAGS'] = 'cuda.root=/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/cuda/8.0.61/,device=cpu,base_compiledir=%s'%theano_compile_dir 
        logger.info( "Using theano compile directory %s", theano_compile_dir )
        os.environ['THEANO_FLAGS'] = 'cuda.enabled=False,base_compiledir=%s'%theano_compile_dir 
        os.environ['KERAS_BACKEND'] = 'theano'
    else:
        import tensorflow as tf
        from keras.backend.tensorflow_backend import set_session
        config = tf.ConfigProto()
        #config.gpu_options.per_process_gpu_memory_fraction = 0.3
        #config.gpu_options.allow_growth = True
        #config.gpu_options.visible_device_list = "0"
        config.intra_op_parallelism_threads = 1
        config.inter_op_parallelism_threads = 1
        set_session(tf.Session(config=config))

    from TopEFT.Tools.DeepLeptonReader import ele_deepLeptonModel, mu_deepLeptonModel
    from TopEFT.Tools.DeepLeptonReader import ele_evaluator,  mu_evaluator
    mu_evaluator.verbosity = 0
    ele_evaluator.verbosity = 0
    lepton_branches_store += ",deepLepton_prompt/F,deepLepton_nonPrompt/F,deepLepton_fake/F,iLepGood/I,iLepOther/I"

lepton_vars_store     = [s.split('/')[0] for s in lepton_branches_store.split(',')]
lepton_vars_read      = [s.split('/')[0] for s in lepton_branches_read .split(',')]

new_variables+= [ 'lep[%s]' % lepton_branches_store ]

if isMC:
    read_variables+= [TreeVariable.fromString('nTrueInt/F')]
    # reading gen particles for top pt reweighting
    read_variables.append( TreeVariable.fromString('ngenPartAll/I') )
    read_variables.append( VectorTreeVariable.fromString('genPartAll[pt/F,eta/F,phi/F,mass/F,pdgId/I,status/I,charge/I,motherId/I,grandmotherId/I,nMothers/I,motherIndex1/I,motherIndex2/I,nDaughters/I,daughterIndex1/I,daughterIndex2/I,isPromptHard/I]', nMax=200 )) # default nMax is 100, which would lead to corrupt values in this case
    read_variables.append( TreeVariable.fromString('genWeight/F') )
    read_variables.append( TreeVariable.fromString('nIsr/I') )
    read_variables.append( VectorTreeVariable.fromString('LHEweight[wgt/F,id/I]',  nMax=1100) )
    if options.keepPhotons:
        read_variables.append( VectorTreeVariable.fromString('gamma[mcPt/F]') )

    new_variables.append('PSweight_central/F')
    for ps in ['isrUp', 'isrDown', 'fsrUp', 'fsrDown']:
        for multiplier in ['red', 'nom', 'cons']:
            new_variables.append('PSweight_%s_%s/F'%(multiplier, ps))
    if options.doTopPtReweighting: 
        new_variables.append('reweightTopPt/F')
    if options.doCRReweighting:
        new_variables.append('reweightCR/F')

    new_variables.extend(['reweightPU36fb/F','reweightPU36fbUp/F','reweightPU36fbDown/F'])
    for i in ["tight_SS","tight_1l","tight_2l","tight_3l","tight_4l"]:
        new_variables.extend(['reweightTrigger_%s/F'%i, 'reweightTriggerUp_%s/F'%i, 'reweightTriggerDown_%s/F'%i, 'reweightLeptonTrackingSF_%s/F'%i,'reweightLeptonTrackingSFUp_%s/F'%i, 'reweightLeptonTrackingSFDown_%s/F'%i])
        new_variables.extend(['reweightLeptonSF_%s/F'%i, 'reweightLeptonSFSyst_%s/F'%i, 'reweightLeptonSFSystUp_%s/F'%i, 'reweightLeptonSFSystDown_%s/F'%i, 'reweightMuSFStat_%s/F'%i, 'reweightMuSFStatUp_%s/F'%i, 'reweightMuSFStatDown_%s/F'%i, 'reweightEleSFStat_%s/F'%i, 'reweightEleSFStatUp_%s/F'%i, 'reweightEleSFStatDown_%s/F'%i ])

    if not options.skipGenMatching:
        TreeVariable.fromString( 'nGenLep/I' ),
        new_variables.append( 'GenLep[%s]'% ( ','.join(genLepVars) ) )
        new_variables.extend(['genZ_pt/F', 'genZ_mass/F', 'genZ_eta/F', 'genZ_phi/F', 'genZ_cosThetaStar/F', 'genZ_daughter_flavor/I' ])

read_variables += [\
    TreeVariable.fromString('nLepGood/I'),
    TreeVariable.fromString('nLepOther/I'),
    VectorTreeVariable.fromString('LepGood[%s]'  % (lepton_branches_read)),
    VectorTreeVariable.fromString('LepOther[%s]' % (lepton_branches_read)),

    TreeVariable.fromString('nJet/I'),
    TreeVariable.fromString('nDiscJet/I'),
    VectorTreeVariable.fromString('Jet[%s]'% ( ','.join(jetVars) ) ),
    VectorTreeVariable.fromString('DiscJet[%s]'% ( ','.join(jetVars) ) )
]

if options.year == 2016:
    read_variables += [\
        TreeVariable.fromString('nJetAll/I'),
        VectorTreeVariable.fromString('JetAll[%s]'% ( ','.join(jetVars) ) )
    ]

if isData: new_variables.extend( ['jsonPassed/I'] )
new_variables.extend( ['nBTag/I', 'nBTagDeepCSV/I', 'ht/F', 'metSig/F', 'nJetSelected/I'] )

new_variables.extend( ['nGoodElectrons/I','nGoodMuons/I','nGoodLeptons/I','nLeptons_FO_3l_genPrompt/I' ] )
for lep_id in extra_lep_ids: new_variables.extend( ['nLeptons_%s/I'%lep_id, 'nMuons_%s/I'%lep_id, 'nElectrons_%s/I'%lep_id] )

# Z related observables
new_variables.extend( ['Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I', 'nonZ_l2_index/I'] )
new_variables.extend( ['Z_pt/F', 'Z_eta/F', 'Z_phi/F', 'Z_lldPhi/F', 'Z_lldR/F',  'Z_mass/F', 'cosThetaStar/F', 'Higgs_mass/F', 'Z_fromTight/I'] )
new_variables.extend( ['Z1_l1_index_4l/I', 'Z1_l2_index_4l/I', 'Z2_l1_index_4l/I', 'Z2_l2_index_4l/I', 'nonZ1_l1_index_4l/I', 'nonZ1_l2_index_4l/I'] )
for i in [1,2]:
    new_variables.extend( ['Z%i_pt_4l/F'%i, 'Z%i_eta_4l/F'%i, 'Z%i_phi_4l/F'%i, 'Z%i_lldPhi_4l/F'%i, 'Z%i_lldR_4l/F'%i,  'Z%i_mass_4l/F'%i, 'Z%i_cosThetaStar_4l/F'%i] )


if options.keepPhotons: 
    new_variables.extend( ['nPhotonGood/I','photon_pt/F','photon_eta/F','photon_phi/F','photon_idCutBased/I'] )
    if isMC: new_variables.extend( ['photon_genPt/F', 'photon_genEta/F'] )
    new_variables.extend( ['met_pt_photonEstimated/F','met_phi_photonEstimated/F','metSig_photonEstimated/F'] )
    new_variables.extend( ['photonJetdR/F','photonLepdR/F'] )
    new_variables.extend( ['TTGJetsEventType/I'] )

# variables for dilepton stop
new_variables.extend( ['dl_mt2ll/F', 'dl_mt2bb/F', 'dl_mt2blbl/F', 'dl_mass/F', 'dl_pt/F', 'dl_eta/F', 'dl_phi/F', 'min_dl_mass/F', 'min_dl_mass_FO_3l/F', 'min_dl_mass_loose/F', 'totalLeptonCharge/I' ] )


# variables for Tims Analysis
new_variables.extend( ['Qll/F', 'mll/F', 'ptll/F', 'mtautau/F', 'mt_min/F', 'met_mu_pt/F'] )

if addSystematicVariations:
    read_variables += map(TreeVariable.fromString, [\
    "met_JetEnUp_Pt/F", "met_JetEnUp_Phi/F", "met_JetEnDown_Pt/F", "met_JetEnDown_Phi/F", "met_JetResUp_Pt/F", "met_JetResUp_Phi/F", "met_JetResDown_Pt/F", "met_JetResDown_Phi/F", 
    "met_UnclusteredEnUp_Pt/F", "met_UnclusteredEnUp_Phi/F", "met_UnclusteredEnDown_Pt/F", "met_UnclusteredEnDown_Phi/F", 
    ] )

    for var in ['JECUp', 'JECDown', 'JERUp', 'JERDown', 'UnclusteredEnUp', 'UnclusteredEnDown']:
        if 'Unclustered' not in var: new_variables.extend( ['nJetSelected_'+var+'/I', 'nBTag_'+var+'/I','ht_'+var+'/F'] )
        new_variables.extend( ['met_pt_'+var+'/F', 'met_phi_'+var+'/F', 'metSig_'+var+'/F'] )
        if options.keepPhotons: new_variables.extend( ['met_pt_photonEstimated_'+var+'/F', 'met_phi_photonEstimated_'+var+'/F', 'metSig_photonEstimated_'+var+'/F'] )
        new_variables.extend( ['dl_mt2ll_'+var+'/F', 'dl_mt2bb_'+var+'/F', 'dl_mt2blbl_'+var+'/F'] )
    # Btag weights Method 1a
    for var in btagEff_CSVv2.btagWeightNames:
        if var!='MC':
            new_variables.append('reweightBTagCSVv2_'+var+'/F')
    for var in btagEff_DeepCSV.btagWeightNames:
        if var!='MC':
            new_variables.append('reweightBTagDeepCSV_'+var+'/F')

# Define a reader
reader = sample.treeReader( \
    variables = read_variables ,
    selectionString = "&&".join(skimConds) if not options.sync else "(1)"
    )

# Calculate photonEstimated met
def getMetPhotonEstimated(met_pt, met_phi, photon):
  met = ROOT.TLorentzVector()
  met.SetPtEtaPhiM(met_pt, 0, met_phi, 0 )
  gamma = ROOT.TLorentzVector()
  gamma.SetPtEtaPhiM(photon['pt'], photon['eta'], photon['phi'], photon['mass'] )
  metGamma = met + gamma
  return (metGamma.Pt(), metGamma.Phi())

## Calculate corrected met pt/phi using systematics for jets
def getMetJetCorrected(met_pt, met_phi, jets, var):
  met_corr_px  = met_pt*cos(met_phi) + sum([(j['pt']-j['pt_'+var])*cos(j['phi']) for j in jets])
  met_corr_py  = met_pt*sin(met_phi) + sum([(j['pt']-j['pt_'+var])*sin(j['phi']) for j in jets])
  met_corr_pt  = sqrt(met_corr_px**2 + met_corr_py**2)
  met_corr_phi = atan2(met_corr_py, met_corr_px)
  return (met_corr_pt, met_corr_phi)

def getMetCorrected(r, var, addPhoton = None):
    if var == "":
      if addPhoton is not None: return getMetPhotonEstimated(r.met_pt, r.met_phi, addPhoton)
      else:                     return (r.met_pt, r.met_phi)

    elif var in [ "JECUp", "JECDown", "UnclusteredEnUp", "UnclusteredEnDown" ]:
      var_ = var
      var_ = var_.replace("JEC", "JetEn")
      var_ = var_.replace("JER", "JetRes")
      met_pt  = getattr(r, "met_" + var_ + "_Pt")
      met_phi = getattr(r, "met_" + var_ + "_Phi")
      if addPhoton is not None: return getMetPhotonEstimated(met_pt, met_phi, addPhoton)
      else:                     return (met_pt, met_phi)

    else:
        raise ValueError

def filler( event ):
    # shortcut
    r = reader.event
    if options.sync: sync.print_header( r.run, r.lumi, r.evt )
    if isMC: gPart = getGenPartsAll(r)

    # weight
    if isMC:
        if lumiScaleFactor is not None:
            event.weight = lumiScaleFactor*r.genWeight
        else:
            try:
                event.weight = event.lumiweight1fb
            except:
                event.weight = 1

        if isnan(event.weight):
            logger.info("Weight is NaN! genweight: %s, lumiScaleFactor: %s"%(r.genWeight, lumiScaleFactor))
            event.weight = 0.

        event.reweightLeptonTrackingSF      = 1
        event.reweightLeptonTrackingSFUp    = 1
        event.reweightLeptonTrackingSFDown  = 1
        event.reweightTrigger       = 1
        event.reweightTriggerUp     = 1
        event.reweightTriggerDown   = 1

        if options.addReweights:
            event.nrw    = weightInfo.nid
            lhe_weights  = reader.products['lhe'].weights()
            weights      = []
            param_points = []
            for weight in lhe_weights:
                # Store nominal weight (First position!) 
                if weight.id=='rwgt_1': event.rw_nominal = weight.wgt
                if not weight.id in weightInfo.id: continue
                pos = weightInfo.data[weight.id]
                event.rw_w[pos] = weight.wgt
                weights.append( weight.wgt )
                interpreted_weight = interpret_weight(weight.id)
                for var in weightInfo.variables:
                    getattr( event, "rw_"+var )[pos] = interpreted_weight[var]
                # weight data for interpolation
                if not hyperPoly.initialized:
                    param_points.append( tuple(interpreted_weight[var] for var in weightInfo.variables) )

            # get list of values of ref point in specific order
            ref_point_coordinates = [weightInfo.ref_point_coordinates[var] for var in weightInfo.variables]

            # Initialize with Reference Point
            if not hyperPoly.initialized: hyperPoly.initialize( param_points, ref_point_coordinates )
            coeff = hyperPoly.get_parametrization( weights )

            # = HyperPoly(weight_data, args.interpolationOrder)
            event.np = hyperPoly.ndof
            event.chi2_ndof = hyperPoly.chi2_ndof(coeff, weights)
            #logger.debug( "chi2_ndof %f coeff %r", event.chi2_ndof, coeff )
            if event.chi2_ndof>10**-6: logger.warning( "chi2_ndof is large: %f", event.chi2_ndof )
            for n in xrange(hyperPoly.ndof):
                event.p_C[n] = coeff[n]

    elif isData:
        event.weight = 1
    else:
        raise NotImplementedError( "isMC %r isData %r " % (isMC, isData) )

    # lumi lists and vetos
    if isData:
        #event.vetoPassed  = vetoList.passesVeto(r.run, r.lumi, r.evt)
        event.jsonPassed  = lumiList.contains(r.run, r.lumi)
        # make data weight zero if JSON was not passed
        if not event.jsonPassed: event.weight = 0
        # store decision to use after filler has been executed
        event.jsonPassed_ = event.jsonPassed

    if isMC:
        event.reweightPU36fb     = nTrueInt36fb_puRW       ( r.nTrueInt )
        event.reweightPU36fbDown = nTrueInt36fb_puRWDown   ( r.nTrueInt )
        event.reweightPU36fbUp   = nTrueInt36fb_puRWUp     ( r.nTrueInt )
    
    # top pt reweighting
    if isMC and options.doTopPtReweighting: 
        event.reweightTopPt = topPtReweightingFunc(getTopPtsForReweighting(r))/topScaleF if doTopPtReweighting else 1.

    # Trigger Decision
    event.triggerDecision = int(treeFormulas['triggerDecision']['TTreeFormula'].EvalInstance())

    # Leptons: Reading LepGood and LepOther and fill new LepGood collection in the output tree
    mu_selector  = muonSelector( "vloose", year = options.year)
    ele_selector = eleSelector( "vloose", year = options.year )
    leptons      = getLeptons(r, collVars=lepton_vars_read, mu_selector = mu_selector, ele_selector = ele_selector)
    leptons.sort(key = lambda p:-p['pt'])

    # add missing indices
    for lep in leptons:
        if not lep.has_key('iLepGood'):  lep['iLepGood']  = -1
        if not lep.has_key('iLepOther'): lep['iLepOther'] = -1

    # remake lepton TTV MVA 
    if options.remakeTTVLeptonMVA:
        for lep in leptons:
            lep['mvaTTV'] = mva(lep)

    # Store leptons
    event.nlep = len(leptons) 

    # Clean electrons based on loose definition, keep muons
    looseElectrons  = filter( lambda l:abs(l['pdgId'])==11, leptons)
    looseMuons      = filter( lambda l:abs(l['pdgId'])==13, leptons)
    
    eleMuOverlapIndices = []
    for m in looseMuons:
        for e in looseElectrons:
            if deltaR(m,e) < 0.05:
                eleMuOverlapIndices.append( leptons.index(e) )

    # copy deep lepton prediction from evaluator
    if options.deepLepton:
        
        # Make deepLepton prediction for all LepGood
        mu_evaluator.setEvent( r )
        ele_evaluator.setEvent( r )
        deepLepton_mu_prediction = mu_evaluator.evaluate( )
        deepLepton_ele_prediction = ele_evaluator.evaluate( )

    for iLep, lep in enumerate(leptons):
        lep['index']  = iLep     # Index wrt to the output collection!
        lep['ptCorr'] = 0.85 * lep['pt'] / lep['jetPtRatiov2']
        for lep_id in extra_lep_ids:
            lep[lep_id] = extra_mu_selector[lep_id](lep) if abs(lep['pdgId'])==13 else extra_ele_selector[lep_id](lep)
        lep['cleanEle'] = 1 if iLep not in eleMuOverlapIndices else 0
        lep['isGenPrompt'] = -1

        if isMC:
            match,prompt, matchType = getGenMatch(lep, gPart)
            lep['isGenPrompt'] = prompt

        if options.deepLepton:
            lep["deepLepton_prompt"], lep["deepLepton_nonPrompt"], lep["deepLepton_fake"] = float('nan'), float('nan'), float('nan')
            if lep.has_key("iLepGood" ):
                if deepLepton_mu_prediction.has_key(lep["iLepGood"]):
                    lep["deepLepton_prompt"], lep["deepLepton_nonPrompt"], lep["deepLepton_fake"] = deepLepton_mu_prediction[lep["iLepGood"]]
                if deepLepton_ele_prediction.has_key(lep["iLepGood"]):
                    lep["deepLepton_prompt"], lep["deepLepton_nonPrompt"], lep["deepLepton_fake"] = deepLepton_ele_prediction[lep["iLepGood"]]

        for b in lepton_vars_store:
            getattr(event, "lep_"+b)[iLep] = lep[b]

    
    # Making the various lepton collections. leptons is the loose collection and is kept.
    leptonCollections = {'loose':leptons}
    for lep_id in extra_lep_ids:
        leptonCollections[lep_id] = filter(  lambda l: (l[lep_id] and l['cleanEle']), leptons )
        setattr(event, "nLeptons_%s"%lep_id, len(leptonCollections[lep_id]))
        setattr(event, "nMuons_%s"%lep_id, len(filter( lambda l:abs(l['pdgId'])==13, leptonCollections[lep_id])))
        setattr(event, "nElectrons_%s"%lep_id, len(filter( lambda l:abs(l['pdgId'])==11, leptonCollections[lep_id])))
    
    event.nLeptons_FO_3l_genPrompt = len([ l for l in leptonCollections['FO_3l'] if l['isGenPrompt']>0 ])

    # Lepton based reweighting
    if isMC:
        for tight_id in tight_lep_ids:

            _leptonSF = leptonSF[tight_id]

            # initialize the weights with 0 to not run into problems with nan handeling in root
            setattr(event, "reweightLeptonTrackingSF_%s"%tight_id,      0)
            setattr(event, "reweightLeptonTrackingSFUp_%s"%tight_id,    0)
            setattr(event, "reweightLeptonTrackingSFDown_%s"%tight_id,  0)

            setattr(event, "reweightTrigger_%s"%tight_id,        0)
            setattr(event, "reweightTriggerUp_%s"%tight_id,      0)
            setattr(event, "reweightTriggerDown_%s"%tight_id,    0)
            
            setattr(event, "reweightLeptonSF_%s"%tight_id,      0)

            setattr(event, "reweightLeptonSFSyst_%s"%(tight_id),     0)
            setattr(event, "reweightLeptonSFSystUp_%s"%(tight_id),   0)
            setattr(event, "reweightLeptonSFSystDown_%s"%(tight_id), 0)

            for flavor in ["Ele", "Mu"]:
                setattr(event, "reweight%sSFStat_%s"%(flavor, tight_id),     0)
                setattr(event, "reweight%sSFStatUp_%s"%(flavor, tight_id),   0)
                setattr(event, "reweight%sSFStatDown_%s"%(flavor, tight_id), 0)
            
            # Calculate trigger SFs            
            if len(leptonCollections[tight_id]) > 0:
                trigg, trigg_err = triggerSF.getSF(leptonCollections[tight_id])
                setattr(event, "reweightTrigger_%s"%tight_id,        trigg)
                setattr(event, "reweightTriggerUp_%s"%tight_id,      trigg + trigg_err)
                setattr(event, "reweightTriggerDown_%s"%tight_id,    trigg - trigg_err)

                # keep the weights, can be removed in the future
                setattr(event, "reweightLeptonTrackingSF_%s"%tight_id,      reduce(mul, [leptonTrackingSF.getSF( pdgId = l['pdgId'], pt  =   l['pt'], eta =   (l['etaSc'] if abs(l['pdgId'])==11 else l['eta']), sigma=0) for l in leptonCollections[tight_id]], 1) )
                setattr(event, "reweightLeptonTrackingSFUp_%s"%tight_id,    reduce(mul, [leptonTrackingSF.getSF( pdgId = l['pdgId'], pt  =   l['pt'], eta =   (l['etaSc'] if abs(l['pdgId'])==11 else l['eta']), sigma=1) for l in leptonCollections[tight_id]], 1) )
                setattr(event, "reweightLeptonTrackingSFDown_%s"%tight_id,  reduce(mul, [leptonTrackingSF.getSF( pdgId = l['pdgId'], pt  =   l['pt'], eta =   (l['etaSc'] if abs(l['pdgId'])==11 else l['eta']), sigma=-1) for l in leptonCollections[tight_id]], 1) )

                # central value for all leptons
                setattr(event, "reweightLeptonSF_%s"%tight_id,          reduce(mul, [_leptonSF.getSF(pdgId=l['pdgId'], pt=l['pt'], eta=l['eta'] if abs(l['pdgId'])==13 else l['etaSc']) for l in leptonCollections[tight_id]], 1) )

                # variations split into syst/stat, stat split into ele/mu (uncorrelated)
                electronsTmp    = [ l for l in leptonCollections[tight_id] if abs(l['pdgId']) == 11 ]
                muonsTmp        = [ l for l in leptonCollections[tight_id] if abs(l['pdgId']) == 13 ]

                for flavor, collection in [("Ele", electronsTmp), ("Mu", muonsTmp)]:
                    centralValue = reduce(mul, [_leptonSF.getSF(pdgId=l['pdgId'], pt=l['pt'], eta=l['eta'] if abs(l['pdgId'])==13 else l['etaSc'], unc='Stat', sigma =  0) for l in collection], 1)
                    centralValue = centralValue if centralValue>0 else 1
                    setattr(event, "reweight%sSFStat_%s"%(flavor, tight_id),      1 )
                    setattr(event, "reweight%sSFStatUp_%s"%(flavor, tight_id),    reduce(mul, [_leptonSF.getSF(pdgId=l['pdgId'], pt=l['pt'], eta=l['eta'] if abs(l['pdgId'])==13 else l['etaSc'], unc='Stat', sigma = +1) for l in collection], 1)/centralValue )
                    setattr(event, "reweight%sSFStatDown_%s"%(flavor, tight_id),  reduce(mul, [_leptonSF.getSF(pdgId=l['pdgId'], pt=l['pt'], eta=l['eta'] if abs(l['pdgId'])==13 else l['etaSc'], unc='Stat', sigma = -1) for l in collection], 1)/centralValue )

                setattr(event, "reweightLeptonSFSyst_%s"%(tight_id),      reduce(mul, [_leptonSF.getSF(pdgId=l['pdgId'], pt=l['pt'], eta=l['eta'] if abs(l['pdgId'])==13 else l['etaSc'], unc='Syst', sigma =  0) for l in leptonCollections[tight_id]], 1) )
                setattr(event, "reweightLeptonSFSystUp_%s"%(tight_id),    reduce(mul, [_leptonSF.getSF(pdgId=l['pdgId'], pt=l['pt'], eta=l['eta'] if abs(l['pdgId'])==13 else l['etaSc'], unc='Syst', sigma = +1) for l in leptonCollections[tight_id]], 1) )
                setattr(event, "reweightLeptonSFSystDown_%s"%(tight_id),  reduce(mul, [_leptonSF.getSF(pdgId=l['pdgId'], pt=l['pt'], eta=l['eta'] if abs(l['pdgId'])==13 else l['etaSc'], unc='Syst', sigma = -1) for l in leptonCollections[tight_id]], 1) )


    # get variables used in 4l analysis. Only 4l collection important.
    if len(leptonCollections["tight_4l"])>1:
        minDLMass, allMasses = getMinDLMass(leptonCollections["tight_4l"])
        event.min_dl_mass = minDLMass[0]
    if len(leptonCollections["FO_3l"])>1:
        minDLMass, allMasses = getMinDLMass(leptonCollections["FO_3l"])
        event.min_dl_mass_FO_3l = minDLMass[0]
    if len(leptonCollections["loose"])>1:
        minDLMass, allMasses = getMinDLMass(leptonCollections["loose"])
        event.min_dl_mass_loose = minDLMass[0]
    event.totalLeptonCharge = sum( [ l['pdgId']/abs(l['pdgId']) for l in leptonCollections["tight_4l"] ] )


    ## Get the Z candidates and do business with them ##
    
    # We only care about (and expect) the leading one Z candidate in the 3l analysis
    (event.Z_mass, Z_l1_tightLepton_index, Z_l2_tightLepton_index) = closestOSDLMassToMZ(leptonCollections["tight_3l"])
    # If we can't find a Z candidate from the tight leptons, look at the FOs
    if not event.Z_mass>=0:
        # this is the case for the non-prompt estimation.
        # need the corrected pt here for leptons that are not tight
        leptonCollections["FO_3l_forZ"] = copy.deepcopy(leptonCollections["FO_3l"])
        for l in leptonCollections["FO_3l_forZ"]:
            if not l['tight_3l']: l['pt'] = l['ptCorr']
        (event.Z_mass, Z_l1_tightLepton_index, Z_l2_tightLepton_index) = closestOSDLMassToMZ(leptonCollections["FO_3l_forZ"])
        nonZ_tightLepton_indices = [ i for i in range(len(leptonCollections["FO_3l_forZ"])) if i not in [Z_l1_tightLepton_index, Z_l2_tightLepton_index] ]
        event.Z_l1_index    = leptonCollections["FO_3l_forZ"][Z_l1_tightLepton_index]['index'] if Z_l1_tightLepton_index>=0 else -1
        event.Z_l2_index    = leptonCollections["FO_3l_forZ"][Z_l2_tightLepton_index]['index'] if Z_l2_tightLepton_index>=0 else -1
        event.nonZ_l1_index = leptonCollections["FO_3l_forZ"][nonZ_tightLepton_indices[0]]['index'] if len(nonZ_tightLepton_indices)>0 else -1
        event.nonZ_l2_index = leptonCollections["FO_3l_forZ"][nonZ_tightLepton_indices[1]]['index'] if len(nonZ_tightLepton_indices)>1 else -1
    else:
        # this is the case for signal events
        event.Z_fromTight = 1
        nonZ_tightLepton_indices = [ i for i in range(len(leptonCollections["tight_3l"])) if i not in [Z_l1_tightLepton_index, Z_l2_tightLepton_index] ]
        event.Z_l1_index    = leptonCollections["tight_3l"][Z_l1_tightLepton_index]['index'] if Z_l1_tightLepton_index>=0 else -1
        event.Z_l2_index    = leptonCollections["tight_3l"][Z_l2_tightLepton_index]['index'] if Z_l2_tightLepton_index>=0 else -1
        event.nonZ_l1_index = leptonCollections["tight_3l"][nonZ_tightLepton_indices[0]]['index'] if len(nonZ_tightLepton_indices)>0 else -1
        event.nonZ_l2_index = leptonCollections["tight_3l"][nonZ_tightLepton_indices[1]]['index'] if len(nonZ_tightLepton_indices)>1 else -1

    # Store Z information 
    if event.Z_mass>=0:
        if leptons[event.Z_l1_index]['pdgId']*leptons[event.Z_l2_index]['pdgId']>0 or abs(leptons[event.Z_l1_index]['pdgId'])!=abs(leptons[event.Z_l2_index]['pdgId']): raise RuntimeError( "not a Z! Should never happen" )
        Z_l1 = ROOT.TLorentzVector()
        Z_l1.SetPtEtaPhiM(leptons[event.Z_l1_index]['pt'], leptons[event.Z_l1_index]['eta'], leptons[event.Z_l1_index]['phi'], 0 )
        Z_l2 = ROOT.TLorentzVector()
        Z_l2.SetPtEtaPhiM(leptons[event.Z_l2_index]['pt'], leptons[event.Z_l2_index]['eta'], leptons[event.Z_l2_index]['phi'], 0 )
        Z = Z_l1 + Z_l2
        event.Z_pt   = Z.Pt()
        event.Z_eta  = Z.Eta()
        event.Z_phi  = Z.Phi()
        event.Z_lldPhi = deltaPhi(leptons[event.Z_l1_index]['phi'], leptons[event.Z_l2_index]['phi'])
        event.Z_lldR   = deltaR(leptons[event.Z_l1_index], leptons[event.Z_l2_index])
        
        ## get the information for cos(theta*)
        # get the Z and lepton (negative charge) vectors
        lm_index = event.Z_l1_index if event.lep_pdgId[event.Z_l1_index] > 0 else event.Z_l2_index
        event.cosThetaStar = cosThetaStar(event.Z_mass, event.Z_pt, event.Z_eta, event.Z_phi, event.lep_pt[lm_index], event.lep_eta[lm_index], event.lep_phi[lm_index] )

    # For 4l, we need to get all (up to 2) Z candidates, which also can be different since the lepton ID is different
    allZCands_4l = getSortedZCandidates(leptonCollections["tight_4l"])
    Z_vectors = []
    for i in [0,1]:
        if len(allZCands_4l) > i:
            (Z_mass, Z_l1_tightLepton_index, Z_l2_tightLepton_index) = allZCands_4l[i]
            Z_l1_index_4l = leptonCollections["tight_4l"][Z_l1_tightLepton_index]['index'] if Z_l1_tightLepton_index>=0 else -1
            Z_l2_index_4l = leptonCollections["tight_4l"][Z_l2_tightLepton_index]['index'] if Z_l2_tightLepton_index>=0 else -1
            setattr(event, "Z%s_mass_4l"%(i+1),       Z_mass)
            setattr(event, "Z%s_l1_index_4l"%(i+1),   Z_l1_index_4l)
            setattr(event, "Z%s_l2_index_4l"%(i+1),   Z_l2_index_4l)
            Z_l1 = ROOT.TLorentzVector()
            Z_l1.SetPtEtaPhiM(leptons[Z_l1_index_4l]['pt'], leptons[Z_l1_index_4l]['eta'], leptons[Z_l1_index_4l]['phi'], 0 )
            Z_l2 = ROOT.TLorentzVector()
            Z_l2.SetPtEtaPhiM(leptons[Z_l2_index_4l]['pt'], leptons[Z_l2_index_4l]['eta'], leptons[Z_l2_index_4l]['phi'], 0 )
            Z = Z_l1 + Z_l2
            setattr(event, "Z%s_pt_4l"%(i+1),         Z.Pt())
            setattr(event, "Z%s_eta_4l"%(i+1),        Z.Eta())
            setattr(event, "Z%s_phi_4l"%(i+1),        Z.Phi())
            setattr(event, "Z%s_lldPhi_4l"%(i+1),     deltaPhi(Z_l1.Phi(), Z_l2.Phi()))
            lm = Z_l1 if leptons[Z_l1_index_4l]['pdgId'] > 0 else Z_l2
            setattr(event, "Z%s_cosThetaStar_4l"%(i+1),  cosThetaStar(Z_mass, Z.Pt(), Z.Eta(), Z.Phi(), lm.Pt(), lm.Eta(), lm.Phi() ))
            Z_vectors.append(Z)
    
    # also get the higgs candidate just for fun
    if len(Z_vectors)>1:
        H = Z_vectors[0] + Z_vectors[1]
        event.Higgs_mass = H.M()

    # take the leptons that are not from the leading Z candidate and assign them as nonZ, ignorant about if they actually form a Z candidate

    # As a start, take the leading two leptons as non-Z. To be overwritten as soon as we have a Z candidate, otherwise one lepton can be both from Z and non-Z
    if len(leptonCollections["tight_4l"])>0:
        event.nonZ1_l1_index_4l = leptonCollections["tight_4l"][0]['index']
    if len(leptonCollections["tight_4l"])>1:
        event.nonZ1_l2_index_4l = leptonCollections["tight_4l"][1]['index']
    if len(allZCands_4l)>0:
        # reset nonZ1_leptons
        event.nonZ1_l1_index_4l = -1
        event.nonZ1_l2_index_4l = -1
        nonZ_tightLepton_indices_4l = [ i for i in range(len(leptonCollections['tight_4l'])) if i not in [allZCands_4l[0][1], allZCands_4l[0][2]] ]

        event.nonZ1_l1_index_4l = leptonCollections["tight_4l"][nonZ_tightLepton_indices_4l[0]]['index'] if len(nonZ_tightLepton_indices_4l)>0 else -1
        event.nonZ1_l2_index_4l = leptonCollections["tight_4l"][nonZ_tightLepton_indices_4l[1]]['index'] if len(nonZ_tightLepton_indices_4l)>1 else -1

    # Now comes the cumbersome part. Do the right jet/lepton x-cleaning. Either use loose leptons (4l case), 3l_FO leptons (3l case) or SS_FO leptons (SS case).
    # We should be careful about what happens for OS DL events (stops dilepton analysis)
    if len(leptonCollections["tight_4l"]) >= 4:
        cleaningCollection = "loose"
    elif len(leptonCollections["FO_3l"]) >= 3:
        cleaningCollection = "FO_3l" # was FO
    elif len(leptonCollections["FO_SS"]) >= 2:
        cleaningCollection = "FO_SS"
    else:
        cleaningCollection = "FO_SS" # Could also do something else here

    # Jets and lepton jet cross-cleaning.
    if options.year == 2016:
        allJets      = getAllJets(r, leptonCollections[cleaningCollection], ptCut=0, jetVars = jetVarNames, absEtaCut=99, jetCollections=[ "JetAll"], idVar='id16')

    elif options.year == 2017:
        allJets      = getAllJets(r, leptonCollections[cleaningCollection], ptCut=0, jetVars = jetVarNames, absEtaCut=99, jetCollections=[ "Jet", "DiscJet"]) #JetId is required
        if options.FEBug:
            for j in allJets:
                corr_V11 = Fall17_17Nov17_V11_MC.correction(rawPt = j['rawPt'], eta = j['eta'], area = j['area'], rho = r.rho, run = r.run )
                corr_V24 = Fall17_17Nov17_V24_MC.correction(rawPt = j['rawPt'], eta = j['eta'], area = j['area'], rho = r.rho, run = r.run )
                j['pt'] *= corr_V24/corr_V11

    selected_jets, other_jets = [], []
    for j in allJets:
        idVar = 'id16' if options.year==2016 else 'id'
        if isAnalysisJet(j, ptCut=25, absEtaCut=2.4, idVar=idVar):
            selected_jets.append( j )
        else:
            other_jets.append( j )

    # Don't change analysis jets even if we keep all jets, hence, apply abs eta cut
    # Keep both b-tagging algorithms, however, DeepCSV is the new standard
    bJetsCSVv2   = filter(lambda j:isBJet(j, tagger = 'CSVv2', year = options.year) and abs(j['eta'])<=2.4, selected_jets)
    bJetsDeepCSV = filter(lambda j:isBJet(j, tagger = 'DeepCSV', year = options.year) and abs(j['eta'])<=2.4, selected_jets)
    nonBJetsCSVv2    = filter(lambda j:not ( isBJet(j, tagger = 'CSVv2', year = options.year) and abs(j['eta'])<=2.4 ), selected_jets)
    nonBJetsDeepCSV  = filter(lambda j:not ( isBJet(j, tagger = 'DeepCSV', year = options.year) and abs(j['eta'])<=2.4 ), selected_jets)

    # Store jets
    event.nJetSelected = len(selected_jets)
    jets_stored        = allJets 
    event.njet         = len(jets_stored)
    for iJet, jet in enumerate(jets_stored):
        for b in jetVarNames:
            getattr(event, "jet_"+b)[iJet] = jet[b]

    if isMC and options.doCRReweighting:
        event.reweightCR = getCRWeight(len(selected_jets))

    # ETmiss
    event.met_pt  = r.met_pt
    event.met_phi = r.met_phi

    # Analysis observables
    event.ht         = sum([j['pt'] for j in selected_jets])
    event.metSig     = event.met_pt/sqrt(event.ht) if event.ht>0 else float('nan')
    event.nBTagCSVv2 = len(bJetsCSVv2)
    event.nBTag      = len(bJetsDeepCSV)


    # Analysis Tim
#    if event.nlep == 2:
#     
#        #if leptons[0]["pdgId"]*leptons[1]["pdgId"] >= 0.: 
#        #    event.Qll = 1.0 
#        #else: 
#        #    event.Qll = -1.0  
#
#        l1 = ROOT.TLorentzVector()
#        l1.SetPtEtaPhiM(leptons[0]['pt'], leptons[0]['eta'], leptons[0]['phi'], 0 )
#        l2 = ROOT.TLorentzVector()
#        l2.SetPtEtaPhiM(leptons[1]['pt'], leptons[1]['eta'], leptons[1]['phi'], 0 )
#        ll = l1 + l2
# 
#        event.ptll = ll.Pt() 
#        event.mll = ll.M()    
#        
#        mt1 = sqrt( 2*leptons[0]["pt"]*event.met_pt*( 1 - cos( leptons[0]['phi'] - event.met_phi ) )) 
#        mt2 = sqrt( 2*leptons[1]["pt"]*event.met_pt*( 1 - cos( leptons[1]['phi'] - event.met_phi ) )) 
#        event.mt_min = min(mt1, mt2) 
#        
#        tau1 = ROOT.TLorentzVector() 
#        tau1.SetPtEtaPhiM(leptons[0]['pt']*(1+cos(event.met_phi-leptons[0]['phi'])/(leptons[0]['pt'])), leptons[0]['eta'], leptons[0]['phi'], 1.77682 )    
#        tau2 = ROOT.TLorentzVector() 
#        tau2.SetPtEtaPhiM(leptons[1]['pt']*(1+cos(event.met_phi-leptons[1]['phi'])/(leptons[1]['pt'])), leptons[1]['eta'], leptons[1]['phi'], 1.77682 )  
#        tautau = tau1 + tau2
#        event.mtautau = tautau.M() 
#
#        #event.mtautau = 2 * leptons[0]['pt'] * leptons[1]['pt'] * \
#        #                ( cosh(leptons[0]['eta']-leptons[1]['eta']) - cos(leptons[0]['phi']-leptons[1]['phi'])  ) * \
#        #                ( 1 + event.met_pt * cos(leptons[0]['phi']-event.met_phi) / leptons[0]['pt']) * \
#        #                ( 1 + event.met_pt * cos(leptons[1]['phi']-event.met_phi) / leptons[1]['pt']) + \
#        #                ( leptons[0]['mass'] * event.met_pt * cos(leptons[0]['phi']-event.met_phi) / leptons[0]['pt'] )**2 + \
#        #                ( leptons[1]['mass'] * event.met_pt * cos(leptons[1]['phi']-event.met_phi) / leptons[1]['pt'] )**2 + \
#        #                ( 2 * leptons[0]['mass']**2 * event.met_pt * cos(leptons[0]['phi']-event.met_phi) / leptons[0]['pt'] ) + \
#        #                ( 2 * leptons[1]['mass']**2 * event.met_pt * cos(leptons[1]['phi']-event.met_phi) / leptons[1]['pt'] )
#        #if event.mtautau > 0.: 
#        #    event.mtautau = sqrt(event.mtautau)
#        #else: event.mtautau = float('nan')
#        
#        met_2D = ROOT.TVector2( event.met_pt * cos(event.met_phi), event.met_pt * sin(event.met_phi) )
#        for lep in leptons:
#            if abs(lep['pdgId']) == 13:
#                lep_2D = ROOT.TVector2( lep['pt'] * cos(lep['phi']), lep['pt'] * sin(lep['phi']) )
#                met_2D += lep_2D 
#        event.met_mu_pt = met_2D.Mod()
#         
#        #event.mll2 = sqrt( 2*leptons[0]["pt"]*leptons[1]["pt"]*( cosh(leptons[0]["eta"] - leptons[1]["eta"] ) -  cos( leptons[0]['phi'] - leptons[1]['phi'] ) )) 
#        #event.ptll2 = sqrt( (leptons[0]['pt'])**2 + (leptons[1]['pt'])**2 + 2 * leptons[0]['pt']  * leptons[1]['pt']  * cos( leptons[0]["phi"] - leptons[1]["phi"] ) )
#    else: 
#        event.Qll = float('nan')
#        event.mll = float('nan') 
#        event.ptll = float('nan')
#        event.mtautau = float('nan')
#        event.mt_min = float('nan')
#        event.met_mu_pt = float('nan')


    #  sync info
    sync.print_met( r.met_pt, r.met_phi ) 
    sync.print_leptons( leptons )
    sync.print_jets( selected_jets )
    logger.sync( "Summary: tight_SS mu %i tight_SS ele %i njets %i nbtags %i",  event.nMuons_tight_SS, event.nElectrons_tight_SS, event.nJetSelected, event.nBTag)
    logger.sync( "#"*30 )

    # Systematics
    jets_sys      = {}
    bjets_sys     = {}
    nonBjets_sys  = {}

    metVariants = [''] # default

    if options.keepPhotons:
        # Keep photons and estimate met including (leading pt) photon
        photons = getGoodPhotons(r, ptCut=20, idLevel="loose", isData=isData)
        event.nPhotonGood = len(photons)
        if event.nPhotonGood > 0:
          metVariants += ['_photonEstimated']  # do all met calculations also for the photonEstimated variant
          event.photon_pt         = photons[0]['pt']
          event.photon_eta        = photons[0]['eta']
          event.photon_phi        = photons[0]['phi']
          event.photon_idCutBased = photons[0]['idCutBased']
          if isMC:
            genPhoton           = getGenPhoton(gPart)
            event.photon_genPt  = genPhoton['pt']  if genPhoton is not None else float('nan')
            event.photon_genEta = genPhoton['eta'] if genPhoton is not None else float('nan')

          event.met_pt_photonEstimated, event.met_phi_photonEstimated = getMetPhotonEstimated(r.met_pt, r.met_phi, photons[0])
          event.metSig_photonEstimated = event.met_pt_photonEstimated/sqrt(event.ht) if event.ht>0 else float('nan')

          event.photonJetdR = min(deltaR(photons[0], j) for j in selected_jets) if len(selected_jets) > 0 else 999
          event.photonLepdR = min(deltaR(photons[0], l) for l in leptons) if len(leptons) > 0 else 999

        if isMC:
           event.TTGJetsEventType = getTTGJetsEventType(r)

    if isMC:
        event.PSweight_central      = r.LHEweight_wgt[1080]

        event.PSweight_red_isrUp    = r.LHEweight_wgt[1082]
        event.PSweight_red_fsrUp    = r.LHEweight_wgt[1083]
        event.PSweight_red_isrDown  = r.LHEweight_wgt[1084]
        event.PSweight_red_fsrDown  = r.LHEweight_wgt[1085]

        event.PSweight_nom_isrUp    = r.LHEweight_wgt[1086]
        event.PSweight_nom_fsrUp    = r.LHEweight_wgt[1087]
        event.PSweight_nom_isrDown  = r.LHEweight_wgt[1088]
        event.PSweight_nom_fsrDown  = r.LHEweight_wgt[1089]

        event.PSweight_cons_isrUp    = r.LHEweight_wgt[1090]
        event.PSweight_cons_fsrUp    = r.LHEweight_wgt[1091]
        event.PSweight_cons_isrDown  = r.LHEweight_wgt[1092]
        event.PSweight_cons_fsrDown  = r.LHEweight_wgt[1093]

    if addSystematicVariations:
        for j in allJets:
            j['pt_JECUp']   =j['pt']/j['corr']*j['corr_JECUp']
            j['pt_JECDown'] =j['pt']/j['corr']*j['corr_JECDown']
            # JERUp, JERDown, JER
            addJERScaling(j)
        for var in ['JECUp', 'JECDown', 'JERUp', 'JERDown']:
            jets_sys[var]       = filter(lambda j: isAnalysisJet(j, ptCut=30, absEtaCut=2.4, ptVar='pt_'+var), allJets)
            bjets_sys[var]      = filter(lambda j: isBJet(j, tagger = 'DeepCSV', year = options.year) and abs(j['eta'])<2.4, jets_sys[var])
            nonBjets_sys[var]   = filter(lambda j: not ( isBJet(j, tagger = 'DeepCSV', year = options.year) and abs(j['eta'])<2.4), jets_sys[var])

            setattr(event, "nJetSelected_"+var, len(jets_sys[var]))
            setattr(event, "ht_"+var,       sum([j['pt_'+var] for j in jets_sys[var]]))
            setattr(event, "nBTag_"+var,    len(bjets_sys[var]))

        for var in ['JECUp', 'JECDown', 'JERUp', 'JERDown', 'UnclusteredEnUp', 'UnclusteredEnDown']:
            for i in metVariants:
                # use cmg MET correction values ecept for JER where it is zero. There, propagate jet variations.
                if 'JER' in var or 'JECV' in var:
                  (met_corr_pt, met_corr_phi) = getMetJetCorrected(getattr(event, "met_pt" + i), getattr(event,"met_phi" + i), jets_sys[var], var)
                else:
                  (met_corr_pt, met_corr_phi) = getMetCorrected(r, var, photons[0] if i.count("photonEstimated") else None)

                setattr(event, "met_pt" +i+"_"+var, met_corr_pt)
                setattr(event, "met_phi"+i+"_"+var, met_corr_phi)
                ht = getattr(event, "ht_"+var) if 'Unclustered' not in var else event.ht 
                setattr(event, "metSig" +i+"_"+var, getattr(event, "met_pt"+i+"_"+var)/sqrt( ht ) if ht>0 else float('nan') )

    if addSystematicVariations:

        # B tagging weights method 1a, first for CSVv2
        for j in selected_jets:
            btagEff_CSVv2.addBTagEffToJet(j)
        #print "CSVv2", selected_jets[0]['beff']['SF'], selected_jets[0]['pt']
        for var in btagEff_CSVv2.btagWeightNames:
            if var!='MC':
                setattr(event, 'reweightBTagCSVv2_'+var, btagEff_CSVv2.getBTagSF_1a( var, bJetsCSVv2, filter( lambda j: abs(j['eta'])<2.4, nonBJetsCSVv2 ) ) )

        # B tagging weights method 1a, now for DeepCSV
        for j in selected_jets:
            btagEff_DeepCSV.addBTagEffToJet(j)
        #print "DeepCSV", selected_jets[0]['beff']['SF'], selected_jets[0]['pt']
        for var in btagEff_DeepCSV.btagWeightNames:
            if var!='MC':
                setattr(event, 'reweightBTagDeepCSV_'+var, btagEff_DeepCSV.getBTagSF_1a( var, bJetsDeepCSV, filter( lambda j: abs(j['eta'])<2.4, nonBJetsDeepCSV ) ) )
    
    
    # dilepton stop variables calculated from tight leptons. 
    for i in metVariants:
        mt2Calc.reset()
        if len(leptonCollections["tight_3l"])>1:
            l1 = ROOT.TLorentzVector()
            l2 = ROOT.TLorentzVector()
            l1.SetPtEtaPhiM(leptonCollections["tight_3l"][0]['pt'], leptonCollections["tight_3l"][0]['eta'], leptonCollections["tight_3l"][0]['phi'], 0 )
            l2.SetPtEtaPhiM(leptonCollections["tight_3l"][1]['pt'], leptonCollections["tight_3l"][1]['eta'], leptonCollections["tight_3l"][1]['phi'], 0 )
            dl = l1+l2
            event.dl_pt   = dl.Pt()
            event.dl_eta  = dl.Eta()
            event.dl_phi  = dl.Phi()
            event.dl_mass = dl.M()
            mt2Calc.setLeptons(l1.Pt(), l1.Eta(), l1.Phi(), l2.Pt(), l2.Eta(), l2.Phi())
            mt2Calc.setMet(getattr(event, 'met_pt'+i), getattr(event, 'met_phi'+i))
            setattr(event, "dl_mt2ll"+i, mt2Calc.mt2ll())

            bj0, bj1 = None, None
            if len(selected_jets)>=2:
                bj0, bj1 = (bJetsDeepCSV+nonBJetsDeepCSV)[:2]
                mt2Calc.setBJets(bj0['pt'], bj0['eta'], bj0['phi'], bj1['pt'], bj1['eta'], bj1['phi'])
                setattr(event, "dl_mt2bb"+i,   mt2Calc.mt2bb())
                setattr(event, "dl_mt2blbl"+i, mt2Calc.mt2blbl())

            if addSystematicVariations:
                for var in ['JECUp', 'JECDown', 'JERUp', 'JERDown', 'UnclusteredEnUp', 'UnclusteredEnDown']:
                    mt2Calc.setMet( getattr(event, "met_pt"+i+"_"+var), getattr(event, "met_phi"+i+"_"+var) )
                    setattr(event, "dl_mt2ll"+i+"_"+var,  mt2Calc.mt2ll())
                    if not 'Unclustered' in var:
                        if len(jets_sys[var])>=2:
                            bj0_, bj1_ = (bjets_sys[var]+nonBjets_sys[var])[:2]
                        else:
                            bj0_, bj1_ = None, None
                    else:
                        bj0_, bj1_ = bj0, bj1
                    if bj0_ and bj1_:
                        mt2Calc.setBJets(bj0_['pt'], bj0_['eta'], bj0_['phi'], bj1_['pt'], bj1_['eta'], bj1_['phi'])
                        setattr(event, 'dl_mt2bb'  +i+'_'+var, mt2Calc.mt2bb())
                        setattr(event, 'dl_mt2blbl'+i+'_'+var, mt2Calc.mt2blbl())

    # gen information on extra leptons
    if isMC and not options.skipGenMatching:
        genSearch.init( gPart )
        # Start with status 1 gen leptons

        # gLep = filter( lambda p:abs(p['pdgId']) in [11, 13] and p['status']==1 and p['pt']>10 and abs(p['eta'])<2.5, gPart )
        # ... no acceptance cuts
        gLep = filter( lambda p:abs(p['pdgId']) in [11, 13] and p['status']==1, gPart )
        for l in gLep:
            ancestry = [ gPart[x]['pdgId'] for x in genSearch.ancestry( l ) ]
            l["n_D"]   =  sum([ancestry.count(p) for p in D_mesons])
            l["n_B"]   =  sum([ancestry.count(p) for p in B_mesons])
            l["n_W"]   =  sum([ancestry.count(p) for p in [24, -24]])
            l["n_t"]   =  sum([ancestry.count(p) for p in [6, -6]])
            l["n_tau"] =  sum([ancestry.count(p) for p in [15, -15]])
            matched_lep = bestDRMatchInCollection(l, leptons) 
            if matched_lep:
                l["lepGood2MatchIndex"] = matched_lep['index']
            else:
                l["lepGood2MatchIndex"] = -1

        # store genleps
        event.nGenLep   = len(gLep)
        for iLep, lep in enumerate(gLep):
            for b in genLepVarNames:
                getattr(event, "GenLep_"+b)[iLep] = lep[b]

        # gen Z
        genZs = filter( lambda p: (abs(p['pdgId'])==23 and genSearch.isLast(p)), gPart )
        genZs.sort( key = lambda p: -p['pt'] )
        if len( genZs )>0:
            genZ = genZs[0]
            event.genZ_pt  = genZ['pt'] 
            event.genZ_mass= genZ['mass']
            event.genZ_eta = genZ['eta']
            event.genZ_phi = genZ['phi']

            lep_m = filter( lambda p: p['pdgId'] in [11, 13, 15], genSearch.daughters( genZ ) )
            event.genZ_daughter_flavor = max([p['pdgId'] for p in genSearch.daughters( genZ )])
            if len( lep_m ) == 1:
                event.genZ_cosThetaStar = cosThetaStar( event.genZ_mass, event.genZ_pt, event.genZ_eta, event.genZ_phi, lep_m[0]['pt'], lep_m[0]['eta'], lep_m[0]['phi'] )
    
# Create a maker. Maker class will be compiled. This instance will be used as a parent in the loop
treeMaker_parent = TreeMaker(
    sequence  = [ filler ],
    variables = [ TreeVariable.fromString(x) for x in new_variables ],
    treeName = "Events"
    )

# Split input in ranges
if options.nJobs>1 and not options.fileBasedSplitting:
    eventRanges = reader.getEventRanges( nJobs = options.nJobs )
else:
    eventRanges = reader.getEventRanges( maxNEvents = options.eventsPerJob, minJobs = options.minNJobs )

logger.info( "Splitting into %i ranges of %i events on average. FileBasedSplitting: %s. Job number %s",  
        len(eventRanges), 
        (eventRanges[-1][1] - eventRanges[0][0])/len(eventRanges), 
        'Yes' if options.fileBasedSplitting else 'No',
        options.job)

#Define all jobs
jobs = [(i, eventRanges[i]) for i in range(len(eventRanges))]

filename, ext = os.path.splitext( os.path.join(output_directory, sample.name + '.root') )

if options.fileBasedSplitting and len(eventRanges)>1:
    raise RuntimeError("Using fileBasedSplitting but have more than one event range!")

clonedEvents = 0
convertedEvents = 0
outputLumiList = {}
for ievtRange, eventRange in enumerate( eventRanges ):

    
    if not options.fileBasedSplitting and options.nJobs>1:
        if ievtRange != options.job: continue

    logger.info( "Processing range %i/%i from %i to %i which are %i events.",  ievtRange, len(eventRanges), eventRange[0], eventRange[1], eventRange[1]-eventRange[0] )

    # Check whether file exists
    fileNumber = options.job if options.job is not None else 0
    outfilename = filename+'_'+str(fileNumber)+ext
    if os.path.isfile(outfilename):
        logger.info( "Output file %s found.", outfilename)
        if not checkRootFile(outfilename, checkForObjects=["Events"]):
            logger.info( "File %s is broken. Overwriting.", outfilename)
        elif not options.overwrite:
            logger.info( "Skipping.")
            continue
        else:
            logger.info( "Overwriting.")

    tmp_directory = ROOT.gDirectory
    outputfile = ROOT.TFile.Open(outfilename, 'recreate')
    tmp_directory.cd()

    if options.small: 
        logger.info("Running 'small'. Not more than 10000 events") 
        nMaxEvents = eventRange[1]-eventRange[0]
        eventRange = ( eventRange[0], eventRange[0] +  min( [nMaxEvents, 10000] ) )

    # Set the reader to the event range
    reader.setEventRange( eventRange )

    # Clone the empty maker in order to avoid recompilation at every loop iteration
    clonedTree = reader.cloneTree( branchKeepStrings, newTreename = "Events", rootfile = outputfile )
    clonedEvents += clonedTree.GetEntries()
    # Add the TTreeFormulas
    for formula in treeFormulas.keys():
        treeFormulas[formula]['TTreeFormula'] = ROOT.TTreeFormula(formula, treeFormulas[formula]['string'], clonedTree )

    maker = treeMaker_parent.cloneWithoutCompile( externalTree = clonedTree )

    maker.start()
    # Do the thing
    reader.start()

    while reader.run():
        maker.run()
        if isData:
            if maker.event.jsonPassed_:
                if reader.event.run not in outputLumiList.keys():
                    outputLumiList[reader.event.run] = set([reader.event.lumi])
                else:
                    if reader.event.lumi not in outputLumiList[reader.event.run]:
                        outputLumiList[reader.event.run].add(reader.event.lumi)

    convertedEvents += maker.tree.GetEntries()
    maker.tree.Write()
    outputfile.Close()
    logger.info( "Written %s", outfilename)

  # Destroy the TTree
    maker.clear()
    
logger.info( "Converted %i events of %i, cloned %i",  convertedEvents, reader.nEvents , clonedEvents )

# Storing JSON file of processed events
if isData:
    jsonFile = filename+'_%s.json'%(0 if options.nJobs==1 else options.job)
    LumiList( runsAndLumis = outputLumiList ).writeJSON(jsonFile)
    logger.info( "Written JSON file %s",  jsonFile )

logger.info("Copying log file to %s", output_directory )
copyLog = subprocess.call(['cp', logFile, output_directory] )
if copyLog:
    logger.info( "Copying log from %s to %s failed", logFile, output_directory)
else:
    logger.info( "Successfully copied log file" )
    os.remove(logFile)
    logger.info( "Removed temporary log file" )

if writeToDPM:
    for dirname, subdirs, files in os.walk( directory ):
        logger.debug( 'Found directory: %s',  dirname )
        for fname in files:
            source = os.path.abspath(os.path.join(dirname, fname))
            postfix = '_small' if options.small else ''
            cmd = ['xrdcp', source, 'root://hephyse.oeaw.ac.at/%s' % os.path.join( user_dpm_directory, 'postprocessed',  options.processingEra+postfix, options.skim, sample.name, fname ) ]
            logger.info( "Issue copy command: %s", " ".join( cmd ) )
            subprocess.call( cmd )

    # Clean up.
    subprocess.call( [ 'rm', '-rf', directory ] ) # Let's risk it.

#if options.deepLepton and options.theano:
#    del deepLeptonModel
#    del evaluator
#    if os.path.exists( theano_compile_dir ):
#        logger.info( "Removing theano compile directory %s", theano_compile_dir )
#        shutil.rmtree( theano_compile_dir )
