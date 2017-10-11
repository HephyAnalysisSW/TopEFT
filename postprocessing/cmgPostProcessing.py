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
from math import sqrt, atan2, sin, cos

# RootTools
from RootTools.core.standard import *

# User specific
import TopEFT.tools.user as user

# Tools for systematics
from TopEFT.tools.helpers                    import closestOSDLMassToMZ, checkRootFile, writeObjToFile, m3, deltaR, bestDRMatchInCollection, deltaPhi, mZ
from TopEFT.tools.addJERScaling              import addJERScaling
from TopEFT.tools.objectSelection            import getMuons, getElectrons, muonSelector, eleSelector, getGoodLeptons, getGoodAndOtherLeptons,  getGoodBJets, getGoodJets, isBJet, jetId, isBJet, getGoodPhotons, getGenPartsAll,getAllJets
from TopEFT.tools.overlapRemovalTTG          import getTTGJetsEventType
from TopEFT.tools.getGenBoson                import getGenZ, getGenPhoton
#from TopEFT.tools.triggerEfficiency          import triggerEfficiency
#from TopEFT.tools.leptonTrackingEfficiency   import leptonTrackingEfficiency

#triggerEff_withBackup   = triggerEfficiency(with_backup_triggers = True)
#triggerEff              = triggerEfficiency(with_backup_triggers = False)
#leptonTrackingSF        = leptonTrackingEfficiency()

#MC tools
from TopEFT.tools.mcTools import pdgToName, GenSearch, B_mesons, D_mesons, B_mesons_abs, D_mesons_abs
genSearch = GenSearch()

# central configuration
targetLumi = 1000 #pb-1 Which lumi to normalize to

logChoices      = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']
triggerChoices  = ['mumu', 'ee']

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--logLevel',                    action='store',         nargs='?',              choices=logChoices,     default='INFO',                     help="Log level for logging")
    argParser.add_argument('--overwrite',                   action='store_true',                                                                                        help="Overwrite existing output files, bool flag set to True  if used")
    argParser.add_argument('--samples',                     action='store',         nargs='*',  type=str,                           default=['TTJets'],                 help="List of samples to be post-processed, given as CMG component name")
    # argParser.add_argument('--triggerSelection',            action='store',         nargs='?',  type=str,   choices=triggerChoices, default=None,                       help="Trigger selection?")
    argParser.add_argument('--eventsPerJob',                action='store',         nargs='?',  type=int,                           default=300000,                     help="Maximum number of events per job (Approximate!).")
    argParser.add_argument('--nJobs',                       action='store',         nargs='?',  type=int,                           default=1,                          help="Maximum number of simultaneous jobs.")
    argParser.add_argument('--job',                         action='store',         nargs='*',  type=int,                           default=[],                         help="Run only job i")
    argParser.add_argument('--minNJobs',                    action='store',         nargs='?',  type=int,                           default=1,                          help="Minimum number of simultaneous jobs.")
    argParser.add_argument('--dataDir',                     action='store',         nargs='?',  type=str,                           default="/a/b/c",                   help="Name of the directory where the input data is stored (for samples read from Heppy).")
    argParser.add_argument('--targetDir',                   action='store',         nargs='?',  type=str,                           default=user.postprocessing_output_directory, help="Name of the directory the post-processed files will be saved")
    argParser.add_argument('--processingEra',               action='store',         nargs='?',  type=str,                           default='TopEFT_PP_v4',             help="Name of the processing era")
    argParser.add_argument('--skim',                        action='store',         nargs='?',  type=str,                           default='dilepTiny',                help="Skim conditions to be applied for post-processing")
    argParser.add_argument('--LHEHTCut',                    action='store',         nargs='?',  type=int,                           default=-1,                         help="LHE cut.")
    argParser.add_argument('--keepForwardJets',             action='store_true',                                                                                        help="Keep forward jets?")
    argParser.add_argument('--keepAllJets',                 action='store_true',                                                                                        help="Keep all jets?")
    argParser.add_argument('--small',                       action='store_true',                                                                                        help="Run the file on a small sample (for test purpose), bool flag set to True if used")
    argParser.add_argument('--skipGenLepMatching',          action='store_true',                                                                                        help="skip matched genleps??")
    argParser.add_argument('--keepLHEWeights',              action='store_true',                                                                                        help="Keep LHEWeights?")
    argParser.add_argument('--checkTTGJetsOverlap',         action='store_true',                                                    default=True,                       help="Keep TTGJetsEventType which can be used to clean TTG events from TTJets samples")
    argParser.add_argument('--skipSystematicVariations',    action='store_true',                                                                                        help="Don't calulcate BTag, JES and JER variations.")
    argParser.add_argument('--noTopPtReweighting',          action='store_true',                                                    default=True,                       help="Skip top pt reweighting.")

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
elif isSingleLep:
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

#if isData and options.triggerSelection is not None:
#    if options.triggerSelection == 'mumu':
#        skimConds.append( "(HLT_mumuIso||HLT_mumuNoiso)" )
#    else:
#        raise ValueError( "Don't know about triggerSelection %s"%options.triggerSelection )
#    sample_name_postFix = "_Trig_"+options.triggerSelection
#    logger.info( "Added trigger selection %s and postFix %s", options.triggerSelection, sample_name_postFix )
#else:
#    sample_name_postFix = ""

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

if isMC:
    from TopEFT.tools.puReweighting import getReweightingFunction
    mcProfile = "Summer16"
    # nTrueIntReweighting
    nTrueInt36fb_puRW        = getReweightingFunction(data="PU_2016_36000_XSecCentral", mc=mcProfile)
    nTrueInt36fb_puRWDown    = getReweightingFunction(data="PU_2016_36000_XSecDown",    mc=mcProfile)
    nTrueInt36fb_puRWUp      = getReweightingFunction(data="PU_2016_36000_XSecUp",      mc=mcProfile)
        
# top pt reweighting
from TopEFT.tools.topPtReweighting import getUnscaledTopPairPtReweightungFunction, getTopPtDrawString, getTopPtsForReweighting
# Decision based on sample name -> whether TTJets or TTLep is in the sample name
isTT = sample.name.startswith("TTJets") or sample.name.startswith("TTLep") or sample.name.startswith("TT_pow")
doTopPtReweighting = isTT and not options.noTopPtReweighting
if doTopPtReweighting:
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


#from TopEFT.tools.leptonSF import leptonSF as leptonSF_
#leptonSF = leptonSF_()


# systematic variations
addSystematicVariations = (not isData) and (not options.skipSystematicVariations)
if addSystematicVariations:
    # B tagging SF
    from TopEFT.tools.btagEfficiency import btagEfficiency
    btagEff = btagEfficiency( fastSim = False )

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

output_directory = os.path.join( directory, options.skim, sample.name )

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
        "LepGood_eta", "LepGood_etaSc", "LepGood_pt","LepGood_phi", "LepGood_dxy", "LepGood_dz","LepGood_tightId", "LepGood_pdgId",
        "LepGood_mediumMuonId","ICHEPmediumMuonId", "LepGood_miniRelIso", "LepGood_relIso03", "LepGood_sip3d", "LepGood_mvaIdSpring15", "LepGood_convVeto", "LepGood_lostHits","LepGood_jetPtRelv2", "LepGood_jetPtRatiov2", "LepGood_eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz"
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
        "nDiscJet", "DiscJet_*",
        "nJetFailId", "JetFailId_*",
        "nLepGood", "LepGood_*",
        "nLepOther", "LepOther_*",
        "nTauGood", "TauGood_*",
    ]
    #branches to be kept for MC samples only
    branchKeepStrings_MC = [\
        "nTrueInt", "genWeight", "xsec", "met_gen*", "lheHTIncoming",
        "ngenPartAll","genPartAll_*","ngenLep","genLep_*"
    ]

    #branches to be kept for data only
    branchKeepStrings_DATA = [ ]

if options.keepLHEWeights:
    branchKeepStrings_MC+=["nLHEweight", "LHEweight_id", "LHEweight_wgt", "LHEweight_original"]

if isSingleLep:
    branchKeepStrings_DATAMC += ['HLT_*']

# Jet variables to be read from chain
jetCorrInfo = ['corr/F', 'corr_JECUp/F', 'corr_JECDown/F'] if addSystematicVariations else []
if isMC:
    if isTiny:
        jetMCInfo = ['mcPt/F', 'hadronFlavour/I','mcMatchId/I']
    else:
        jetMCInfo = ['mcMatchFlav/I', 'partonId/I', 'partonMotherId/I', 'mcPt/F', 'mcFlavour/I', 'hadronFlavour/I', 'mcMatchId/I']
        jetMCInfo.append('partonFlavour/I')
else:
    jetMCInfo = []

if not isTiny:
    branchKeepStrings_DATAMC+=[
        "ngamma", "gamma_idCutBased", "gamma_hOverE", "gamma_r9", "gamma_sigmaIetaIeta", "gamma_chHadIso04", "gamma_chHadIso", "gamma_phIso",
        "gamma_neuHadIso", "gamma_relIso", "gamma_pdgId", "gamma_pt", "gamma_eta", "gamma_phi", "gamma_mass",
        "gamma_chHadIsoRC04", "gamma_chHadIsoRC"]
    if isMC: branchKeepStrings_DATAMC+=[ "gamma_mcMatchId", "gamma_mcPt", "gamma_genIso04", "gamma_genIso03", "gamma_drMinParton"]

if sample.isData:
    lumiScaleFactor=None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_DATA
    from FWCore.PythonUtilities.LumiList import LumiList
    # Apply golden JSON
    sample.heppy.json = '$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
    lumiList = LumiList(os.path.expandvars(sample.heppy.json))
    logger.info( "Loaded json %s", sample.heppy.json )
else:
    lumiScaleFactor = xSection*targetLumi/float(sample.normalization) if xSection is not None else None
    branchKeepStrings = branchKeepStrings_DATAMC + branchKeepStrings_MC

jetVars = ['pt/F', 'rawPt/F', 'eta/F', 'phi/F', 'id/I', 'btagCSV/F', 'area/F'] + jetCorrInfo + jetMCInfo
jetVarNames = [x.split('/')[0] for x in jetVars]
genLepVars      = ['pt/F', 'phi/F', 'eta/F', 'pdgId/I', 'index/I', 'lepGoodMatchIndex/I', 'matchesPromptGoodLepton/I', 'n_t/I','n_W/I', 'n_B/I', 'n_D/I', 'n_tau/I']
genLepVarNames  = [x.split('/')[0] for x in genLepVars]

read_variables = map(TreeVariable.fromString, ['met_pt/F', 'met_phi/F', 'run/I', 'lumi/I', 'evt/l', 'nVert/I'] )
read_variables += [ TreeVariable.fromString('ngamma/I'),
                    VectorTreeVariable.fromString('gamma[pt/F,eta/F,phi/F,mass/F,idCutBased/I,pdgId/I]') ]

new_variables = [ 'weight/F']
new_variables+= [ 'JetGood[%s]'% ( ','.join(jetVars) ) ]

if isMC:
    read_variables+= [TreeVariable.fromString('nTrueInt/F'), VectorTreeVariable.fromString('LepGood[mcMatchId/I, mcMatchAny/I]'), VectorTreeVariable.fromString('LepOther[mcMatchId/I, mcMatchAny/I]')]
    # reading gen particles for top pt reweighting
    read_variables.append( TreeVariable.fromString('ngenPartAll/I') )
    read_variables.append( VectorTreeVariable.fromString('genPartAll[pt/F,eta/F,phi/F,mass/F,pdgId/I,status/I,charge/I,motherId/I,grandmotherId/I,nMothers/I,motherIndex1/I,motherIndex2/I,nDaughters/I,daughterIndex1/I,daughterIndex2/I,isPromptHard/I]', nMax=200 )) # default nMax is 100, which would lead to corrupt values in this case
    read_variables.append( TreeVariable.fromString('genWeight/F') )
    read_variables.append( TreeVariable.fromString('nIsr/I') )
    read_variables.append( VectorTreeVariable.fromString('gamma[mcPt/F]') )

    new_variables.extend([ 'reweightTopPt/F', 'reweightPU36fb/F','reweightPU36fbUp/F','reweightPU36fbDown/F'])
    if not options.skipGenLepMatching:
        TreeVariable.fromString( 'nGenLep/I' ),
        new_variables.append( 'GenLep[%s]'% ( ','.join(genLepVars) ) )

read_variables += [\
    TreeVariable.fromString('nLepGood/I'),
    TreeVariable.fromString('nLepOther/I'),
    VectorTreeVariable.fromString('LepGood[pt/F,eta/F,etaSc/F,phi/F,pdgId/I,tightId/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,mediumMuonId/I,ICHEPmediumMuonId/I,mvaIdSpring15/F,lostHits/I,convVeto/I,dxy/F,dz/F,jetPtRelv2/F,jetPtRatiov2/F,eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz/I,mvaIdSpring16/F,hadronicOverEm/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,etaSc/F]'),
    VectorTreeVariable.fromString('LepOther[pt/F,eta/F,etaSc/F,phi/F,pdgId/I,tightId/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,mediumMuonId/I,ICHEPmediumMuonId/I,mvaIdSpring15/F,lostHits/I,convVeto/I,dxy/F,dz/F,jetPtRelv2/F,jetPtRatiov2/F,eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz/I,mvaIdSpring16/F,hadronicOverEm/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,etaSc/F]'),
    TreeVariable.fromString('nJet/I'),
    TreeVariable.fromString('nDiscJet/I'),
    VectorTreeVariable.fromString('Jet[%s]'% ( ','.join(jetVars) ) ),
    VectorTreeVariable.fromString('DiscJet[%s]'% ( ','.join(jetVars) ) )
]

if isData: new_variables.extend( ['jsonPassed/I'] )
new_variables.extend( ['nBTag/I', 'ht/F', 'metSig/F'] )

if isSingleLep:
    new_variables.extend( ['m3/F', 'm3_ind1/I', 'm3_ind2/I', 'm3_ind3/I'] )
if isTriLep or isDiLep or isSingleLep:
    new_variables.extend( ['nGoodMuons/I', 'nGoodElectrons/I' ] )
    new_variables.extend( ['l1_pt/F', 'l1_eta/F', 'l1_phi/F', 'l1_pdgId/I', 'l1_index/I', 'l1_jetPtRelv2/F', 'l1_jetPtRatiov2/F', 'l1_miniRelIso/F', 'l1_relIso03/F', 'l1_dxy/F', 'l1_dz/F', 'l1_mIsoWP/I' ] )
    if isMC: new_variables.extend(['l1_mcMatchId/I', 'l1_mcMatchAny/I'])
    new_variables.extend( ['mlmZ_mass/F'] )
    new_variables.extend( ['mt_photonEstimated/F'])

if isTriLep or isDiLep:

    for i in [2,3,4]:
        new_variables.extend( ['l%i_pt/F'%i, 'l%i_eta/F'%i, 'l%i_phi/F'%i, 'l%i_pdgId/I'%i, 'l%i_index/I'%i, 'l%i_jetPtRelv2/F'%i, 'l%i_jetPtRatiov2/F'%i, 'l%i_miniRelIso/F'%i, 'l%i_relIso03/F'%i, 'l%i_dxy/F'%i, 'l%i_dz/F'%i, 'l%i_mIsoWP/I'%i ] )
        if isMC: new_variables.extend(['l%i_mcMatchId/I'%i, 'l%i_mcMatchAny/I'%i])
    
    for i in [1,2]:
        new_variables.extend( ['Z_l%i_pt/F'%i, 'Z_l%i_eta/F'%i, 'Z_l%i_phi/F'%i, 'Z_l%i_pdgId/I'%i, 'Z_l%i_index/I'%i, 'Z_l%i_relIso03/F'%i, 'Z_l%i_dxy/F'%i, 'Z_l%i_dz/F'%i ] )

    new_variables.extend( ['isDilep/I', 'isTrilep/I', 'isQuadlep/I', 'isDilepSF/I', 'isTTZcand/I', 'nEle/I','nMu/I','nLep/I' ] )
    new_variables.extend( ['dl_pt/F', 'dl_eta/F', 'dl_phi/F', 'dl_dphi/F', 'dl_mass/F'] )
    if isMC: new_variables.extend( \
        [   'zBoson_genPt/F', 'zBoson_genEta/F', 
         ] )
if isTriLep:
    new_variables.extend( ['l3_pt/F', 'l3_eta/F', 'l3_phi/F', 'l3_pdgId/I', 'l3_index/I', 'l3_jetPtRelv2/F', 'l3_jetPtRatiov2/F', 'l3_miniRelIso/F', 'l3_relIso03/F', 'l3_dxy/F', 'l3_dz/F', 'l3_mIsoWP/I' ] )
    if isMC: new_variables.extend(['l3_mcMatchId/I', 'l3_mcMatchAny/I'])

new_variables.extend( ['nPhotonGood/I','photon_pt/F','photon_eta/F','photon_phi/F','photon_idCutBased/I'] )
if isMC: new_variables.extend( ['photon_genPt/F', 'photon_genEta/F'] )
new_variables.extend( ['met_pt_photonEstimated/F','met_phi_photonEstimated/F','metSig_photonEstimated/F'] )
new_variables.extend( ['photonJetdR/F','photonLepdR/F'] )
if isTriLep or isDiLep:
  new_variables.extend( ['dlg_mass/F' ] )

if options.checkTTGJetsOverlap:
    new_variables.extend( ['TTGJetsEventType/I'] )

if addSystematicVariations:
    read_variables += map(TreeVariable.fromString, [\
    "met_JetEnUp_Pt/F", "met_JetEnUp_Phi/F", "met_JetEnDown_Pt/F", "met_JetEnDown_Phi/F", "met_JetResUp_Pt/F", "met_JetResUp_Phi/F", "met_JetResDown_Pt/F", "met_JetResDown_Phi/F", 
    "met_UnclusteredEnUp_Pt/F", "met_UnclusteredEnUp_Phi/F", "met_UnclusteredEnDown_Pt/F", "met_UnclusteredEnDown_Phi/F", 
    ] )

    for var in ['JECUp', 'JECDown', 'JERUp', 'JERDown', 'UnclusteredEnUp', 'UnclusteredEnDown']:
        if 'Unclustered' not in var: new_variables.extend( ['nJetGood_'+var+'/I', 'nBTag_'+var+'/I','ht_'+var+'/F'] )
        new_variables.extend( ['met_pt_'+var+'/F', 'met_phi_'+var+'/F', 'metSig_'+var+'/F'] )
        new_variables.extend( ['met_pt_photonEstimated_'+var+'/F', 'met_phi_photonEstimated_'+var+'/F', 'metSig_photonEstimated_'+var+'/F'] )
    # Btag weights Method 1a
    for var in btagEff.btagWeightNames:
        if var!='MC':
            new_variables.append('reweightBTag_'+var+'/F')


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
    if isMC: event.reweightTopPt = topPtReweightingFunc(getTopPtsForReweighting(r))/topScaleF if doTopPtReweighting else 1.

    # jet/met related quantities, also load the leptons already
    if options.keepAllJets:
        jetAbsEtaCut = 99.
    else:
        jetAbsEtaCut = 2.4
        
    #allJets_old      = getGoodJets(r, ptCut=0, jetVars = jetVarNames, absEtaCut=jetAbsEtaCut)
    #jets_old         = filter(lambda j:jetId(j, ptCut=30, absEtaCut=jetAbsEtaCut), allJets_old)
    #soft_jets    = filter(lambda j:jetId(j, ptCut=0,  absEtaCut=jetAbsEtaCut) and j['pt']<30., allJets_old) if options.keepAllJets else []
    #bJets_old        = filter(lambda j:isBJet(j) and abs(j['eta'])<=2.4    , jets_old)
    #nonBJets     = filter(lambda j:not ( isBJet(j) and abs(j['eta'])<=2.4 ), jets_old)

    mu_selector  = muonSelector( isoVar = "relIso04", barrelIso = 0.25, endcapIso = 0.25, absEtaCut = 2.4, dxy = 0.05, dz = 0.1 )
    ele_selector = eleSelector(  isoVar = "relIso03", barrelIso = 0.1,  endcapIso = 0.1,  absEtaCut = 2.5, dxy = 0.05, dz = 0.1, eleId = "M", noMissingHits=False )
    #leptons_pt10 = getGoodAndOtherLeptons(r, ptCut=10, mu_selector = mu_selector, ele_selector = ele_selector)
    leptons_pt10 = getGoodAndOtherLeptons(r, ptCut=10, mu_selector = mu_selector, ele_selector = ele_selector)
    leptons      = filter(lambda l:l['pt']>10, leptons_pt10)

    leptons.sort(key = lambda p:-p['pt'])
    
    allJets      = getAllJets(r, leptons, ptCut=0, jetVars = jetVarNames, absEtaCut=jetAbsEtaCut)
    jets         = filter(lambda j:jetId(j, ptCut=30, absEtaCut=jetAbsEtaCut), allJets)
    soft_jets    = filter(lambda j:jetId(j, ptCut=0,  absEtaCut=jetAbsEtaCut) and j['pt']<30., allJets) if options.keepAllJets else []
    bJets        = filter(lambda j:isBJet(j) and abs(j['eta'])<=2.4    , jets)
    nonBJets     = filter(lambda j:not ( isBJet(j) and abs(j['eta'])<=2.4 ), jets)

    event.met_pt  = r.met_pt
    event.met_phi = r.met_phi

    # Filling jets
    store_jets = jets if not options.keepAllJets else soft_jets + jets
    store_jets.sort( key = lambda j:-j['pt'])
    event.nJetGood   = len(store_jets)
    for iJet, jet in enumerate(store_jets):
        for b in jetVarNames:
            getattr(event, "JetGood_"+b)[iJet] = jet[b]

    if isSingleLep:
        # Compute M3 and the three indiced of the jets entering m3
        event.m3, event.m3_ind1, event.m3_ind2, event.m3_ind3 = m3( jets )

    event.ht         = sum([j['pt'] for j in jets])
    event.metSig     = event.met_pt/sqrt(event.ht) if event.ht>0 else float('nan')
    event.nBTag      = len(bJets)

    jets_sys      = {}
    bjets_sys     = {}
    nonBjets_sys  = {}

    metVariants = [''] # default

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

      event.photonJetdR = min(deltaR(photons[0], j) for j in jets) if len(jets) > 0 else 999
      event.photonLepdR = min(deltaR(photons[0], l) for l in leptons_pt10) if len(leptons_pt10) > 0 else 999

    if options.checkTTGJetsOverlap and isMC:
       event.TTGJetsEventType = getTTGJetsEventType(r)

    if addSystematicVariations:
        for j in allJets:
            j['pt_JECUp']   =j['pt']/j['corr']*j['corr_JECUp']
            j['pt_JECDown'] =j['pt']/j['corr']*j['corr_JECDown']
            # JERUp, JERDown, JER
            addJERScaling(j)
        for var in ['JECUp', 'JECDown', 'JERUp', 'JERDown']:
            jets_sys[var]       = filter(lambda j:jetId(j, ptCut=30, absEtaCut=jetAbsEtaCut, ptVar='pt_'+var), allJets)
            bjets_sys[var]      = filter(lambda j: isBJet(j) and abs(j['eta'])<2.4, jets_sys[var])
            nonBjets_sys[var]   = filter(lambda j: not ( isBJet(j) and abs(j['eta'])<2.4), jets_sys[var])

            setattr(event, "nJetGood_"+var, len(jets_sys[var]))
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

    if isSingleLep or isTriLep or isDiLep:
        event.nGoodMuons      = len(filter( lambda l:abs(l['pdgId'])==13, leptons))
        event.nGoodElectrons  = len(filter( lambda l:abs(l['pdgId'])==11, leptons))

        (event.mlmZ_mass, zl1, zl2) = closestOSDLMassToMZ(leptons)

        l_pdgs = []
        if len(leptons)>=1:
            event.l1_pt     = leptons[0]['pt']
            event.l1_eta    = leptons[0]['eta']
            event.l1_phi    = leptons[0]['phi']
            event.l1_pdgId  = leptons[0]['pdgId']
            event.l1_index  = leptons[0]['index']
            if isMC:
              event.l1_mcMatchId   = leptons[0]['mcMatchId']
              event.l1_mcMatchAny  = leptons[0]['mcMatchAny']
            event.l1_jetPtRatiov2  = leptons[0]['jetPtRatiov2']
            event.l1_jetPtRelv2    = leptons[0]['jetPtRelv2']
            event.l1_miniRelIso = leptons[0]['miniRelIso']
            event.l1_relIso03 = leptons[0]['relIso03']
            event.l1_dxy = leptons[0]['dxy']
            event.l1_dz = leptons[0]['dz']
            l_pdgs.append(abs(leptons[0]['pdgId']))

            if len(leptons)>=2:
                for i in range(1,len(leptons)):
                    j = i+1
                    setattr(event, 'l%i_pt'%j, leptons[i]['pt'])
                    setattr(event, 'l%i_eta'%j, leptons[i]['eta'])
                    setattr(event, 'l%i_phi'%j, leptons[i]['phi'])
                    setattr(event, 'l%i_pdgId'%j, leptons[i]['pdgId'])
                    setattr(event, 'l%i_index'%j, leptons[i]['index'])
                    setattr(event, 'l%i_miniRelIso'%j, leptons[i]['miniRelIso'])
                    setattr(event, 'l%i_relIso03'%j, leptons[i]['relIso03'])
                    setattr(event, 'l%i_dxy'%j, leptons[i]['dxy'])
                    setattr(event, 'l%i_dz'%j, leptons[i]['dz'])
                    if isMC:
                        setattr(event, 'l%i_mcMatchId'%j, leptons[i]['mcMatchId'])
                        setattr(event, 'l%i_mcMatchAny'%j, leptons[i]['mcMatchAny'])

                    l_pdgs.append(abs(leptons[i]['pdgId']))
                
                if event.mlmZ_mass > 0:
                    for i,j in enumerate([zl1, zl2]):
                        setattr(event, 'Z_l%i_pt'%(i+1), leptons[j]['pt'])
                        setattr(event, 'Z_l%i_phi'%(i+1), leptons[j]['phi'])
                        setattr(event, 'Z_l%i_eta'%(i+1), leptons[j]['eta'])
                        setattr(event, 'Z_l%i_pdgId'%(i+1), leptons[j]['pdgId'])
                        setattr(event, 'Z_l%i_index'%(i+1), leptons[j]['index'])
                        setattr(event, 'Z_l%i_relIso03'%(i+1), leptons[j]['relIso03'])
                        setattr(event, 'Z_l%i_dxy'%(i+1), leptons[j]['dxy'])
                        setattr(event, 'Z_l%i_dz'%(i+1), leptons[j]['dz'])
                    if event.Z_l1_pdgId * event.Z_l2_pdgId > 1:
                        print "Problem!"
                        print zl1, zl2
                        print leptons[zl1]['pt'], leptons[zl2]['pt']
                        print event.Z_l1_pdgId, event.Z_l2_pdgId
                        print event.Z_l1_pt, event.Z_l2_pt
                        print event.mlmZ_mass

                #if event.mlmZ_mass > 0:
                    Z_l1 = ROOT.TLorentzVector()
                    Z_l1.SetPtEtaPhiM(event.Z_l1_pt, event.Z_l1_eta, event.Z_l1_phi, 0 )
                    Z_l2 = ROOT.TLorentzVector()
                    Z_l2.SetPtEtaPhiM(event.Z_l2_pt, event.Z_l2_eta, event.Z_l2_phi, 0 )
                    dl = Z_l1 + Z_l2
                    event.dl_pt   = dl.Pt()
                    event.dl_eta  = dl.Eta()
                    event.dl_phi  = dl.Phi()
                    event.dl_dphi = deltaPhi(event.Z_l1_phi,event.Z_l2_phi)
                    event.dl_mass = dl.M()

        event.nEle = event.nGoodElectrons
        event.nMu = event.nGoodMuons
        event.nLep = len(leptons)
        event.isDilep = len(leptons) == 2 
        event.isDilepSF = ( len(leptons) == 2 and l_pdgs[0] == l_pdgs[1] )
        event.isTrilep = len(leptons) == 3
        event.isQuadlep = len(leptons) == 4
        event.isTTZcand = abs(event.mlmZ_mass - mZ) < 10

        # For TTZ studies: find Z boson candidate, and use third lepton to calculate mt
        (event.mlmZ_mass, zl1, zl2) = closestOSDLMassToMZ(leptons_pt10)

    if addSystematicVariations:
        # B tagging weights method 1a
        for j in jets:
            btagEff.addBTagEffToJet(j)
        for var in btagEff.btagWeightNames:
            if var!='MC':
                setattr(event, 'reweightBTag_'+var, btagEff.getBTagSF_1a( var, bJets, filter( lambda j: abs(j['eta'])<2.4, nonBJets ) ) )

    # gen information on extra leptons
    if isMC and not options.skipGenLepMatching:
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
            matched_lep = bestDRMatchInCollection(l, leptons_pt10)
            if matched_lep:
                l["lepGoodMatchIndex"] = matched_lep['index']
                if isSingleLep:
                    l["matchesPromptGoodLepton"] = l["lepGoodMatchIndex"] in [event.l1_index]
                elif isTriLep or isDiLep:
                    l["matchesPromptGoodLepton"] = l["lepGoodMatchIndex"] in [event.l1_index, event.l2_index]
                else:
                    l["matchesPromptGoodLepton"] = 0
            else:
                l["lepGoodMatchIndex"] = -1
                l["matchesPromptGoodLepton"] = 0
        event.nGenLep   = len(gLep)
        for iLep, lep in enumerate(gLep):
            for b in genLepVarNames:
                getattr(event, "GenLep_"+b)[iLep] = lep[b]

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
