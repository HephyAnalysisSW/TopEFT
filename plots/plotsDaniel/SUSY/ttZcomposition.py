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
postProcessing_directory = "TopEFT_PP_2016_mva_v19/dilep/"

from TopEFT.samples.color           import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter
from TopEFT.Tools.helpers           import deltaR, deltaR2, deltaPhi
from TopEFT.Tools.objectSelection   import getJets
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.triggerSelector import triggerSelector
from TopEFT.Tools.user            import plot_directory

import TopEFT.Tools.logger as logger

import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)


dirs = {}
dirs['TTZ']         = ['TTZToLLNuNu_ext','TTZToQQ', 'TTZToLLNuNu_m1to10']#, 'TTZToQQ']
dirs['TTZToLLNuNu'] = ['TTZToLLNuNu_m1to10', 'TTZToLLNuNu_ext']
dirs['TTZToQQ']     = ['TTZToQQ']

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

# Define samples
TTZ         = Sample.fromDirectory(name="TTZ", treeName="Events", isData=False, color=color.TTZ, texName="t#bar{t}Z", directory=directories['TTZ'])
TTZToLLNuNu = Sample.fromDirectory(name="TTZToLLNuNu", treeName="Events", isData=False, color=color.TTZ, texName="t#bar{t}Z(ll, #nu#nu)", directory=directories['TTZToLLNuNu'])
TTZToQQ     = Sample.fromDirectory(name="TTZToQQ", treeName="Events", isData=False, color=color.WZ, texName="t#bar{t}Z(qq)", directory=directories['TTZToQQ'])

dilepSelection      = cutInterpreter.cutString('lepSelDilepSUSY-njet3p-btag1p-mt2ll100-met80')
dilepSelection += '&&nlep==2&&nLeptons_tight_3l==2&&((nElectrons_tight_3l==1&&nMuons_tight_3l==1)||(nElectrons_tight_3l==2&&abs(Z_mass-91.2)>10)||(nMuons_tight_3l==2&&abs(Z_mass-91.2)>10))&&genZ_pt>=0'
#dilepSelection = cutInterpreter.cutString('njet3p-btag1p') + '&&genZ_pt>=0'
#dilepSelection += '&&(abs(genZ_daughter_flavor)==12||abs(genZ_daughter_flavor)==14||abs(genZ_daughter_flavor)==16)'

invisibleSelection  = dilepSelection + '&&(abs(genZ_daughter_flavor)==12||abs(genZ_daughter_flavor)==14||abs(genZ_daughter_flavor)==16)'
leptonicSelection   = dilepSelection + '&&(abs(genZ_daughter_flavor)==11||abs(genZ_daughter_flavor)==13)'
tauSelection        = dilepSelection + '&&(abs(genZ_daughter_flavor)==15)'
hadronicSelection   = dilepSelection + '&&(abs(genZ_daughter_flavor)<7)'


selection     = "&&".join([dilepSelection])

## Sequence
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I,btagDeepCSV/F]", "njet/I","nJetSelected/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I",
                    "genZ_pt/F",
                    "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I",
                    "Z_phi/F","Z_pt/F", "Z_mass/F", "Z_eta/F","Z_lldPhi/F", "Z_lldR/F"
                    ]

sequence = []

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
    plot_directory_ = os.path.join(plot_directory, 'ttZcomposition', 'test_dilep_mt2ll100_met80%s'%ext)
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
#DY_HT_LO.read_variables = [VectorTreeVariable.fromString('jet[hadronFlavour/I]') ] 

TTZ_invisible   = copy.deepcopy(TTZ)
TTZ_leptonic    = copy.deepcopy(TTZ)
TTZ_tau         = copy.deepcopy(TTZ)
TTZ_hadronic    = copy.deepcopy(TTZ)

TTZ_invisible.color = ROOT.kYellow+1
TTZ_invisible.texName = "t#bar{t}Z(inv)"
TTZ_leptonic.color = ROOT.kOrange+8
TTZ_leptonic.texName = "t#bar{t}Z(ll)"
TTZ_tau.color = ROOT.kRed-3
TTZ_tau.texName = "t#bar{t}Z(#tau#tau)"
TTZ_hadronic.color = ROOT.kGreen+3
TTZ_hadronic.texName = "t#bar{t}Z(qq)"

#mc = [DY_twoTrueBsElse, DY_twoTrueBsFromG, DY_twoTrueBsFromP, DY_twoTrueBsFromQ, DY_oneTrueBs, DY_fakeBs,TTX,boson, Top]
mc = [TTZ_leptonic,TTZ_tau,TTZ_hadronic,TTZ_invisible]

for s in mc:
#    s.setSelectionString([getFilterCut(isData=False), tr.getSelection("MC")])
    s.read_variables = ['reweightPU36fb/F', 'reweightBTagDeepCSV_SF/F']
#    s.weight         = lambda event, s: event.reweightBTagDeepCSV_SF*event.reweightPU36fb
    s.style = styles.fillStyle(s.color)
#    s.scale = lumi_scale

TTZ_invisible.addSelectionString([invisibleSelection])
TTZ_leptonic.addSelectionString([leptonicSelection])
TTZ_tau.addSelectionString([tauSelection])
TTZ_hadronic.addSelectionString([hadronicSelection])

Data = TTZ
#Data.setSelectionString([getFilterCut(isData=True)]) #trigger already applied in post-processing
Data.style          = styles.errorStyle(ROOT.kBlack)
Data.texName = "t#bar{t}Z"

if small:
    for s in mc + [Data]:
        s.reduceFiles( to = 1 )

stack = Stack(mc, Data)

weight_ = lambda event, sample: event.weight

Plot.setDefaults(stack = stack, weight = staticmethod(weight_), selectionString = selection, addOverFlowBin='upper')

plots = []

plots.append(Plot(
  name = 'dl_mass', texX = 'M(ll) (GeV)', texY = 'Number of Events',
  attribute = TreeVariable.fromString( "Z_mass/F" ),
  binning=[40,0,200],
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
    texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "met_pt/F" ),
    binning=[400/20,0,400],
))

plots.append(Plot(
    texX = 'M_{T2}(ll) (GeV)', texY = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "dl_mt2ll/F" ),
    binning=[10,0,400],
))

plots.append(Plot(
    texX = 'M_{T2}(blbl) (GeV)', texY = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "dl_mt2blbl/F" ),
    binning=[10,0,400],
))


plotting.fill(plots, read_variables = read_variables, sequence = sequence)

dataMCScale = 1
drawPlots(plots, dataMCScale)

