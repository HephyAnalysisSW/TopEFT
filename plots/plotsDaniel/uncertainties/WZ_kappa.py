# Standard imports
import ROOT
import os
import sys
import pickle
import math
import copy

# Analysis
from TopEFT.Analysis.SetupHelpers import *
from TopEFT.Analysis.regions      import regionsE, noRegions, regionsReweight, regions4l, regionsReweight4l
from TopEFT.Tools.u_float      import u_float
from TopEFT.Analysis.Region       import Region
from TopEFT.Tools.user import results_directory

from TopEFT.Analysis.estimators         import *
from TopEFT.Analysis.DataObservation    import DataObservation

from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
parser.add_option("--controlRegion",  action='store', default='', choices = ['', 'nbtag0-njet3p', 'nbtag1p-njet02', 'nbtag1p-njet2', 'nbtag0-njet02', 'nbtag0-njet0p', 'nbtag0-njet1p', 'nbtag0-njet2p'], help="Use any CRs cut?")
parser.add_option("--sample", action='store', default='WZ', choices = ["WZ", "TTX", "TTW", "TZQ", "rare", "nonprompt", "pseudoData", "TTZ", "Data", "ZZ", "rare_noZZ"], help="Choose which sample to run the estimates for")
parser.add_option("--year",            action='store',      default=2016, choices = [ '2016', '2017', '20167' ], help='Which year?')
parser.add_option("--skipSystematics", action='store_true', help="Don't run the systematic variations")
parser.add_option("--overwrite", action='store_true', help="Overwrite?")
(options, args) = parser.parse_args()

#RootTools
from RootTools.core.standard import *

from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter import cutInterpreter

## 2016
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v7/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

## 2017
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2017_mva_v7/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *

from TopEFT.Analysis.Setup              import Setup
year                    = int(options.year)
setup                   = Setup(year=year, nLeptons=3)
estimators              = estimatorList(setup)
setup.estimators        = estimators.constructEstimatorList(["WZ", "TTX", "TTW", "TZQ", "rare"])
setup.reweightRegions   = regionsReweight
setup.channels          = [channel(-1,-1)]
setup.regions           = regionsE

setupCR = setup.systematicClone(parameters={'nJets':(1,-1), 'nBTags':(0,0)})

trueVar     = "jet_hadronFlavour"
reweightUp  = "((Sum$(abs(%s)==5)>0)*%s+(Sum$(abs(%s)==5)==0))"%(trueVar,'1.20',trueVar)
reweightDo  = "((Sum$(abs(%s)==5)>0)*%s+(Sum$(abs(%s)==5)==0))"%(trueVar,'0.80',trueVar)

setup_bUp   = setup.systematicClone(sys={"reweight":[reweightUp]})
setup_bDown = setup.systematicClone(sys={"reweight":[reweightDo]})

setupCR_bUp     = setupCR.systematicClone(sys={"reweight":[reweightUp]})
setupCR_bDown   = setupCR.systematicClone(sys={"reweight":[reweightDo]})

WZ = MCBasedEstimate(name="WZ", sample=setup.samples["WZ"], cacheDir=results_directory+"/uncertainties/WZ/")
WZ.initCache(results_directory+"/uncertainties/WZ/")

setups = [setup, setup_bUp, setup_bDown, setupCR, setupCR_bUp, setupCR_bDown]

results = {}

processes = ["WZ0b", "WZ1b", "kappa", "kappa_bUp", "kappa_bDown"]
Nbins = 12
hists = {}
for process in processes:
    hists[process] = ROOT.TH1F(process,"", Nbins, 0, Nbins)

for i,r in enumerate(setup.regions):
    for c in setup.channels:
        res = []
        for s in setups:
            # all results
            result = WZ.cachedEstimate(r, c, s, save=True)
            res.append(result)
            
        kappa = res[0]/res[3]
        deltaKappa = (res[1]/res[4]) - (res[2]/res[5])
        kappa_bUp = res[1]/res[4]
        kappa_bDown = res[2]/res[5]
        print r
        print abs(kappa_bUp-kappa)/kappa, abs(kappa_bDown-kappa)/kappa
        print abs(kappa_bUp-kappa_bDown)/2.
        hists["WZ0b"].SetBinContent(i+1, res[3].val)
        hists["WZ1b"].SetBinContent(i+1, res[0].val)
        hists["kappa"].SetBinContent(i+1, kappa.val)
        hists["kappa_bUp"].SetBinContent(i+1, kappa.val + (kappa_bUp.val-kappa_bDown.val)/2.)
        hists["kappa_bDown"].SetBinContent(i+1, kappa.val - (kappa_bUp.val-kappa_bDown.val)/2.)


hists["WZ0b"].legendText = "WZ, 0b"
hists["WZ0b"].style = styles.fillStyle(color.WZ)
hists["WZ1b"].legendText = "WZ, #geq1b"
hists["WZ1b"].style = styles.lineStyle(ROOT.kBlack, width=2)

boxes = []
ratio_boxes = []
for ib in range(1, 1 + Nbins ):
    kappa           = hists["kappa"].GetBinContent(ib)
    kappaUp_err     = abs(hists["kappa_bUp"].GetBinContent(ib) - kappa)
    happaDown_err   = abs(hists["kappa_bDown"].GetBinContent(ib) - kappa)

    # uncertainty box in main histogram
    up = hists["kappa_bUp"].GetBinContent(ib)/kappa
    down = hists["kappa_bDown"].GetBinContent(ib)/kappa
    print kappa, up, down
    box = ROOT.TBox( hists['kappa'].GetXaxis().GetBinLowEdge(ib),  max([0.006, down]), hists['kappa'].GetXaxis().GetBinUpEdge(ib), max([0.006, up]) )
    box.SetLineColor(ROOT.kBlack)
    box.SetFillStyle(3444)
    box.SetFillColor(ROOT.kBlack)


    boxes.append( box )

def drawObjects( isData=False, lumi=36. ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Simulation') if not isData else (0.15, 0.95, 'CMS Preliminary'),
      (0.75, 0.95, '%sfb^{-1} (13 TeV)'%int(lumi) )
    ]
    return [tex.DrawLatex(*l) for l in lines]

def setBinLabels( hist ):
    for i in range(1, hist.GetNbinsX()+1):
        hist.GetXaxis().SetBinLabel(i, "%s"%i)

for p in processes:
    setBinLabels(hists[p])

drawObjects = drawObjects( isData=False, lumi=round(35.9,0))

plots = [[hists["WZ0b"]], [hists["WZ1b"]]]

from TopEFT.Tools.user              import plot_directory

plotting.draw(
    Plot.fromHisto("WZ",
                plots,
                texX = "Signal Region"
            ),
    plot_directory = os.path.join(plot_directory, "signalRegions_WZ"),
    logX = False, logY = True, sorting = True,
    legend = (0.74,0.80-0.010*8, 0.95, 0.80),
    widths = {'x_width':700, 'y_width':600},
    yRange = (0.3,3000.),
    #yRange = (0.03, [0.001,0.5]),
    ratio = {'yRange': (0.6, 1.4), 'drawObjects':boxes, 'texY':"#kappa"},
    drawObjects = drawObjects,
    copyIndexPHP = True,
)



### add plotting and kosmetics from regions plot here



