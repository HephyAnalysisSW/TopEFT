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

def drawPlots(plots, subDirectory=''):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, args.plot_directory, subDirectory)
    plot_directory_ = os.path.join(plot_directory_, "log") if log else os.path.join(plot_directory_, "lin")
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot

      plotting.draw(plot,
	    plot_directory = plot_directory_,
	    ratio = None, #{'yRange':(0.1,1.9)} if not args.noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = {},
	    legend =  ( (0.17,0.9-0.05*sum(map(len, plot.histos))/2,1.,0.9), 2),
	    drawObjects = drawObjects( ),
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

selection = [ 
    ("nlep3p", "Sum$(GenLep_pt>20&&(abs(GenLep_pdgId)==11||abs(GenLep_pdgId)==13)&&abs(GenLep_eta)<2.4)>=3"),
    ("njet1p", "Sum$(GenJet_pt>20&&abs(GenJet_eta)<2.4)>=1"),
]

selectionString = "&&".join( c[1] for c in selection )
subDirectory    = '-'.join(  c[0] for c in selection )

for sample in samples:
    sample.setSelectionString( "(1)" )
    sample.style = styles.lineStyle(sample.color)

weight_         = None

stack = Stack(*[ [ sample ] for sample in samples] )

if args.small:
    for sample in stack.samples:
        sample.reduceFiles( to = 1 )

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

plotting.fill(plots, read_variables = read_variables, sequence = sequence, max_events = 100 if args.small else -1)

drawPlots(plots, subDirectory = subDirectory)

#logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )
