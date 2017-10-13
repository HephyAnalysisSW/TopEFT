#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi
from RootTools.core.standard      import *
from TopEFT.tools.user            import plot_directory
from TopEFT.tools.helpers         import deltaPhi, getObjDict, getVarValue
from TopEFT.tools.objectSelection import getFilterCut
from TopEFT.tools.cutInterpreter  import cutInterpreter

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--signal',             action='store',      default=None,            nargs='?', choices=[None, "ewkDM"], help="Add signal to plot")
argParser.add_argument('--onlyTTZ',            action='store_true', default=False,           help="Plot only ttZ")
argParser.add_argument('--noData',             action='store_true', default=False,           help='also plot data?')
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--plot_directory',     action='store',      default='80X_v4')
argParser.add_argument('--selection',          action='store',      default='lepSel-njet3p-btag1p')
argParser.add_argument('--badMuonFilters',     action='store',      default="Summer2016",  help="Which bad muon filters" )
args = argParser.parse_args()

#
# Logger
#
import TopEFT.tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"
if args.noData:                       args.plot_directory += "_noData"
if args.badMuonFilters!="Summer2016": args.plot_directory += "_badMuonFilters_"+args.badMuonFilters
if args.signal:                       args.plot_directory += "_signal_"+args.signal
if args.onlyTTZ:                      args.plot_directory += "_onlyTTZ"
#
# Make samples, will be searched for in the postProcessing directory
#
postProcessing_directory = "TopEFT_PP_v4/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

if args.signal == "ewkDM":
    postProcessing_directory = "TopEFT_PP_v4/trilep/"
    from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *
    ewkDM_0     = ewkDM_ttZ_ll
    ewkDM_1     = ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20

    ewkDM_2     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767
    ewkDM_3     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767
    ewkDM_4     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767
    ewkDM_5     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25
    ewkDM_6     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25
    ewkDM_7     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25
    ewkDM_8     = ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25


    ewkDM_0.style = styles.lineStyle( ROOT.kBlack, width=3, dotted=False, dashed=False )
    ewkDM_1.style = styles.lineStyle( ROOT.kBlack, width=3, dotted=True )

    ewkDM_2.style = styles.lineStyle( ROOT.kMagenta, width=3)
    ewkDM_3.style = styles.lineStyle( ROOT.kMagenta, width=3, dotted=True)
    ewkDM_4.style = styles.lineStyle( ROOT.kMagenta, width=3, dashed=True)

    ewkDM_5.style = styles.lineStyle( ROOT.kBlue, width=3)
    ewkDM_6.style = styles.lineStyle( ROOT.kBlue, width=3, dotted=True)
    ewkDM_7.style = styles.lineStyle( ROOT.kGreen+2, width=3)
    ewkDM_8.style = styles.lineStyle( ROOT.kGreen+2, width=3, dotted=True)


    #signals = [ewkDM_0,ewkDM_1]
    #signals = [ewkDM_1]
    signals = [ewkDM_2,ewkDM_3,ewkDM_4,ewkDM_5,ewkDM_6,ewkDM_7,ewkDM_8]
else:
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

def drawPlots(plots, mode, dataMCScale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.plot_directory, mode + ("_log" if log else ""), args.selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      if not args.noData: 
        if mode == "all": plot.histos[1][0].legendText = "Data"
        if mode == "SF":  plot.histos[1][0].legendText = "Data (SF)"

      plotting.draw(plot,
	    plot_directory = plot_directory_,
	    ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = {},
	    legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
	    drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale )
      )

#
# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F]", "njet/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/F]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I", 
                    "Z_phi/F","Z_pt/F", "Z_mass/F", "Z_lldPhi/F", "Z_lldR/F"
                    ]

sequence = []

def getDPhiZLep( event, sample ):
    event.dPhiZLep = deltaPhi(event.lep_phi[event.nonZ_l1_index], event.Z_phi)

def getDPhiZJet( event, sample ):
    event.dPhiZJet = deltaPhi(event.jet_phi[0], event.Z_phi) if event.njet>0 and event.Z_mass>0 else float('nan')

def getJets( event, sample ):
    jetVars     = ['eta','pt','phi','btagCSV']
    event.jets_sortbtag  = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'njet')))]
    event.jets_sortbtag.sort( key = lambda l:-l['btagCSV'] )

mt = 172.5
def getTopCands( event, sample ):
    
    lepton  = ROOT.TLorentzVector()
    met     = ROOT.TLorentzVector()
    b1      = ROOT.TLorentzVector()
    b2      = ROOT.TLorentzVector()
    
    lepton.SetPtEtaPhiM(event.lep_pt[event.nonZ_l1_index], event.lep_eta[event.nonZ_l1_index], event.lep_phi[event.nonZ_l1_index], 0)
    met.SetPtEtaPhiM(event.met_pt, 0, event.met_phi, 0)
    b1.SetPtEtaPhiM(event.jets_sortbtag[0]['pt'], event.jets_sortbtag[0]['eta'], event.jets_sortbtag[0]['phi'], 0. )
    b2.SetPtEtaPhiM(event.jets_sortbtag[1]['pt'], event.jets_sortbtag[1]['eta'], event.jets_sortbtag[1]['phi'], 0. )

    W    = lepton + met
    top1 = W + b1
    top2 = W + b2

    ## order top candidates in terms of mass closest to the top mass
    if abs(top1.M()-mt) > abs(top2.M()-mt): top1, top2 = top2, top1
    #if top1.Pt() < top2.Pt(): top1, top2 = top2, top1

    event.top1_mass = top1.M()
    event.top1_pt   = top1.Pt()
    event.top1_phi  = top1.Phi()

    event.top2_mass = top2.M()
    event.top2_pt   = top2.Pt()
    event.top2_phi  = top2.Phi()

    event.b1_pt     = b1.Pt()
    event.b1_phi    = b1.Phi()
    event.b2_pt     = b2.Pt()
    event.b2_phi    = b2.Phi()


sequence = [getDPhiZLep, getDPhiZJet,getJets,getTopCands ]


def getLeptonSelection( mode ):
  if   mode=="mumumu": return "nGoodMuons==3&&nGoodElectrons==0"
  elif mode=="mumue":  return "nGoodMuons==2&&nGoodElectrons==1"
  elif mode=="muee":   return "nGoodMuons==1&&nGoodElectrons==2"
  elif mode=="eee":    return "nGoodMuons==0&&nGoodElectrons==3"

#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['mumumu','mumue','muee', 'eee']
for index, mode in enumerate(allModes):
    yields[mode] = {}
    if not args.noData:
      if   mode=="mumu": data_sample = DoubleMuon_Run2016_backup
      if   mode=="mumu": data_sample.texName = "data (2 #mu)"

      data_sample.setSelectionString([getFilterCut(isData=True, badMuonFilters = args.badMuonFilters), getLeptonSelection(mode)])
      data_sample.name           = "data"
      data_sample.read_variables = ["evt/I","run/I"]
      data_sample.style          = styles.errorStyle(ROOT.kBlack)
      lumi_scale                 = data_sample.lumi/1000

    if args.noData: lumi_scale = 35.9
    weight_ = lambda event, sample: event.weight

    if args.onlyTTZ:
        mc = [ TTZtoLLNuNu ]
    else:
        mc             = [ TTZtoLLNuNu , TTX, WZ, rare ]#, nonprompt ]

    for sample in mc: sample.style = styles.fillStyle(sample.color)

    for sample in mc + signals:
      sample.scale          = lumi_scale
      #sample.read_variables = ['reweightTopPt/F','reweightDilepTriggerBackup/F','reweightLeptonSF/F','reweightBTag_SF/F','reweightPU36fb/F', 'nTrueInt/F', 'reweightLeptonTrackingSF/F']
      #sample.weight         = lambda event, sample: event.reweightTopPt*event.reweightBTag_SF*event.reweightLeptonSF*event.reweightDilepTriggerBackup*event.reweightPU36fb*event.reweightLeptonTrackingSF
      sample.setSelectionString([getFilterCut(isData=False, badMuonFilters = args.badMuonFilters), getLeptonSelection(mode)])

    if not args.noData:
      stack = Stack(mc, data_sample)
    else:
      stack = Stack(mc)

    stack.extend( [ [s] for s in signals ] )

    if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 1 )

    # Use some defaults
    Plot.setDefaults(stack = stack, weight = weight_, selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper')

    plots = []
    
    plots.append(Plot(
      name = 'yield', texX = 'yield', texY = 'Number of Events',
      attribute = lambda event, sample: 0.5 + index,
      binning=[4, 0, 4],
    ))
    
    plots.append(Plot(
      name = 'nVtxs', texX = 'vertex multiplicity', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nVert/I" ),
      binning=[50,0,50],
    ))
    
    plots.append(Plot(
        texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_pt/F" ),
        binning=[400/20,0,400],
    ))
    
    plots.append(Plot(
        texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_phi/F" ),
        binning=[10,-pi,pi],
    ))
    
    plots.append(Plot(
        texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[25,0,500],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_coarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 40 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[20,0,800],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_superCoarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[3,0,800],
    ))
    
    plots.append(Plot(
        texX = '#Delta#phi(ll)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_lldPhi/F" ),
        binning=[10,0,pi],
    ))

    plots.append(Plot(
        name = "dPhiZL",
        texX = '#Delta#phi(Z,l)', texY = 'Number of Events',
        attribute = lambda event, sample:event.dPhiZLep,
        binning=[10,0,pi],
    ))
    
    #plots.append(Plot( #FIXME -> what is this? Didn't understand the formula
    #    name = "dPhiZL_RF",
    #    texX = '#Delta#phi(Z,l) in Z RF', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.dPhiZLep_RF,
    #    binning=[10,0,pi],
    #))
    
    plots.append(Plot(
        name = "dPhiZJet",
        texX = '#Delta#phi(Z,j1)', texY = 'Number of Events',
        attribute = lambda event, sample:event.dPhiZJet,
        binning=[10,0,pi],
    ))
    
    plots.append(Plot(
        name = "lZ1_pt",
        texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning=[30,0,300],
    ))
    
    plots.append(Plot(
        name = 'lZ1_pt_ext', texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning=[20,40,440],
    ))
    
    plots.append(Plot(
        name = "lZ2_pt",
        texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning=[30,0,300],
    ))
    
    plots.append(Plot(
        name = 'lZ2_pt_ext', texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning=[20,40,440],
    ))
    
    plots.append(Plot(
        name = 'lnonZ1_pt',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[30,0,300],
    ))

    plots.append(Plot(
        name = 'lnonZ1_pt',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[12,0,180],
    ))
    
    
    plots.append(Plot(
        texX = 'M(ll) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "Z_mass/F" ),
        binning=[10,81,101],
    ))

    plots.append(Plot(
        name = "Z_mass_wide",
        texX = 'M(ll) (GeV)', texY = 'Number of Events / 2 GeV',
        attribute = TreeVariable.fromString( "Z_mass/F" ),
        binning=[50,20,120],
    ))
    
    plots.append(Plot(
      texX = 'N_{jets}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "njet/I" ),
      binning=[5,2.5,7.5],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet1_pt', attribute = lambda event, sample: event.jet_pt[0],
      binning=[600/30,0,600],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(2nd leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet2_pt', attribute = lambda event, sample: event.jet_pt[1],
      binning=[600/30,0,600],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'bjet1_pt', attribute = lambda event, sample: event.b1_pt,
      binning=[20,0,400],
    ))

    plots.append(Plot(
      texX = 'p_{T}(2nd leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'bjet2_pt', attribute = lambda event, sample: event.b2_pt,
      binning=[20,0,400],
    ))
    
    plots.append(Plot(
        name = "top_cand1_pt", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 30 GeV',
        attribute = lambda event, sample:event.top1_pt,
        binning=[20,0,600],
    ))

    plots.append(Plot(
        name = "top_cand1_pt_coarse", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 200 GeV',
        attribute = lambda event, sample:event.top1_pt,
        binning=[3,0,600],
    ))

    plots.append(Plot(
        name = "top_cand1_mass", texX = 'M(t cand1) (GeV)', texY = 'Number of Events / 15 GeV',
        attribute = lambda event, sample:event.top1_mass,
        binning=[20,0,300],
    ))

    plots.append(Plot(
        name = "top_cand1_phi", texX = '#phi(t cand1)', texY = 'Number of Events',
        attribute = lambda event, sample:event.top1_phi,
        binning=[10,-pi,pi],
    ))

    plots.append(Plot(
        name = "top_cand2_pt", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 30 GeV',
        attribute = lambda event, sample:event.top2_pt,
        binning=[20,0,600],
    ))

    plots.append(Plot(
        name = "top_cand2_mass", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 15 GeV',
        attribute = lambda event, sample:event.top2_mass,
        binning=[20,0,300],
    ))

    plots.append(Plot(
        name = "top_cand2_phi", texX = '#phi(t cand1)', texY = 'Number of Events',
        attribute = lambda event, sample:event.top2_phi,
        binning=[10,-pi,pi],
    ))

    plotting.fill(plots, read_variables = read_variables, sequence = sequence)

    # Get normalization yields from yield histogram
    for plot in plots:
      if plot.name == "yield":
        for i, l in enumerate(plot.histos):
          for j, h in enumerate(l):
            yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
            h.GetXaxis().SetBinLabel(1, "#mu#mu#mu")
            h.GetXaxis().SetBinLabel(2, "#mu#mue")
            h.GetXaxis().SetBinLabel(3, "#muee")
            h.GetXaxis().SetBinLabel(4, "eee")
    if args.noData: yields[mode]["data"] = 0

    yields[mode]["MC"] = sum(yields[mode][s.name] for s in mc)
    dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    drawPlots(plots, mode, dataMCScale)
    allPlots[mode] = plots

# Add the different channels into SF and all
for mode in ["comb1","comb2","all"]:
    yields[mode] = {}
    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in ['eee','muee','mumue', 'mumumu'])
        except: yields[mode][y] = 0
    dataMCScale = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
    
    for plot in allPlots['mumumu']:
        if mode=="comb1":
            tmp = allPlots['mumue']
        elif mode=="comb2":
            tmp = allPlots['muee']
        else:
            tmp = allPlots['eee']
        for plot2 in (p for p in tmp if p.name == plot.name):
            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
                    if i==k:
                        j.Add(l)
    
    if mode == "all": drawPlots(allPlots['mumumu'], mode, dataMCScale)

logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )

