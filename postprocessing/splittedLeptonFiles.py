# Standard imports
import ROOT
import os
import sys
from fnmatch import fnmatch
import importlib

# RootTools
from RootTools.core.Sample import *

# TopEFT
from TopEFT.Tools.user import skim_output_directory

# parser
def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--logLevel',                    action='store',         nargs='?',              choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET', 'SYNC'],     default='INFO',                     help="Log level for logging")
    #argParser.add_argument('--overwrite',                   action='store_true',                                                                                        help="Overwrite existing output files, bool flag set to True  if used")
    argParser.add_argument('--year',                        action='store',                     type=int,   choices=[2016,2017],    required = True,                    help="Which year?")
    argParser.add_argument('--sample',                      action='store',         nargs='?',  type=str,                           default='WZTo3LNu',                help="List of samples to be post-processed, given as CMG component name")
    argParser.add_argument('--nJobs',                       action='store',         nargs='?',  type=int,                           default=1,                          help="Maximum number of simultaneous jobs.")
    argParser.add_argument('--job',                         action='store',                     type=int,                           default=0,                          help="Run only job i")
    #argParser.add_argument('--targetDir',                   action='store',         nargs='?',  type=str,                           default=user.postprocessing_output_directory, help="Name of the directory the post-processed files will be saved")
    argParser.add_argument('--small',                       action='store_true',                                                                                        help="Run the file on a small sample (for test purpose), bool flag set to True if used")
    argParser.add_argument('--forceProxy',                  action='store_true',                                                                                        help="Don't check certificate")
    argParser.add_argument('--version',                     action='store',         nargs='?',  type=str,  required = True,         help="Version for output directory")

    return argParser

options = get_parser().parse_args()

# Logging
import TopEFT.Tools.logger as logger
logger  = logger.get_logger(options.logLevel, logFile = None)
import RootTools.core.logger as logger_rt
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None )

maxN = 2 if options.small else None

if options.year == 2016:
    module_ = 'CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2'
    MCgeneration = "Summer16"
    from TopEFT.samples.heppy_dpm_samples import lepton_2016_heppy_mapper as lepton_heppy_mapper
else:
    module_ = 'CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD'
    MCgeneration = "Fall17"
    from TopEFT.samples.heppy_dpm_samples import lepton_2017_heppy_mapper as lepton_heppy_mapper

try:
    heppy_sample = getattr(importlib.import_module( module_ ), options.sample)
except:
    raise ValueError( "Could not load sample '%s' from %s "%( options.sample, module_ ) )


sample = lepton_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
    
if sample is None or len(sample.files)==0:
    logger.info( "Sample %r is empty. Exiting" % sample )
    sys.exit(-1)
else:
    logger.info( "Sample %s has %i files", sample.name, len(sample.files))

len_orig = len(sample.files)
sample = sample.split( n=options.nJobs, nSub=options.job)
logger.info( " Run over %i/%i files for job %i/%i."%(len(sample.files), len_orig, options.job, options.nJobs))
logger.debug( "Files to be run over:\n%s", "\n".join(sample.files) )

#output directory

output_directory = os.path.join( skim_output_directory, options.version+('_small' if options.small else ''), str(options.year) ) 

leptonClasses  = [{'Name':'Prompt', 'Var': 'lep_isPromptId'}, {'Name':'NonPrompt', 'Var': 'lep_isNonPromptId'}, {'Name':'Fake', 'Var': 'lep_isFakeId'}]
leptonFlavours = [
                    {'Name':'muo', 'pdgId': 13},
                    {'Name':'ele', 'pdgId': 11}, 
                 ]

#pt cuts
ptCuts = [[10,float("inf")]]

#make FileList
pattern  = 'tree.root'

#helper TChain for CloneTree
ch = ROOT.TChain('tree')
ch.Add(sample.files[0])
#inputFileList = TestFileList

postfix = '' if options.nJobs==1 else "_%i" % options.job

for leptonFlavour in leptonFlavours:
    for leptonClass in leptonClasses:
        for ptCut in ptCuts:
            output_filename = os.path.join( output_directory, 
                                            leptonFlavour['Name'], 
                                            leptonClass['Name'], 
                                            'pt_%i_to_%s' %( ptCut[0], 'inf' if ptCut[1]==float("inf") else str(ptCut[1]) ),
                                            sample.name,
                                            'lepton%s.root'%postfix )

            dirname = os.path.dirname( output_filename )
            if not os.path.exists( dirname ):
                os.makedirs( dirname )

            outputFile     = ROOT.TFile(output_filename, 'recreate')
            outputFileTree = ch.CloneTree(0,"")

            for inputFile in sample.files:
                readFile     = ROOT.TFile.Open(inputFile, 'read')
                readFileTree = readFile.Get('tree')
                readFileTree.CopyAddresses(outputFileTree)

                pdgId     = readFileTree.GetLeaf("lep_pdgId")
                isClassId = readFileTree.GetLeaf(leptonClass["Var"])
                pt        = readFileTree.GetLeaf("lep_pt")

                for i in xrange(readFileTree.GetEntries()):
                    pdgId.GetBranch().GetEntry(i)
                    isClassId.GetBranch().GetEntry(i)
                    pt.GetBranch().GetEntry(i)

                    lep_pdgId     = pdgId.GetValue()
                    lep_isClassId = isClassId.GetValue()
                    lep_pt        = pt.GetValue()

                    #print lep_pdgId, lep_isClassId 
                    if abs(lep_pdgId)==leptonFlavour["pdgId"] and lep_isClassId==1 and lep_pt>ptCut[0] and lep_pt<=ptCut[1]:
                        inputEntry = readFileTree.GetEntry(i)
                        readFileTree.CopyAddresses(outputFileTree)
                        outputEntry = outputFileTree.Fill()
                        if inputEntry!=outputEntry:
                            print ("error while copying entry")
                            break
                readFile.Close()

            print ("%i entries copied to %s" %(outputFileTree.GetEntries(), output_filename))
            outputFile.Write(output_filename, outputFile.kOverwrite)
            outputFile.Close()

