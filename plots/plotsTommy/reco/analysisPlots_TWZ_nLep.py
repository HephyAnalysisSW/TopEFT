#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi, acos, cosh
from RootTools.core.standard      import *
from TopEFT.Tools.user            import plot_directory
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, deltaR, deltaR2
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.cutInterpreter  import cutInterpreter
from TopEFT.Tools.triggerSelector import triggerSelector
from TopEFT.samples.color         import color

# for mt2ll
from TopEFT.Tools.mt2Calculator              import mt2Calculator
mt2Calc = mt2Calculator()

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--noData',             action='store_true', default=True,           help='also plot data?')
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--plot_directory',      action='store',      default='Histo_Integral')#'analysisPlots_4l')
argParser.add_argument('--selection',           action='store',      default='None')#'quadlepTWZ-onZ1-noZ2')  # quadlep-lepSelQuad-njet2p-btag0p-onZ1-offZ2 or quadlep-lepSelQuad-njet2p-btag1p-onZ1-offZ2 for signal regions
argParser.add_argument('--normalize',           action='store_true', default=False,             help="Normalize yields" )
argParser.add_argument('--year',                action='store',      default=2016,   type=int,  help="Which year?" )
args = argParser.parse_args()


# PU reweighting on the fly
from TopEFT.Tools.puProfileCache    import puProfile
from TopEFT.Tools.puReweighting     import getReweightingFunction
from TopEFT.samples.helpers         import fromHeppySample

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"
if args.noData:                       args.plot_directory += "_noData"
if args.normalize: args.plot_directory += "_normalize"
#
# Make samples, will be searched for in the postProcessing directory
#

if args.year == 2016:
    data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
    from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *
    data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
    from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

data_directory = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"

signals = []

#
# Text on the plots
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

scaling = { i+1:0 for i in range(len(signals)) }

def drawPlots(plots, mode, dataMCScale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.plot_directory, mode + ("_log" if log else ""), args.selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      if not args.noData: 
        if mode == "all": plot.histos[1][0].legendText = "Data"
        if mode == "SF":  plot.histos[1][0].legendText = "Data (SF)"
      extensions_ = ["pdf", "png", "root"]# if mode == 'all' else ['png']

      plotting.draw(plot,
	    plot_directory = plot_directory_,
        extensions = extensions_,
	    ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = scaling if args.normalize else {},
	    legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
	    drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale ),
        copyIndexPHP = True,
      )

def getLeptonSelection( mode ):
#    if   mode=="nLep":  return "nMuons_tight_4l+nElectrons_tight_4l>=1" 
    if mode =="nLep":   return "(1)"

#
# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I]", "njet/I","nJetSelected/I",
                    "lep[mediumMuonId/I,pt/F,eta/F,phi/F,pdgId/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,lostHits/I,convVeto/I,dxy/F,dz/F,hadronicOverEm/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,mvaTTV/F]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "Z1_l1_index_4l/I", "Z1_l2_index_4l/I", "nonZ1_l1_index_4l/I", "nonZ1_l2_index_4l/I", "Z2_l1_index_4l/I", "Z2_l2_index_4l/I", 
                    "Z1_phi_4l/F","Z1_pt_4l/F", "Z1_mass_4l/F", "Z1_eta_4l/F","Z1_lldPhi_4l/F", "Z1_lldR_4l/F", "Z1_cosThetaStar_4l/F","Higgs_mass/F",
                    "Z2_phi_4l/F","Z2_pt_4l/F", "Z2_mass_4l/F", "Z2_eta_4l/F", "Z2_cosThetaStar_4l/F", "totalLeptonCharge/I",
                    ]

sequence = []

def getLooseLeptonMult( event, sample ):
    leptons = [getObjDict(event, 'lep_', ['eta','pt','phi','charge', 'pdgId', 'sourceId','mediumMuonId'], i) for i in range(len(event.lep_pt))]
    lepLoose = [ l for l in leptons if l['pt'] > 10 and ((l['mediumMuonId'] and abs(l['pdgId'])==13) or abs(l['pdgId'])==11)  ]
    event.nLepLoose = len(lepLoose)

sequence.append( getLooseLeptonMult )


#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['nLep']
for index, mode in enumerate(allModes):
    yields[mode] = {}
    logger.info("Working on mode %s", mode)
    if not args.noData:
        data_sample = Run2016 if args.year == 2016 else Run2017
        data_sample.texName = "data"

        data_sample.setSelectionString([getFilterCut(isData=True, year=args.year), getLeptonSelection(mode)])
        data_sample.name           = "data"
        data_sample.read_variables = ["evt/I","run/I"]
        data_sample.style          = styles.errorStyle(ROOT.kBlack)
        lumi_scale                 = data_sample.lumi/1000

    if args.noData: lumi_scale = 35.9 if args.year == 2016 else 41.0
    weight_ = lambda event, sample: event.weight
    lumi_scale = 300    

    TTZ_mc = TTZtoLLNuNu

    if args.year == 2016:
        # TWZ
        #mc              = [ TWZ, TTZ_mc, TTX_rare2, TZQ, WZ_amcatnlo, rare, ZZ, nonpromptMC ]
        #mc              = [ yt_TWZ, TTZ_mc, TTX_rare2, TZQ, WZ_amcatnlo, rare, ZZ, nonpromptMC ]

#        mc = [ TWZ ]
        mc = [ yt_TWZ ]
#        mc = [ yt_TWZ_filter, yt_TWZ ]
#        mc = [ yt_TWZ_filter ]
        # TTWW
        # TZZ 

        #mc              = [ yt_TZZ, ZZ, TTZ_mc, WZ_amcatnlo, rare, nonpromptMC, TZQ, TTX_rare2 ]
        #mc              = [ TTWW, TTTT, TTW, TTZtoLLNuNu, nonpromptMC, TTX_rare2, rare, ZZ ]
        #mc             = [ TTWW, TTW, TTZtoLLNuNu, WZ_amcatnlo, nonpromptMC, TTX_rare2, rare, ZZ ]
        #mc             = [ TTZtoLLNuNu, TTW, TTX_rare2, TTWW, rare ]
    
    for sample in mc: sample.style = styles.fillStyle(sample.color)

    for sample in mc + signals:
      sample.scale          = lumi_scale
      #sample.read_variables = ['reweightBTagCSVv2_SF/F', 'reweightBTagDeepCSV_SF/F', 'reweightPU36fb/F', 'reweightTrigger_tight_4l/F', 'reweightLeptonTrackingSF_tight_4l/F', 'nTrueInt/F', 'reweightPU36fb/F', 'reweightLeptonSF_tight_4l/F']#, 'reweightLeptonSF_tight_4l/F']
      
      sample.weight = lambda event, sample: 1
#      if args.year == 2016:
#          sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightTrigger_tight_4l*event.reweightLeptonTrackingSF_tight_4l*event.reweightPU36fb*event.reweightLeptonSF_tight_4l #*nTrueInt36fb_puRW(event.nTrueInt)
#      else:
#          sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightTrigger_tight_4l*event.reweightPU36fb*event.reweightLeptonSF_tight_4l #*event.reweightLeptonSF_tight_4l #*nTrueInt36fb_puRW(event.nTrueInt)
#      tr = triggerSelector(args.year)
      sample.setSelectionString(getLeptonSelection(mode))  
    #sample.setSelectionString([getFilterCut(isData=False, year=args.year), getLeptonSelection(mode), tr.getSelection("MC")])

    if not args.noData:
      stack = Stack(mc, data_sample)
    else:
      stack = Stack(mc)

    stack.extend( [ [s] for s in signals ] )

    if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 1 )
    
    # Use some defaults
    Plot.setDefaults(stack = stack, weight = staticmethod(weight_), selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='both')

    plots = []
    
    plots.append(Plot(
      texX = 'N_{l, loose}', texY = 'Number of Events',
      name = 'nLepLoose', attribute = lambda event, sample: event.nlep,
      #binning=[7,0.5,7.5],
      binning=[8,-0.5,7.5],
    ))

    plotting.fill(plots, read_variables = read_variables, sequence = sequence)

    if args.noData: yields[mode]["data"] = 0

    # noData
    dataMCScale = 0

    for plot in plots:
        for i, l in enumerate(plot.histos):
            for j, h in enumerate(l):
                test = h.Integral(4,6)
                print "INTEGRAL", test
#                    print h.GetXaxis().SetBinLabel(3,"test")
    drawPlots(plots, mode, dataMCScale)
    allPlots[mode] = plots

exit()

# Add the different channels into SF and all
for mode in ["comb1","comb2","comb3","all"]:
    yields[mode] = {}
    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in ['eeee','mueee','mumuee', 'mumumue', 'mumumumu'])
        except: yields[mode][y] = 0
    dataMCScale = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
    
    for plot in allPlots['mumumumu']:
        if mode=="comb1":
            tmp = allPlots['mumumue']
        elif mode=="comb2":
            tmp = allPlots['mumuee']
        elif mode=="comb3":
            tmp = allPlots['mueee']
        else:
            tmp = allPlots['eeee']
        for plot2 in (p for p in tmp if p.name == plot.name):
            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
                    if i==k:
                        j.Add(l)
    
    if mode == "all": drawPlots(allPlots['mumumumu'], mode, dataMCScale)

logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )


