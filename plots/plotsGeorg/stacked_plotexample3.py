# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

def fillStyle( color, style, lineColor = ROOT.kBlack, errors = False):
    def func( histo ):
        lc = lineColor if lineColor is not None else color
        histo.SetLineColor( lc )
        histo.SetMarkerSize( 0 )
        histo.SetMarkerStyle( 0 )
        histo.SetMarkerColor( lc )
        histo.SetFillColor( color )
        histo.SetFillStyle( style)
        histo.drawOption = "hist"
        if errors: histo.drawOption+='E'
        return 
    return func

from TopEFT.Tools.user import plot_directory

# data -> replace this with importing samples when needed 
#sample = Sample.fromFiles( "small", texName = "my first sample!", files = ["/afs/hephy.at/data/rschoefbeck01/cmgTuples/georg/TTJets_SingleLeptonFromTbar_1/treeProducer/tree.root"], treeName="tree")
sample1 = Sample.fromFiles( "TTJets", texName = "TTJets_SingleLeptonFromTbar", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar/treeProducer/tree.root"], treeName="tree")
sample2 = Sample.fromFiles( "QCD",    texName = "QCD_Pt120to170", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/QCD_Pt120to170/treeProducer/tree.root"], treeName="tree")

#sample1.style =  styles.lineStyle( color= ROOT.kBlue)
sample1.style =  fillStyle(color=ROOT.kBlue, style=3004, lineColor=ROOT.kBlue)
#sample2.style =  styles.lineStyle( color= ROOT.kRed)
sample2.style =  fillStyle(color=ROOT.kRed, style=3004, lineColor=ROOT.kRed)

# variables to read
read_variables = [
"run/I",
"lumi/I", 
"evt/l", 
"lep_trackerHits/I", 
"lep_innerTrackChi2/F", 
"lep_pdgId/I", 
"lep_segmentCompatibility/F", 
"lep_sigmaIEtaIEta/F",
"lep_mcMatchPdgId/I",
"lep_mcMatchId/I",
"lep_mcMatchAny/I",
"lep_mvaIdSpring16/F",
"lep_pt/F",

"lep_etaSc/F",                  #electrons (|etaSc|<=1.479 barrel cuts, |etaSc|>1.479 endcap cuts)              #Electron supercluster pseudorapidity for Leptons after the preselection : 0 at: 0x4109bd0
"lep_full5x5_sigmaIetaIeta/F",  #electrons (barrel: <0.0104,     endcap: <0.0305)                               #Electron full5x5_sigmaIetaIeta for Leptons after the preselection : 0 at: 0x411d5c0 
"lep_dEtaInSeed/F",             #electrons (barrel: | |<0.00353, endcap: | |<0.00567)                           #DeltaEta wrt ele SC seed for Leptons after the preselection : 0 at: 0x411e850
"lep_dPhiScTrkIn/F",            #electrons (barrel: | |<0.0499,  endcap: | |<0.0165)                            #Electron deltaPhiSuperClusterTrackAtVtx (without absolute value!) for Leptons after the preselection : 0 at: 0x41083f0
"lep_relIso03/F",               #electrons (barrel: <0.0361,     endcap: <0.094)       #muons <0.1              #PF Rel Iso, R=0.3, pile-up corrected for Leptons after the preselection : 0 at: 0x410f640
"lep_eInvMinusPInv/F",          #electrons (barrel: | |<0.0278,  endcap: | |<0.0158)                            #Electron 1/E - 1/p  (without absolute value!) for Leptons after the preselection : 0 at: 0x4108f90   
"lep_lostOuterHits/I",          #electrons (barrel: 1,           endcap: 1)                                     #Number of lost hits on inner track for Leptons after the preselection : 0 at: 0x4101ee0
"lep_convVeto/I",               #electrons yes                                                                  #Conversion veto (always true for muons) for Leptons after the preselection : 0 at: 0x410e5c0
"lep_hadronicOverEm/F",         #electrons                                                                      #Electron hadronicOverEm for Leptons after the preselection : 0 at: 0x4108990
"lep_rho/F",                    #electrons                                                                      #rho for Leptons after the preselection : 0 at: 0x4117d20
"lep_jetDR/F",                                                                         #(muons <=0.3)           #deltaR(lepton, nearest jet) for Leptons after the preselection : 0 at: 0x411ca70
"lep_dxy/F",                                                                           #mouns                   #d_{xy} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410c4b0
"lep_dz/F",                                                                            #mouns                   #d_{z} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410ca30
"lep_isGlobalMuon/I",                                                                  #muons yes               #Muon is global for Leptons after the preselection : 0 at: 0x4106c30
]

# Define stack
mc    = [sample1,sample2]  # A full example would be e.g. mc = [ttbar, ttz, ttw, ...]
stack = Stack(mc) # A full example would be e.g. stack = Stack( mc, [data], [signal1], [signal2] ) -> Samples in "mc" are stacked in the plot

# Set some defaults -> these need not be specified below for each plot
weight = lambda event, sample: 1.  # could be e.g. weight = lambda event, sample: event.weight
selectionString = "(lep_pt>=25 && abs(lep_pdgId)==11 && lep_relIso03<0.1)"          # could be a complicated cut
Plot.setDefaults(stack = stack, weight = weight, selectionString = selectionString, addOverFlowBin='upper')

# Sequence
sequence = []

# Add a new fancy variable
#def make_fancy_variable( event, sample ):
#    event.fancy_variable = event.lep_trackerHits**2 
#sequence.append( make_fancy_variable )


def isPrompt(lepton):
    return abs(lepton.lep_mcMatchId) in [6,23,24,25,37]

def isNonPrompt(lepton):
    return not isPrompt(lepton) and abs(lepton.lep_mcMatchAny) in [4, 5]

def isFake(lepton):
    return not isPrompt(lepton) and not ( abs(lepton.lep_mcMatchAny) in [4, 5] )

def print_mcmatchId( event, sample ):
    if isNonPrompt(event) and event.lep_mvaIdSpring16<0.3 and sample.name=="TTJets":
        print event.lep_mcMatchId

#sequence.append(print_mcmatchId)


# Start with an empty list
plots = []

# Add plots
plots.append(Plot(name='EleMVA',
    texX = 'electron MVA', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_mvaIdSpring16/F" ),
    binning=[30,-1,1],
))
plots.append(Plot( name='EleMVAclassPrompt',
    texX = 'electron MVA', texY = 'Number of Events',
    attribute = lambda lepton, sample: lepton.lep_mvaIdSpring16 if isPrompt(lepton) else float('nan'),
    binning=[30,-1,1],
))
plots.append(Plot( name='EleMVAclassNonPrompt',
    texX = 'electron MVA', texY = 'Number of Events',
    attribute = lambda lepton, sample: lepton.lep_mvaIdSpring16 if isNonPrompt(lepton) else float('nan'),
    binning=[30,-1,1],
))
plots.append(Plot( name='EleMVAclassFake',
    texX = 'electron MVA', texY = 'Number of Events',
    attribute = lambda lepton, sample: lepton.lep_mvaIdSpring16 if isFake(lepton) else float('nan'),
    binning=[30,-1,1],
))

plots.append(Plot(name='ElePt',
    texX = 'pt', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_pt/F" ),
    binning=[100,0,500],
))
plots.append(Plot(name='pdgId',
    texX = 'pdgId', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_pdgId/I" ),
    binning=[61,-30,30],
))
plots.append(Plot(name='EleEtaSc',
    texX = 'etaSc', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_etaSc/F" ),
    binning=[60,-3,3],
))
plots.append(Plot(name='EleFull5x5SigmaIetaIeta',
    texX = 'full5x5_sigmaIetaIeta', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_full5x5_sigmaIetaIeta/F" ),
    binning=[100,0,0.1],
))
plots.append(Plot(name='EleDEtaInSeed',
    texX = 'dEtaInSeed', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_dEtaInSeed/F" ),
    binning=[100,-4,4],
))
plots.append(Plot(name='EleDPhiScTrkIn',
    texX = 'dPhiScTrkIn', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_dPhiScTrkIn/F" ),
    binning=[100,-2,2],
))
plots.append(Plot(name='EleRelIso03',
    texX = 'relIso03', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_relIso03/F" ),
    binning=[100,0,0.11],
))
plots.append(Plot(name='EleEInvMinusPInv',
    texX = 'eInvMinusPInv', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_eInvMinusPInv/F" ),
    binning=[60,-1,1],
))
plots.append(Plot(name='EleLostOuterHits',
    texX = 'lostOuterHits', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_lostOuterHits/I" ),
    binning=[16,0,15],
))
plots.append(Plot(name='EleConvVeto',
    texX = 'convVeto', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_convVeto/I" ),
    binning=[2,0,1],
))
plots.append(Plot(name='EleHadronicOverEm',
    texX = 'hadronicOverEm', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_hadronicOverEm/F" ),
    binning=[30,0,3],
))
plots.append(Plot(name='EleRho',
    texX = 'rho', texY = 'Number of Events',
    attribute = TreeVariable.fromString( "lep_rho/F" ),
    binning=[100,0,5],
))


#plots.append(Plot( name = "fancy_variable",
#    texX = 'Number of tracker hits squared', texY = 'Number of Events',
#    attribute = lambda event, sample: event.fancy_variable, # <--- can use any 'event' attribute, including the ones we define in 'sequence'    binning=[30,0,900],
#))


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
    plot_directory_ = os.path.join(plot_directory, 'stacked_plots', ("log" if log else "lin"))
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

