# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

# adapted from RootTools (added fillstyle)
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

from copy import deepcopy

# define classes
def isPrompt(lepton):
    return abs(lepton.lep_mcMatchId) in [6,23,24,25,37]

def isNonPrompt(lepton):
    return not isPrompt(lepton) and abs(lepton.lep_mcMatchAny) in [4, 5]

def isFake(lepton):
    return not isPrompt(lepton) and not ( abs(lepton.lep_mcMatchAny) in [4, 5] )

# data -> replace this with importing samples when needed 
#sample = Sample.fromFiles( "small", texName = "my first sample!", files = ["/afs/hephy.at/data/rschoefbeck01/cmgTuples/georg/TTJets_SingleLeptonFromTbar_1/treeProducer/tree.root"], treeName="tree")
#sample = Sample.fromFiles( "TTJets", texName = "TTJets_SingleLeptonFromTbar", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar/treeProducer/tree.root"], treeName="tree")
#sample = Sample.fromFiles( "QCD",    texName = "QCD_Pt120to170", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/QCD_Pt120to170/treeProducer/tree.root"], treeName="tree")
sample = Sample.fromFiles( "TTJetsClasses", texName = "TTJets_SingleLeptonFromTbar_with_classes", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar_with_classes/treeProducer/tree.root"], treeName="tree")

samplePrompt =    deepcopy(sample)
sampleNonPrompt = deepcopy(sample)
sampleFake =      deepcopy(sample)

samplePrompt.setSelectionString( "(lep_isPromptId==1)" )
sampleNonPrompt.setSelectionString( "(lep_isNonPromptId==1)" )
sampleFake.setSelectionString( "(lep_isFakeId==1)" )

samplePrompt.name = "Prompt"
sampleNonPrompt.name = "NonPrompt"
sampleFake.name = "Fake"

samplePrompt.texName = "Prompt"
sampleNonPrompt.texName = "NonPrompt"
sampleFake.texName = "Fake"

samplePrompt.style =  fillStyle(color=ROOT.kCyan, style=3004, lineColor=ROOT.kCyan)
sampleNonPrompt.style =     fillStyle(color=ROOT.kBlue, style=3004, lineColor=ROOT.kBlue)
sampleFake.style =       fillStyle(color=ROOT.kGray, style=3004, lineColor=ROOT.kGray)

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
"lep_isPromptId/I",
"lep_isNonPromptId/I",
"lep_isFakeId/I",
]

# Define stack
mc    = [samplePrompt,sampleNonPrompt,sampleFake]  # A full example would be e.g. mc = [ttbar, ttz, ttw, ...]
stack = Stack(mc) # A full example would be e.g. stack = Stack( mc, [data], [signal1], [signal2] ) -> Samples in "mc" are stacked in the plot

# Define some parameters for plots and selection
ecalTypes=["","EndCap","Barrel"]
leptonType=11
plotnameprefix="Ele" if leptonType==11 else "Muo" if leptonType==13 else "define lepton type"

for ecalType in ecalTypes:
    plotname=plotnameprefix+ecalType

    # Set some defaults -> these need not be specified below for each plot
    weight = lambda event, sample: 1.  # could be e.g. weight = lambda event, sample: event.weight
    selectionString = "(lep_pt>=25 && abs(lep_pdgId)==11 && lep_relIso03<0.1 && abs(lep_etaSc)<=1.479)" if ecalType=="Barrel" else "(lep_pt>=25 && abs(lep_pdgId)==11 && lep_relIso03<0.1 && abs(lep_etaSc)>1.479)" if ecalType=="EndCap" else "(lep_pt>=25 && abs(lep_pdgId)==11 && lep_relIso03<0.1)" # could be a complicated cut
    Plot.setDefaults(stack = stack, weight = weight, selectionString = selectionString, addOverFlowBin='upper')

    # Sequence
    sequence = []

    # Add a new fancy variable
    def make_absEInvMinusPInv( event, sample ):
        event.absEInvMinusPInv = abs(event.lep_eInvMinusPInv)
    sequence.append( make_absEInvMinusPInv)

    def print_mcmatchId( event, sample ):
        if isNonPrompt(event) and event.lep_mvaIdSpring16<0.3 and sample==sample:
            print event.lep_mcMatchId

    def print_class( event, sample ):
        assert isPrompt(event) + isNonPrompt(event) + isFake(event)==1, "Should never happen!"

        print event.lep_isPromptId, event.lep_isNonPromptId, event.lep_isFakeId, event.lep_mcMatchId, event.lep_mcMatchAny, isPrompt(event), isNonPrompt(event), isFake(event), event.lep_pdgId
        print sample, samplePrompt, sampleNonPrompt, sampleFake
        print "Fill", event.lep_isPromptId if ((isPrompt(event) and sample==samplePrompt) or (isNonPrompt(event) and sample==sampleNonPrompt) or (isFake(event) and sample==sampleFake)) else float('nan')
        print "Fill2", (isPrompt(event) and sample==samplePrompt),(isNonPrompt(event) and sample==sampleNonPrompt),(isFake(event) and sample==sampleFake)
    #sequence.append(print_class)

    # Start with an empty list
    plots = []
    # Add plots
    plots.append(Plot(name=plotname+'ClassPrompt',
        texX = 'isPrompt', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_isPromptId,
        binning=[2,0,1],
    ))
    plots.append(Plot(name=plotname+'ClassNonPrompt',
        texX = 'isNonPrompt', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_isNonPromptId,
        binning=[2,0,1],
    ))
    plots.append(Plot(name=plotname+'ClassFake',
        texX = 'isFake', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_isFakeId,
        binning=[2,0,1],
    ))
    plots.append(Plot(name=plotname+'mcMatchId',
        texX = 'mcMatchId', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_mcMatchId,
        binning=[61,-30,30],
    ))
    plots.append(Plot(name=plotname+'mcMatchAny',
        texX = 'mcMatchAny', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_mcMatchAny,
        binning=[61,-30,30],
    ))
    plots.append(Plot(name=plotname+'MVA',
        texX = 'electron MVA', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_mvaIdSpring16 if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[30,-1,1],
    ))
    plots.append(Plot(name=plotname+'Pt',
        texX = 'pt', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_pt if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[100,0,500],
    ))
    plots.append(Plot(name=plotname+'pdgId',
        texX = 'pdgId', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_pdgId if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[61,-30,30],
    ))
    plots.append(Plot(name=plotname+'EtaSc',
        texX = 'etaSc', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_etaSc if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[60,-3,3],
    ))
    plots.append(Plot(name=plotname+'Full5x5SigmaIetaIeta',
        texX = 'full5x5_sigmaIetaIeta', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_full5x5_sigmaIetaIeta if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[30,0,0.06],
    ))
    plots.append(Plot(name=plotname+'DEtaInSeed',
        texX = 'dEtaInSeed', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_dEtaInSeed if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[30,-0.03,0.03],
    ))
    plots.append(Plot(name=plotname+'DPhiScTrkIn',
        texX = 'dPhiScTrkIn', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_dPhiScTrkIn if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[20,-0.2,0.2],
    ))
    plots.append(Plot(name=plotname+'RelIso03',
        texX = 'relIso03', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_relIso03 if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[90,0,0.3],
    ))
    plots.append(Plot(name=plotname+'EInvMinusPInv',
        texX = '|1/E-1/p|', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.absEInvMinusPInv if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[30,0,0.15],
    ))
    plots.append(Plot(name=plotname+'LostOuterHits',
        texX = 'lostOuterHits', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_lostOuterHits if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[16,0,15],
    ))
    plots.append(Plot(name=plotname+'ConvVeto',
        texX = 'convVeto', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_convVeto if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[2,0,1],
    ))
    plots.append(Plot(name=plotname+'HadronicOverEm',
        texX = 'hadronicOverEm', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_hadronicOverEm if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[30,0,0.1],
    ))
    plots.append(Plot(name=plotname+'Rho',
        texX = 'rho', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_rho if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[100,0,5],
    ))
    plots.append(Plot(name=plotname+'Dxy',
        texX = 'dxy', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_dxy if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[60,-0.1,0.1],
    ))
    plots.append(Plot(name=plotname+'Dz',
        texX = 'dz', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.lep_dz if ((isPrompt(lepton) and sample==samplePrompt) or (isNonPrompt(lepton) and sample==sampleNonPrompt) or (isFake(lepton) and sample==sampleFake)) else float('nan'),
        binning=[60,-0.2,0.2],
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
        plot_directory_ = os.path.join(plot_directory, 'histogram_plots', 'stacked_classes', plotname, ("log" if log else "lin"))
        for plot in plots:
          #if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
          
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

