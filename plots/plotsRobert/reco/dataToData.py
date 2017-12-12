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
from TopEFT.Tools.user            import plot_directory
from TopEFT.Tools.helpers         import deltaR, deltaPhi, getObjDict, getVarValue
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.cutInterpreter  import cutInterpreter

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--plot_directory',     action='store',      default='data_to_data')
argParser.add_argument('--selection',          action='store',      default='dilepOS')
args = argParser.parse_args()

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)


if args.small:                        args.plot_directory += "_small"
#
# Make samples, will be searched for in the postProcessing directory
#

postProcessing_directory = "TopEFT_PP_2017_v14/dilep"
data_directory           = "/afs/hephy.at/data/rschoefbeck01/cmgTuples"  
from TopEFT.samples.cmgTuples_Data25ns_92X_Run2017_postProcessed import *

postProcessing_directory = "TopEFT_PP_v14/trilep/"
data_directory           = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"  
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *

# define 3l selections
def getLeptonSelection( mode ):
  if   mode=="mumu": return "nGoodMuons==2&&nGoodElectrons==0"
  elif mode=="mue":  return "nGoodMuons==1&&nGoodElectrons==1"
  elif mode=="ee":   return "nGoodMuons==0&&nGoodElectrons==2"
  elif mode=='all':  return "nGoodMuons+nGoodElectrons==2"

#logger.info( "PU reweighting for data %s", signal.name )
#signal_nvtx = signal.get1DHistoFromDraw("nVtx", [20,0,100], selectionString = sel_string, weightString="weight")
#signal_nvtx.Scale(1./signal_nvtx.Integral())
#
#signal.reweight_nvtx_histo = TTZ_nvtx.Clone()
#signal.reweight_nvtx_histo.Divide(signal_nvtx)
#
#signal.weight = get_reweight( "Z_pt", signal.reweight_nvtx_histo )

# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F]", "nJetSelected/I", "njet/I",
                    "lep[pt/F,eta/F,etaSc/F,phi/F,pdgId/I,tightId/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,mediumMuonId/I,lostHits/I,convVeto/I,dxy/F,dz/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,mvaTTH/F,relIso/F]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I", 
                    "Z_phi/F", "Z_eta/F", "Z_pt/F", "Z_mass/F", "Z_lldPhi/F", "Z_lldR/F"
                    ]
sequence = []

#
# Text on the plots
#
def drawObjects( lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Preliminary' ), 
      (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)'% lumi_scale )
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots, mode, lumi_scale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.plot_directory, mode + ("_log" if log else ""), args.selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      #if mode == "all": plot.histos[1][0].legendText = "Data"
      #if mode == "SF":  plot.histos[1][0].legendText = "Data (SF)"

      plotting.draw(plot,
	    plot_directory = plot_directory_,
	    #ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    #scaling = {0:1} if args.normalizeToSM else {},
	    legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
	    drawObjects = drawObjects( lumi_scale ),
        copyIndexPHP = True
      )

#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['mumu','mue','ee']
for index, mode in enumerate(allModes):
    yields[mode] = {}
    if mode == "mumu":
        data_2016_sample = SingleMuon_Run2016 
        data_2016_sample.texName = "data 2016 (2#mu)"
        data_2017_sample = SingleMuon_Run2017 
        data_2017_sample.texName = "data 2017 (2#mu)"
    elif mode == "ee":
        data_2016_sample = SingleElectron_Run2016
        data_2016_sample.texName = "data 2016 (2e)"
        data_2017_sample = SingleElectron_Run2017
        data_2017_sample.texName = "data 2017 (2e)"
    elif mode == 'mue':
        data_2016_sample = SingleEleMu_Run2016
        data_2016_sample.texName = "data 2016 (1#mu, 1e)"
        data_2017_sample = SingleEleMu_Run2017
        data_2017_sample.texName = "data 2017 (1#mu, 1e)"
    else: raise ValueError    

    data_2016_sample.setSelectionString([getFilterCut(isData=True, badMuonFilters = "Summer2016", year=2016), getLeptonSelection(mode)])
    data_2016_sample.read_variables = ["evt/I","run/I"]
    data_2016_sample.style          = styles.errorStyle(ROOT.kBlack)
    lumi_2016_scale                 = data_2016_sample.lumi/1000

    data_2017_sample.setSelectionString([getFilterCut(isData=True, badMuonFilters = "Summer2017", year=2017), getLeptonSelection(mode)])
    data_2017_sample.read_variables = ["evt/I","run/I"]
    data_2017_sample.style          = styles.errorStyle(ROOT.kBlack)
    lumi_2017_scale                 = data_2017_sample.lumi/1000

    weight_ = lambda event, sample: event.weight

    stack = Stack( data_2017_sample, data_2016_sample )

    if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 1 )

    # Use some defaults
    Plot.setDefaults(stack = stack, weight = weight_, selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin=None)

    plots = []
    
    plots.append(Plot(
      name = 'yield', texX = 'yield', texY = 'Number of Events',
      attribute = lambda event, sample: 0.5 + index,
      binning=[3, 0, 3],
    ))
    
    plots.append(Plot(
      name = 'nVtxs', texX = 'vertex multiplicity', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nVert/I" ),
      binning=[80,0,80],
      addOverFlowBin='upper',
    ))
    
    plots.append(Plot(
        texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_pt/F" ),
        binning=[400/20,0,400],
      addOverFlowBin='upper',
    ))
    
    plots.append(Plot(
        texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_phi/F" ),
        binning=[10,-pi,pi],
    ))
    
    plots.append(Plot(
        texX = 'p_{T}(Z) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[25,0,500],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_coarse', texX = 'p_{T}(Z) (GeV)', texY = 'Number of Events / 40 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[20,0,800],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_superCoarse', texX = 'p_{T}(Z) (GeV)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[3,0,800],
    ))

    plots.append(Plot(
        name = 'Z_pt_reweighting', texX = 'p_{T}(Z) (GeV)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[20,0,1000],
    ))

    plots.append(Plot(
        name = 'Z_eta', texX = '#eta(Z) ', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_eta/F" ),
        binning=[30,-3,3],
    ))
    
    plots.append(Plot(
        texX = '#Delta#phi(ll)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_lldPhi/F" ),
        binning=[10,0,pi],
    ))

    plots.append(Plot(
        texX = '#DeltaR(ll)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_lldR/F" ),
        binning=[10,0,4],
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
        binning=[60,0,120],
    ))

    plots.append(Plot(
      texX = 'Cos(#Delta#phi(ll, E_{T}^{miss}))', texY = 'Number of Events',
      name = 'cosZMetphi',
      attribute = lambda event, sample: cos( event.Z_phi - event.met_phi ), 
      read_variables = ["met_phi/F", "Z_phi/F"],
      binning = [10,-1,1],
    ))

    plots.append(Plot(
      texX = 'E_{T}^{miss}/#sqrt{H_{T}} (GeV^{1/2})', texY = 'Number of Events',
      attribute = TreeVariable.fromString('metSig/F'),
      binning= [30,0,30],
    ))
    
    plots.append(Plot(
      texX = 'N_{jets}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nJetSelected/I" ),
      binning=[5,2.5,7.5],
      addOverFlowBin='upper',
    ))

    plots.append(Plot( name = "nBTagCSVv2",
      texX = 'number of medium b-tags (CSVM)', texY = 'Number of Events',
      attribute = TreeVariable.fromString('nBTag/I'),
      binning=[8,0,8],
      addOverFlowBin='upper',
    ))

    plots.append(Plot( name = "nBTagDeepCSV",
      texX = 'number of medium b-tags (DeepCSV)', texY = 'Number of Events',
      attribute = TreeVariable.fromString('nBTagDeepCSV/I'),
      binning=[8,0,8],
      addOverFlowBin='upper',
    ))

    plots.append(Plot(
      texX = 'H_{T} (GeV)', texY = 'Number of Events / 25 GeV',
      attribute = TreeVariable.fromString( "ht/F" ),
      binning=[500/25,0,600],
      addOverFlowBin='upper',
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet1_pt', attribute = lambda event, sample: event.jet_pt[0],
      binning=[600/30,0,600],
    ))

    plots.append(Plot(
      texX = '#eta(leading jet) (GeV)', texY = 'Number of Events',
      name = 'jet1_eta', attribute = lambda event, sample: abs(event.jet_eta[0]),
      binning=[10,0,3],
    ))

    plots.append(Plot(
      texX = '#phi(leading jet) (GeV)', texY = 'Number of Events',
      name = 'jet1_phi', attribute = lambda event, sample: event.jet_phi[0],
      binning=[10,-pi,pi],
    ))
    
    plots.append(Plot(
      texX = 'leading jet b-tag Disc. CSVv2', texY = 'Number of Events',
      name = 'jet1_CSVv2', attribute = lambda event, sample: event.jet_btagCSV[0],
      binning=[40,0,1],
    ))

    plots.append(Plot(
      texX = 'leading jet b-tag Disc. DeepCSV', texY = 'Number of Events',
      name = 'jet1_DeepCSV', attribute = lambda event, sample: event.jet_DFb[0] + event.jet_DFbb[0],
      binning=[40,0,1],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(2nd leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet2_pt', attribute = lambda event, sample: event.jet_pt[1],
      binning=[600/30,0,600],
    ))

    plots.append(Plot(
      texX = '#eta(2nd leading jet) (GeV)', texY = 'Number of Events',
      name = 'jet2_eta', attribute = lambda event, sample: abs(event.jet_eta[1]),
      binning=[10,0,3],
    ))

    plots.append(Plot(
      texX = '#phi(2nd leading jet) (GeV)', texY = 'Number of Events',
      name = 'jet2_phi', attribute = lambda event, sample: event.jet_phi[1],
      binning=[10,-pi,pi],
    ))
    
    plots.append(Plot(
      texX = '2nd leading jet b-tag Disc. CSVv2', texY = 'Number of Events',
      name = 'jet2_CSVv2', attribute = lambda event, sample: event.jet_btagCSV[1],
      binning=[40,0,1],
    ))

    plots.append(Plot(
      texX = '2nd leading jet b-tag Disc. DeepCSV', texY = 'Number of Events',
      name = 'jet2_DeepCSV', attribute = lambda event, sample: event.jet_DFb[1] + event.jet_DFbb[1],
      binning=[40,0,1],
    ))

    plots.append(Plot( name = "l1_pt",
      texX = 'p_{T}(l_{1}) (GeV)', texY = 'Number of Events / 15 GeV',
      attribute = lambda event, sample: event.lep_pt[0], 
      binning=[20,0,300],
    ))
  
    plots.append(Plot( name = "l1_dxy",
      texX = 'd_{xy}(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_dxy[0], 
      binning=[40,-0.2,0.2],
    ))

    plots.append(Plot( name = "l1_dz",
      texX = 'd_{z}(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_dz[0], 
      binning=[40,-0.2,0.2],
    ))
  
    plots.append(Plot( name = "l1_eta",
      texX = '#eta(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_eta[0], 
      binning=[30,-3,3],
    ))
  
    plots.append(Plot( name = "l1_phi",
      texX = '#phi(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_phi[0], 
      binning=[10,-pi,pi],
    ))
 
    plots.append(Plot( name = "l1_etaSc",
      texX = '#etaSc(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_etaSc[0], 
      binning=[30,-3,3],
    ))

    plots.append(Plot( name = "l1_relIso03",
      texX = 'relIso03(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_relIso03[0], 
      binning=[30,0,1],
    ))

    plots.append(Plot( name = "l1_relIso04",
      texX = 'relIso04(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_relIso04[0], 
      binning=[30,0,1],
    ))
 
    plots.append(Plot( name = "l1_sip3d",
      texX = 'sip3d(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_sip3d[0], 
      binning=[50,0,5],
    ))
 
    plots.append(Plot( name = "l1_lostHits",
      texX = 'lostHits(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_lostHits[0], 
      binning=[5,0,5],
    ))

    plots.append(Plot( name = "l1_dEtaScTrkIn",
      texX = 'dEtaScTrkIn(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_dEtaScTrkIn[0], 
      binning=[50,0,.01],
    ))

    plots.append(Plot( name = "l1_dPhiScTrkIn",
      texX = 'dPhiScTrkIn(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_dPhiScTrkIn[0], 
      binning=[50,0,.1],
    ))

    plots.append(Plot( name = "l1_eInvMinusPInv",
      texX = 'eInvMinusPInv(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_eInvMinusPInv[0], 
      binning=[50,0,0.02],
    ))

    plots.append(Plot( name = "l1_full5x5_sigmaIetaIeta",
      texX = 'full5x5_sigmaIetaIeta(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_full5x5_sigmaIetaIeta[0], 
      binning=[50,0,.04],
    ))

    plots.append(Plot( name = "l1_convVeto",
      texX = 'convVeto(l_{1})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_convVeto[0], 
      binning=[2,0,2],
    ))
 
    plots.append(Plot( name = "l2_pt",
      texX = 'p_{T}(l_{2}) (GeV)', texY = 'Number of Events / 15 GeV',
      attribute = lambda event, sample: event.lep_pt[1], 
      binning=[20,0,300],
    ))
  
    plots.append(Plot( name = "l2_dxy",
      texX = 'd_{xy}(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_dxy[1], 
      binning=[40,-0.2,0.2],
    ))

    plots.append(Plot( name = "l2_dz",
      texX = 'd_{z}(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_dz[1], 
      binning=[40,-0.2,0.2],
    ))
  
    plots.append(Plot( name = "l2_eta",
      texX = '#eta(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_eta[1], 
      binning=[30,-3,3],
    ))
  
    plots.append(Plot( name = "l2_phi",
      texX = '#phi(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_phi[1], 
      binning=[10,-pi,pi],
    ))

    plots.append(Plot( name = "l2_etaSc",
      texX = '#etaSc(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_etaSc[1], 
      binning=[30,-3,3],
    ))

    plots.append(Plot( name = "l2_relIso03",
      texX = 'relIso03(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_relIso03[1], 
      binning=[30,0,1],
    ))

    plots.append(Plot( name = "l2_relIso04",
      texX = 'relIso04(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_relIso04[1], 
      binning=[30,0,1],
    ))
 
    plots.append(Plot( name = "l2_sip3d",
      texX = 'sip3d(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_sip3d[1], 
      binning=[50,0,5],
    ))
 
    plots.append(Plot( name = "l2_lostHits",
      texX = 'lostHits(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_lostHits[1], 
      binning=[5,0,5],
    ))

    plots.append(Plot( name = "l2_dEtaScTrkIn",
      texX = 'dEtaScTrkIn(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_dEtaScTrkIn[1], 
      binning=[50,0,.01],
    ))

    plots.append(Plot( name = "l2_dPhiScTrkIn",
      texX = 'dPhiScTrkIn(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_dPhiScTrkIn[1], 
      binning=[50,0,.1],
    ))

    plots.append(Plot( name = "l2_eInvMinusPInv",
      texX = 'eInvMinusPInv(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_eInvMinusPInv[1], 
      binning=[50,0,0.02],
    ))

    plots.append(Plot( name = "l2_full5x5_sigmaIetaIeta",
      texX = 'full5x5_sigmaIetaIeta(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_full5x5_sigmaIetaIeta[1], 
      binning=[50,0,.04],
    ))

    plots.append(Plot( name = "l2_convVeto",
      texX = 'convVeto(l_{2})', texY = 'Number of Events',
      attribute = lambda event, sample: event.lep_convVeto[1], 
      binning=[2,0,2],
    ))
 

    plots.append(Plot(
      name = 'cosMetJet1phi',
      texX = 'Cos(#Delta#phi(E_{T}^{miss}, leading jet))', texY = 'Number of Events',
      attribute = lambda event, sample: cos( event.met_phi - event.jet_phi[0]), 
      read_variables = ["met_phi/F", "jet[phi/F]"],
      binning = [10,-1,1],
    ))
    
    plots.append(Plot(
      name = 'cosMetJet1phi_smallBinning',
      texX = 'Cos(#Delta#phi(E_{T}^{miss}, leading jet))', texY = 'Number of Events',
      attribute = lambda event, sample: cos( event.met_phi - event.jet_phi[0] ) , 
      read_variables = ["met_phi/F", "jet[phi/F]"],
      binning = [20,-1,1],
    ))

    plots.append(Plot(
      name = 'cosZJet1phi',
      texX = 'Cos(#Delta#phi(Z, leading jet))', texY = 'Number of Events',
      attribute = lambda event, sample: cos( event.Z_phi - event.jet_phi[0] ) ,
      read_variables =  ["Z_phi/F", "jet[phi/F]"],
      binning = [10,-1,1],
    ))

    plots.append(Plot(
      name = 'cosMetJet2phi',
      texX = 'Cos(#Delta#phi(E_{T}^{miss}, second jet))', texY = 'Number of Events',
      attribute = lambda event, sample: cos( event.met_phi - event.jet_phi[1] ) , 
      read_variables = ["met_phi/F", "jet[phi/F]"],
      binning = [10,-1,1],
    ))
    
    plots.append(Plot(
      name = 'cosMetJet2phi_smallBinning',
      texX = 'Cos(#Delta#phi(E_{T}^{miss}, second jet))', texY = 'Number of Events',
      attribute = lambda event, sample: cos( event.met_phi - event.jet_phi[1] ) , 
      read_variables = ["met_phi/F", "jet[phi/F]"],
      binning = [20,-1,1],
    ))

    plots.append(Plot(
      name = 'cosZJet2phi',
      texX = 'Cos(#Delta#phi(Z, 2nd leading jet))', texY = 'Number of Events',
      attribute = lambda event, sample: cos( event.Z_phi - event.jet_phi[0] ),
      read_variables = ["Z_phi/F", "jet[phi/F]"],
      binning = [10,-1,1],
    ))

    plots.append(Plot(
      name = 'cosJet1Jet2phi',
      texX = 'Cos(#Delta#phi(leading jet, 2nd leading jet))', texY = 'Number of Events',
      attribute = lambda event, sample: cos( event.jet_phi[1] - event.jet_phi[0] ) ,
      read_variables =  ["jet[phi/F]"],
      binning = [10,-1,1],
    ))
    
#    plots.append(Plot(
#      texX = 'p_{T}(leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
#      name = 'bjet1_pt', attribute = lambda event, sample: event.b1_pt,
#      binning=[20,0,400],
#    ))
#
#    plots.append(Plot(
#      texX = 'p_{T}(2nd leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
#      name = 'bjet2_pt', attribute = lambda event, sample: event.b2_pt,
#      binning=[20,0,400],
#    ))
#    
#    plots.append(Plot(
#        name = "top_cand1_pt", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 30 GeV',
#        attribute = lambda event, sample:event.top1_pt,
#        binning=[20,0,600],
#    ))
#
#    plots.append(Plot(
#        name = "top_cand1_pt_coarse", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 200 GeV',
#        attribute = lambda event, sample:event.top1_pt,
#        binning=[3,0,600],
#    ))
#
#    plots.append(Plot(
#        name = "top_cand1_mass", texX = 'M(t cand1) (GeV)', texY = 'Number of Events / 15 GeV',
#        attribute = lambda event, sample:event.top1_mass,
#        binning=[20,0,300],
#    ))
#
#    plots.append(Plot(
#        name = "top_cand1_phi", texX = '#phi(t cand1)', texY = 'Number of Events',
#        attribute = lambda event, sample:event.top1_phi,
#        binning=[10,-pi,pi],
#    ))
#
#    plots.append(Plot(
#        name = "top_cand2_pt", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 30 GeV',
#        attribute = lambda event, sample:event.top2_pt,
#        binning=[20,0,600],
#    ))
#
#    plots.append(Plot(
#        name = "top_cand2_mass", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 15 GeV',
#        attribute = lambda event, sample:event.top2_mass,
#        binning=[20,0,300],
#    ))
#
#    plots.append(Plot(
#        name = "top_cand2_phi", texX = '#phi(t cand1)', texY = 'Number of Events',
#        attribute = lambda event, sample:event.top2_phi,
#        binning=[10,-pi,pi],
#    ))

    plotting.fill(plots, read_variables = read_variables, sequence = sequence)

    # Get normalization yields from yield histogram
    for plot in plots:
      if plot.name == "yield":
        for i, l in enumerate(plot.histos):
          for j, h in enumerate(l):
            yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
            h.GetXaxis().SetBinLabel(1, "#mu#mu")
            h.GetXaxis().SetBinLabel(2, "#mue")
            h.GetXaxis().SetBinLabel(3, "ee")

    drawPlots(plots, mode, lumi_2017_scale)
    allPlots[mode] = plots

# Add the different channels into SF and all
for mode in ["comb1","comb2","all"]:
    yields[mode] = {}
    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in ['ee','mue', 'mumu'])
        except: yields[mode][y] = 0
    
    for plot in allPlots['mumu']:
        if mode=="comb1":
            tmp = allPlots['mue']
        elif mode=="comb2":
            tmp = allPlots['ee']
        for plot2 in (p for p in tmp if p.name == plot.name):
            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
                    if i==k:
                        j.Add(l)
    
    if mode == "all": drawPlots(allPlots['mumu'], mode, lumi_2017_scale)

logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )
