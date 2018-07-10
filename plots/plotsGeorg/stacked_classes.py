###########
# imports #
###########

# Standard imports
import ROOT
import os
from array import array
from copy import deepcopy
import math

# RootTools
from RootTools.core.standard import *

# User specific 
from TopEFT.Tools.user import plot_directory
plot_directory_=os.path.join(plot_directory, 'DeepLepton')
plot_directory=plot_directory_

# plot samples definitions
from def_plot_samples import plot_samples, histo_plot_variables

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

##############################
# load samples and variables #
##############################

#define samples for electorns and muons
samples=plot_samples()
sampleEle=samples["ele"]
sampleMuo=samples["muo"]
PlotTrainData=samples["plottraindata"]  #1=true, 0=false
ElectronDate=samples["eledate"]
MuonDate=samples["muodate"]

# variables to read
read_variables=histo_plot_variables()

#########################
# define plot structure #
#########################

leptonFlavours=[]
leptonFlavours.append({"Name":"Electron", "ShortName":"ele", "pdgId":11, "sample":sampleEle, "selectionString": "abs(lep_pdgId)==11", "date":ElectronDate})
leptonFlavours.append({"Name":"Muon", "ShortName":"muo", "pdgId":13, "sample":sampleMuo, "selectionString": "abs(lep_pdgId)==13", "date":MuonDate})

pt_cuts=[]
pt_cuts.append({"Name":"pt15to25","lower_limit":15, "upper_limit":25, "selectionString": "lep_pt>=15&&lep_pt<25"})
pt_cuts.append({"Name":"pt25toInf","lower_limit":25, "selectionString": "lep_pt>=25"})

ecalTypes=[]
ecalTypes.append({"Name":"All", "selectionString": "abs(lep_etaSc)>0."})
ecalTypes.append({"Name":"EndCap", "selectionString": "abs(lep_etaSc)>1.479"})
ecalTypes.append({"Name":"Barrel", "selectionString": "abs(lep_etaSc)<=1.479"})

####################################
# loop over samples and draw plots #
####################################

for leptonFlavour in leptonFlavours:

    #define class samples
    samplePrompt =    deepcopy(leptonFlavour["sample"])
    sampleNonPrompt = deepcopy(leptonFlavour["sample"])
    sampleFake =      deepcopy(leptonFlavour["sample"])

    samplePrompt.setSelectionString("(lep_isPromptId==1&&"+leptonFlavour["selectionString"]+")")
    sampleNonPrompt.setSelectionString("(lep_isNonPromptId==1&&"+leptonFlavour["selectionString"]+")")
    sampleFake.setSelectionString("(lep_isFakeId==1&&"+leptonFlavour["selectionString"]+")")

    samplePrompt.name = "Prompt"
    sampleNonPrompt.name = "NonPrompt"
    sampleFake.name = "Fake"

    samplePrompt.texName = "Prompt"
    sampleNonPrompt.texName = "NonPrompt"
    sampleFake.texName = "Fake"

    samplePrompt.style =  fillStyle(color=ROOT.kCyan, style=3004, lineColor=ROOT.kCyan)
    sampleNonPrompt.style =     fillStyle(color=ROOT.kBlue, style=3004, lineColor=ROOT.kBlue)
    sampleFake.style =       fillStyle(color=ROOT.kGray, style=3004, lineColor=ROOT.kGray)

    # Define stack
    mc    = [samplePrompt,sampleNonPrompt,sampleFake]  # A full example would be e.g. mc = [ttbar, ttz, ttw, ...]
    stack = Stack(mc) # A full example would be e.g. stack = Stack( mc, [data], [signal1], [signal2] ) -> Samples in "mc" are stacked in the plot

    if leptonFlavour["Name"]=="Muon":
        ecalTypes=[]
        ecalTypes.append({"Name":"All", "selectionString": "abs(lep_etaSc)>0."})

    for pt_cut in pt_cuts:
        for ecalType in ecalTypes:
                
            # Set some defaults -> these need not be specified below for each plot
            weight = staticmethod(lambda event, sample: 1.)  # could be e.g. weight = lambda event, sample: event.weight
            selectionString = "("+pt_cut["selectionString"]+"&&"+ecalType["selectionString"]+")" # could be a complicated cut
            Plot.setDefaults(stack = stack, weight = weight, selectionString = selectionString, addOverFlowBin='upper')
            plotname=""
            # Sequence
            sequence = []

            # Add a new fancy variable
            def make_absEInvMinusPInv( event, sample ):
                event.absEInvMinusPInv = abs(event.lep_eInvMinusPInv)
            sequence.append( make_absEInvMinusPInv)

            #def print_mcmatchId( event, sample ):
            #    if isNonPrompt(event) and event.lep_mvaIdSpring16<0.3 and sample==sample:
            #        print event.lep_mcMatchId

            #def print_class( event, sample ):
            #    assert isPrompt(event) + isNonPrompt(event) + isFake(event)==1, "Should never happen!"

            #    print event.lep_isPromptId, event.lep_isNonPromptId, event.lep_isFakeId, event.lep_mcMatchId, event.lep_mcMatchAny, isPrompt(event), isNonPrompt(event), isFake(event), event.lep_pdgId
            #    #print "Fill", event.lep_isPromptId if ((isPrompt(event) and sample==samplePrompt) or (isNonPrompt(event) and sample==sampleNonPrompt) or (isFake(event) and sample==sampleFake)) else float('nan')
            #    #print "Fill2", (isPrompt(event) and sample==samplePrompt),(isNonPrompt(event) and sample==sampleNonPrompt),(isFake(event) and sample==sampleFake)
            ##sequence.append(print_class)

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
                attribute = lambda lepton, sample: lepton.lep_mvaIdSpring16, 
                binning=[30,-1,1],
            ))
            plots.append(Plot(name=plotname+'Pt',
                texX = 'pt', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_pt,
                binning=[100,0,500],
            ))
            plots.append(Plot(name=plotname+'pdgId',
                texX = 'pdgId', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_pdgId,
                binning=[61,-30,30],
            ))
            plots.append(Plot(name=plotname+'EtaSc',
                texX = 'etaSc', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_etaSc,
                binning=[60,-3,3],
            ))
            plots.append(Plot(name=plotname+'Full5x5SigmaIetaIeta',
                texX = 'full5x5_sigmaIetaIeta', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_full5x5_sigmaIetaIeta,
                binning=[30,0,0.06],
            ))
            plots.append(Plot(name=plotname+'DEtaInSeed',
                texX = 'dEtaInSeed', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_dEtaInSeed,
                binning=[30,-0.03,0.03],
            ))
            plots.append(Plot(name=plotname+'DPhiScTrkIn',
                texX = 'dPhiScTrkIn', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_dPhiScTrkIn,
                binning=[20,-0.2,0.2],
            ))
            plots.append(Plot(name=plotname+'RelIso03',
                texX = 'relIso03', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_relIso03,
                binning=[90,0,0.3],
            ))
            plots.append(Plot(name=plotname+'EInvMinusPInv',
                texX = '|1/E-1/p|', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.absEInvMinusPInv,
                binning=[30,0,0.15],
            ))
            plots.append(Plot(name=plotname+'LostOuterHits',
                texX = 'lostOuterHits', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_lostOuterHits,
                binning=[16,0,15],
            ))
            plots.append(Plot(name=plotname+'ConvVeto',
                texX = 'convVeto', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_convVeto,
                binning=[2,0,1],
            ))
            plots.append(Plot(name=plotname+'HadronicOverEm',
                texX = 'hadronicOverEm', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_hadronicOverEm,
                binning=[30,0,0.1],
            ))
            plots.append(Plot(name=plotname+'Rho',
                texX = 'rho', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_rho,
                binning=[100,0,5],
            ))
            plots.append(Plot(name=plotname+'Dxy',
                texX = 'dxy', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_dxy,
                binning=[60,-0.1,0.1],
            ))
            plots.append(Plot(name=plotname+'Dz',
                texX = 'dz', texY = 'Number of Events',
                attribute = lambda lepton, sample: lepton.lep_dz,
                binning=[60,-0.2,0.2],
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
                  (0.15, 0.95, 'TrainData' if PlotTrainData else 'TestData'),
                  (0.45, 0.95, pt_cut["Name"]+" "+ecalType["Name"]+" "+leptonFlavour["Name"]+"s")
                ]
                return [tex.DrawLatex(*l) for l in lines]

            # Draw a plot and make it look nice-ish
            def drawPlots(plots, dataMCScale):
              for log in [False, True]:
                plot_directory_ = os.path.join(plot_directory, leptonFlavour["date"], leptonFlavour["Name"], 'histograms_'+('TrainData' if PlotTrainData else 'TestData'), pt_cut["Name"]+"_"+ecalType["Name"]+"_"+leptonFlavour["Name"]+"s", ("log" if log else "lin"))
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

