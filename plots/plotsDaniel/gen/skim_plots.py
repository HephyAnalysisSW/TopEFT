#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)

from math                                import sqrt, cos, sin, pi, isnan
from RootTools.core.standard             import *
from TopEFT.tools.user                   import plot_directory
from TopEFT.tools.helpers                import deltaPhi

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--samples',            action='store',      nargs='*',               help="Which samples?")
argParser.add_argument('--plot_directory',     action='store',      default='gen')
#argParser.add_argument('--selection',          action='store',      default='njet2p-btag1p-relIso0.12-looseLeptonVeto-mll20-met80-metSig5-dPhiJet0-dPhiJet1')
argParser.add_argument('--normalize',          action='store_true',                          help="Normalize histograms to 1?")
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
args = argParser.parse_args()

#
# Logger
#
import TopEFT.tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small: args.plot_directory += "_small"

# Import samples
from TopEFT.samples.skim_benchmarks import *

samples = map( eval, args.samples ) 

##
## Text on the plots
##
def drawObjects( hasData = False ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if hasData else 'CMS Simulation'), 
      #(0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'gen', args.plot_directory)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot

      plotting.draw(plot,
	    plot_directory = plot_directory_,
	    ratio = None, #{'yRange':(0.1,1.9)} if not args.noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (3., "auto") if log else (0.001, "auto"),
	    scaling = {},
	    legend =  ( (0.17,0.9-0.05*sum(map(len, plot.histos))/2,1.,0.9), 2),
	    drawObjects = drawObjects( ),
        normalize = args.normalize,
      )

#
# Read variables and sequences
#

read_variables = [
    "GenMet_pt/F", "GenMet_phi/F", 
    "nGenJet/I", "GenJet[pt/F,eta/F,phi/F]", 
    "nGenLep/I", "GenLep[pt/F,eta/F,phi/F,pdgId/I,motherPdgId/I]", 
    "ntop/I", "top[pt/F,eta/F,phi/F]", 
    "nZ/I", "Z[pt/F,eta/F,phi/F]", 
]

#def makeleptons( event, sample):
#
#    print [ event.GenLep_pt[i] for i in xrange(event.nGenLep) ]

#sequence = [ makeleptons ]

sequence = []

def getLepsFromZ( event, sample ):
    leps = []
    for i, motherId in enumerate(event.GenLep_motherPdgId):
        if abs(motherId) == 23:
            leps.append( {'pt':event.GenLep_pt[i], 'phi': event.GenLep_phi[i], 'pdgId': event.GenLep_pdgId[i], 'eta': event.GenLep_eta[i]} )
    return leps

def makeDeltaPhi( event, sample ):
    leps = getLepsFromZ( event, sample )
    if len(leps) == 2 and leps[0]['pdgId']*leps[1]['pdgId']<0:
        event.dPhi_ll = deltaPhi(leps[0]['phi'], leps[1]['phi'])
    else:
        event.dPhi_ll = -1

def getLeadingZ( event, sample ):
    Zs = [ z for z in event.Z_pt ]
    event.leading_Z_pt = Zs[0] if not isnan(Zs[0]) else -1

sequence.append( makeDeltaPhi )
sequence.append( getLeadingZ )

for sample in samples:
    sample.setSelectionString( "(1)" )
    sample.style = styles.lineStyle(sample.color)

weight_         = None
selectionString = None

stack = Stack(*[ [ sample ] for sample in samples] )

if args.small:
    for sample in stack.samples:
        sample.reduceFiles( to = 1 )

# Use some defaults
Plot.setDefaults(stack = stack, weight = weight_, selectionString = selectionString, addOverFlowBin='upper')
  
plots = []

plots.append(Plot( name = "leading_Z_pT",
  texX = 'leading Z p_{T} (GeV)', texY = 'Number of Events / 20 GeV',
  attribute = lambda event, sample: event.leading_Z_pt,
  binning=[400/20,0,400],
))

plots.append(Plot( name = "leading_Z_pT_ext",
  texX = 'leading Z p_{T} (GeV)', texY = 'Number of Events / 40 GeV',
  attribute = lambda event, sample: event.leading_Z_pt,
  binning=[800/40,0,800],
))

plots.append(Plot( name = "leading_Z_pT_coarse",
  texX = 'leading Z p_{T} (GeV)', texY = 'Number of Events / 100 GeV',
  attribute = lambda event, sample: event.leading_Z_pt,
  binning=[800/100,0,800],
))

plots.append(Plot(
  texX = 'gen E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
  attribute = TreeVariable.fromString( "GenMet_pt/F" ),
  binning=[400/20,0,400],
))

#plots.append(Plot(
#  texX = 'gen #phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
#  attribute = TreeVariable.fromString( "GenMet_phi/F" ),
#  binning=[10,-pi,pi],
#))

plots.append(Plot(
texX = 'number of gen jets', texY = 'Number of Events',
attribute = TreeVariable.fromString('nGenJet/I'),
binning=[14,0,14],
))

plots.append(Plot(
texX = '#Delta#phi(ll)', texY = 'Number of Events',
name = 'deltaPhi_ll',
attribute = lambda event, sample:event.dPhi_ll,
binning=[16,0,pi],
))

plots.append(Plot(
texX = '#Delta#phi(ll)', texY = 'Number of Events',
name = 'deltaPhi_ll_coarse',
attribute = lambda event, sample:event.dPhi_ll,
binning=[4,0,pi],
))


#plots.append(Plot(
#texX = 'H_{T} (GeV)', texY = 'Number of Events / 25 GeV',
#attribute = TreeVariable.fromString( "ht/F" ),
#binning=[500/25,0,600],
#))
#
#plots.append(Plot(
#texX = 'm(ll) of leading dilepton (GeV)', texY = 'Number of Events / 4 GeV',
#attribute = TreeVariable.fromString( "dl_mass/F" ),
#binning=[200/4,0,200],
#))
#
#plots.append(Plot(
#texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 10 GeV',
#attribute = TreeVariable.fromString( "dl_pt/F" ),
#binning=[20,0,400],
#))
#
#plots.append(Plot(
#  texX = '#eta(ll) ', texY = 'Number of Events',
#  name = 'dl_eta', attribute = lambda event, sample: abs(event.dl_eta), read_variables = ['dl_eta/F'],
#  binning=[10,0,3],
#))
#
#plots.append(Plot(
#texX = '#phi(ll)', texY = 'Number of Events',
#attribute = TreeVariable.fromString( "dl_phi/F" ),
#binning=[10,-pi,pi],
#))
#
plots.append(Plot(
texX = 'Cos(#Delta#phi(ll, E_{T}^{miss}))', texY = 'Number of Events',
name = 'cosZMetphi',
attribute = lambda event, sample: cos( event.dPhi_ll - event.GenMet_phi ), 
binning = [10,-1,1],
))

#plots.append(Plot(
#texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events / 15 GeV',
#attribute = TreeVariable.fromString( "GenLep_pt/F" ),
#binning=[20,0,300],
#))
#
#plots.append(Plot(
#texX = 'p_{T}(l_{2}) (GeV)', texY = 'Number of Events / 15 GeV',
#attribute = TreeVariable.fromString( "GenLep_pt[1]/F" ),
#binning=[20,0,300],
#))
#
#
#plots.append(Plot(
#texX = '#eta(l_{1})', texY = 'Number of Events',
#name = 'l1_eta', attribute = lambda event, sample: abs(event.l1_eta), read_variables = ['l1_eta/F'],
#binning=[15,0,3],
#))
#
#plots.append(Plot(
#texX = '#phi(l_{1})', texY = 'Number of Events',
#attribute = TreeVariable.fromString( "l1_phi/F" ),
#binning=[10,-pi,pi],
#))
#
#plots.append(Plot(
#texX = 'p_{T}(l_{2}) (GeV)', texY = 'Number of Events / 15 GeV',
#attribute = TreeVariable.fromString( "l2_pt/F" ),
#binning=[20,0,300],
#))
#
#plots.append(Plot(
#texX = '#eta(l_{2})', texY = 'Number of Events',
#name = 'l2_eta', attribute = lambda event, sample: abs(event.l2_eta), read_variables = ['l2_eta/F'],
#binning=[15,0,3],
#))
#
#plots.append(Plot(
#texX = '#phi(l_{2})', texY = 'Number of Events',
#attribute = TreeVariable.fromString( "l2_phi/F" ),
#binning=[10,-pi,pi],
#))
#
## Plots only when at least one jet:
#if args.selection.count('njet2') or args.selection.count('njet1'):
#plots.append(Plot(
#  texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
#  name = 'jet1_pt', attribute = lambda event, sample: event.JetGood_pt[0],
#  binning=[600/30,0,600],
#))
#
#plots.append(Plot(
#  texX = '#eta(leading jet) (GeV)', texY = 'Number of Events',
#  name = 'jet1_eta', attribute = lambda event, sample: abs(event.JetGood_eta[0]),
#  binning=[10,0,3],
#))
#
#plots.append(Plot(
#  texX = '#phi(leading jet) (GeV)', texY = 'Number of Events',
#  name = 'jet1_phi', attribute = lambda event, sample: event.JetGood_phi[0],
#  binning=[10,-pi,pi],
#))
#
#plots.append(Plot(
#  name = 'cosMetJet1phi',
#  texX = 'Cos(#Delta#phi(E_{T}^{miss}, leading jet))', texY = 'Number of Events',
#  attribute = lambda event, sample: cos( event.met_phi - event.JetGood_phi[0]), 
#  read_variables = ["met_phi/F", "JetGood[phi/F]"],
#  binning = [10,-1,1],
#))
#
#plots.append(Plot(
#  name = 'cosMetJet1phi_smallBinning',
#  texX = 'Cos(#Delta#phi(E_{T}^{miss}, leading jet))', texY = 'Number of Events',
#  attribute = lambda event, sample: cos( event.met_phi - event.JetGood_phi[0] ) , 
#  read_variables = ["met_phi/F", "JetGood[phi/F]"],
#  binning = [20,-1,1],
#))
#
#plots.append(Plot(
#  name = 'cosZJet1phi',
#  texX = 'Cos(#Delta#phi(Z, leading jet))', texY = 'Number of Events',
#  attribute = lambda event, sample: cos( event.dl_phi - event.JetGood_phi[0] ) ,
#  read_variables =  ["dl_phi/F", "JetGood[phi/F]"],
#  binning = [10,-1,1],
#))
#
## Plots only when at least two jets:
#if args.selection.count('njet2'):
#plots.append(Plot(
#  texX = 'p_{T}(2nd leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
#  name = 'jet2_pt', attribute = lambda event, sample: event.JetGood_pt[1],
#  binning=[600/30,0,600],
#))
#
#plots.append(Plot(
#  texX = '#eta(2nd leading jet) (GeV)', texY = 'Number of Events',
#  name = 'jet2_eta', attribute = lambda event, sample: abs(event.JetGood_eta[1]),
#  binning=[10,0,3],
#))
#
#plots.append(Plot(
#  texX = '#phi(2nd leading jet) (GeV)', texY = 'Number of Events',
#  name = 'jet2_phi', attribute = lambda event, sample: event.JetGood_phi[1],
#  binning=[10,-pi,pi],
#))
#
#plots.append(Plot(
#  name = 'cosMetJet2phi',
#  texX = 'Cos(#Delta#phi(E_{T}^{miss}, second jet))', texY = 'Number of Events',
#  attribute = lambda event, sample: cos( event.met_phi - event.JetGood_phi[1] ) , 
#  read_variables = ["met_phi/F", "JetGood[phi/F]"],
#  binning = [10,-1,1],
#))
#
#plots.append(Plot(
#  name = 'cosMetJet2phi_smallBinning',
#  texX = 'Cos(#Delta#phi(E_{T}^{miss}, second jet))', texY = 'Number of Events',
#  attribute = lambda event, sample: cos( event.met_phi - event.JetGood_phi[1] ) , 
#  read_variables = ["met_phi/F", "JetGood[phi/F]"],
#  binning = [20,-1,1],
#))
#
#plots.append(Plot(
#  name = 'cosZJet2phi',
#  texX = 'Cos(#Delta#phi(Z, 2nd leading jet))', texY = 'Number of Events',
#  attribute = lambda event, sample: cos( event.dl_phi - event.JetGood_phi[0] ),
#  read_variables = ["dl_phi/F", "JetGood[phi/F]"],
#  binning = [10,-1,1],
#))
#
#plots.append(Plot(
#  name = 'cosJet1Jet2phi',
#  texX = 'Cos(#Delta#phi(leading jet, 2nd leading jet))', texY = 'Number of Events',
#  attribute = lambda event, sample: cos( event.JetGood_phi[1] - event.JetGood_phi[0] ) ,
#  read_variables =  ["JetGood[phi/F]"],
#  binning = [10,-1,1],
#))


plotting.fill(plots, read_variables = read_variables, sequence = sequence, max_events = 100 if args.small else -1)


drawPlots(plots)

#logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )
