''' Analysis script for 1D 2l plots (RootTools)
'''

#Standard imports
import ROOT
from math import sqrt, cos, sin, pi, acos
import itertools,os
import copy

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
args = argParser.parse_args()


#RootTools
from RootTools.core.standard import *
from TopEFT.Tools.user import data_directory

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_v14/trilep/"

from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter
import TopEFT.Tools.logger as logger

import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)


dirs = {}
dirs['TTZ_LO']          = ["TTZ_LO"]
dirs['TTZToLLNuNu_ext'] = ['TTZToLLNuNu_ext']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

sample  = Sample.fromDirectory(name="TTZ_LO", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}Z (LO)", directory=directories['TTZ_LO'])
sample2 = Sample.fromDirectory(name="TTZ_NLO", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}Z, Z#rightarrowll (NLO)", directory=directories['TTZToLLNuNu_ext'])

data_directory = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_v20/trilep/"

dirs = {}
dirs['WZTo3LNu_amcatnlo']   = ["WZTo3LNu_amcatnlo"]
dirs['WZTo3LNu']     = ['WZTo3LNu']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

sample  = Sample.fromDirectory(name="WZTo3LNu_amcatnlo", treeName="Events", isData=False, color=color.TTJets, texName="WZ MG (NLO)", directory=directories['WZTo3LNu_amcatnlo'])
sample2 = Sample.fromDirectory(name="WZTo3LNu_powheg", treeName="Events", isData=False, color=color.TTJets, texName="WZ powheg (NLO)", directory=directories['WZTo3LNu'])


selection = cutInterpreter.cutString('trilep-Zcand-lepSelTTZ-njet3p-btag1p-onZ')
WZselection = cutInterpreter.cutString('trilep-looseVeto-Zcand-lepSelTTZ-njet0p-btag0-onZloose')

selection = WZselection

weight_central  = "weight"
weight_reweight = "weight * reweightTopPt"

# binning
binning = [25,0,500]
binning = [10,0,500]

binningCTS = [10,-1,1]
# LO
h_central   = sample.get1DHistoFromDraw( "Z_pt", selectionString = selection, binning = binning,  addOverFlowBin = 'upper', weightString = weight_central )
h_reweight  = sample.get1DHistoFromDraw( "Z_pt", selectionString = selection, binning = binning,  addOverFlowBin = 'upper', weightString = weight_reweight )
h_central.style = styles.lineStyle( ROOT.kRed,  width=2, errors=True )
h_reweight.style = styles.lineStyle( ROOT.kBlue, width=2, errors=True )

h_CTS_central   = sample.get1DHistoFromDraw( "cosThetaStar", selectionString = selection, binning = binningCTS,  addOverFlowBin = 'upper', weightString = weight_central )
h_CTS_reweight  = sample.get1DHistoFromDraw( "cosThetaStar", selectionString = selection, binning = binningCTS,  addOverFlowBin = 'upper', weightString = weight_reweight )
h_CTS_central.style = styles.lineStyle( ROOT.kRed,  width=2, errors=True )
h_CTS_reweight.style = styles.lineStyle( ROOT.kBlue, width=2, errors=True )


# NLO
h_central_NLO   = sample2.get1DHistoFromDraw( "Z_pt", selectionString = selection, binning = binning,  addOverFlowBin = 'upper', weightString = weight_central )
h_reweight_NLO  = sample2.get1DHistoFromDraw( "Z_pt", selectionString = selection, binning = binning,  addOverFlowBin = 'upper', weightString = weight_reweight )
h_central_NLO.style = styles.lineStyle( ROOT.kOrange, width=2, errors=True )
h_reweight_NLO.style = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )

h_CTS_central_NLO   = sample2.get1DHistoFromDraw( "cosThetaStar", selectionString = selection, binning = binningCTS,  addOverFlowBin = 'upper', weightString = weight_central )
h_CTS_reweight_NLO  = sample2.get1DHistoFromDraw( "cosThetaStar", selectionString = selection, binning = binningCTS,  addOverFlowBin = 'upper', weightString = weight_reweight )
h_CTS_central_NLO.style = styles.lineStyle( ROOT.kOrange, width=2, errors=True )
h_CTS_reweight_NLO.style = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )


#h_central.legendText = "t#bar{t}Z (LO)"
h_central.legendText = "WZ MG (NLO)"
h_reweight.legendText = "t#bar{t}Z (LO), p_{T}(t) reweighted"
#h_central_NLO.legendText = "t#bar{t}Z, Z#rightarrowll (NLO)"
h_central_NLO.legendText = "WZ powheg (NLO)"
h_reweight_NLO.legendText = "t#bar{t}Z, Z#rightarrowll (NLO), p_{T}(t) rew."

h_CTS_central.legendText = "t#bar{t}Z (LO)"
h_CTS_reweight.legendText = "t#bar{t}Z (LO), p_{T}(t) reweighted"
h_CTS_central_NLO.legendText = "t#bar{t}Z, Z#rightarrowll (NLO)"
h_CTS_reweight_NLO.legendText = "t#bar{t}Z, Z#rightarrowll (NLO), p_{T}(t) rew."


def drawObjects( ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Simulation'),
      (0.75, 0.95, 'MC (13 TeV)' )
    ]
    return [tex.DrawLatex(*l) for l in lines]

#plots = [[ h_central ], [ h_reweight ]]
#plots = [[ h_central ], [ h_central_NLO ]]
plots = [[ h_central ], [ h_central_NLO ]]

plotting.draw(
    Plot.fromHisto("WZ_Z_pt",
                plots,
                texX = "p_{T}(Z) (GeV)"
            ),
    plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/topPt/",
    logX = False, logY = True, #sorting = True, 
    #yRange = (0.008,3.),
    yRange = (0.03, 150.),
    #yRange = (0.03, [0.001,0.5]),
    ratio = {'yRange': (0.88, 1.12)},
    #ratio = {'yRange': (0.5, 1.5)},
    scaling = {0:1},
    drawObjects = drawObjects()
)

#plots = [[ h_CTS_central ], [ h_CTS_reweight ]]
##plots = [[ h_CTS_central ], [ h_CTS_central_NLO ]]
##plots = [[ h_CTS_central_NLO ], [ h_CTS_reweight_NLO ]]
#
#plotting.draw(
#    Plot.fromHisto("cosThetaStar_topPtReweighted",
#                plots,
#                texX = "cos(#theta*)"
#            ),
#    plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/topPt/",
#    logX = False, logY = True, #sorting = True, 
#    yRange = (0.008,3.),
#    #yRange = (0.03, [0.001,0.5]),
#    ratio = {'yRange': (0.88, 1.12)},
#    scaling = {0:1},
#    drawObjects = drawObjects()
#)

