# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

# User specific 
from TopEFT.Tools.user import plot_directory

# data -> replace this with importing samples when needed 
sample = Sample.fromFiles( "small", texName = "my first sample!", files = ["/afs/hephy.at/data/rschoefbeck01/cmgTuples/georg/TTJets_SingleLeptonFromTbar_1/treeProducer/tree.root"], treeName="tree")

# variables to read
read_variables = [ "run/I", "lumi/I", "evt/l", "lep_trackerHits/I", "lep_innerTrackChi2/F", "lep_pdgId/I", "lep_segmentCompatibility/F", "lep_sigmaIEtaIEta/F", "lep_etaSc/F", "lep_mcMatchPdgId/I" ]

# Define stack
mc    = [sample]  # A full example would be e.g. mc = [ttbar, ttz, ttw, ...]
stack = Stack(mc) # A full example would be e.g. stack = Stack( mc, [data], [signal1], [signal2] ) -> Samples in "mc" are stacked in the plot

# Set some defaults -> these need not be specified below for each plot
weight = lambda event, sample: 1.  # could be e.g. weight = lambda event, sample: event.weight
selectionString = "(1)"            # could be a complicated cut
Plot.setDefaults(stack = stack, weight = weight, selectionString = selectionString, addOverFlowBin='upper')

# Sequence
sequence = []

# Add a new fancy variable
def make_fancy_variable( event, sample ):
    event.fancy_variable = event.lep_trackerHits**2 
sequence.append( make_fancy_variable )

# Start with an empty list
plots = []

# Add plots
plots.append(Plot(
    texX = 'Number of tracker hits', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_trackerHits/I" ), # <-- can use any branch 
    binning=[30,0,30],
))

plots.append(Plot( name = "fancy_variable",
    texX = 'Number of tracker hits squared', texY = 'Number of Events',
    attribute = lambda event, sample: event.fancy_variable, # <--- can use any 'event' attribute, including the ones we define in 'sequence'
    binning=[30,0,900],
))


# Fill everything.
plotting.fill(plots, read_variables = read_variables, sequence = sequence)

#
# Helper: Add text on the plots
#
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

# Draw a plot and make it look nice-ish
def drawPlots(plots, dataMCScale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'example_plots', ("log" if log else "lin"))
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot

      plotting.draw(plot,
        plot_directory = plot_directory_,
        #ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
        logX = False, logY = log, sorting = True,
        yRange = (0.03, "auto") if log else (0.001, "auto"),
        scaling = {},
        legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
        drawObjects = drawObjects( False, dataMCScale , lumi_scale = -1 ),
        copyIndexPHP = True
      )

# Draw the plots
drawPlots(plots, dataMCScale = -1)

