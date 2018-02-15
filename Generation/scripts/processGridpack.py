#!/usr/bin/env python

'''
Generate events from a gridpack by running a cmsRun job and then the genPostProcessor
'''

# Standard imports
import os, sys
import subprocess
import shutil

# TopEFT
from TopEFT.Tools.user import skim_output_directory

#RootTools
from RootTools.core.helpers import checkRootFile

# Logging
import TopEFT.Tools.logger as logger

CMSSW_BASE = os.path.expandvars("$CMSSW_BASE")
cfg_path = os.path.join(CMSSW_BASE, 'src/TopEFT/Generation/production/cfg/')

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--gridpack',    action='store',     default='/afs/hephy.at/data/rschoefbeck02/TopEFT/results/gridpacks/ewkDM_ttZ_ll_DC1A_1p200000.tar.xz',    nargs='?', help="Which gridpack?")
argParser.add_argument('--maxEvents',   action='store',     default=100000,                                                         nargs='?', help="How many events?")
argParser.add_argument('--nJetMax',     action='store',     default=0,                                                              nargs='?', help="How many jets to match?")
argParser.add_argument('--genSampleDir',action='store',     default='/afs/hephy.at/data/rschoefbeck01/TopEFT/genSamples/',          nargs='?', help="Where to store the genSample")
argParser.add_argument('--overwrite',   action='store_true',                                                                        help="Overwrite?")
argParser.add_argument('--overwriteGenFile',   action='store_true',                                                                 help="OverwriteGenFile?")
argParser.add_argument('--keepGenSample',action='store_true',                                                                       help="keep the intermediate gen sample?")
argParser.add_argument('--outDir',      action='store',     default='v2',                                                           nargs='?', help="Where are the gridpacks?")
argParser.add_argument('--cfg',         action='store',     default='$CMSSW_BASE/src/TopEFT/Generation/production/cfg/GEN.py',      help="Which cfg?")
argParser.add_argument('--logLevel',    action='store',     nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )

args = argParser.parse_args()

logger = logger.get_logger(args.logLevel, logFile = None)

# Check if the gridpack exists
if not os.path.exists( args.gridpack ):
    logger.error( "Gridpack %s not found. Exit", args.gridpack )
    sys.exit(0)

gp       = os.path.basename(args.gridpack).rstrip('.tar.xz')

# Check if the output is there
out_file = os.path.join( skim_output_directory, 'gen', args.outDir, gp, gp+'.root') 
if os.path.exists( out_file ) and checkRootFile( out_file, checkForObjects=["Events"] ):
    logger.info( "Found output file %s.", out_file )
    if args.overwrite:
        os.remove( out_file )
        logger.info( "Deleted, because I overwrite." )
    else:
        sys.exit(0)
else:
    logger.info( "Did not find output file %s. Look for gen sample. ", out_file )

# Check if the intermediate gen file is there
gen_file = os.path.join( args.genSampleDir, gp, 'events.root' ) 
if os.path.exists( gen_file ):
    logger.info( "Found edm gen file %s.", gen_file)
    if args.overwriteGenFile:
        os.remove( gen_file )
        logger.info( "Deleted, because I overwrite." )

# Produce the GEN file if needed
if not os.path.exists( gen_file ):
    logger.info( "Making gen file" )
    gen_dir = os.path.join( args.genSampleDir, gp )
    if not os.path.exists(gen_dir): os.makedirs( gen_dir )

    cfg_file = os.path.expandvars( args.cfg )
    if not os.path.exists( cfg_file ):
        logger.error( "cmsrun cfg %s not found. Exit.", cfg_file )
        sys.exit( 1 ) 

    command = "cd {gen_dir}; cmsRun {cfg_file} gridpack={gridpack} maxEvents={maxEvents} nJetMax={nJetMax} outputDir={gen_dir}".format( gen_dir=gen_dir, cfg_file=cfg_file, gridpack=args.gridpack,  maxEvents=args.maxEvents, nJetMax=args.nJetMax)
    logger.debug( "Executing %s", command )
    subprocess.call(command, shell=True)

# Now it should be here either way
if not os.path.exists( gen_file ):
    logger.error( "Edm gen file %s not found. Exit.", gen_file)
    sys.exit(1)

# Run genpostprocessing

command = "python {genPostprocessingScript} --targetDir={outDir} --inputFiles={gen_file} --targetSampleName={gp} --logLevel={logLevel}".format( 
        genPostprocessingScript=os.path.expandvars("$CMSSW_BASE/src/TopEFT/postprocessing/genPostProcessing.py"),
        outDir = args.outDir,
        gen_file = gen_file,
        gp = gp,
        logLevel = args.logLevel
    )
logger.debug( "Executing %s", command )
subprocess.call(command, shell=True)

if not args.keepGenSample and len(gp)>0:
    logger.info( "Clean up %s", os.path.join( args.genSampleDir, gp ) )
    shutil.rmtree( os.path.join( args.genSampleDir, gp ) )
else:
    logger.info( "Keep edm file %s", gen_file )
