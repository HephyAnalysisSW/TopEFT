#!/usr/bin/env python
''' Make flat ntuple from GEN data tier 
'''
#
# Standard imports and batch mode
#
import ROOT
import os, sys
ROOT.gROOT.SetBatch(True)
import itertools
from math                                import sqrt, cos, sin, pi, acos
import imp

#RootTools
from RootTools.core.standard             import *

#TopEFT
from TopEFT.Tools.user                   import skim_output_directory
from TopEFT.Tools.helpers                import deltaPhi, deltaR, deltaR2, cosThetaStar, closestOSDLMassToMZ
from TopEFT.Tools.DelphesReader          import DelphesReader
from TopEFT.Tools.objectSelection        import isGoodDelphesJet, isGoodDelphesLepton
#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',              action='store_true', help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--overwrite',          action='store',      nargs='?', choices = ['none', 'all', 'target'], default = 'none', help='Overwrite?')#, default = True)
argParser.add_argument('--targetDir',          action='store',      default='v5')
argParser.add_argument('--sample',             action='store',      default='fwlite_ttZ_ll_LO_scan', help="Name of the sample loaded from fwlite_benchmarks. Only if no inputFiles are specified")
argParser.add_argument('--inputFiles',         action='store',      nargs = '*', default=[])
argParser.add_argument('--targetSampleName',   action='store',      default=None, help="Name of the sample in case inputFile are specified. Otherwise ignored")
argParser.add_argument('--nJobs',              action='store',      nargs='?', type=int, default=1,  help="Maximum number of simultaneous jobs.")
argParser.add_argument('--job',                action='store',      nargs='?', type=int, default=0,  help="Run only job i")
args = argParser.parse_args()

#
# Logger
#
import TopEFT.Tools.logger as _logger
import RootTools.core.logger as _logger_rt
logger    = _logger.get_logger(   args.logLevel, logFile = None)
logger_rt = _logger_rt.get_logger(args.logLevel, logFile = None)

# Load sample either from 
if len(args.inputFiles)>0:
    logger.info( "Input files found. Ignoring 'sample' argument. Files: %r", args.inputFiles)
    sample = FWLiteSample( args.targetSampleName, args.inputFiles)
else:
    sample_file = "$CMSSW_BASE/python/TopEFT/samples/delphes_upgrade.py"
    samples = imp.load_source( "samples", os.path.expandvars( sample_file ) )
    sample = getattr( samples, args.sample )
    logger.debug( 'Loaded sample %s with %i files.', sample.name, len(sample.files) )

maxEvents = -1
if args.small: 
    args.targetDir += "_small"
    maxEvents=5000 # Number of files
    sample.files=sample.files[:1]

xsec = sample.xsec
nEvents = sample.chain.GetEntries()
lumiweight1fb = xsec * 1000. / nEvents
logger.info( "Calculated lumiweight1fb %4.3f (xsec %4.3f, nEvents %i)", lumiweight1fb, xsec, nEvents )


# output directory
output_directory = os.path.join(skim_output_directory, 'delphes', args.targetDir, sample.name) 
if not os.path.exists( output_directory ): 
    os.makedirs( output_directory )
    logger.info( "Created output directory %s", output_directory )

# Load reweight pickle file if supposed to keep weights. 
extra_variables = []

# Run only job number "args.job" from total of "args.nJobs"
if args.nJobs>1:
    n_files_before = len(sample.files)
    sample = sample.split(args.nJobs)[args.job]
    n_files_after  = len(sample.files)
    logger.info( "Running job %i/%i over %i files from a total of %i.", args.job, args.nJobs, n_files_after, n_files_before)

def varnames( vec_vars ):
    return [v.split('/')[0] for v in vec_vars.split(',')]

def vecSumPt(*args):
    return sqrt( sum([o['pt']*cos(o['phi']) for o in args],0.)**2 + sum([o['pt']*sin(o['phi']) for o in args],0.)**2 )

def addIndex( collection ):
    for i  in range(len(collection)):
        collection[i]['index'] = i

variables = []

# Lumi weight 1fb
variables += ["lumiweight1fb/F"]

# reconstructed bosons
variables     += ["Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I",  "Z_pt/F", "Z_eta/F", "Z_phi/F", "Z_mass/F", "Z_lldPhi/F", "Z_lldR/F", "Z_cosThetaStar/F"]

# reconstructed leptons
lep_vars       = "pt/F,eta/F,phi/F,pdgId/I,charge/I,isolationVar/F,isolationVarRhoCorr/F,sumPtCharged/F,sumPtNeutral/F,sumPtChargedPU/F,sumPt/F,ehadOverEem/F"
variables         += ["lep[%s]"%lep_vars]
lep_varnames  = varnames( lep_vars )

#
variables += ["nBTag/I", "nMuons/I", "nElectrons/I"]
    
# reconstructed jets
jet_vars    = 'pt/F,eta/F,phi/F,bTag/F,bTagPhys/I,bTagAlgo/I' 
variables      += ["jet[%s]"%jet_vars]
jet_write_varnames = varnames( jet_vars )
variables += ["bj0_%s"%var for var in jet_vars.split(',')]
variables += ["bj1_%s"%var for var in jet_vars.split(',')]
jet_varnames= varnames( jet_vars )

variables      += ["met_pt/F", "met_phi/F"]
 
def fill_vector_collection( event, collection_name, collection_varnames, objects):
    setattr( event, "n"+collection_name, len(objects) )
    for i_obj, obj in enumerate(objects):
        for var in collection_varnames:
            getattr(event, collection_name+"_"+var)[i_obj] = obj[var]

def fill_vector( event, collection_name, collection_varnames, obj):
    if obj is None: return
    for var in collection_varnames:
        setattr(event, collection_name+"_"+var, obj[var] )

reader = DelphesReader( sample )

def filler( event ):

    if reader.position % 100==0: logger.info("At event %i/%i", reader.position, reader.nEvents)
    event.lumiweight1fb = lumiweight1fb

    # read jets
    jets =  filter( lambda j: isGoodDelphesJet(j), reader.jets()) 
    jets.sort( key = lambda p:-p['pt'] )
    addIndex( jets )

    # make b jets
#    for j in jets:
#        print j['pt'], j['eta'], j['bTag'], j['bTagPhys'], j['bTagAlgo']
    bJets    = filter( lambda j:j['bTagPhys']>=4, jets )
    nonBJets = filter( lambda j:not (j['bTagPhys']<4), jets )
    bj0, bj1 = ( bJets + nonBJets + [None, None] )[:2] 
    fill_vector( event, "bj0", jet_write_varnames, bj0) 
    fill_vector( event, "bj1", jet_write_varnames, bj1) 

    event.nBTag = len( bJets )

    # read leptons
    allLeps = reader.muonsTight() + reader.electrons()
    allLeps.sort( key = lambda p:-p['pt'] )
    leps =  filter( isGoodDelphesLepton, allLeps )
    # cross-cleaning of reco-objects
    # leps = filter( lambda l: (min([999]+[deltaR2(l, j) for j in jets if j['pt']>30]) > 0.3**2 ), leps )
    # give index to leptons
    addIndex( leps )

    # Store
    fill_vector_collection( event, "lep",    lep_varnames, leps )
    fill_vector_collection( event, "jet",    jet_varnames, jets )

    event.nMuons     = len( filter( lambda l:abs(l['pdgId'])==13, leps ) )
    event.nElectrons = len( filter( lambda l:abs(l['pdgId'])==11, leps ) )

    # MET
    met = reader.met()[0]

    event.met_pt  = met['pt']
    event.met_phi = met['phi']

    # search for Z in leptons
    (event.Z_mass, Z_l1_index, Z_l2_index) = closestOSDLMassToMZ(leps)
    nonZ_indices = [ i for i in range(len(leps)) if i not in [Z_l1_index, Z_l2_index] ]
    event.Z_l1_index    = leps[Z_l1_index]['index'] if Z_l1_index>=0 else -1
    event.Z_l2_index    = leps[Z_l2_index]['index'] if Z_l2_index>=0 else -1
    event.nonZ_l1_index = leps[nonZ_indices[0]]['index'] if len(nonZ_indices)>0 else -1
    event.nonZ_l2_index = leps[nonZ_indices[1]]['index'] if len(nonZ_indices)>1 else -1

    # Store Z information 
    if event.Z_mass>=0:
        if leps[event.Z_l1_index]['pdgId']*leps[event.Z_l2_index]['pdgId']>0 or abs(leps[event.Z_l1_index]['pdgId'])!=abs(leps[event.Z_l2_index]['pdgId']): 
            raise RuntimeError( "not a Z! Should not happen" )
        Z_l1 = ROOT.TLorentzVector()
        Z_l1.SetPtEtaPhiM(leps[event.Z_l1_index]['pt'], leps[event.Z_l1_index]['eta'], leps[event.Z_l1_index]['phi'], 0 )
        Z_l2 = ROOT.TLorentzVector()
        Z_l2.SetPtEtaPhiM(leps[event.Z_l2_index]['pt'], leps[event.Z_l2_index]['eta'], leps[event.Z_l2_index]['phi'], 0 )
        Z = Z_l1 + Z_l2
        event.Z_pt   = Z.Pt()
        event.Z_eta  = Z.Eta()
        event.Z_phi  = Z.Phi()
        event.Z_lldPhi = deltaPhi(leps[event.Z_l1_index]['phi'], leps[event.Z_l2_index]['phi'])
        event.Z_lldR   = deltaR(leps[event.Z_l1_index], leps[event.Z_l2_index])
        lm_index = event.Z_l1_index if leps[event.Z_l1_index]['pdgId'] > 0 else event.Z_l2_index
        event.Z_cosThetaStar = cosThetaStar(event.Z_mass, event.Z_pt, event.Z_eta, event.Z_phi, leps[lm_index]['pt'], leps[lm_index]['eta'], leps[lm_index]['phi'] )

         
tmp_dir     = ROOT.gDirectory
output_filename =  os.path.join(output_directory, sample.name + '.root')

_logger.   add_fileHandler( output_filename.replace('.root', '.log'), args.logLevel )
_logger_rt.add_fileHandler( output_filename.replace('.root', '_rt.log'), args.logLevel )

if os.path.exists( output_filename ) and args.overwrite =='none' :
    logger.info( "File %s found. Quit.", output_filename )
    sys.exit(0)

output_file = ROOT.TFile( output_filename, 'recreate')
output_file.cd()
maker = TreeMaker(
    sequence  = [ filler ],
    variables = [ TreeVariable.fromString(x) for x in variables ] + extra_variables,
    treeName = "Events"
    )

tmp_dir.cd()

counter = 0
reader.start()
maker.start()

while reader.run( ):
    maker.run()

    counter += 1
    if counter == maxEvents:  break

logger.info( "Done with running over %i events.", reader.nEvents )

output_file.cd()
maker.tree.Write()
output_file.Close()

logger.info( "Written output file %s", output_filename )
