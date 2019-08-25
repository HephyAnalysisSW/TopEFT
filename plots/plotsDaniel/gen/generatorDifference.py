# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',        action='store',      default='INFO',  nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--makePlots',        action='store_true',       help="Make reweighting matrix plots?")
args = argParser.parse_args()

# Logger
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

from TopEFT.Analysis.run.SignalReweightingTemplate import *

makePlot = True

# Benchmarks for testing
from TopEFT.samples.gen_fwlite_benchmarks import *
from TopEFT.Tools.user import results_directory, plot_directory

cacheDir = os.path.join( results_directory, 'TTZ_MC_ReweightingTemplate' )

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v20/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2017_mva_v17/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *

source_gen = TTZtoLLNuNu
target_gen = TTZtoLLNuNu_17

signalReweighting = SignalReweighting( source_sample = source_gen, target_sample = target_gen, cacheDir = cacheDir, template_draw_string = 'genZ_pt:genZ_cosThetaStar')

signalReweighting.cosThetaStar_binning = [ -1., -0.6, -0.2, 0.2, 0.6, 1. ]
signalReweighting.Z_pt_binning         = [ 0, 100, 200, 300, 400, 1000 ]


# reweighting selection
selection = "genZ_pt>0"#abs(genZ_mass-91.2)<10"#&&(abs(genZ_daughter_flavor)==11 || abs(genZ_daughter_flavor)==13 || abs(genZ_daughter_flavor)==15 )"

# reweighting function
f = signalReweighting.cachedReweightingFunc( selection, weight="weight" )

# plot the reweighting matrix
if args.makePlots:
    matrix = signalReweighting.cachedTemplate( selection, overwrite=False, weight="weight" )

    matrixPlot = Plot2D.fromHisto( target_gen.name, texY = "p_{T}(Z)", texX = "cos(#Theta*)", histos = [[matrix]])
    matrixPlot.drawOption = "colz etext"

    def optimizeLogZ(histo):
        histo.GetZaxis().SetMoreLogLabels()
        histo.GetZaxis().SetNoExponent()

    ROOT.gStyle.SetPaintTextFormat("2.2f")
    plotting.draw2D( matrixPlot, plot_directory = os.path.join( plot_directory, 'TTZ_MC_reweightingMatrices', source_gen.name), logY = False, logZ = False, copyIndexPHP = True, zRange = [0.80, 1.20], extensions = ["png","pdf"], histModifications = [optimizeLogZ])

