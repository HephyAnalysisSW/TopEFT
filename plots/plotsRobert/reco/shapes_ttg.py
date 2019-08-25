#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi, atan2, cosh, sinh
from RootTools.core.standard      import *
from TopEFT.Tools.user            import plot_directory
from TopEFT.Tools.helpers         import deltaR, deltaPhi, getObjDict, getVarValue
from TopEFT.Tools.objectSelection import getFilterCut, isBJet, isAnalysisJet
from TopEFT.Tools.cutInterpreter  import cutInterpreter

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',      nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--signal',             action='store',      default=None,        nargs='?', choices=[None, 'fwf'], help='Add signal to plot')
#argParser.add_argument('--background',         action='store',      default='OnlyTTZ',   choices = ['OnlyTTZ', 'All', 'None'],        help="choose bkg")
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
#argParser.add_argument('--Run2017',                                 action='store_true',     help='2017 data & MC?', )
argParser.add_argument('--reweightPtGToSM',                         action='store_true',     help='Reweight Pt(Z) to the SM for all the signals?', )
argParser.add_argument('--normalizeBSM',                            action='store_true',     help='Scale BSM signal to total MC?', )
argParser.add_argument('--plot_directory',     action='store',      default='80X_ttg0j_v14')
argParser.add_argument('--selection',          action='store',      default='lepSelTTG-njet2p-btag1p')
args = argParser.parse_args()

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"
if args.signal and args.signal is not None: args.plot_directory += "_signal_"+args.signal
#if args.background is not None:       args.plot_directory += "_bkg%s"%args.background
if args.reweightPtGToSM:              args.plot_directory += "_reweightPtGToSM"
if args.normalizeBSM:                 args.plot_directory += "_normalizeBSM"

#
# Make samples, will be searched for in the postProcessing directory
#

#postProcessing_directory = "TopEFT_PP_v14/dilep/"
#data_directory           = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"  
#from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_v14/dilep/"
data_directory           = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"  
from TopEFT.samples.cmgTuples_ttGamma0j_Summer16_mAODv2_postProcessed import *

if args.signal is None:
    signals = []
elif args.signal == "fwf": 
    ttGamma0j_ll.style                = styles.fillStyle( color.TTZtoLLNuNu, errors=False )
    ttGamma0j_ll.texName = "t#bar{t}#gamma #rightarrow l#bar{l}b#bar{b}#nu#bar{#nu}#gamma"
    ttGamma0j_ll_DAG_0p250000.style   = styles.lineStyle( ROOT.kBlue + 2, errors=True, width=2, dotted=False, dashed=False )
    ttGamma0j_ll_DVG_0p250000.style   = styles.lineStyle( ROOT.kBlue + 2, errors=True, width=2, dotted=False, dashed=False )
    ttGamma0j_ll_DAG_0p500000.style   = styles.lineStyle( ROOT.kRed + 2,  errors=True, width=2, dotted=False, dashed=False )
    #ttGamma0j_ll_DAG_m0p500000.style  = styles.lineStyle( ROOT.kRed + 2, width=2, dotted=False, dashed=False ) 
    ttGamma0j_ll_DVG_m0p500000.style  = styles.lineStyle( ROOT.kGreen + 1, width=2, dotted=False, dashed=False ) 
    ttGamma0j_ll_DVG_0p500000.style   = styles.lineStyle( ROOT.kMagenta + 1, width=2, dotted=False, dashed=False )

    signals = [ttGamma0j_ll, ttGamma0j_ll_DVG_0p250000 ,ttGamma0j_ll_DAG_0p500000]

def getter( var ):
    return lambda event, sample: getattr( event, var )

# define 2l selections
def getLeptonSelection( mode ):
  if   mode=="mumu": return "nGoodMuons==2&&nGoodElectrons==0"
  elif mode=="mue":  return "nGoodMuons==1&&nGoodElectrons==1"
  elif mode=="ee":   return "nGoodMuons==0&&nGoodElectrons==2"
  elif mode=='all':  return "nGoodMuons+nGoodElectrons==2"

## backgrounds / mc
#if args.background == "OnlyTTZ":
#    mc = [ TTZtoLLNuNu ]
#elif args.background == "All":
#    mc = [ TTZtoLLNuNu , TTX, WZ, TTW, TZQ, rare ]#, nonprompt ]
#else:
#    mc = []
mc = []

for sample in mc: sample.style = styles.fillStyle(sample.color)

# reweighting 
if args.reweightPtGToSM:
    sel_string = "&&".join([getFilterCut(isData=False), getLeptonSelection('all'), cutInterpreter.cutString(args.selection)])
    TTG_ptG = ttGamma0j_ll.get1DHistoFromDraw("photon_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
    TTG_ptG.Scale(1./TTG_ptG.Integral())

    def get_reweight( var, histo ):

        def reweight(event, sample):
            i_bin = histo.FindBin(getattr( event, var ) )
            return histo.GetBinContent(i_bin)

        return reweight

    for signal in signals:
        logger.info( "Computing PtG reweighting for signal %s", signal.name )
        signal_ptG = signal.get1DHistoFromDraw("photon_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
        signal_ptG.Scale(1./signal_ptG.Integral())

        signal.reweight_ptG_histo = TTG_ptG.Clone()
        signal.reweight_ptG_histo.Divide(signal_ptG)

        signal.weight = get_reweight( "photon_pt", signal.reweight_ptG_histo )

# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,id/I]", "njet/I","nJetSelected/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "ngamma/I", "photon_pt/F", "photon_eta/F", "photon_phi/F",
                    ]
sequence = []

def extra_observables( event, sample ):

    G = {'pt':event.photon_pt, 'eta':event.photon_eta, 'phi':event.photon_phi}
    G_2D        = ROOT.TVector2( event.photon_pt*cos(event.photon_phi), event.photon_pt*sin(event.photon_phi) )
    n_G_2D      = ROOT.TVector2( cos(event.photon_phi), sin(event.photon_phi) )
    #G_3D        = ROOT.TVector2( event.photon_pt*cos(event.photon_phi), event.photon_pt*sin(event.photon_phi) )
    #n_G_3D      = ROOT.TVector2( cos(event.photon_phi), sin(event.photon_phi) )

    # me_x,y
    met_2D = ROOT.TVector2( event.met_pt*cos(event.met_phi), event.met_pt*sin(event.met_phi) )
    event.deltaPhi_G_MET = deltaPhi( G['phi'], event.met_phi ) 

    event.deltaPhi_ll = deltaPhi(event.lep_phi[0],  event.lep_phi[1])
    event.deltaR_ll   = deltaR({'phi':event.lep_phi[0], 'eta':event.lep_eta[0]},  {'phi':event.lep_phi[1], 'eta':event.lep_eta[1]})

    ## get jets
    jetVars     = ['eta','pt','phi','btagCSV','id']
    jets        = filter( isAnalysisJet, [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'njet')))] )
    jets.sort( key = lambda l:-l['pt'] )

    bJets       = filter(lambda j: isBJet(j, tagger = 'CSVv2') and abs(j['eta'])<=2.4, jets )
    nonBJets    = filter(lambda j: not ( isBJet(j, tagger = 'CSVv2') and abs(j['eta'])<=2.4 ), jets)

    # take highest-pT b-jet, supplement by non-bjets if there are less than two
    bj1, bj2 = (bJets+nonBJets)[:2]
    l_bj1 = ROOT.TLorentzVector()
    l_bj1.SetPtEtaPhiM( bj1['pt'], bj1['eta'], bj1['phi'], 0 )
    l_bj2 = ROOT.TLorentzVector()
    l_bj2.SetPtEtaPhiM( bj2['pt'], bj2['eta'], bj2['phi'], 0 )

    # leptons
    l_lep1 = ROOT.TLorentzVector() 
    l_lep1.SetPtEtaPhiM( event.lep_pt[0], event.lep_eta[0], event.lep_phi[0], 0 )
    lep1 = {'pt':event.lep_pt[0], 'eta':event.lep_eta[0], 'phi':event.lep_phi[0]}
    l_lep2 = ROOT.TLorentzVector() 
    l_lep2.SetPtEtaPhiM( event.lep_pt[1], event.lep_eta[1], event.lep_phi[1], 0 )
    lep2 = {'pt':event.lep_pt[1], 'eta':event.lep_eta[1], 'phi':event.lep_phi[1]}

    # resolve pairing ambiguity
    max1 = max([(l_lep1 + l_bj1).M(), (l_lep2 + l_bj2).M()])
    max2 = max([(l_lep1 + l_bj2).M(), (l_lep2 + l_bj1).M()])
    if max1<max2: #Choose pairing with smaller invariant mass
        pass 
    else:
        # switch
        bj1, bj2     = bj2, bj1 
        l_bj1, l_bj2 = l_bj2, l_bj1

    event.M_lb_max = max(max1, max2)
    event.M_lb_min = min(max1, max2)

    # G & leps
    dPhi_G_l1 = deltaPhi( G['phi'], lep1['phi'] ) 
    dPhi_G_l2 = deltaPhi( G['phi'], lep2['phi'] ) 
    event.dPhi_G_l_max = max(dPhi_G_l1, dPhi_G_l2)
    event.dPhi_G_l_min = min(dPhi_G_l1, dPhi_G_l2)
    dR_G_l1 = deltaR( G, lep1 ) 
    dR_G_l2 = deltaR( G, lep2 ) 
    event.dR_G_l_max = max(dR_G_l1, dR_G_l2)
    event.dR_G_l_min = min(dR_G_l1, dR_G_l2)

    return

sequence.append( extra_observables )

#
# Text on the plots
#
def drawObjects( lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Simulation'), 
      (0.60, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale),
      (0.60, 0.84, 'N_{jets} #geq 2'),
      (0.60, 0.79,  'N_{b-tags} #geq 1'),
      (0.60, 0.74, 'all lepton flavors')
    ]
    return [tex.DrawLatex(*l) for l in lines] 

def drawPlots(plots, mode):
    for plot in plots:
        if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
        for log in [False, True]:
            plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.plot_directory, mode + ("_log" if log else ""), args.selection)
            if isinstance( plot, Plot2D):
                plotting.draw2D(plot,
                  plot_directory = plot_directory_,
                  #ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
                  logX = False, logY = False, logZ=log, 
                  #scaling = {i:0 for i in range(1, len(plot.histos))} if args.normalizeBSM else {},
                  #legend = [ (0.15,0.9-0.025*sum(map(len, plot.histos)),0.9,0.9), 2],
                  drawObjects = drawObjects( lumi_scale ),
                  copyIndexPHP = True
                )
            else:
                plotting.draw(plot,
                  plot_directory = plot_directory_,
                  #ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
                  logX = False, logY = log, sorting = True,
                  yRange = (0.9, "auto") if log else (0.001, "auto"),
                  scaling = {i:0 for i in range(1, len(plot.histos))} if args.normalizeBSM else {},
                  legend = [ (0.2,0.88-0.05*sum(map(len, plot.histos)),0.6,0.88), 1],
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

    lumi_scale = 150
    weight_ = lambda event, sample: event.weight

    for sample in mc + signals:
      sample.scale          = lumi_scale
      #sample.read_variables = ['reweightTopPt/F','reweightDilepTriggerBackup/F','reweightLeptonSF/F','reweightBTag_SF/F','reweightPU36fb/F', 'nTrueInt/F', 'reweightLeptonTrackingSF/F']
      #sample.weight         = lambda event, sample: event.reweightTopPt*event.reweightBTag_SF*event.reweightLeptonSF*event.reweightDilepTriggerBackup*event.reweightPU36fb*event.reweightLeptonTrackingSF
      sample.setSelectionString([getFilterCut(isData=False), getLeptonSelection(mode)])

      stack = Stack(mc)

    stack.extend( [ [s] for s in signals ] )

    stack = Stack( *filter( lambda s: s!=[], stack ) ) # if bkg is None

    if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 1 )

    # Use some defaults
    Plot.  setDefaults(stack = stack, weight = weight_, selectionString = cutInterpreter.cutString(args.selection))
    Plot2D.setDefaults(               weight = weight_, selectionString = cutInterpreter.cutString(args.selection))

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
    
    plots.append(Plot(name = "Gamma_pt",
        texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample: event.photon_pt,
        binning=[25,0,500],
    ))
    
    plots.append(Plot(
        name = 'Gamma_pt_coarse', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample: event.photon_pt,
        binning=[12,40,800],
    ))
    
    plots.append(Plot(
        name = 'Gamma_pt_superCoarse', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events / 40 GeV',
        attribute = lambda event, sample: event.photon_pt,
        binning=[19,40,800],
    ))

    plots.append(Plot(
        name = 'Gamma_pt_reweighting', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events',
        attribute = lambda event, sample: event.photon_pt,
        binning=[20,0,1000],
    ))

    plots.append(Plot(
        name = 'Gamma_eta', texX = '#eta(#gamma) ', texY = 'Number of Events',
        attribute = lambda event, sample: event.photon_eta,
        binning=[30,-3,3],
    ))

    plots.append(Plot( name = "deltaPhi_ll",
        texX = '#Delta#phi(ll)', texY = 'Number of Events',
        attribute = lambda event, sample: event.deltaPhi_ll,
        binning=[20,0,pi],
    ))

    plots.append(Plot( name = "deltaPhi_ll_coarse",
        texX = '#Delta#phi(ll)', texY = 'Number of Events',
        attribute = lambda event, sample: event.deltaPhi_ll,
        binning=[10,0,pi],
    ))

    plots.append(Plot( name = "deltaPhi_G_MET",
        texX = '#Delta#phi(#gamma, E_{T}^{miss})', texY = 'Number of Events',
        attribute = lambda event, sample: event.deltaPhi_G_MET,
        binning=[20,0,pi],
    ))

    plots.append(Plot( name = "deltaR_ll",
        texX = '#DeltaR(ll)', texY = 'Number of Events',
        attribute = lambda event, sample: event.deltaR_ll,
        binning=[10,0,4],
    ))

    plots.append(Plot(name = "M_lb_max",
        texX = 'M_{max}(lb) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample: event.M_lb_max,
        binning=[25,0,800],
    ))

    plots.append(Plot(name = "M_lb_min",
        texX = 'M_{min}(lb) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample: event.M_lb_min,
        binning=[25,0,800],
    ))

    plots.append(Plot( name = "dPhi_G_l_max",
        texX = '#Delta#phi_{max}(#gamma, l)', texY = 'Number of Events',
        attribute = lambda event, sample: event.dPhi_G_l_max,
        binning=[20,0,pi],
    ))

    plots.append(Plot( name = "dPhi_G_l_min",
        texX = '#Delta#phi_{min}(#gamma, l)', texY = 'Number of Events',
        attribute = lambda event, sample: event.dPhi_G_l_min,
        binning=[20,0,pi],
    ))

    plots.append(Plot( name = "dR_G_l_max",
        texX = '#Delta R_{max}(#gamma, l)', texY = 'Number of Events',
        attribute = lambda event, sample: event.dR_G_l_max,
        binning=[20,0,4],
    ))

    plots.append(Plot( name = "dR_G_l_min",
        texX = '#Delta R_{min}(#gamma, l)', texY = 'Number of Events',
        attribute = lambda event, sample: event.dR_G_l_min,
        binning=[20,0,4],
    ))
    
#    plots.append(Plot(
#        name = 'lnonZ1_pt',
#        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 10 GeV',
#        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
#        binning=[30,0,300],
#    ))
#
#    plots.append(Plot(
#        name = 'lnonZ1_pt_ext',
#        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 10 GeV',
#        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
#        binning=[12,0,180],
#    ))
#    
#    plots.append(Plot(
#        texX = 'M(ll) (GeV)', texY = 'Number of Events / 20 GeV',
#        attribute = TreeVariable.fromString( "Z_mass/F" ),
#        binning=[10,81,101],
#    ))
#
#    plots.append(Plot(
#        name = "Z_mass_wide",
#        texX = 'M(ll) (GeV)', texY = 'Number of Events / 2 GeV',
#        attribute = TreeVariable.fromString( "Z_mass/F" ),
#        binning=[50,20,120],
#    ))
#    
#    plots.append(Plot(
#      texX = 'N_{jets}', texY = 'Number of Events',
#      attribute = TreeVariable.fromString( "nJetSelected/I" ),
#      binning=[5,2.5,7.5],
#    ))
#    
#    plots.append(Plot(
#      texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
#      name = 'jet1_pt', attribute = lambda event, sample: event.jet_pt[0],
#      binning=[600/30,0,600],
#    ))
#    
#    plots.append(Plot(
#      texX = 'p_{T}(2nd leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
#      name = 'jet2_pt', attribute = lambda event, sample: event.jet_pt[1],
#      binning=[600/30,0,600],
#    ))


    ###############################################################################
#    plots.append(Plot(
#      name = 'mT', texX = 'm_{T}(l_{3},E_{T}^{miss}) (GeV)', texY = 'Number of Events / 5 GeV',
#      attribute = lambda event, sample: event.mT,
#      binning=[30, 0, 150],
#    ))
#    
#    plots.append(Plot(
#      name = 'mt', texX = 'm_{T}(b_{lep},l_{3},E_{T}^{miss}) (GeV)', texY = 'Number of Events / 12 GeV',
#      attribute = lambda event, sample: event.mt,
#      binning=[30, 0, 360],
#    ))
#
#    plots.append(Plot(
#      name = 'ST', texX = 'S_{T} (GeV)', texY = 'Number of Events / 20 GeV',
#      attribute = lambda event, sample: event.ST,
#      binning=[30, 0, 600],
#    ))
#    
#    plots.append(Plot(
#      name = 'St', texX = 'S_{t} (GeV)', texY = 'Number of Events / 30 GeV',
#      attribute = lambda event, sample: event.St,
#      binning=[30, 0, 900],
#    ))
#
#    plots.append(Plot2D(
#      name = 'TTZ', stack = Stack(TTZtoLLNuNu), texX = 'cos#theta^{*}(Z)', texY = 'L_{p}(W)',
#      attribute = [ lambda event, sample: event.cosThetaStar,
#                    lambda event, sample: event.Lp  ],
#      binning=[20,-1,1,30,-1.5,1.5],
#    ))
#
#    for fname, ftex, binning in [\
#        [ 'absDPhiZ', '|#Delta#phi|(Z,%s)',   [20, 0, pi] ],
#        [ 'projZ',    'n_{Z} . (%s)',         [20,0,400]],
#        [ 'projorthZ','n_{Z,#perp } . (%s)', [20,0,400]],
#        #[ 'dotZ',     lambda vec: vec.Dot( Z_2D )  )],
#        #[ 'projorthZ',lambda vec: vec.Dot( n_orth_Z_2D )  )],
#        ]:
#
#        for vname, vtex in [\
#                [ "met",         "E_{T}^{miss}"], 
#                [ "met_blep",    "E_{T}^{miss}+b_{lep}"],
#                [ "met_l3",      "E_{T}^{miss}+l_{3}"],
#                [ "l3",          "l_{3}"],
#                [ "blep",        "b_{lep}"], 
#                [ "l3_blep",     "l_{3}+b_{lep}"],
#                [ "met_l3_blep", "E_{T}^{miss}+l_{3}+b_{lep}"],
#            ]:
#
#            plots.append(Plot(
#              name = '%s_%s'%(fname, vname), texX = ftex%vtex, texY = 'Number of Events',
#              attribute = getter( "%s_%s"%(fname, vname) ),
#              binning   = binning,
#            ))
#    for fname, ftex, binning in [\
#        [ 'dRZ', '|#Delta R|(Z,%s)',   [30, 0, 6] ],
#        ]:
#
#        for vname, vtex in [\
#                [ "l3",          "l_{3}"],
#                [ "blep",        "b_{lep}"], 
#                [ "l3_blep",     "l_{3}+b_{lep}"],
#            ]:
#
#            plots.append(Plot(
#              name = '%s_%s'%(fname, vname), texX = ftex%vtex, texY = 'Number of Events',
#              attribute = getter( "%s_%s"%(fname, vname) ),
#              binning   = binning,
#            ))


    plotting.fill(plots, read_variables = read_variables, sequence = sequence)

    for plot in plots:
        for h in sum(plot.histos,[]):
            h.Sumw2(0)

    # Get normalization yields from yield histogram
    for plot in plots:
      if plot.name == "yield":
        for i, l in enumerate(plot.histos):
          for j, h in enumerate(l):
            yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
            h.GetXaxis().SetBinLabel(1, "#mu#mu")
            h.GetXaxis().SetBinLabel(2, "#mue")
            h.GetXaxis().SetBinLabel(3, "ee")
    #if args.noData: yields[mode]["data"] = 0

    yields[mode]["MC"] = sum(yields[mode][s.name] for s in mc)
    #dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    drawPlots(plots, mode)
    allPlots[mode] = plots

# Add the different channels into SF and all
for mode in ["comb1","comb2","all"]:
    yields[mode] = {}
    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in allModes)
        except: yields[mode][y] = 0
    
    for plot in allPlots['mumu']:
        if mode=="comb1":
            tmp = allPlots['mue'] if 'mue' in allModes else []
        elif mode=="comb2":
            tmp = allPlots['ee']
        for plot2 in (p for p in tmp if p.name == plot.name):
            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
                    if i==k:
                        j.Add(l)
    
    if mode == "all": drawPlots(allPlots['mumu'], mode)

logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )

