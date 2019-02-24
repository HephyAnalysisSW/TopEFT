''' Analysis script for 1D 2l plots (RootTools)
'''

#Standard imports
import ROOT
from math import sqrt, cos, sin, pi, acos
import itertools,os
import copy

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel', action='store', default='INFO', nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',    action='store_true', help="Reduce number of events")
args = argParser.parse_args()


#RootTools
from RootTools.core.standard import *
from TopEFT.Tools.user import data_directory

data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *

from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter
import TopEFT.Tools.logger as logger

import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)


dirs = {}
dirs['TTZToLLNuNu_ext'] = ['TTZToLLNuNu_amc_psw']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

sample  = Sample.fromDirectory(name="TTZ_NLO", treeName="Events", isData=False, color=color.TTJets, texName="t#bar{t}Z (NLO)", directory=directories['TTZToLLNuNu_ext'])

if args.small: sample.reduceFiles(to=1)

selection = cutInterpreter.cutString('trilep-Zcand-lepSelTTZ-njet3p-btag1p-onZ')

weight_central  = "weight * LHEweight_wgt[9]/genWeight"
weight_reweight = "weight * LHEweight_wgt[972]/genWeight"

# LO
logger.info("Working on ptZ plots")
h_ptZ_c     = sample.get1DHistoFromDraw( "Z_pt", selectionString = selection, binning = [50,0,500],  addOverFlowBin = 'upper', weightString = weight_central )
h_ptZ_r     = sample.get1DHistoFromDraw( "Z_pt", selectionString = selection, binning = [50,0,500],  addOverFlowBin = 'upper', weightString = weight_reweight )

logger.info("Working on cosThetaStar plots")
h_cosTh_c   = sample.get1DHistoFromDraw( "cosThetaStar", selectionString = selection, binning = [10,-1,1],  addOverFlowBin = 'upper', weightString = weight_central )
h_cosTh_r   = sample.get1DHistoFromDraw( "cosThetaStar", selectionString = selection, binning = [10,-1,1],  addOverFlowBin = 'upper', weightString = weight_reweight )

logger.info("Working on nJet plots")
h_nJet_c    = sample.get1DHistoFromDraw( "nJetSelected", selectionString = selection, binning = [6,3,9],  addOverFlowBin = 'upper', weightString = weight_central )
h_nJet_r    = sample.get1DHistoFromDraw( "nJetSelected", selectionString = selection, binning = [6,3,9],  addOverFlowBin = 'upper', weightString = weight_reweight )

logger.info("Working on nBTag plots")
h_nBTag_c   = sample.get1DHistoFromDraw( "nBTag", selectionString = selection, binning = [4,1,5],  addOverFlowBin = 'upper', weightString = weight_central )
h_nBTag_r   = sample.get1DHistoFromDraw( "nBTag", selectionString = selection, binning = [4,1,5],  addOverFlowBin = 'upper', weightString = weight_reweight )

hists = [h_ptZ_c,h_ptZ_r,h_cosTh_c,h_cosTh_r,h_nJet_c,h_nJet_r,h_nBTag_c,h_nBTag_r]
plotTuples = [(h_ptZ_c,h_ptZ_r), (h_cosTh_c,h_cosTh_r), (h_nJet_c,h_nJet_r), (h_nBTag_c,h_nBTag_r)]

for h in hists:
    h.Scale(1/h.Integral()) 

for t in plotTuples:
    t[0].style = styles.lineStyle( ROOT.kRed+1,  width=2, errors=True )
    t[0].legendText = "NNPDF3.1 nnlo"
    t[1].style = styles.lineStyle( ROOT.kGreen+2,  width=2, errors=True )
    t[1].legendText = "NNPDF3.0 nlo"

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

postFix = "_small" if args.small else ""
plotDir = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/PDF"+postFix

plots = [[ h_ptZ_c ], [ h_ptZ_r ]]

plotting.draw(
    Plot.fromHisto("TTZ_ptZ", plots, texX = "p_{T}(Z) (GeV)"),
    plot_directory = plotDir,
    logX = False, logY = True, 
    #yRange = (0.03, 0.2),
    ratio = {'yRange': (0.88, 1.12)},
    drawObjects = drawObjects(),
    copyIndexPHP = True,
)


plots = [[ h_cosTh_c ], [ h_cosTh_r ]]

plotting.draw(
    Plot.fromHisto("TTZ_cosThetaStar", plots, texX = "cos(#Theta*)"),
    plot_directory = plotDir,
    logX = False, logY = True, 
    #yRange = (0.03, 0.2),
    ratio = {'yRange': (0.88, 1.12)},
    drawObjects = drawObjects(),
    copyIndexPHP = True,
)


plots = [[ h_nJet_c ], [ h_nJet_r ]]

plotting.draw(
    Plot.fromHisto("TTZ_nJetSelected", plots, texX = "N_{j}"),
    plot_directory = plotDir,
    logX = False, logY = True, 
    yRange = (0.03, 1.3),
    ratio = {'yRange': (0.88, 1.12)},
    drawObjects = drawObjects(),
    copyIndexPHP = True,
)


plots = [[ h_nBTag_c ], [ h_nBTag_r ]]

plotting.draw(
    Plot.fromHisto("TTZ_nBTag", plots, texX = "N_{b-tag}"),
    plot_directory = plotDir,
    logX = False, logY = True, 
    yRange = (0.03, 1.3),
    ratio = {'yRange': (0.88, 1.12)},
    drawObjects = drawObjects(),
    copyIndexPHP = True,
)

