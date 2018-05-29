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


data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v7/trilep/"

dirs = {}
dirs['WZTo3LNu_amcatnlo']   = ["WZTo3LNu_amcatnlo"]
dirs['WZTo3LNu']     = ['WZTo3LNu_comb']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

WZ_amc  = Sample.fromDirectory(name="WZTo3LNu_amcatnlo", treeName="Events", isData=False, color=color.TTJets, texName="WZ MG (NLO)", directory=directories['WZTo3LNu_amcatnlo'])
WZ_pow = Sample.fromDirectory(name="WZTo3LNu_powheg", treeName="Events", isData=False, color=color.TTJets, texName="WZ powheg (NLO)", directory=directories['WZTo3LNu'])


selection = cutInterpreter.cutString('trilep-Zcand-lepSelTTZ-njet3p-btag1p-onZ')
WZselection = cutInterpreter.cutString('trilep-Zcand-lepSelTTZ-njet1p-btag0p-onZ')

trueVar = "jet_hadronFlavour"
#trueVar = "jet_mcFlavour"

#oneTrueB = "Sum$(jet_btagDeepCSV>0.6324&&abs(%s)==5)==1"
#moreTrueB = "Sum$(jet_btagDeepCSV>0.6324&&abs(%s)==5)>1"
oneTrueB = "Sum$(abs(%s)==5)==1"%(trueVar)
moreTrueB = "Sum$(abs(%s)==5)>1"%(trueVar)
trueCs = "Sum$(abs(%s)==4)>=1&&Sum$(abs(%s)==5)==0"%(trueVar, trueVar)
onlyTrueB = "(Sum$(jet_btagDeepCSV>0.6324)==Sum$(jet_btagDeepCSV>0.6324&&abs(%s)==5))"%trueVar

oneFakeB = "Sum$(jet_btagDeepCSV>0.6324&&abs(%s)!=5)==1"%trueVar
moreFakeB = "Sum$(jet_btagDeepCSV>0.6324&&abs(%s)!=5)>1"%trueVar
#onlyFakeB = "(Sum$(jet_btagDeepCSV>0.6324)==Sum$(jet_btagDeepCSV>0.6324&&abs(%s)!=5))"%trueVar
onlyFakeB = "Sum$(abs(%s)==5)==0"%trueVar
onlyFakeB_noC = "Sum$(abs(%s)==5)==0&&Sum$(abs(%s)==4)==0"%(trueVar, trueVar)

selection = selection

weight_central  = "weight*reweightBTagDeepCSV_SF*reweightPU36fb*reweightTrigger_tight_3l*reweightLeptonTrackingSF_tight_3l*35.9"
reweight        = weight_central #+ "*((Sum$(abs(%s)==5)>0)*%s+(Sum$(abs(%s)==5)==0))"%(trueVar,'0.5',trueVar)

# binning
#binning = [10,0,500]
binning = [4, 0,4]

sample = WZ_pow

## Z_pt
#h_all       = sample.get1DHistoFromDraw( "Z_pt", selectionString = selection, binning = binning,  addOverFlowBin = 'upper', weightString = weight_central )
#h_allFake   = sample.get1DHistoFromDraw( "Z_pt", selectionString = selection + "&&" + onlyFakeB, binning = binning,  addOverFlowBin = 'upper', weightString = weight_central )
#
#h_oneTrue   = sample.get1DHistoFromDraw( "Z_pt", selectionString = selection + "&&" + oneTrueB, binning = binning,  addOverFlowBin = 'upper', weightString = weight_central )
#h_moreTrue  = sample.get1DHistoFromDraw( "Z_pt", selectionString = selection + "&&" + moreTrueB, binning = binning,  addOverFlowBin = 'upper', weightString = weight_central )

h_all       = sample.get1DHistoFromDraw( "nBTag", selectionString = WZselection, binning = binning,  addOverFlowBin = 'upper', weightString = weight_central )
h_allFake   = sample.get1DHistoFromDraw( "nBTag", selectionString = WZselection + "&&" + onlyFakeB_noC, binning = binning,  addOverFlowBin = 'upper', weightString = reweight )

h_oneTrue   = sample.get1DHistoFromDraw( "nBTag", selectionString = WZselection + "&&" + oneTrueB, binning = binning,  addOverFlowBin = 'upper', weightString = reweight )
h_moreTrue  = sample.get1DHistoFromDraw( "nBTag", selectionString = WZselection + "&&" + moreTrueB, binning = binning,  addOverFlowBin = 'upper', weightString = reweight )
h_trueCs    = sample.get1DHistoFromDraw( "nBTag", selectionString = WZselection + "&&" + trueCs, binning = binning,  addOverFlowBin = 'upper', weightString = reweight )


h_all.style         = styles.lineStyle( color.WZ, width=2, dashed=True )
#h_allFake.style     = styles.lineStyle( ROOT.kRed, width=2, errors=True )
#h_oneTrue.style     = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )
#h_moreTrue.style    = styles.lineStyle( ROOT.kOrange+1, width=2, errors=True )
h_allFake.style     = styles.fillStyle( ROOT.kRed )
h_oneTrue.style     = styles.fillStyle( ROOT.kOrange+1 )
h_moreTrue.style    = styles.fillStyle( ROOT.kGreen+1 )
h_trueCs.style      = styles.fillStyle( ROOT.kBlue-9 )



#h_central.legendText = "t#bar{t}Z (LO)"
h_all.legendText        = "WZ powheg (NLO)"
#h_all.legendText        = "WZ amc@NLO (NLO)"
h_allFake.legendText    = "no true b, c"
h_trueCs.legendText     = "#geq 1 true c, no b"
h_oneTrue.legendText    = "1 true b"
h_moreTrue.legendText    = "#geq 2 true bs"

print "Total events", h_all.Integral()

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

plots = [[ h_all ], [ h_moreTrue, h_oneTrue, h_trueCs, h_allFake ] ]
#plots = [[ h_all ], [ h_moreTrue, h_oneTrue ] ]

plotting.draw(
    Plot.fromHisto("WZ_nbtag_c",
                plots,
                #texX = "p_{T}(Z) (GeV)"
                texX = "n_{b-tag}"
            ),
    plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/WZ/",
    logX = False, logY = True, sorting = True, 
    #yRange = (0.008,3.),
    #yRange = (0.03, 150.),
    #yRange = (0.03, [0.001,0.5]),
    #ratio = {'yRange': (0.0, 1.12)},
    #ratio = {'yRange': (0.5, 1.5)},
    drawObjects = drawObjects(),
    copyIndexPHP = True
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

