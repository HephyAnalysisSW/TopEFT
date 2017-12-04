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

from array import array
from operator import mul
from math import sqrt, atan2, sin, cos, cosh

# RootTools
from RootTools.core.standard import *

# User specific
import TopEFT.tools.user as user

# Tools for systematics
from TopEFT.tools.helpers                    import closestOSDLMassToMZ, checkRootFile, writeObjToFile, deltaR, bestDRMatchInCollection, deltaPhi, mZ, cosThetaStar
from TopEFT.tools.addJERScaling              import addJERScaling
from TopEFT.tools.objectSelection            import getMuons, getElectrons, muonSelector, eleSelector, getGoodLeptons, getGoodAndOtherLeptons, lepton_branches_data, lepton_branches_mc
from TopEFT.tools.objectSelection            import getGoodBJets, getGoodJets, isBJet, isAnalysisJet, getGoodPhotons, getGenPartsAll, getAllJets
from TopEFT.tools.overlapRemovalTTG          import getTTGJetsEventType
from TopEFT.tools.getGenBoson                import getGenZ, getGenPhoton
#from TopEFT.tools.triggerEfficiency          import triggerEfficiency
#from TopEFT.tools.leptonTrackingEfficiency   import leptonTrackingEfficiency

#triggerEff_withBackup   = triggerEfficiency(with_backup_triggers = True)
#triggerEff              = triggerEfficiency(with_backup_triggers = False)
#leptonTrackingSF        = leptonTrackingEfficiency()

#MC tools
from TopEFT.tools.mcTools import GenSearch, B_mesons, D_mesons, B_mesons_abs, D_mesons_abs
genSearch = GenSearch()

# central configuration
targetLumi = 1000 #pb-1 Which lumi to normalize to

logChoices      = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']
triggerChoices  = ['mumu', 'ee', 'mue', 'mu', 'e', 'e_for_mu']

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--logLevel',                    action='store',         nargs='?',              choices=logChoices,     default='INFO',                     help="Log level for logging")
    argParser.add_argument('--overwrite',                   action='store_true',                                                                                        help="Overwrite existing output files, bool flag set to True  if used")
    argParser.add_argument('--samples',                     action='store',         nargs='*',  type=str,                           default=['WZTo3LNu_amcatnlo'],      help="List of samples to be post-processed, given as CMG component name")
    argParser.add_argument('--triggerSelection',            action='store',         nargs='?',  type=str,   choices=triggerChoices, default=None,                       help="Trigger selection?")
    argParser.add_argument('--eventsPerJob',                action='store',         nargs='?',  type=int,                           default=300000,                     help="Maximum number of events per job (Approximate!).")
    argParser.add_argument('--nJobs',                       action='store',         nargs='?',  type=int,                           default=1,                          help="Maximum number of simultaneous jobs.")
    argParser.add_argument('--job',                         action='store',         nargs='*',  type=int,                           default=[],                         help="Run only job i")
    argParser.add_argument('--minNJobs',                    action='store',         nargs='?',  type=int,                           default=1,                          help="Minimum number of simultaneous jobs.")
    argParser.add_argument('--dataDir',                     action='store',         nargs='?',  type=str,                           default="/a/b/c",                   help="Name of the directory where the input data is stored (for samples read from Heppy).")
    argParser.add_argument('--targetDir',                   action='store',         nargs='?',  type=str,                           default=user.postprocessing_output_directory, help="Name of the directory the post-processed files will be saved")
    argParser.add_argument('--processingEra',               action='store',         nargs='?',  type=str,                           default='TopEFT_PP_v4',             help="Name of the processing era")
    argParser.add_argument('--skim',                        action='store',         nargs='?',  type=str,                           default='dilepTiny',                help="Skim conditions to be applied for post-processing")
    argParser.add_argument('--LHEHTCut',                    action='store',         nargs='?',  type=int,                           default=-1,                         help="LHE cut.")
    argParser.add_argument('--keepAllJets',                 action='store_true',                                                                                        help="Keep all jets?")
    argParser.add_argument('--small',                       action='store_true',                                                                                        help="Run the file on a small sample (for test purpose), bool flag set to True if used")
    argParser.add_argument('--leptonConvinience',           action='store_true',                                                                                        help="Store l1_pt, l1_eta, ... l4_xyz?")
    argParser.add_argument('--skipGenMatching',          action='store_true',                                                                                        help="skip matched genleps??")
    argParser.add_argument('--keepLHEWeights',              action='store_true',                                                                                        help="Keep LHEWeights?")
    argParser.add_argument('--keepPhotons',                 action='store_true',                                                                                        help="Keep photon information?")
    argParser.add_argument('--skipSystematicVariations',    action='store_true',                                                                                        help="Don't calulcate BTag, JES and JER variations.")
    argParser.add_argument('--doTopPtReweighting',          action='store_true',                                                                                        help="Top pt reweighting?")

    return argParser

options = get_parser().parse_args()

# Logging
import TopEFT.tools.logger as logger
logFile = '/tmp/%s_%s_%s_njob%s.txt'%(options.skim, '_'.join(options.samples), os.environ['USER'], str(0 if options.nJobs==1 else options.job[0]))
logger  = logger.get_logger(options.logLevel, logFile = logFile)

import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None )

# Flags 
isDiLep     =   options.skim.lower().startswith('dilep')
isTriLep    =   options.skim.lower().startswith('trilep')
isSingleLep =   options.skim.lower().startswith('singlelep')
isInclusive = options.skim.lower().count('inclusive') 
isTiny      =   options.skim.lower().count('tiny') 

writeToDPM = options.targetDir == '/dpm/'

# Skim condition
skimConds = []
if isDiLep:
    skimConds.append( "Sum$(LepGood_pt>10&&abs(LepGood_eta)<2.5) + Sum$(LepOther_pt>10&&abs(LepOther_eta)<2.5)>=2" )
if isTriLep:
    skimConds.append( "Sum$(LepGood_pt>10&&abs(LepGood_eta)&&LepGood_relIso03<0.4) + Sum$(LepOther_pt>10&&abs(LepOther_eta)<2.5&&LepOther_relIso03<0.4)>=2 && Sum$(LepOther_pt>10&&abs(LepOther_eta)<2.5)+Sum$(LepGood_pt>10&&abs(LepGood_eta)<2.5)>=3" )
if isSingleLep:
    skimConds.append( "Sum$(LepGood_pt>20&&abs(LepGood_eta)<2.5) + Sum$(LepOther_pt>20&&abs(LepOther_eta)<2.5)>=1" )
if isInclusive:
    skimConds = []

maxN = 2 if options.small else None
from TopEFT.samples.helpers import fromHeppySample
samples = [ fromHeppySample(s, data_path = options.dataDir, maxN = maxN) for s in options.samples ]
logger.debug("Reading from CMG tuples: %s", ",".join(",".join(s.files) for s in samples) )
    
if len(samples)==0:
    logger.info( "No samples found. Was looking for %s. Exiting" % options.samples )
    sys.exit(-1)

isData = False not in [s.isData for s in samples]
isMC   =  True not in [s.isData for s in samples]

# Check that all samples which are concatenated have the same x-section.
assert isData or len(set([s.heppy.xSection for s in samples]))==1, "Not all samples have the same xSection: %s !"%(",".join([s.name for s in samples]))
assert isMC or len(samples)==1, "Don't concatenate data samples"

xSection = samples[0].heppy.xSection if isMC else None

diMuTriggers        = ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ"," HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ"]
diEleTriggers       = ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"]
EMuTriggers         = ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL", "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ"]

if isData and options.triggerSelection is not None:
    if options.triggerSelection == 'mu':
        skimConds.append( "(HLT_SingleMuTTZ)" )
    elif options.triggerSelection == 'e':
        skimConds.append( "(HLT_SingleEleTTZ)" )
    elif options.triggerSelection == 'e_for_mu':
        skimConds.append( "(HLT_SingleEleTTZ && !HLT_SingleMuTTZ)" )
    elif options.triggerSelection == 'ee':
        skimConds.append( "(%s)&&!(HLT_SingleMuTTZ||HLT_SingleEleTTZ)"%"||".join(diEleTriggers) )
    elif options.triggerSelection == 'mue':
        skimConds.append( "(%s)&&!(HLT_SingleMuTTZ||HLT_SingleEleTTZ)"%"||".join(EMuTriggers) )
    elif options.triggerSelection == 'mumu':
        skimConds.append( "(%s)&&!(HLT_SingleMuTTZ||HLT_SingleEleTTZ)"%"||".join(diMuTriggers) )
    else:
        raise ValueError( "Don't know about triggerSelection %s"%options.triggerSelection )
    sample_name_postFix = "_Trig_"+options.triggerSelection
    logger.info( "Added trigger selection %s and postFix %s", options.triggerSelection, sample_name_postFix )
else:
    sample_name_postFix = ""

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
    sample.name+=sample_name_postFix
else:
    raise ValueError( "Need at least one sample. Got %r",samples )

if isMC:
    from TopEFT.tools.puReweighting import getReweightingFunction
    mcProfile = "Summer16"
    # nTrueIntReweighting
    nTrueInt36fb_puRW        = getReweightingFunction(data="PU_2016_36000_XSecCentral", mc=mcProfile)
    nTrueInt36fb_puRWDown    = getReweightingFunction(data="PU_2016_36000_XSecDown",    mc=mcProfile)
    nTrueInt36fb_puRWUp      = getReweightingFunction(data="PU_2016_36000_XSecUp",      mc=mcProfile)
        
# top pt reweighting
# Decision based on sample name -> whether TTJets or TTLep is in the sample name
isTT = sample.name.startswith("TTJets") or sample.name.startswith("TTLep") or sample.name.startswith("TT_pow")
doTopPtReweighting = isTT and options.doTopPtReweighting
if doTopPtReweighting:

    from TopEFT.tools.topPtReweighting import getUnscaledTopPairPtReweightungFunction, getTopPtDrawString, getTopPtsForReweighting

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

# systematic variations
addSystematicVariations = (not isData) and (not options.skipSystematicVariations)
if addSystematicVariations:
    # B tagging SF
    from TopEFT.tools.btagEfficiency import btagEfficiency
    
    # CSVv2
    effFile         = '$CMSSW_BASE/src/TopEFT/tools/data/btagEfficiencyData/TTLep_pow_Moriond17_2j_2l_CSVv2_eta.pkl'
    sfFile          = '$CMSSW_BASE/src/TopEFT/tools/data/btagEfficiencyData/CSVv2_Moriond17_B_H.csv'
    btagEff_CSVv2   = btagEfficiency( effFile = effFile, sfFile = sfFile, fastSim = False )

    # DeepCSV
    effFile         = '$CMSSW_BASE/src/TopEFT/tools/data/btagEfficiencyData/TTLep_pow_Moriond17_2j_2l_deepCSV_eta.pkl'
    sfFile          = '$CMSSW_BASE/src/TopEFT/tools/data/btagEfficiencyData/DeepCSV_Moriond17_B_H.csv'
    btagEff_DeepCSV = btagEfficiency( effFile = effFile, sfFile = sfFile, fastSim = False )

# LHE cut (DY samples)
if options.LHEHTCut>0:
    sample.name+="_lheHT"+str(options.LHEHTCut)
    logger.info( "Adding upper LHE cut at %f", options.LHEHTCut )
    skimConds.append( "lheHTIncoming<%f"%options.LHEHTCut )

# output directory (store temporarily when running on dpm)
if writeToDPM:
    import uuid
    # Allow parallel processing of N threads on one worker
    directory = os.path.join('/tmp/%s'%os.environ['USER'], str(uuid.uuid4()), options.processingEra)
    if not os.path.exists( directory ):
        os.makedirs( directory )
    from TopEFT.tools.user import dpm_directory as user_dpm_directory
else:
    directory  = os.path.join(options.targetDir, options.processingEra) 

postfix = '_small' if options.small else ''
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

# Jet variables to be read from chain
jetCorrInfo = ['corr/F', 'corr_JECUp/F', 'corr_JECDown/F'] if addSystematicVariations else []
if isMC:
    if isTiny:
        jetMCInfo = ['mcPt/F', 'hadronFlavour/I', 'mcMatchId/I']
    else:
        jetMCInfo = ['mcMatchFlav/I', 'partonId/I', 'partonMotherId/I', 'mcPt/F', 'mcFlavour/I', 'hadronFlavour/I', 'mcMatchId/I', 'partonFlavour/I']
else:
    jetMCInfo = []

if sample.isData:
    lumiScaleFactor=None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_DATA
    from FWCore.PythonUtilities.LumiList import LumiList
    # Apply golden JSON
    sample.heppy.json = '$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
    #if is2017:
    #    sample.heppy.json = '$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_294927-306126_13TeV_PromptReco_Collisions17_JSON.txt'
    lumiList = LumiList(os.path.expandvars(sample.heppy.json))
    logger.info( "Loaded json %s", sample.heppy.json )
else:
    lumiScaleFactor = xSection*targetLumi/float(sample.normalization) if xSection is not None else None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_MC

jetVars = ['pt/F', 'rawPt/F', 'eta/F', 'phi/F', 'id/I', 'btagCSV/F', 'area/F', 'DFb/F', 'DFbb/F'] + jetCorrInfo + jetMCInfo
jetVarNames = [x.split('/')[0] for x in jetVars]
genLepVars      = ['pt/F', 'phi/F', 'eta/F', 'pdgId/I', 'index/I', 'lepGood2MatchIndex/I', 'n_t/I','n_W/I', 'n_B/I', 'n_D/I', 'n_tau/I']
genLepVarNames  = [x.split('/')[0] for x in genLepVars]

read_variables = map(TreeVariable.fromString, ['met_pt/F', 'met_phi/F', 'run/I', 'lumi/I', 'evt/l', 'nVert/I'] )
if options.keepPhotons:
    read_variables += [ TreeVariable.fromString('ngamma/I'),
                        VectorTreeVariable.fromString('gamma[pt/F,eta/F,phi/F,mass/F,idCutBased/I,pdgId/I]') ]

new_variables = [ 'weight/F']
new_variables+= [ 'jet[%s]'% ( ','.join(jetVars) ) ]

lepton_branches_store = lepton_branches_mc if isMC else lepton_branches_data
lepton_branches_store += ',relIso/F'
lepton_vars_store     = [s.split('/')[0] for s in lepton_branches_store.split(',')]
new_variables+= [ 'lep[%s]' % lepton_branches_store ]

if isMC:
    read_variables+= [TreeVariable.fromString('nTrueInt/F')]
    # reading gen particles for top pt reweighting
    read_variables.append( TreeVariable.fromString('ngenPartAll/I') )
    read_variables.append( VectorTreeVariable.fromString('genPartAll[pt/F,eta/F,phi/F,mass/F,pdgId/I,status/I,charge/I,motherId/I,grandmotherId/I,nMothers/I,motherIndex1/I,motherIndex2/I,nDaughters/I,daughterIndex1/I,daughterIndex2/I,isPromptHard/I]', nMax=200 )) # default nMax is 100, which would lead to corrupt values in this case
    read_variables.append( TreeVariable.fromString('genWeight/F') )
    read_variables.append( TreeVariable.fromString('nIsr/I') )
    if options.keepPhotons:
        read_variables.append( VectorTreeVariable.fromString('gamma[mcPt/F]') )

    if options.doTopPtReweighting: 
        new_variables.append('reweightTopPt/F')

    new_variables.extend(['reweightPU36fb/F','reweightPU36fbUp/F','reweightPU36fbDown/F'])

    if not options.skipGenMatching:
        TreeVariable.fromString( 'nGenLep/I' ),
        new_variables.append( 'GenLep[%s]'% ( ','.join(genLepVars) ) )
        new_variables.extend(['genZ_pt/F', 'genZ_mass/F', 'genZ_eta/F', 'genZ_phi/F', 'genZ_cosThetaStar/F' ])

read_variables += [\
    TreeVariable.fromString('nLepGood/I'),
    TreeVariable.fromString('nLepOther/I'),
    VectorTreeVariable.fromString('LepGood[%s]'  % (lepton_branches_mc if isMC else lepton_branches_data)),
    VectorTreeVariable.fromString('LepOther[%s]' % (lepton_branches_mc if isMC else lepton_branches_data)),

    TreeVariable.fromString('nJet/I'),
    TreeVariable.fromString('nDiscJet/I'),
    VectorTreeVariable.fromString('Jet[%s]'% ( ','.join(jetVars) ) ),
    VectorTreeVariable.fromString('DiscJet[%s]'% ( ','.join(jetVars) ) )
]

if isData: new_variables.extend( ['jsonPassed/I'] )
new_variables.extend( ['nBTag/I', 'nBTagDeepCSV/I', 'ht/F', 'metSig/F', 'nJetSelected/I'] )

if options.leptonConvinience:
    lep_convinience_branches = ['l{n}_pt/F', 'l{n}_eta/F', 'l{n}_phi/F', 'l{n}_pdgId/I', 'l{n}_index/I', 'l{n}_miniRelIso/F', 'l{n}_relIso/F', 'l{n}_dxy/F', 'l{n}_dz/F' ]
    if isMC: lep_convinience_branches.extend(['l{n}_mcMatchId/I', 'l{n}_mcMatchAny/I'])
    lep_convinience_vars     = [s.split('_')[1].split('/')[0] for s in lep_convinience_branches ]
    for i in range(1,5):
        new_variables.extend( [var.format(n=i) for var in lep_convinience_branches] )

new_variables.extend( ['nGoodElectrons/I','nGoodMuons/I','nGoodLeptons/I' ] )


# Z related observables
new_variables.extend( ['Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I', 'nonZ_l2_index/I'] )
new_variables.extend( ['Z_pt/F', 'Z_eta/F', 'Z_phi/F', 'Z_lldPhi/F', 'Z_lldR/F',  'Z_mass/F', 'cosThetaStar/F'] )

if options.keepPhotons: 
    new_variables.extend( ['nPhotonGood/I','photon_pt/F','photon_eta/F','photon_phi/F','photon_idCutBased/I'] )
    if isMC: new_variables.extend( ['photon_genPt/F', 'photon_genEta/F'] )
    new_variables.extend( ['met_pt_photonEstimated/F','met_phi_photonEstimated/F','metSig_photonEstimated/F'] )
    new_variables.extend( ['photonJetdR/F','photonLepdR/F'] )
    new_variables.extend( ['TTGJetsEventType/I'] )

if addSystematicVariations:
    read_variables += map(TreeVariable.fromString, [\
    "met_JetEnUp_Pt/F", "met_JetEnUp_Phi/F", "met_JetEnDown_Pt/F", "met_JetEnDown_Phi/F", "met_JetResUp_Pt/F", "met_JetResUp_Phi/F", "met_JetResDown_Pt/F", "met_JetResDown_Phi/F", 
    "met_UnclusteredEnUp_Pt/F", "met_UnclusteredEnUp_Phi/F", "met_UnclusteredEnDown_Pt/F", "met_UnclusteredEnDown_Phi/F", 
    ] )

    for var in ['JECUp', 'JECDown', 'JERUp', 'JERDown', 'UnclusteredEnUp', 'UnclusteredEnDown']:
        if 'Unclustered' not in var: new_variables.extend( ['nJetSelected_'+var+'/I', 'nBTag_'+var+'/I','ht_'+var+'/F'] )
        new_variables.extend( ['met_pt_'+var+'/F', 'met_phi_'+var+'/F', 'metSig_'+var+'/F'] )
        if options.keepPhotons: new_variables.extend( ['met_pt_photonEstimated_'+var+'/F', 'met_phi_photonEstimated_'+var+'/F', 'metSig_photonEstimated_'+var+'/F'] )
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
    selectionString = "&&".join(skimConds)
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
    if isMC: gPart = getGenPartsAll(r)

    # weight
    if isMC:
        event.weight = lumiScaleFactor*r.genWeight if lumiScaleFactor is not None else 1
    elif isData:
        event.weight = 1
    else:
        raise NotImplementedError( "isMC %r isData %r " % (isMC, isData) )

    # lumi lists and vetos
    if isData:
        #event.vetoPassed  = vetoList.passesVeto(r.run, r.lumi, r.evt)
        event.jsonPassed  = lumiList.contains(r.run, r.lumi)
        # store decision to use after filler has been executed
        event.jsonPassed_ = event.jsonPassed

    if isMC:
        event.reweightPU36fb     = nTrueInt36fb_puRW       ( r.nTrueInt )
        event.reweightPU36fbDown = nTrueInt36fb_puRWDown   ( r.nTrueInt )
        event.reweightPU36fbUp   = nTrueInt36fb_puRWUp     ( r.nTrueInt )

    # top pt reweighting
    if isMC and options.doTopPtReweighting: 
        event.reweightTopPt = topPtReweightingFunc(getTopPtsForReweighting(r))/topScaleF if doTopPtReweighting else 1.

    # Leptons: Reading LepGood and LepOther and fill new LepGood collection in the output tree
    mu_selector  = muonSelector( isoVar = "relIso04", barrelIso = 0.25, endcapIso = 0.25, absEtaCut = 2.4, dxy = 0.05, dz = 0.1 )
    ele_selector = eleSelector(  isoVar = "relIso03", barrelIso = 0.1,  endcapIso = 0.1,  absEtaCut = 2.5, dxy = 0.05, dz = 0.1, eleId = "M", noMissingHits=False )
    leptons      = getGoodAndOtherLeptons(r, ptCut=10, mu_selector = mu_selector, ele_selector = ele_selector)
    leptons.sort(key = lambda p:-p['pt'])

    # Store leptons
    event.nlep = len(leptons)
    for iLep, lep in enumerate(leptons):
        lep['index']  = iLep     # Index wrt to the output collection!
        lep['relIso'] = lep["relIso04"] if abs(lep['pdgId'])==13 else lep["relIso03"] 
        for b in lepton_vars_store:
            getattr(event, "lep_"+b)[iLep] = lep[b]

    # Storing lepton counters
    event.nGoodMuons     = len(filter( lambda l:abs(l['pdgId'])==13, leptons))
    event.nGoodElectrons = len(filter( lambda l:abs(l['pdgId'])==11, leptons))
    event.nGoodLeptons   = len(leptons)

    # Lepton convinience
    if options.leptonConvinience:
        for i in range(min(4, len(leptons))):
            for var in lep_convinience_vars:
                setattr( event, "l{n}_{var}".format( n=i+1, var=var), leptons[i][var] )
 
    # Identify best Z 
    (event.Z_mass, event.Z_l1_index, event.Z_l2_index) = closestOSDLMassToMZ(leptons)
    nonZ_lepton_indices = [ i for i in range(len(leptons)) if i not in [event.Z_l1_index, event.Z_l2_index] ]
    event.nonZ_l1_index = nonZ_lepton_indices[0] if len(nonZ_lepton_indices)>0 else -1
    event.nonZ_l2_index = nonZ_lepton_indices[1] if len(nonZ_lepton_indices)>1 else -1

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

    # Jets and lepton jet cross-cleaning    
    allJets      = getAllJets(r, leptons, ptCut=0, jetVars = jetVarNames, absEtaCut=99, jetCollections=[ "Jet", "DiscJet"]) #JetId is required
    selected_jets, other_jets = [], []
    for j in allJets:
        if isAnalysisJet(j, ptCut=30, absEtaCut=2.4):
            selected_jets.append( j )
        else:
            if options.keepAllJets:
                other_jets.append( j )

    # Don't change analysis jets even if we keep all jets, hence, apply abs eta cut
    bJets        = filter(lambda j:isBJet(j, tagger = 'CSVv2') and abs(j['eta'])<=2.4, selected_jets)
    bJetsDeepCSV = filter(lambda j:isBJet(j, tagger = 'DeepCSV') and abs(j['eta'])<=2.4, selected_jets)
    nonBJets     = filter(lambda j:not ( isBJet(j, tagger = 'CSVv2') and abs(j['eta'])<=2.4 ), selected_jets)
    nonBJetsDeepCSV  = filter(lambda j:not ( isBJet(j, tagger = 'DeepCSV') and abs(j['eta'])<=2.4 ), selected_jets)

    # Store jets
    event.nJetSelected   = len(selected_jets)
    jets_stored = allJets if options.keepAllJets else selected_jets
    event.njet        = len(jets_stored)
    for iJet, jet in enumerate(jets_stored):
        for b in jetVarNames:
            getattr(event, "jet_"+b)[iJet] = jet[b]

    # ETmiss
    event.met_pt  = r.met_pt
    event.met_phi = r.met_phi

    # Analysis observables
    event.ht         = sum([j['pt'] for j in selected_jets])
    event.metSig     = event.met_pt/sqrt(event.ht) if event.ht>0 else float('nan')
    event.nBTag      = len(bJets)
    event.nBTagDeepCSV = len(bJetsDeepCSV)

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
            genPhoton       = getGenPhoton(gPart)
            event.photon_genPt  = genPhoton['pt']  if genPhoton is not None else float('nan')
            event.photon_genEta = genPhoton['eta'] if genPhoton is not None else float('nan')

          event.met_pt_photonEstimated, event.met_phi_photonEstimated = getMetPhotonEstimated(r.met_pt, r.met_phi, photons[0])
          event.metSig_photonEstimated = event.met_pt_photonEstimated/sqrt(event.ht) if event.ht>0 else float('nan')

          event.photonJetdR = min(deltaR(photons[0], j) for j in selected_jets) if len(selected_jets) > 0 else 999
          event.photonLepdR = min(deltaR(photons[0], l) for l in leptons) if len(leptons) > 0 else 999

        if isMC:
           event.TTGJetsEventType = getTTGJetsEventType(r)

    if addSystematicVariations:
        for j in allJets:
            j['pt_JECUp']   =j['pt']/j['corr']*j['corr_JECUp']
            j['pt_JECDown'] =j['pt']/j['corr']*j['corr_JECDown']
            # JERUp, JERDown, JER
            addJERScaling(j)
        for var in ['JECUp', 'JECDown', 'JERUp', 'JERDown']:
            jets_sys[var]       = filter(lambda j: isAnalysisJet(j, ptCut=30, absEtaCut=2.4, ptVar='pt_'+var), allJets)
            bjets_sys[var]      = filter(lambda j: isBJet(j) and abs(j['eta'])<2.4, jets_sys[var])
            nonBjets_sys[var]   = filter(lambda j: not ( isBJet(j) and abs(j['eta'])<2.4), jets_sys[var])

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
                setattr(event, 'reweightBTagCSVv2_'+var, btagEff_CSVv2.getBTagSF_1a( var, bJets, filter( lambda j: abs(j['eta'])<2.4, nonBJets ) ) )

        # B tagging weights method 1a, now for DeepCSV
        for j in selected_jets:
            btagEff_DeepCSV.addBTagEffToJet(j)
        #print "DeepCSV", selected_jets[0]['beff']['SF'], selected_jets[0]['pt']
        for var in btagEff_DeepCSV.btagWeightNames:
            if var!='MC':
                setattr(event, 'reweightBTagDeepCSV_'+var, btagEff_DeepCSV.getBTagSF_1a( var, bJetsDeepCSV, filter( lambda j: abs(j['eta'])<2.4, nonBJetsDeepCSV ) ) )

    # gen information on extra leptons
    if isMC and not options.skipGenMatching:
        genSearch.init( gPart )
        # Start with status 1 gen leptons in acceptance
        gLep = filter( lambda p:abs(p['pdgId']) in [11, 13] and p['status']==1 and p['pt']>20 and abs(p['eta'])<2.5, gPart )
        for l in gLep:
            ancestry = [ gPart[x]['pdgId'] for x in genSearch.ancestry( l ) ]
            l["n_D"]   =  sum([ancestry.count(p) for p in D_mesons])
            l["n_B"]   =  sum([ancestry.count(p) for p in B_mesons])
            l["n_W"]   =  sum([ancestry.count(p) for p in [24, -24]])
            l["n_t"]   =  sum([ancestry.count(p) for p in [6, -6]])
            l["n_tau"] =  sum([ancestry.count(p) for p in [15, -15]])
            matched_lep = bestDRMatchInCollection(l, leptons) #FIXME -> fix all the gen / reco match indices!
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
            if len( lep_m ) == 1:
                event.genZ_cosThetaStar = cosThetaStar( event.genZ_mass, event.genZ_pt, event.genZ_eta, event.genZ_phi, lep_m[0]['pt'], lep_m[0]['eta'], lep_m[0]['phi'] )
    
# Create a maker. Maker class will be compiled. This instance will be used as a parent in the loop
treeMaker_parent = TreeMaker(
    sequence  = [ filler ],
    variables = [ TreeVariable.fromString(x) for x in new_variables ],
    treeName = "Events"
    )

# Split input in ranges
if options.nJobs>1:
    eventRanges = reader.getEventRanges( nJobs = options.nJobs )
else:
    eventRanges = reader.getEventRanges( maxNEvents = options.eventsPerJob, minJobs = options.minNJobs )

logger.info( "Splitting into %i ranges of %i events on average.",  len(eventRanges), (eventRanges[-1][1] - eventRanges[0][0])/len(eventRanges) )

#Define all jobs
jobs = [(i, eventRanges[i]) for i in range(len(eventRanges))]

filename, ext = os.path.splitext( os.path.join(output_directory, sample.name + '.root') )

clonedEvents = 0
convertedEvents = 0
outputLumiList = {}
for ievtRange, eventRange in enumerate( eventRanges ):

    if len(options.job)>0 and not ievtRange in options.job: continue

    logger.info( "Processing range %i/%i from %i to %i which are %i events.",  ievtRange, len(eventRanges), eventRange[0], eventRange[1], eventRange[1]-eventRange[0] )

    # Check whether file exists
    outfilename = filename+'_'+str(ievtRange)+ext
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

    clonedTree = reader.cloneTree( branchKeepStrings, newTreename = "Events", rootfile = outputfile )
    clonedEvents += clonedTree.GetEntries()
    # Clone the empty maker in order to avoid recompilation at every loop iteration
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
    jsonFile = filename+'.json'
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
