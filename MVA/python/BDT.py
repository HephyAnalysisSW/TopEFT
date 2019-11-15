#!/usr/bin/env python

from Analysis.TMVA.Trainer       import Trainer
from Analysis.TMVA.Reader        import Reader
from Analysis.TMVA.defaults      import default_methods, default_factory_settings 
from TopEFT.Tools.user           import plot_directory
from TopEFT.Tools.user           import mva_directory 
from TopEFT.Tools.cutInterpreter import *
from operator                    import attrgetter

# Arguments
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--plot_directory',     action='store',             default=None)
#argParser.add_argument('--selection',          action='store', type=str,   default="quadlepTWZ-onZ1-noZ2")#-btag1-njet1p")#None)
argParser.add_argument('--selection',          action='store', type=str,   default="btag1-njet1p")#-btag1-njet1p")#None)
argParser.add_argument('--trainingFraction',   action='store', type=float, default=0.5)
argParser.add_argument('--small',              action='store_true')
argParser.add_argument('--overwrite',          action='store_true')

import Analysis.Tools.logger as logger
logger = logger.get_logger("INFO", logFile = None )

args = argParser.parse_args()

if args.plot_directory == None:
    args.plot_directory = plot_directory

if args.selection == None:
    selectionString = "(1)"
else:
    selectionString = cutInterpreter.cutString( args.selection )

# Samples
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

signal      = TWZ
backgrounds = [ TTZtoLLNuNu ]
samples = backgrounds + [signal]
for sample in samples:
    sample.setSelectionString( selectionString )
    if args.small:
        sample.reduceFiles(to = 1)

# Training variables
weightString = "weight"
read_variables = [\
                    "weight/F",
                    "nLeptons_tight_4l/I",
                    "nBTag/I",
                    "met_pt/F",
                    "ht/F",
                    "Z1_mass_4l/F",
                    "Z2_mass_4l/F",
                    ]

# sequence 
sequence = []
def myFancyVar( event ):
    event.myFancyVar = 2*event.nBTag
sequence.append( myFancyVar )

mva_variables =  {
                    "met_pt":attrgetter("met_pt"), # copy
                    "ht"    :attrgetter("ht"), # copy
                    #"myvar1" :(lambda event: event.nBTag), # calculate on the fly
                    #"myvar2" :(lambda event: event.myFancyVar), # from sequence
                 }

## TMVA Trainer instance
#trainer = Trainer( 
#    signal = signal, 
#    backgrounds = backgrounds, 
#    output_directory = mva_directory, 
#    plot_directory   = plot_directory, 
#    mva_variables    = mva_variables,
#    label            = "Test", 
#    fractionTraining = args.trainingFraction, 
#    )
#
#trainer.createTestAndTrainingSample( 
#    read_variables   = read_variables,   
#    sequence         = sequence,
#    weightString     = weightString,
#    overwrite        = args.overwrite, 
#    )
#
#trainer.addMethod(method = default_methods["BDT"])
#trainer.addMethod(method = default_methods["MLP"])
#
#trainer.trainMVA( factory_settings = default_factory_settings )
#trainer.plotEvaluation()

reader = Reader( 
    mva_variables    = mva_variables, 
    output_directory = mva_directory,
    label            = "Test")

reader.addMethod(method = default_methods["BDT"])
#reader.addMethod(method = default_methods["MLP"])

print reader.evaluate("BDT", met_pt=100, ht=-210)
print reader.evaluate("BDT", met_pt=120, ht=-210)
