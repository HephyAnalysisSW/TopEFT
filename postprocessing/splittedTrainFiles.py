# Standard imports
import ROOT
import os
import sys
import importlib
import random

# RootTools
from RootTools.core.Sample import *

# TopEFT
from TopEFT.Tools.user import skim_output_directory as input_directory
from TopEFT.Tools.user import trainingFiles_directory as output_directory
#from TopEFT.postprocessing.deepLeptonSamplesForTraining import deepLeptonSignalSamples, deepLeptonBackgroundSamples

def deepLeptonSignalSamples(year):

    if year==2016:
        SignalSamples = [

        'TTJets_SingleLeptonFromTbar',
        'TTJets_SingleLeptonFromTbar_ext',
        'TTJets_SingleLeptonFromT',
        'TTJets_SingleLeptonFromT_ext',

        'TTJets_DiLepton',
        'TTJets_DiLepton_ext',

        #'TTJets',
        #'TTJets_LO',
        #'TT_pow_ext3',
        #'TT_pow',
        #'TTLep_pow',
        #'TTSemiLep_pow',
        #'TTJets_LO_HT600to800_ext',
        #'TTJets_LO_HT800to1200_ext',
        #'TTJets_LO_HT1200to2500_ext',
        #'TTJets_LO_HT2500toInf_ext',

                        ]

    if year==2017:
        SignalSamples = [

        #'TTJets',
        #'TTLep_pow',
        #'TTHad_pow',
        #'TTSemi_pow',
        'TTJets_SingleLeptonFromT',
        #'TTLep_pow_TuneDown',
        #'TTLep_pow_TuneUp',
        #'TTLep_pow_hdampDown',
        #'TTLep_pow_hdampUp',

                        ]

    return SignalSamples

def deepLeptonBackgroundSamples(year):

    if year==2016:
        BackgroundSamples = [

        'QCD_Pt20to30_EMEnriched',
        'QCD_Pt30to50_EMEnriched',
        'QCD_Pt30to50_EMEnriched_ext',
        'QCD_Pt50to80_EMEnriched_ext',
        'QCD_Pt80to120_EMEnriched_ext',
        'QCD_Pt120to170_EMEnriched',
        'QCD_Pt170to300_EMEnriched',
        'QCD_Pt300toInf_EMEnriched',

        'QCD_Pt_20to30_bcToE',
        'QCD_Pt_30to80_bcToE',
        'QCD_Pt_80to170_bcToE',
        'QCD_Pt_170to250_bcToE',
        'QCD_Pt_250toInf_bcToE',

        'QCD_Pt15to20_Mu5',
        'QCD_Pt20to30_Mu5',
        'QCD_Pt30to50_Mu5',
        'QCD_Pt50to80_Mu5',
        'QCD_Pt80to120_Mu5',
        'QCD_Pt80to120_Mu5_ext',
        'QCD_Pt120to170_Mu5',
        'QCD_Pt170to300_Mu5',
        'QCD_Pt170to300_Mu5_ext',
        'QCD_Pt300to470_Mu5',
        'QCD_Pt300to470_Mu5_ext',
        'QCD_Pt300to470_Mu5_ext2',
        'QCD_Pt470to600_Mu5',
        'QCD_Pt470to600_Mu5_ext',
        'QCD_Pt470to600_Mu5_ext2',
        'QCD_Pt600to800_Mu5',
        'QCD_Pt600to800_Mu5_ext',
        'QCD_Pt800to1000_Mu5',
        'QCD_Pt800to1000_Mu5_ext',
        'QCD_Pt800to1000_Mu5_ext2',
        'QCD_Pt1000toInf_Mu5',
        'QCD_Pt1000toInf_Mu5_ext',

                        ]
    if year==2017:
        BackgroundSamples = [

        'QCD_Pt15to20_EMEnriched',
        'QCD_Pt20to30_EMEnriched',
        'QCD_Pt30to50_EMEnriched',
        'QCD_Pt50to80_EMEnriched',
        'QCD_Pt80to120_EMEnriched',
        'QCD_Pt120to170_EMEnriched',
        'QCD_Pt170to300_EMEnriched',
        'QCD_Pt300toInf_EMEnriched',

        'QCD_Pt15to20_bcToE',
        'QCD_Pt20to30_bcToE',
        'QCD_Pt30to80_bcToE',
        'QCD_Pt80to170_bcToE',
        'QCD_Pt170to250_bcToE',
        'QCD_Pt250toInf_bcToE',

        'QCD_Pt15to20_Mu5',
        'QCD_Pt20to30_Mu5',
        'QCD_Pt30to50_Mu5',
        'QCD_Pt50to80_Mu5',
        'QCD_Pt80to120_Mu5',
        'QCD_Pt120to170_Mu5',
        'QCD_Pt170to300_Mu5',
        'QCD_Pt300to470_Mu5',
        'QCD_Pt470to600_Mu5',
        'QCD_Pt600to800_Mu5',
        'QCD_Pt800to1000_Mu5',
        'QCD_Pt1000toInf_Mu5',

                        ]

    return BackgroundSamples


#settings
ptSelection   = 'pt_10_to_inf'
sampleSelection = 'SlDlTTJetsVsQCD'
#sampleSelection = 'TTJetsVsQCD'

#parser
def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--year',                        action='store',                     type=int,   choices=[2016,2017],    required = True,               help="Which year?")
    argParser.add_argument('--sample',                      action='store',         nargs='?',  type=str,                           default='WZTo3LNu',            help="List of samples to be post-processed, given as CMG component name")
    argParser.add_argument('--nJobs',                       action='store',         nargs='?',  type=int,                           default=1,                     help="Maximum number of simultaneous jobs.")
    argParser.add_argument('--job',                         action='store',                     type=int,                           default=0,                     help="Run only job i")
    argParser.add_argument('--version',                     action='store',         nargs='?',  type=str,  required = True,                                        help="Version for output directory")
    argParser.add_argument('--flavour',                     action='store',                     type=str,   choices=['ele','muo'],    required = True,             help="Which flavour?")

    return argParser

options = get_parser().parse_args()
#
## Logging
#import TopEFT.Tools.logger as logger
#logger  = logger.get_logger(options.logLevel, logFile = None)
#import RootTools.core.logger as logger_rt
#logger_rt = logger_rt.get_logger(options.logLevel, logFile = None )

#define signal and background samples
samplesPrompt    = deepLeptonSignalSamples(options.year)
samplesNonPrompt = deepLeptonBackgroundSamples(options.year)
samplesFake      = samplesNonPrompt


#define structure
leptonClasses  = [
                    {'Name':'Prompt',    'Var':'lep_isPromptId',    'SampleList':samplesPrompt,    'TChain':ROOT.TChain('tree'), 'Entries':0 }, 
                    {'Name':'NonPrompt', 'Var':'lep_isNonPromptId', 'SampleList':samplesNonPrompt, 'TChain':ROOT.TChain('tree'), 'Entries':0 }, 
                    {'Name':'Fake',      'Var':'lep_isFakeId',      'SampleList':samplesFake,      'TChain':ROOT.TChain('tree'), 'Entries':0 },
                 ]
leptonFlavours = [
                    {'Name':options.flavour, 'pdgId': 11 if options.flavour=='ele' else 13},
                 ]

postfix = '' if options.nJobs==1 else "_%i" % options.job

#Loop
for leptonFlavour in leptonFlavours:
    leptonClasses[0]['TChain'] = ROOT.TChain('tree')
    leptonClasses[1]['TChain'] = ROOT.TChain('tree')
    leptonClasses[2]['TChain'] = ROOT.TChain('tree')

    for leptonClass in leptonClasses:
        inputPath = os.path.join( input_directory, options.version, str(options.year), leptonFlavour['Name'], leptonClass['Name'], ptSelection)
        inputList = [(os.path.join( inputPath, s )) for s in leptonClass['SampleList']]
        selectionString = '(evt%'+str(options.nJobs)+'=='+str(options.job)+')'
        classSample = Sample.fromDirectory( leptonClass['Name'], inputList, 'tree', None, selectionString) 
        #print classSample.files

        for sampleFile in classSample.files:
                
            leptonClass['TChain'].Add(sampleFile)
 
        leptonClass['TChain'] = leptonClass['TChain'].CopyTree(classSample.selectionString)
 
        leptonClass['Entries'] = leptonClass['TChain'].GetEntries()
        print leptonFlavour['Name'], leptonClass['Name'], leptonClass['Entries']

    x = [['Prompt', 'NonPrompt', 'Fake'], [leptonClass['Entries'] for leptonClass in leptonClasses]]
    y = sum(([t] * w for t, w in zip(*x)), [])
    #for i in range(20):
    #    print(random.choice(y))

    n_maxfileentries = 100000
    n_actualentries  = 0
    n_file           = 1

    n_Prompt    = leptonClasses[0]['Entries']
    n_NonPrompt = leptonClasses[1]['Entries']
    n_Fake      = leptonClasses[2]['Entries']

    chPrompt    = leptonClasses[0]['TChain']
    chNonPrompt = leptonClasses[1]['TChain']
    chFake      = leptonClasses[2]['TChain']

    counter  = {'Prompt': 1, 'NonPrompt': 1, 'Fake': 1}
    nEntries = {'Prompt': n_Prompt, 'NonPrompt': n_NonPrompt, 'Fake': n_Fake}
    TChain   = {'Prompt': chPrompt, 'NonPrompt': chNonPrompt, 'Fake': chFake}

    outputPath = os.path.join( output_directory, options.version, str(options.year), leptonFlavour['Name'], ptSelection, sampleSelection, 'modulo_'+str(options.job)+'_trainfile_' )
    dirname = os.path.dirname( outputPath )
    if not os.path.exists( dirname ):
        os.makedirs( dirname )

    while (counter['Prompt']<n_Prompt and counter['NonPrompt']<n_NonPrompt and counter['Fake']<n_Fake):

        #(re)create and save output files
        if n_actualentries==0 and n_file==1:
            outputFile     = ROOT.TFile(str(outputPath)+str(n_file)+'.root', 'recreate')
            outputFileTree = chFake.CloneTree(0,"")
        if n_actualentries==0 and n_file>=2:
            print ("%i entries copied to %s" % (outputFileTree.GetEntries(), outputPath+str(n_file-1)+".root"))
            print (counter['Prompt'], counter['NonPrompt'], counter['Fake'])
            outputFile.Write(outputPath+str(n_file-1)+".root", outputFile.kOverwrite)
            outputFile.Close()
            outputFile     = ROOT.TFile(outputPath+str(n_file)+".root", 'recreate')
            outputFileTree = chFake.CloneTree(0,"")

        #write lepton from random class into output file
        leptonClass  = random.choice(y)
        inputEntry   = TChain[leptonClass].GetEntry(counter[leptonClass])
        TChainTree   = TChain[leptonClass].GetTree()

        TChainTree.CopyAddresses(outputFileTree)
        outputEntry  = outputFileTree.Fill()
        if inputEntry!=outputEntry: 
            print ("error while copying entry")
            break 
       
        #increase counters
        counter[leptonClass] += 1
        n_actualentries += 1

        #check if maximal file entries reached
        if n_actualentries>=n_maxfileentries:
            n_actualentries=0
            n_file += 1

    #Save and Close last output File        
    print ("%i entries copied to %s" % (outputFileTree.GetEntries(), outputPath+str(n_file)+".root"))
    print (counter['Prompt'], counter['NonPrompt'], counter['Fake'])
    outputFile.Write(outputPath+str(n_file)+".root", outputFile.kOverwrite)
    outputFile.Close()

