#!/usr/bin/env python

# Standard imports
from operator                    import attrgetter
import ROOT

# Logger
import TopEFT.Tools.logger as logger
logger = logger.get_logger("INFO", logFile = None )

# Training variables
read_variables = [\
                    "weight/F",
                    "nLeptons_tight_4l/I",
                    "nBTag/I",
                    "nJetSelected/I",
                    "met_pt/F",
                    "ht/F",
                    "Z1_mass_4l/F",
                    "Z2_mass_4l/F",
                    "lep[pt/F,eta/F]",
                    "nonZ1_l1_index_4l/I",
                    "Z1_pt_4l/F",
                    "jet[pt/F,eta/F]",
                    "nMuons_tight_4l/I",
                    "nElectrons_tight_4l/I",
                    "nlep/I",
                    ]

# sequence 
sequence = []

def flavorBin( event, sample=None):
    event.flavorBin = 0
    if      event.nMuons_tight_4l==4 and event.nElectrons_tight_4l==0: event.flavorBin = 1 
    elif    event.nMuons_tight_4l==3 and event.nElectrons_tight_4l==1: event.flavorBin = 2
    elif    event.nMuons_tight_4l==2 and event.nElectrons_tight_4l==2: event.flavorBin = 3
    elif    event.nMuons_tight_4l==1 and event.nElectrons_tight_4l==3: event.flavorBin = 4
    elif    event.nMuons_tight_4l==0 and event.nElectrons_tight_4l==4: event.flavorBin = 5    
sequence.append( flavorBin )

## met, ht, nonZ1_pt/eta, Z1_pt, nJet, nBTag, lep1_eta
#mva_variables =  {
##                    "met_pt"    :attrgetter("met_pt"), # copy
#                    "ht"        :attrgetter("ht"), # copy
#                    "lnonZ1_pt" :(lambda event: event.lep_pt[event.nonZ1_l1_index_4l]),
#                    "lnonZ1_eta":(lambda event: event.lep_eta[event.nonZ1_l1_index_4l]),
#                    "Z1_pt_4l"  :attrgetter("Z1_pt_4l"),
##                    "lep1_pt"   :(lambda event: event.lep_pt[0]),
##                    "lep2_pt"   :(lambda event: event.lep_pt[1]),
#                    "lep1_eta"  :(lambda event: event.lep_eta[0]),
##                    "lep2_eta"  :(lambda event: event.lep_eta[1]),
#                    "nJetSelected":attrgetter("nJetSelected"),
#                    "nBTag"     :attrgetter("nBTag"),      
##                    "yield"     :(lambda event: event.flavorBin),
##                    "jet1_pt"   :(lambda event: event.jet_pt[0]),
##                    "nLepLoose":(lambda event: event.nlep),
#                    #"myvar1" :(lambda event: event.nBTag), # calculate on the fly
#                    #"myvar2" :(lambda event: event.myFancyVar), # from sequence
#                 }

#mva_variables = {
#                "ht":attrgetter("ht"),
##                "lnonZ1_pt":(lambda event: event.lep_pt[event.nonZ1_l1_index_4l]),
#                "Z1_pt_4l":attrgetter("Z1_pt_4l"),
#                "nJetSelected":attrgetter("nJetSelected"),
#
#                }
#
mva_variables = {
                "mva_ht"          :(lambda event, sample: event.ht),
                "mva_met_pt"      :(lambda event, sample: event.met_pt),
                "mva_nJetSelected":(lambda event, sample: event.nJetSelected),
                "mva_nBTag"       :(lambda event, sample: event.nBTag),
                "mva_flavorBin"   :(lambda event, sample: event.flavorBin),
                }

bdt1 = {
"type"                : ROOT.TMVA.Types.kBDT,
"name"                : "bdt1",
"color"               : ROOT.kGreen,
"options"             : ["!H","!V","NTrees=50","BoostType=Grad","Shrinkage=0.20","UseBaggedBoost","GradBaggingFraction=0.5","SeparationType=GiniIndex","nCuts=500","PruneMethod=NoPruning","MaxDepth=1"],
}

# MaxDepth3?
bdt2 = {
"type"                : ROOT.TMVA.Types.kBDT,
"name"                : "bdt2",
"color"               : ROOT.kYellow,
"options"             : ["!H","!V","NTrees=250","BoostType=Grad","Shrinkage=0.20","UseBaggedBoost","GradBaggingFraction=0.5","SeparationType=GiniIndex","nCuts=250","PruneMethod=NoPruning","MaxDepth=1"],
"mva_variables"       : mva_variables,
}
bdt3 = {
"type"                : ROOT.TMVA.Types.kBDT,
"name"                : "bdt3",
"color"               : ROOT.kBlack,
"options"             : ["!H","!V","NTrees=250","BoostType=Grad","Shrinkage=0.20","UseBaggedBoost","GradBaggingFraction=0.5","SeparationType=GiniIndex","nCuts=1000","PruneMethod=NoPruning","MaxDepth=1"],
"mva_variables"       : mva_variables,
}
bdt4 = {
"type"                : ROOT.TMVA.Types.kBDT,
"name"                : "bdt4",
"color"               : ROOT.kRed,
"options"             : ["!H","!V","NTrees=50","BoostType=Grad","Shrinkage=0.20","UseBaggedBoost","GradBaggingFraction=0.5","SeparationType=GiniIndex","nCuts=250","PruneMethod=NoPruning","MaxDepth=1"],
"mva_variables"       : mva_variables,
}

mlp1 = {
"type"                : ROOT.TMVA.Types.kMLP,
"name"                : "mlp1",
#"layers"              : [3],
"layers"              : "N+3",
"color"               : ROOT.kRed+5,
"options"             : ["!H","!V","VarTransform=Norm,Deco","NeuronType=sigmoid","NCycles=10000","TrainingMethod=BP","LearningRate=0.03", "DecayRate=0.01","Sampling=0.3","SamplingEpoch=0.8","ConvergenceTests=1","CreateMVAPdfs=True","TestRate=10" ],
"mva_variables"       : mva_variables,
}

## Samples
#from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
#
##signal      = yt_TWZ
##signal2     = TWZ
#signal  = yt_TZZ
#signal2 = ZZ
#
##print "yt_TZZ", signal.chain.CopyTree(selectionString).GetEntries()
##print "ZZ", signal2.chain.CopyTree(selectionString).GetEntries()
##print "yt_TWZ", signal.chain.CopyTree(selectionString).GetEntries()
##print "TWZ", signal2.chain.CopyTree(selectionString).GetEntries()
#
##exit()
#
##backgrounds = [ TTZtoLLNuNu ]
#backgrounds = [ ZZ ]
#samples = backgrounds + [signal]
#for sample in samples:
#    sample.setSelectionString( selectionString )
#    if args.small:
#        sample.reduceFiles(to = 1)
#
### TMVA Trainer instance
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
#weightString = "(1)"
#trainer.createTestAndTrainingSample( 
#    read_variables   = read_variables,   
#    sequence         = sequence,
#    weightString     = weightString,
#    overwrite        = args.overwrite, 
#    )
#
#trainer.addMethod(method = default_methods["BDT"])
#trainer.addMethod(method = default_methods["MLP"])



#ncuts 250
#trainer.addMethod(method = bdt1)
#trainer.addMethod(method = bdt2)
#trainer.addMethod(method = bdt3)
#trainer.addMethod(method = bdt4)
#trainer.addMethod(method = mlp1)

#trainer.trainMVA( factory_settings = default_factory_settings )
#trainer.plotEvaluation()

#reader = Reader( 
#    mva_variables    = mva_variables, 
#    output_directory = mva_directory,
#    label            = "Test")

#reader.addMethod(method = default_methods["BDT"])
#reader.addMethod(method = default_methods["MLP"])

#print reader.evaluate("BDT", met_pt=100, ht=-210, Z1_pt_4l=100, lnonZ1_pt=100, lnonZ1_eta=0)
#print reader.evaluate("BDT", met_pt=120, ht=-210)
