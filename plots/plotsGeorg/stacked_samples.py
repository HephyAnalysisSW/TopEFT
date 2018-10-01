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

#define classes
def isPrompt(lepton):
    return abs(lepton.lep_mcMatchId) in [6,23,24,25,37]

def isNonPrompt(lepton):
    return not isPrompt(lepton) and abs(lepton.lep_mcMatchAny) in [4, 5]

def isFake(lepton):
    return not isPrompt(lepton) and not ( abs(lepton.lep_mcMatchAny) in [4, 5] )

# data -> replace this with importing samples when needed 
sample1 = Sample.fromFiles( "TTJets", texName = "TTJets_SingleLeptonFromTbar", files = [
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/TTJets_1.root",
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/TTJets_2.root"
], treeName="tree")
sample2 = Sample.fromFiles( "QCD",    texName = "QCD_Pt120to170", files = [
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/DLTrainData/QCD_1.root"
], treeName="tree")

#sample1.style =  styles.lineStyle( color= ROOT.kBlue)
sample1.style =  fillStyle(color=ROOT.kYellow + 1, style=3004, lineColor=ROOT.kYellow +1)
#sample2.style =  styles.lineStyle( color= ROOT.kRed)
sample2.style =  fillStyle(color=ROOT.kGreen +1, style=3004, lineColor=ROOT.kGreen +1)

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
"npfCand_neutral/I",
"npfCand_charged/I",
"npfCand_photon/I",
"npfCand_electron/I",
"npfCand_muon/I"
]

# Define stack
mc    = [sample1,sample2]  # A full example would be e.g. mc = [ttbar, ttz, ttw, ...]
stack = Stack(mc) # A full example would be e.g. stack = Stack( mc, [data], [signal1], [signal2] ) -> Samples in "mc" are stacked in the plot

# Define some parameters for plots and selection
ecaltypes=["","EndCap","Barrel"]

for ecaltype in ecaltypes:
    plotname="Ele"+ecaltype

    # Set some defaults -> these need not be specified below for each plot
    weight = staticmethod(lambda event, sample: 1.)  # could be e.g. weight = lambda event, sample: event.weight
    selectionString = "(abs(lep_pdgId)==11 && abs(lep_etaSc)<=1.479)" if ecaltype=="Barrel" else "(abs(lep_pdgId)==11 && abs(lep_etaSc)>1.479)" if ecaltype=="EndCap" else "(abs(lep_pdgId)==11)" # could be a complicated cut
    #selectionString = "(lep_pt>=25 && abs(lep_pdgId)==11 && lep_relIso03<0.1 && abs(lep_etaSc)<=1.479)" if ecaltype=="Barrel" else "(lep_pt>=25 && abs(lep_pdgId)==11 && lep_relIso03<0.1 && abs(lep_etaSc)>1.479)" if ecaltype=="EndCap" else "(lep_pt>=25 && abs(lep_pdgId)==11 && lep_relIso03<0.1)" # could be a complicated cut
    Plot.setDefaults(stack = stack, weight = weight, selectionString = selectionString, addOverFlowBin='upper')

    # Sequence
    sequence = []

    # Add a new fancy variable
    def make_absEInvMinusPInv( event, sample ):
        event.absEInvMinusPInv = abs(event.lep_eInvMinusPInv)
    sequence.append( make_absEInvMinusPInv)

    def print_mcmatchId( event, sample ):
        if isNonPrompt(event) and event.lep_mvaIdSpring16<0.3 and sample.name=="TTJets":
            print event.lep_mcMatchId

    #sequence.append(print_mcmatchId)

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
        attribute = TreeVariable.fromString( "lep_mvaIdSpring16/F" ),
        binning=[30,-1,1],
    ))

    plots.append(Plot(name=plotname+'Pt',
        texX = 'pt', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_pt/F" ),
        binning=[100,0,500],
    ))
    plots.append(Plot(name=plotname+'pdgId',
        texX = 'pdgId', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_pdgId/I" ),
        binning=[61,-30,30],
    ))
    plots.append(Plot(name=plotname+'EtaSc',
        texX = 'etaSc', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_etaSc/F" ),
        binning=[60,-3,3],
    ))
    plots.append(Plot(name=plotname+'Full5x5SigmaIetaIeta',
        texX = 'full5x5_sigmaIetaIeta', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_full5x5_sigmaIetaIeta/F" ),
        binning=[30,0,0.06],
    ))
    plots.append(Plot(name=plotname+'DEtaInSeed',
        texX = 'dEtaInSeed', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_dEtaInSeed/F" ),
        binning=[30,-0.03,0.03],
    ))
    plots.append(Plot(name=plotname+'DPhiScTrkIn',
        texX = 'dPhiScTrkIn', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_dPhiScTrkIn/F" ),
        binning=[20,-0.2,0.2],
    ))
    plots.append(Plot(name=plotname+'RelIso03',
        texX = 'relIso03', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_relIso03/F" ),
        binning=[90,0,0.3],
    ))
    plots.append(Plot(name=plotname+'EInvMinusPInv',
        texX = '|1/E-1/p|', texY = 'Number of Events',
        attribute = lambda event, sample: event.absEInvMinusPInv,
        binning=[30,0,0.15],
    ))
    plots.append(Plot(name=plotname+'LostOuterHits',
        texX = 'lostOuterHits', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_lostOuterHits/I" ),
        binning=[16,0,15],
    ))
    plots.append(Plot(name=plotname+'ConvVeto',
        texX = 'convVeto', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_convVeto/I" ),
        binning=[2,0,1],
    ))
    plots.append(Plot(name=plotname+'HadronicOverEm',
        texX = 'hadronicOverEm', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_hadronicOverEm/F" ),
        binning=[30,0,0.1],
    ))
    plots.append(Plot(name=plotname+'Rho',
        texX = 'rho', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_rho/F" ),
        binning=[100,0,5],
    ))
    plots.append(Plot(name=plotname+'Dxy',
        texX = 'dxy', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_dxy/F" ),
        binning=[60,-0.1,0.1],
    ))
    plots.append(Plot(name=plotname+'Dz',
        texX = 'dz', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_dz/F" ),
        binning=[60,-0.2,0.2],
    ))
    plots.append(Plot(name=plotname+'jetDR',
        texX = 'jetDR', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "lep_jetDR/F" ),
        binning=[61,-3,3],
    ))

    plots.append(Plot(name=plotname+'npfCand_neutral',
        texX = 'npfCand_neutral', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.npfCand_neutral,
        binning=[21,0,20],
    ))
    plots.append(Plot(name=plotname+'npfCand_charged',
        texX = 'npfCand_charged', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.npfCand_charged,
        binning=[71,0,70],
    ))
    plots.append(Plot(name=plotname+'npfCand_photon',
        texX = 'npfCand_photon', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.npfCand_photon,
        binning=[41,0,40],
    ))
    plots.append(Plot(name=plotname+'npfCand_electron',
        texX = 'npfCand_electron', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.npfCand_electron,
        binning=[21,0,20],
    ))
    plots.append(Plot(name=plotname+'npfCand_muon',
        texX = 'npfCand_muon', texY = 'Number of Events',
        attribute = lambda lepton, sample: lepton.npfCand_muon,
        binning=[21,0,20],
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
        plot_directory_ = os.path.join(plot_directory, 'histogram_plots', 'stacked_samples', plotname, ("log" if log else "lin"))
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

