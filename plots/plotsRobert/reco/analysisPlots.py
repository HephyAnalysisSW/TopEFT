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
argParser.add_argument('--signal',             action='store',      default='C2VA0p2',       nargs='?', choices=["dipoleEllipsis", 'currentEllipsis', 'C2VA0p2', 'cuW'], help="Add signal to plot")
argParser.add_argument('--onlyTTZ',            action='store_true', default=False,           help="Plot only ttZ")
argParser.add_argument('--noData',             action='store_true', default=False,           help='also plot data?')
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--reweightPtZToSM',                         action='store_true',     help='Reweight Pt(Z) to the SM for all the signals?', )
argParser.add_argument('--plot_directory',     action='store',      default='80X_v5')
argParser.add_argument('--selection',          action='store',      default='lepSelTTZ-njet3p-btag1p-onZ')
argParser.add_argument('--badMuonFilters',     action='store',      default="Summer2016",  help="Which bad muon filters" )
args = argParser.parse_args()

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"
if args.noData:                       args.plot_directory += "_noData"
if args.badMuonFilters!="Summer2016": args.plot_directory += "_badMuonFilters_"+args.badMuonFilters
if args.signal:                       args.plot_directory += "_signal_"+args.signal
if args.onlyTTZ:                      args.plot_directory += "_onlyTTZ"
if args.reweightPtZToSM:              args.plot_directory += "_reweightPtZToSM"
#
# Make samples, will be searched for in the postProcessing directory
#
postProcessing_directory = "TopEFT_PP_v12/trilep/"
data_directory           = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
from TopEFT.samples.cmgTuples_ttZ0j_Summer16_mAODv2_postProcessed import *

if args.signal ==  "C2VA0p2":
    signals = [ttZ0j_ll, ttZ0j_ll_DC2A_0p200000_DC2V_0p200000]
    ttZ0j_ll.style = styles.lineStyle( ROOT.kBlack, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC2A_0p200000_DC2V_0p200000.style = styles.lineStyle( ROOT.kBlue,   width=2, dotted=False )

elif args.signal == "currentEllipsis":
    ttZ0j_ll.style                              = styles.lineStyle( ROOT.kBlack, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p500000_DC1V_0p500000.style  = styles.lineStyle( ROOT.kRed, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000.style = styles.lineStyle( ROOT.kBlue, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_1p000000.style                = styles.lineStyle( ROOT.kGreen, width=2, dotted=False, dashed=False )

    signals = [ttZ0j_ll, ttZ0j_ll_DC1A_0p500000_DC1V_0p500000, ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000, ttZ0j_ll_DC1A_1p000000]
elif args.signal == "dipoleEllipsis":
    ttZ0j_ll.style                                                              = styles.lineStyle( ROOT.kBlack, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700.style     = styles.lineStyle( ROOT.kRed, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700.style    = styles.lineStyle( ROOT.kGreen, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000.style                   = styles.lineStyle( ROOT.kBlue, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700.style    = styles.lineStyle( ROOT.kMagenta, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700.style   = styles.lineStyle( ROOT.kCyan, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000.style                  = styles.lineStyle( ROOT.kAzure, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000.style                  = styles.lineStyle( ROOT.kGreen+2, width=2, dotted=False, dashed=False )
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000.style                   = styles.lineStyle( ROOT.kMagenta+2, width=2, dotted=False, dashed=False )
    signals = [
        ttZ0j_ll,
        ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700,
        ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700,
        ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000,
        ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700,
        ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700,
        ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000,
        ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000,
        ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000
    ]
elif args.signal == 'cuW':

    ttZ0j_ll.style               = styles.lineStyle( ROOT.kBlack, width=2, dotted=False, dashed=False )
    ttZ0j_ll_cuW_0p100000.style  = styles.lineStyle( ROOT.kBlue, width=2, dotted=False, dashed=False )
    ttZ0j_ll_cuW_0p200000.style  = styles.lineStyle( ROOT.kRed, width=2, dotted=False, dashed=False )
    ttZ0j_ll_cuW_0p300000.style  = styles.lineStyle( ROOT.kGreen, width=2, dotted=False, dashed=False )
    ttZ0j_ll_cuW_m0p100000.style = styles.lineStyle( ROOT.kMagenta, width=2, dotted=False, dashed=False )
    ttZ0j_ll_cuW_m0p200000.style = styles.lineStyle( ROOT.kOrange, width=2, dotted=False, dashed=False )
    ttZ0j_ll_cuW_m0p300000.style = styles.lineStyle( ROOT.kAzure, width=2, dotted=False, dashed=False )

    signals = [ttZ0j_ll, ttZ0j_ll_cuW_0p100000, ttZ0j_ll_cuW_0p200000, ttZ0j_ll_cuW_0p300000, ttZ0j_ll_cuW_m0p100000, ttZ0j_ll_cuW_m0p200000, ttZ0j_ll_cuW_m0p300000]
# define 3l selections
def getLeptonSelection( mode ):
  if   mode=="mumumu": return "nGoodMuons==3&&nGoodElectrons==0"
  elif mode=="mumue":  return "nGoodMuons==2&&nGoodElectrons==1"
  elif mode=="muee":   return "nGoodMuons==1&&nGoodElectrons==2"
  elif mode=="eee":    return "nGoodMuons==0&&nGoodElectrons==3"
  elif mode=='all':    return "nGoodMuons+nGoodElectrons==3"

# backgrounds / mc
if args.onlyTTZ:
    mc = [ TTZtoLLNuNu ]
else:
    mc             = [ TTZtoLLNuNu , TTX, WZ, TTW, TZQ, rare ]#, nonprompt ]

for sample in mc: sample.style = styles.fillStyle(sample.color)

# reweighting 
if args. reweightPtZToSM:
    sel_string = "&&".join([getFilterCut(isData=False, badMuonFilters = args.badMuonFilters), getLeptonSelection('all'), cutInterpreter.cutString(args.selection)])
    TTZ_ptZ = TTZtoLLNuNu.get1DHistoFromDraw("Z_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
    TTZ_ptZ.Scale(1./TTZ_ptZ.Integral())

    def get_reweight( var, histo ):

        def reweight(event, sample):
            i_bin = histo.FindBin(getattr( event, var ) )
            return histo.GetBinContent(i_bin)

        return reweight

    for signal in signals:
        logger.info( "Computing PtZ reweighting for signal %s", signal.name )
        signal_ptZ = signal.get1DHistoFromDraw("Z_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
        signal_ptZ.Scale(1./signal_ptZ.Integral())

        signal.reweight_ptZ_histo = TTZ_ptZ.Clone()
        signal.reweight_ptZ_histo.Divide(signal_ptZ)

        signal.weight = get_reweight( "Z_pt", signal.reweight_ptZ_histo )

# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F]", "njet/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I", 
                    "Z_phi/F", "Z_eta/F", "Z_pt/F", "Z_mass/F", "Z_lldPhi/F", "Z_lldR/F"
                    ]

sequence = []

def getDPhiZLep( event, sample ):
    event.dPhiZLep = deltaPhi(event.lep_phi[event.nonZ_l1_index], event.Z_phi)
sequence.append( getDPhiZLep )

def getDRZLep( event, sample ):
    event.dRZLep = deltaR({'phi':event.lep_phi[event.nonZ_l1_index],'eta':event.lep_eta[event.nonZ_l1_index]},{'phi': event.Z_phi, 'eta':event.Z_eta})
sequence.append( getDRZLep )

def getDPhiZJet( event, sample ):
    event.dPhiZJet = deltaPhi(event.jet_phi[0], event.Z_phi) if event.njet>0 and event.Z_mass>0 else float('nan')
sequence.append( getDPhiZJet )

def getJets( event, sample ):
    jetVars     = ['eta','pt','phi','btagCSV']
    event.jets_sortbtag  = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'njet')))]
    event.jets_sortbtag.sort( key = lambda l:-l['btagCSV'] )
sequence.append( getJets )

#def getL( event, sample):
#
#    # Lp generalization for Z's. Doesn't work, because Z couples to L and R
#    pxZ = event.Z_pt*cos(event.Z_phi)
#    pyZ = event.Z_pt*sin(event.Z_phi)
#    pxZl1 = event.lep_pt[event.Z_l1_index]*cos(event.lep_phi[event.Z_l1_index])
#    pyZl1 = event.lep_pt[event.Z_l1_index]*sin(event.lep_phi[event.Z_l1_index])
#
#    event.LZp  = (pxZ*pxZl1+pyZ*pyZl1)/event.Z_pt**2
#
#    # 3D generalization of the above 
#    if  event.lep_pdgId[event.Z_l1_index]>0:
#        Z_lp_index, Z_lm_index = event.Z_l1_index, event.Z_l2_index
#    else:
#        Z_lm_index, Z_lp_index = event.Z_l1_index, event.Z_l2_index
#
#    lp  = ROOT.TVector3()
#    lp.SetPtEtaPhi(event.lep_pt[Z_lp_index], event.lep_eta[Z_lp_index], event.lep_phi[Z_lp_index])
#    lm  = ROOT.TVector3()
#    lm.SetPtEtaPhi(event.lep_pt[Z_lm_index], event.lep_eta[Z_lm_index], event.lep_phi[Z_lm_index])
#    Z = lp+lm
#    event.LZp3D = lp*Z/(Z*Z)
#
#    event.LZp = 1-event.lep_pt[Z_lp_index]/event.Z_pt*cos(event.lep_phi[Z_lp_index] - event.Z_phi)
#    event.LZm = 1-event.lep_pt[Z_lm_index]/event.Z_pt*cos(event.lep_phi[Z_lm_index] - event.Z_phi)
#
#    # Lp for the W
#    pxNonZl1 = event.lep_pt[event.nonZ_l1_index]*cos(event.lep_phi[event.nonZ_l1_index])
#    pyNonZl1 = event.lep_pt[event.nonZ_l1_index]*sin(event.lep_phi[event.nonZ_l1_index])
#    pxW      = event.met_pt*cos(event.met_phi) + pxNonZl1
#    pyW      = event.met_pt*sin(event.met_phi) + pyNonZl1
#    event.Lp = (pxW*pxNonZl1 + pyW*pyNonZl1)/(pxW**2+pyW**2)
#sequence.append( getL )
#
#mt = 172.5
#def getTopCands( event, sample ):
#    
#    lepton  = ROOT.TLorentzVector()
#    met     = ROOT.TLorentzVector()
#    b1      = ROOT.TLorentzVector()
#    b2      = ROOT.TLorentzVector()
#    
#    lepton.SetPtEtaPhiM(event.lep_pt[event.nonZ_l1_index], event.lep_eta[event.nonZ_l1_index], event.lep_phi[event.nonZ_l1_index], 0)
#    met.SetPtEtaPhiM(event.met_pt, 0, event.met_phi, 0)
#    b1.SetPtEtaPhiM(event.jets_sortbtag[0]['pt'], event.jets_sortbtag[0]['eta'], event.jets_sortbtag[0]['phi'], 0. )
#    b2.SetPtEtaPhiM(event.jets_sortbtag[1]['pt'], event.jets_sortbtag[1]['eta'], event.jets_sortbtag[1]['phi'], 0. )
#
#    W    = lepton + met
#    top1 = W + b1
#    top2 = W + b2
#
#    ## order top candidates in terms of mass closest to the top mass
#    if abs(top1.M()-mt) > abs(top2.M()-mt): top1, top2 = top2, top1
#    #if top1.Pt() < top2.Pt(): top1, top2 = top2, top1
#
#    event.top1_mass = top1.M()
#    event.top1_pt   = top1.Pt()
#    event.top1_phi  = top1.Phi()
#
#    event.top2_mass = top2.M()
#    event.top2_pt   = top2.Pt()
#    event.top2_phi  = top2.Phi()
#
#    event.b1_pt     = b1.Pt()
#    event.b1_phi    = b1.Phi()
#    event.b2_pt     = b2.Pt()
#    event.b2_phi    = b2.Phi()
#
#sequence.append( getTopCands )

def get3rdLepKin( event, sample ):
    
    Zx, Zy = event.Z_pt*cos(event.Z_phi), event.Z_pt*sin(event.Z_phi)
    lx, ly = event.lep_pt[event.nonZ_l1_index]*cos(event.lep_phi[event.nonZ_l1_index]), event.lep_pt[event.nonZ_l1_index]*sin(event.lep_phi[event.nonZ_l1_index])
   
    event.pZl = (Zx*lx+Zy*ly)/event.lep_pt[event.nonZ_l1_index] 
    event.plZ = (Zx*lx+Zy*ly)/event.Z_pt
    event.ptrel = (lx*Zy-ly*Zx)/event.Z_pt

sequence.append( get3rdLepKin )

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
        name = "Z_lldEta",
        texX = '#Delta #eta(ll)', texY = 'Number of Events',
        attribute = lambda event, sample: abs(event.lep_eta[event.Z_l1_index] - event.lep_eta[event.Z_l2_index]),
        binning=[10,0,4],
    ))

    plots.append(Plot(
        name = "dPhiZL",
        texX = '#Delta#phi(Z,l)', texY = 'Number of Events',
        attribute = lambda event, sample:event.dPhiZLep,
        binning=[10,0,pi],
    ))

#    plots.append(Plot(
#        name = "LZp",
#        texX = 'LZp', texY = 'Number of Events',
#        attribute = lambda event, sample: event.LZp,
#        binning=[15,0.5,2],
#    ))
#
#    plots.append(Plot(
#        name = "LZp3D",
#        texX = 'LZp3D', texY = 'Number of Events',
#        attribute = lambda event, sample: event.LZp3D,
#        binning=[15,-0.5,2],
#    ))
#
#    plots.append(Plot(
#        name = "LZm",
#        texX = 'LZm', texY = 'Number of Events',
#        attribute = lambda event, sample: event.LZm,
#        binning=[15,0.5,2],
#    ))
#
#    plots.append(Plot(
#        name = "LZp",
#        texX = 'LZp', texY = 'Number of Events',
#        attribute = lambda event, sample: event.LZp,
#        binning=[15,0.5,2],
#    ))
#
#    plots.append(Plot(
#        name = "Lp",
#        texX = 'Lp', texY = 'Number of Events',
#        attribute = lambda event, sample: event.Lp,
#        binning=[25,-0.5,2],
#    ))
#    plots.append(Plot(
#        name = "Lp_plus",
#        texX = 'Lp_{+}', texY = 'Number of Events',
#        attribute = lambda event, sample: event.Lp if event.lep_pdgId[event.nonZ_l1_index] > 0 else float('nan'),
#        binning=[25,-0.5,2],
#    ))
#    plots.append(Plot(
#        name = "Lp_minus",
#        texX = 'Lp_{-}', texY = 'Number of Events',
#        attribute = lambda event, sample: event.Lp if event.lep_pdgId[event.nonZ_l1_index] < 0 else float('nan'),
#        binning=[25,-0.5,2],
#    ))

    plots.append(Plot(
        name = "pZl",
        texX = '#vec{p}(Z) . #vec{n}(l)', texY = 'Number of Events',
        attribute = lambda event, sample:event.pZl,
        binning=[20,0,200],
    ))

    plots.append(Plot(
        name = "plZ",
        texX = '#vec{p}(l) . #vec{n}(Z)', texY = 'Number of Events',
        attribute = lambda event, sample:event.plZ,
        binning=[20,0,200],
    ))

    plots.append(Plot(
        name = "ptrel",
        texX = 'p_{T,l}(rel.)', texY = 'Number of Events',
        attribute = lambda event, sample:event.ptrel,
        binning=[20,0,200],
    ))

    plots.append(Plot(
        name = "dRZL",
        texX = '#Delta#R(Z,l)', texY = 'Number of Events',
        attribute = lambda event, sample:event.dRZLep,
        binning=[12,0,6],
    ))
    
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
        name = 'lnonZ1_pt_ext',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[12,0,180],
    ))

    plots.append(Plot(
        name = "l3_pt",
        texX = 'p_{T}(l_{3}) (GeV)', texY = 'Number of Events / 5 GeV',
        attribute = lambda event, sample:event.lep_pt[2],
        binning=[20,0,100],
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

