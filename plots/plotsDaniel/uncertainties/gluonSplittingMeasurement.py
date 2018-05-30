''' Analysis script for 1D 2l plots (RootTools)
'''

#Standard imports
import ROOT
from math import sqrt, cos, sin, pi, acos
import itertools,os
import copy

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--small',               action='store_true', help="For testing")
argParser.add_argument('--noData',              action='store_true', help="Omit data")
argParser.add_argument('--logLevel',            action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
args = argParser.parse_args()


#RootTools
from RootTools.core.standard import *
from TopEFT.Tools.user import data_directory

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_v14/trilep/"

from TopEFT.samples.color           import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter
from TopEFT.Tools.helpers           import deltaR, deltaR2
from TopEFT.Tools.objectSelection   import getJets
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.triggerSelector import triggerSelector
from TopEFT.Tools.user            import plot_directory

import TopEFT.Tools.logger as logger

import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)


data_directory = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v2/dilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *

dirs = {}
dirs['DY_HT_LO'] = ['DYJetsToLL_M50_LO_ext_comb_lheHT70','DYJetsToLL_M50_HT70to100', 'DYJetsToLL_M50_HT100to200_comb', 'DYJetsToLL_M50_HT200to400_comb', 'DYJetsToLL_M50_HT400to600_comb', 'DYJetsToLL_M50_HT600to800', 'DYJetsToLL_M50_HT800to1200', 'DYJetsToLL_M50_HT1200to2500', 'DYJetsToLL_M50_HT2500toInf']
dirs['top']      = ['TTLep_pow'] + ['TToLeptons_sch_amcatnlo', 'T_tch_powheg', 'TBar_tch_powheg']

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

# Define samples
DY_HT_LO = Sample.fromDirectory(name="DY_HT_LO", treeName="Events", isData=False, color=ROOT.kBlue+1, texName="DY HT (LO)", directory=directories['DY_HT_LO'])
Top      = Sample.fromDirectory(name="Top", treeName="Events", isData=False, color=color.TTJets, texName="t/t#bar{t}", directory=directories['top'])

Data    = Run2016

flavorSelection = "((nGoodElectrons==2&&nGoodMuons==0)||(nGoodElectrons==0&&nGoodMuons==2))"
selection = "Sum$(lep_pt>40&&lep_tight>0)>0&&Sum$(lep_pt>20&&lep_tight>0)>1 && abs(Z_mass-91.2)<10 && nBTag>=1 && nJetSelected>=2"
tr = triggerSelector(2016)

selection     = "&&".join([flavorSelection, selection])

## Sequence
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I,btagDeepCSV/F]", "njet/I","nJetSelected/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I",
                    "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I",
                    "Z_phi/F","Z_pt/F", "Z_mass/F", "Z_eta/F","Z_lldPhi/F", "Z_lldR/F"
                    ]

jetVars = ['eta','pt','phi','btagDeepCSV', 'hadronFlavour']

def getBJetDR( event, sample ):
    jets = getJets(event, jetVars=jetVars, jetColl="jet")
    trueBJets = [ j for j in jets if abs(j['hadronFlavour'])==5 ]
    bjets = [ j for j in jets if j['btagDeepCSV']>0.6324 ]

    minDR = -1
    if len(bjets)>1:
        minDR = 999.
        comb = itertools.combinations(bjets, 2)
        for c in comb:
            dR = deltaR(c[0], c[1])
            if dR < minDR: minDR = dR

    event.bjet_dR = minDR
    return
    ##
sequence = [getBJetDR]

## Plotting
lumi_scale = 35.9
noData = args.noData
small = args.small

def drawObjects( plotData, dataMCScale, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'),
      (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines]

def drawPlots(plots, dataMCScale):
  for log in [False, True]:
    ext = "_small" if small else ""
    ext += "_log" if log else ""
    plot_directory_ = os.path.join(plot_directory, 'gluonSplitting', 'test%s'%ext)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      extensions_ = ["pdf", "png", "root"]

      plotting.draw(plot,
        plot_directory = plot_directory_,
        extensions = extensions_,
        ratio = {'yRange':(0.1,1.9)} if not noData else None,
        logX = False, logY = log, sorting = True,
        yRange = (0.03, "auto") if log else (0.001, "auto"),
        legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
        drawObjects = drawObjects( not noData, dataMCScale , lumi_scale ),
        copyIndexPHP = True,
      )

# Samples
DY_HT_LO.read_variables = [VectorTreeVariable.fromString('jet[hadronFlavour/I]') ] 

DY_trueBs = copy.deepcopy(DY_HT_LO)
DY_trueBs.setSelectionString(["Sum$(jet_pt>30&&abs(jet_eta)<2.4&&jet_id&&jet_hadronFlavour==5)>0"])
DY_trueBs.color = ROOT.kGreen-8
DY_trueBs.texName = "DY (LO), N_{true b-jets}#geq1"

DY_fakeBs = copy.deepcopy(DY_HT_LO)
DY_fakeBs.setSelectionString(["Sum$(jet_pt>30&&abs(jet_eta)<2.4&&jet_id&&jet_hadronFlavour==5)==0"])
DY_fakeBs.color = ROOT.kGreen+1
DY_fakeBs.texName = "DY (LO), N_{true b-jets}=0"


mc = [DY_trueBs, DY_fakeBs, Top]
for s in mc:
    s.setSelectionString([getFilterCut(isData=False), tr.getSelection("MC")])
    s.read_variables = ['reweightPU36fb/F', 'reweightBTagDeepCSV_SF/F']
    s.weight         = lambda event, s: event.reweightBTagDeepCSV_SF*event.reweightPU36fb
    s.style = styles.fillStyle(s.color)

Data.setSelectionString([getFilterCut(isData=True)])
Data.style          = styles.errorStyle(ROOT.kBlack)

if small:
    for s in mc + [Data]:
        s.reduceFiles( to = 1 )

stack = Stack(mc, Data)

weight_ = lambda event, sample: event.weight

Plot.setDefaults(stack = stack, weight = weight_, selectionString = selection, addOverFlowBin='upper')

plots = []

plots.append(Plot(
  name = 'dl_mass', texX = 'M(ll) (GeV)', texY = 'Number of Events',
  attribute = TreeVariable.fromString( "Z_mass/F" ),
  binning=[20,81.20,101.20],
))

plots.append(Plot(
  name = 'nBTag', texX = 'N_{b-tag}', texY = 'Number of Events',
  attribute = TreeVariable.fromString( "nBTag/I" ),
  binning=[4,-0.5,3.5],
))

plots.append(Plot(
  name = 'nJetSelected', texX = 'N_{jets}', texY = 'Number of Events',
  attribute = TreeVariable.fromString( "nJetSelected/I" ),
  binning=[8,-0.5,7.5],
))

plots.append(Plot(
    name = 'bjet_dR',
    texX = '#DeltaR(b-tagged jets)', texY = 'Number of Events',
    attribute = lambda event, sample:event.bjet_dR,
    binning=[20,0,4],
))

plots.append(Plot(
    texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "met_pt/F" ),
    binning=[400/20,0,400],
))

plots.append(Plot(
    texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "Z_pt/F" ),
    binning=[20,0,400],
))

plots.append(Plot(
    name = "cosThetaStar", texX = 'cos#theta(l*)', texY = 'Number of Events / 0.2',
    attribute = TreeVariable.fromString( "cosThetaStar/F" ),
    binning=[10,-1,1],
))


plotting.fill(plots, read_variables = read_variables, sequence = sequence)

dataMCScale = 1
drawPlots(plots, dataMCScale)

