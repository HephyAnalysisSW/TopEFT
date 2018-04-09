#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT
ROOT.gROOT.SetBatch(True)

from math                           import sqrt, cos, sin, pi
from RootTools.core.standard        import *
from RootTools.plot.helpers         import copyIndexPHP
from TopEFT.Tools.user              import plot_directory
from TopEFT.Tools.helpers           import deltaPhi
from TopEFT.Tools.objectSelection   import getFilterCut
from TopEFT.Tools.cutInterpreter    import cutInterpreter
from TopEFT.Tools.lock              import waitForLock, removeLock

import pickle, os, time
import errno
#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',          action='store',      default='INFO',     nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--signal',            action='store',      default='None',        nargs='?', choices=['None', 'ewkDM'], help="Add signal to plot")
argParser.add_argument('--noData',            action='store_true', default=False,       help='also plot data?')
argParser.add_argument('--plot_directory',    action='store',      default='mva_v2')
argParser.add_argument('--selection',         action='store',            default='trilep-Zcand-lepSelTTZ-njet3p-btag1p-onZ')
argParser.add_argument('--selectSys',         action='store',      default='all')
#argParser.add_argument('--noMultiThreading',  action='store_true', default='False', help="noMultiThreading?") # Need no multithreading when doing batch-to-natch
argParser.add_argument('--showOnly',          action='store',      default=None)
argParser.add_argument('--small',             action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--runLocal',             action='store_true',     help='Run local or submit?', )
argParser.add_argument('--isChild',           action='store_true', default=False)
argParser.add_argument('--normalizeBinWidth', action='store_true', default=False,       help='normalize wider bins?')
argParser.add_argument('--dryRun',            action='store_true', default=False,       help='do not launch subjobs')
argParser.add_argument("--year",              action='store', type=int,      default=2016, choices = [ 2016, 2017 ], help='Which year?')
args = argParser.parse_args()

print args.year

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

jetSelection    = "nJetSelected"
bJetSelectionM  = "nBTag"

#
# Systematics to run over
#
jet_systematics    = ['JECUp','JECDown']# 'JERDown','JECVUp','JECVDown']
met_systematics    = ['UnclusteredEnUp', 'UnclusteredEnDown']
jme_systematics    = jet_systematics + met_systematics
weight_systematics = ['PU36fbUp', 'PU36fbDown', 'BTagDeepCSV_SF_b_Down', 'BTagDeepCSV_SF_b_Up', 'BTagDeepCSV_SF_l_Down', 'BTagDeepCSV_SF_l_Up', 'TriggerUp','TriggerDown', 'LeptonTrackingSFDown', 'LeptonTrackingSFUp']


if args.selectSys != "all" and args.selectSys != "combine": all_systematics = [args.selectSys if args.selectSys != 'None' else None]
else:                                                       all_systematics = [None] + weight_systematics + jet_systematics
#else:                                                       all_systematics = [None] + jet_systematics


sys_pairs = [\
    ('JEC',         'JECUp', 'JECDown'),
    ('PU36fb',      'PU36fbUp', 'PU36fbDown'),
#    ('TopPt',       'TopPt', None),
#   ('JER',         'JERUp', 'JERDown'),
    ('BTag_b',      'BTagDeepCSV_SF_b_Down', 'BTagDeepCSV_SF_b_Up' ),
    ('BTag_l',      'BTagDeepCSV_SF_l_Down', 'BTagDeepCSV_SF_l_Up'),
    ('trigger',     'TriggerDown', 'TriggerUp'),
    ('tracker',     'LeptonTrackingSFDown', 'LeptonTrackingSFUp')
]

#
# If this is the mother process, launch the childs and exit (I know, this could potententially be dangereous if the --isChild and --selection commands are not given...)
#

def wrapper(com):
  import os
  os.system(com)

#if not args.isChild and args.selection is None and (args.selectSys == "all" or args.selectSys == "combine"):
if not args.isChild and (args.selectSys == "all" or args.selectSys == "combine"):
  jobs = []
  for sys in (all_systematics if args.selectSys == "all" else ["combine"]):
    command = "python systematicsPlots.py --selection=" + args.selection + (" --noData" if args.noData else "")\
               + (" --isChild")\
               + (" --small" if args.small else "")\
               + (" --plot_directory=" + args.plot_directory)\
               + (" --logLevel=" + args.logLevel)\
               + (" --selectSys=" + str(sys))\
               + (" --signal=" + args.signal)\
               + (" --year=" + str(args.year))\
               + (" --normalizeBinWidth" if args.normalizeBinWidth else "")
    if args.selectSys == 'combine':
        jobs.append(command)
    elif args.selectSys == 'all':
        if args.runLocal:
            jobs.append(command)
        else:
            jobs.append( "submitBatch.py --title='sys' '%s'"%command )

#  if args.noMultiThreading: 
  logger.info("Running/submitting all systematics.")
  results = map(wrapper, jobs)
  logger.info("Done with running/submitting systematics.")
  exit(0)

if args.noData:                   args.plot_directory += "_noData"
if args.signal == "DM":           args.plot_directory += "_DM"
if args.signal == "T2tt":         args.plot_directory += "_T2tt"
if args.small:                    args.plot_directory += "_small"

print args.year
try: os.makedirs(os.path.join(plot_directory, 'systematicsPlots', str(args.year), args.plot_directory))
except: pass

#
# Make samples, will be searched for in the postProcessing directory
#

postProcessing_directory = "TopEFT_PP_2016_mva_v2/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2016_mva_v2/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *

postProcessing_directory = "TopEFT_PP_2017_mva_v3/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v3/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *


signals = []
if   args.signal == "ewkDM":
    data_directory = '/afs/hephy.at/data/rschoefbeck02/cmgTuples/'
    postProcessing_directory = "TopEFT_PP_v19/trilep/"
    from TopEFT.samples.cmgTuples_ttZ0j_Summer16_mAODv2_postProcessed import *

    SM          = ttZ0j_ll

    current1    = ttZ0j_ll_DC1A_1p000000
    current2    = ttZ0j_ll_DC1A_0p500000_DC1V_0p500000
    current3    = ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000

    SM.style       = styles.lineStyle( ROOT.kBlack, width=3, errors = True )
    current1.style = styles.lineStyle( ROOT.kMagenta, width=3, errors = True )
    current2.style = styles.lineStyle( ROOT.kBlue, width=3, errors = True )
    current3.style = styles.lineStyle( ROOT.kGreen+1, width=3, errors = True )

    dipole1     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700
    dipole2     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700
    dipole3     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700
    dipole4     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700
    dipole5     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000
    dipole6     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000
    dipole7     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000
    dipole8     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000

    dipoles = [ dipole1, dipole2, dipole3, dipole4, dipole5, dipole6, dipole7, dipole8 ]

    colors = [ ROOT.kMagenta+1, ROOT.kOrange, ROOT.kBlue, ROOT.kCyan+1, ROOT.kGreen+1, ROOT.kRed, ROOT.kViolet, ROOT.kYellow+2 ]
    for i, dipole in enumerate(dipoles):
        dipole.style = styles.lineStyle( colors[i], width=3 )
 

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
      (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if False else (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 


def addSys( selectionString , sys = None ):
    if   sys in jet_systematics: return selectionString.replace('nJetSelected', 'nJetSelected_' + sys).replace('nBTag', 'nBTag_' + sys)
    elif sys in met_systematics: return selectionString.replace('met_pt', 'met_pt_' + sys)
    else:                        return selectionString


def weightMC( sys = None ):
    # weights used right now: PU, BTag, trigger, tracking
    if sys is None:
        return (lambda event, sample:event.weight*event.reweightPU36fb*event.reweightBTagDeepCSV_SF*event.reweightTrigger*event.reweightLeptonTrackingSF,"weight * reweightPU36fb * reweightBTagDeepCSV_SF * reweightTrigger * reweightLeptonTrackingSF")
    elif 'PU' in sys:
        return (lambda event, sample:event.weight*event.reweightBTagDeepCSV_SF*event.reweightTrigger*event.reweightLeptonTrackingSF*getattr(event, "reweight"+sys), "weight * reweightBTagDeepCSV_SF * reweightTrigger * reweightLeptonTrackingSF * reweight"+sys)
    elif 'BTag' in sys:
        return (lambda event, sample:event.weight*event.reweightPU36fb*event.reweightTrigger*event.reweightLeptonTrackingSF*getattr(event, "reweight"+sys), "weight * reweightPU36fb * reweightTrigger * reweightLeptonTracking * reweight"+sys)
    elif 'Trigger' in sys:
        return (lambda event, sample:event.weight*event.reweightPU36fb*event.reweightBTagDeepCSV_SF*event.reweightLeptonTrackingSF*getattr(event, "reweight"+sys), "weight * reweightPU36fb * reweightBTagDeepCSV_SF * reweightLeptonTracking * reweight"+sys)
    elif 'Tracking' in sys:
        return (lambda event, sample:event.weight*event.reweightPU36fb*event.reweightBTagDeepCSV_SF*event.reweightTrigger*getattr(event, "reweight"+sys), "weight * reweightPU36fb * reweightBTagDeepCSV_SF * reweightTrigger * reweight"+sys)
    #elif sys in weight_systematics:
    #    return (lambda event, sample:event.weight*event.reweightBTagDeepCSV_SF*event.reweightPU36fb*getattr(event, "reweight"+sys), "weight*reweightPU36fb*reweightBTagDeepCSV_SF*reweight"+sys)
    elif sys in jme_systematics :
        return weightMC( sys = None )
    else:
        raise ValueError( "Systematic %s not known"%sys )
    
#
# Read variables and sequences
#
read_variables = ["weight/F", "jet[pt/F,eta/F,phi/F,btagCSV/F]", "Z_mass/F", "Z_eta/F",
                  "met_pt/F", "met_phi/F", "lep[pt/F,eta/F,relIso03/F]", "nGoodMuons/F", "nGoodElectrons/F",
                  "nBTag/I", "nJetSelected/I","run/I","evt/l"]

sequence = []

def getLeptonSelection( mode ):
  if   mode=="mumumu":  return "nGoodMuons==3&&nGoodElectrons==0"
  elif mode=="mumue":   return "nGoodMuons==2&&nGoodElectrons==1"
  elif mode=="muee":    return "nGoodMuons==1&&nGoodElectrons==2"
  elif mode=="eee":     return "nGoodMuons==0&&nGoodElectrons==3"
  elif mode=="all":     return "nGoodLeptons==3"


#
# Loop over channels
#
allPlots   = {}
allModes   = ['mumumu','mumue','muee', 'eee', 'all']
allModes   = ['all']
for index, mode in enumerate(allModes):

    logger.info('Working on mode ' + str(mode))

    if args.year == 2016:
        data_sample = Run2016
        data_sample.setSelectionString([getFilterCut(isData=True), getLeptonSelection(mode)])
    elif args.year == 2017:
        data_sample = Run2017
        data_sample.setSelectionString([getFilterCut(isData=True, year=2017), getLeptonSelection(mode)])

    lumi_scale = data_sample.lumi/1000
    data_sample.texName = "data"
    data_sample.read_variables = ['weight/F']
    data_sample.style   = styles.errorStyle( ROOT.kBlack )

    data_weight = lambda event, sample: event.weight
    data_weight_string = "weight"

    logger.info('Lumi scale is ' + str(lumi_scale))

    if args.year == 2016:
        TTZ_mc  = TTZtoLLNuNu
        TTW_mc  = TTW
        TZQ_mc  = TZQ
        TTX_mc  = TTX
        WZ_mc   = WZ_powheg
        rare_mc = rare
        non_mc  = nonprompt
        
    elif args.year == 2017:
        TTZ_mc  = TTZtoLLNuNu_17
        TTW_mc  = TTW_17
        TZQ_mc  = TZQ_17
        TTX_mc  = TTX_17
        WZ_mc   = WZ_amcatnlo_17
        rare_mc = rare_17
        non_mc  = nonprompt_17

    mc    = [ TTZ_mc , TTW_mc, TZQ_mc, TTX_mc, WZ_mc, rare_mc, non_mc ]
    if args.small:
        for sample in mc:# + ([data_sample] if type(data_sample)!=type([]) else data_sample):
            sample.reduceFiles( to = 1 )

    for sample in mc:
        sample.scale           = lumi_scale
        sample.style           = styles.fillStyle(sample.color, lineColor = sample.color)
        sample.read_variables  = ['reweightBTagDeepCSV_SF/F','reweightPU36fb/F','nTrueInt/F', 'reweightTrigger/F', 'reweightLeptonTrackingSF/F', 'Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I']
        sample.read_variables += ["reweight%s/F"%s    for s in weight_systematics]
        sample.read_variables += ["nJetSelected_%s/I"%s   for s in jet_systematics]
        sample.read_variables += ["nBTag_%s/I"%s      for s in jet_systematics]
        sample.setSelectionString([getFilterCut(isData=False, year=args.year), getLeptonSelection(mode)])

    for s in signals:
        s.scale          = lumi_scale
        #s.read_variables = ['reweightBTagCSVv2_SF/F','reweightPU36fb/F','nTrueInt/F']
        #s.weight         = lambda event, sample: event.reweightLeptonSF*event.reweightDilepTriggerBackup*event.reweightPU36fb
        s.setSelectionString([getFilterCut(isData=False), getLeptonSelection(mode)])

    for sample in [data_sample]:
        sample.read_variables  = ['Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I']

    # Use some defaults
    Plot.setDefaults( selectionString = cutInterpreter.cutString(args.selection) )
  
    stack_mc        = Stack( mc )
    #stack_signal    = Stack( mc[1:] + [dipole1] )

    if   args.signal == "ewkDM": stack_data = Stack( data_sample, signals ) 
    else:                       stack_data = Stack( data_sample )
    sys_stacks = {sys:copy.deepcopy(stack_mc) for sys in [None] + weight_systematics + jme_systematics }
    plots = []
  

    nBtagBinning = [6, 0, 6]

    nbtags_data  = Plot( 
        name            = "nbtags_data",
        texX            = 'number of b-tags (deepCSV)', texY = 'Number of Events',
        stack           = stack_data,
        attribute       = TreeVariable.fromString('nBTag/I'),
        binning         = nBtagBinning,
        weight          = data_weight,
        ) 
    plots.append( nbtags_data )

    nbtags_mc  = {sys: Plot(
        name            = "nbtags" if sys is None else "nbtags_mc_%s" % sys,
        texX            = 'number of b-tags (deepCSV)', texY = 'Number of Events',
        stack           = sys_stacks[sys],
        attribute       = TreeVariable.fromString('nBTag/I') if sys is None or sys in weight_systematics or sys in met_systematics else TreeVariable.fromString( "nBTag_%s/I" % sys ),
        binning         = nBtagBinning,
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( nbtags_mc.values() )

    jetBinning = [10,0,10]

    njets_data  = Plot( 
        name            = "njets_data",
        texX            = 'number of jets',
        texY            = 'Number of Events',
        stack           = stack_data,
        attribute       = TreeVariable.fromString('nJetSelected/I'),
        binning         = jetBinning,
        weight          = data_weight,
        )
    plots.append( njets_data )

    njets_mc  = {sys: Plot(
        name            = "njets" if sys is None else "njets_mc_%s" % sys,
        texX            = 'number of jets',
        texY            = 'Number of Events',
        stack           = sys_stacks[sys],
        attribute       = TreeVariable.fromString('nJetSelected/I') if sys is None or sys in weight_systematics or sys in met_systematics else TreeVariable.fromString( "nJetSelected_%s/I" % sys ),
        binning         = jetBinning,
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( njets_mc.values() )
    
    cosThetaStarBinning = [-1,-0.6, -0.2, 0.2, 0.6, 1.0]
    
    cosThetaStar_data  = Plot(
        name            = "cosThetaStar_data",
        texX            = 'cos(#theta*)',
        texY            = 'Number of Events',
        stack           = stack_data,
        attribute       = TreeVariable.fromString('cosThetaStar/F'),
        binning         = Binning.fromThresholds(cosThetaStarBinning),
        weight          = data_weight,
        )
    plots.append( cosThetaStar_data )

    cosThetaStar_mc  = {sys: Plot(
        name            = "cosThetaStar" if sys is None else "cosThetaStar_mc_%s" % sys,
        texX            = 'cos(#theta*)',
        texY            = 'Number of Events',
        stack           = sys_stacks[sys],
        attribute       = TreeVariable.fromString('cosThetaStar/F'),
        binning         = Binning.fromThresholds(cosThetaStarBinning),
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }

    plots.extend( cosThetaStar_mc.values() )
    
    ZptBinning = [0, 100, 200, 400, 800]

    Zpt_data  = Plot( 
        name            = "Z_pt_data",
        texX            = 'p_{T}(Z) (GeV)', 
        texY            = 'Number of Events' if args.normalizeBinWidth else "Number of Events",
        stack           = stack_data, 
        attribute       = TreeVariable.fromString( "Z_pt/F" ),
        binning         = Binning.fromThresholds( ZptBinning ),
        weight          = data_weight,
        )
    plots.append( Zpt_data )
    
    Zpt_mc  = {sys: Plot(
        name            = "Z_pt" if sys is None else "Z_pt_mc_%s" % sys,
        texX            = 'p_{T}(Z) (GeV)',
        texY            = 'Number of Events' if args.normalizeBinWidth else "Number of Events",
        stack           = sys_stacks[sys],
        attribute       = TreeVariable.fromString('Z_pt/F'),
        binning         = Binning.fromThresholds( ZptBinning ),
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( Zpt_mc.values() )

    ZptBinning_fine = range(0,650,50)
    
    Zpt_data_fine  = Plot(
        name            = "Z_pt_fine_data",
        texX            = 'p_{T}(Z) (GeV)',
        texY            = 'Number of Events / 50 GeV' if args.normalizeBinWidth else "Number of Events",
        stack           = stack_data,
        attribute       = TreeVariable.fromString( "Z_pt/F" ),
        binning         = Binning.fromThresholds( ZptBinning_fine ),
        weight          = data_weight,
        )
    plots.append( Zpt_data_fine )

    Zpt_mc_fine  = {sys: Plot(
        name            = "Z_pt_fine" if sys is None else "Z_pt_fine_mc_%s" % sys,
        texX            = 'p_{T}(Z) (GeV)',
        texY            = 'Number of Events / 50 GeV' if args.normalizeBinWidth else "Number of Events",
        stack           = sys_stacks[sys],
        attribute       = TreeVariable.fromString('Z_pt/F'),
        binning         = Binning.fromThresholds( ZptBinning_fine ),
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( Zpt_mc_fine.values() )

    met_data  = Plot( 
        name            = "met_pt_data",
        texX            = 'E_{T}^{miss} (GeV)', 
        texY            = 'Number of Events' if args.normalizeBinWidth else "Number of Event / 50 GeV",
        stack           = stack_data, 
        attribute       = TreeVariable.fromString( "met_pt/F" ),
        binning         = [10,0,500],
        weight          = data_weight,
        )
    plots.append( met_data )

    met_mc  = {sys: Plot(
        name            = "met_pt" if sys is None else "met_pt_mc_%s" % sys,
        texX            = 'E_{T}^{miss} (GeV)',
        texY            = 'Number of Events' if args.normalizeBinWidth else "Number of Event / 50 GeV",
        stack           = sys_stacks[sys],
        attribute       = TreeVariable.fromString('met_pt/F') if sys not in met_systematics else TreeVariable.fromString( "met_pt_%s/F" % sys ),
        binning         = [10,0,500],
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( met_mc.values() )


    massBinning = range(80,102,2)

    mass_data  = Plot(
        name            = "Z_mass_data",
        texX            = 'M(ll) (GeV)',
        texY            = 'Number of Events / 2 GeV' if args.normalizeBinWidth else "Number of Event",
        stack           = stack_data,
        attribute       = TreeVariable.fromString( "Z_mass/F" ),
        binning         = Binning.fromThresholds( massBinning ),
        weight          = data_weight,
        )
    plots.append( mass_data )

    mass_mc  = {sys: Plot(
        name            = "Z_mass" if sys is None else "Z_mass_mc_%s" % sys,
        texX            = 'M(ll) (GeV)',
        texY            = 'Number of Events / 2 GeV' if args.normalizeBinWidth else "Number of Event",
        stack           = sys_stacks[sys],
        attribute       = TreeVariable.fromString('Z_mass/F'),
        binning         = Binning.fromThresholds( massBinning ),
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( mass_mc.values() )

    # leptons

    l1_pt_data  = Plot(
        name            = "l1_pt_data",
        texX            = 'p_{T}(leading-l) (GeV)',
        texY            = 'Number of Events / 10 GeV',
        stack           = stack_data,
#        attribute       = TreeVariable.fromString('lep_pt[0]/F'),
        attribute       = lambda event, sample:event.lep_pt[0],
        binning         = [40,0,400],
        weight          = data_weight,
        )
    plots.append( l1_pt_data )

    l1_pt_mc  = {sys: Plot(
        name            = "l1_pt" if sys is None else "l1_pt_mc_%s" % sys,
        texX            = 'p_{T}(leading-l) (GeV)',
        texY            = 'Number of Events / 10 GeV',
        stack           = sys_stacks[sys],
#        attribute       = TreeVariable.fromString('lep_pt[0]/F'),
        attribute       = lambda event, sample:event.lep_pt[0],
        binning         = [40,0,400],
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( l1_pt_mc.values() )

    Zl1_pt_data  = Plot(
        name            = "Zl1_pt_data",
        texX            = 'p_{T}(l_{1,Z}) (GeV)',
        texY            = 'Number of Events / 10 GeV',
        stack           = stack_data,
#        attribute       = TreeVariable.fromString('lep_pt[Z_l1_index/I]/F'),
        attribute       = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning         = [40,0,400],
        weight          = data_weight,
        )
    plots.append( Zl1_pt_data )

    Zl1_pt_mc  = {sys: Plot(
        name            = "Zl1_pt" if sys is None else "Zl1_pt_mc_%s" % sys,
        texX            = 'p_{T}(l_{1,Z}) (GeV)',
        texY            = 'Number of Events / 10 GeV',
        stack           = sys_stacks[sys],
#        attribute       = TreeVariable.fromString('lep_pt[Z_l1_index/I]/F'),
        attribute       = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning         = [40,0,400],
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( Zl1_pt_mc.values() )

    Zl2_pt_data  = Plot(
        name            = "Zl2_pt_data",
        texX            = 'p_{T}(l_{2,Z}) (GeV)',
        texY            = 'Number of Events / 10 GeV',
        stack           = stack_data,
        attribute       = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning         = [20,0,200],
        weight          = data_weight,
        )
    plots.append( Zl2_pt_data )

    Zl2_pt_mc  = {sys: Plot(
        name            = "Zl2_pt"  if sys is None else "Zl2_pt_mc_%s" % sys,
        texX            = 'p_{T}(l_{2,Z}) (GeV)',
        texY            = 'Number of Events / 10 GeV',
        stack           = sys_stacks[sys],
        attribute       = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning         = [20,0,200],
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( Zl2_pt_mc.values() )

    nonZl1_pt_data  = Plot(
        name            = "nonZl1_pt_data",
        texX            = 'p_{T}(l_{1,non-Z}) (GeV)',
        texY            = 'Number of Events / 10 GeV',
        stack           = stack_data,
        attribute       = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning         = [20,0,200],
        weight          = data_weight,
        )
    plots.append( nonZl1_pt_data )

    nonZl1_pt_mc  = {sys: Plot(
        name            = "nonZl1_pt"  if sys is None else "nonZl1_pt_mc_%s" % sys,
        texX            = 'p_{T}(l_{1,non-Z}) (GeV)',
        texY            = 'Number of Events / 10 GeV',
        stack           = sys_stacks[sys],
        attribute       = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning         = [20,0,200],
        selectionString = addSys(cutInterpreter.cutString(args.selection), sys),
        weight          = weightMC( sys = sys )[0],
        ) for sys in all_systematics }
    plots.extend( nonZl1_pt_mc.values() )

    plotConfigs = [\
            [ nbtags_mc, nbtags_data, -1],
            [ njets_mc, njets_data, -1],
            [ cosThetaStar_mc, cosThetaStar_data, 1],
            [ Zpt_mc, Zpt_data, 1 ],
            [ Zpt_mc_fine, Zpt_data_fine, -1 ],
            [ met_mc, met_data, 1],
            [ mass_mc, mass_data, -1],
            [ l1_pt_mc, l1_pt_data, -1],
            [ Zl1_pt_mc, Zl1_pt_data, -1],
            [ Zl2_pt_mc, Zl2_pt_data, -1],
            [ nonZl1_pt_mc, nonZl1_pt_data, -1],

    ]

    print args.year
    result_dir  = os.path.join(plot_directory, "systematicsPlots", str(args.year), args.plot_directory, mode, args.selection)
    result_file = os.path.join(result_dir, 'results.pkl')
    try: os.makedirs(result_dir)
    except: pass

    ## get the norm etc - not needed for ttZ!
    if args.selectSys != "combine": 
      
        plotting.fill(plots, read_variables = read_variables, sequence = sequence)

        waitForLock( result_file ) 
        if os.path.exists(result_file):
            allPlots = pickle.load(file( result_file ))
            allPlots.update({p.name : p.histos for p in plots})
        else:                           
            allPlots = {p.name : p.histos for p in plots}
        pickle.dump( allPlots, file( result_file, 'w' ) )
        removeLock( result_file ) 
        logger.info( "Done for sys " + args.selectSys )

    else:
        allPlots = pickle.load(file( result_file ))

        from RootTools.plot.Plot import addOverFlowBin1D
        for p in plots:
            p.histos = allPlots[p.name]
            for s in p.histos:
                for h in s:
                    addOverFlowBin1D(h, "upper")
                    if h.Integral()==0: logger.warning( "Found empty histogram %s in results file %s", h.GetName(), result_file )

        for plot_mc, plot_data, bin_width in plotConfigs:
            if args.normalizeBinWidth and bin_width>0:
                for p in plot_mc.values() + [plot_data]:
                    for histo in sum(p.histos, []):
                        histo.Scale(1,"width")

            
            # For now, keep Toms way of adding shape uncertainties (the following part is only used for that)
            if None in plot_mc.keys():
                shapeHists = {comp:plot_mc[None].histos[0][mc.index(comp)] for comp in mc}
            else:
                print "Couldn't find central histogram! Taking %s insted."%plot_mc.keys()[0]
                shapeHists = {comp:plot_mc[plot_mc.keys()[0]].histos[0][comp] for comp in mc}

            print shapeHists

            #Calculating systematics
            h_summed = {k: plot_mc[k].histos_added[0][0].Clone() for k in plot_mc.keys()}

            h_rel_err = h_summed[None].Clone()
            h_rel_err.Reset()

            #MC statistical error
            for ib in range( 1 + h_rel_err.GetNbinsX() ):
                h_rel_err.SetBinContent(ib, h_summed[None].GetBinError(ib)**2 )

            h_sys = {}
            goOn = False
            for k, s1, s2 in ([s for s in sys_pairs if s[0] == args.showOnly] if args.showOnly else sys_pairs):
              goOn = True
              h_sys[k] = h_summed[s1].Clone()
              h_sys[k].Scale(-1)
              h_sys[k].Add(h_summed[s2])
            if not goOn: continue

            # Adding in quadrature
            for k in h_sys.keys():
                print k
                for ib in range( 1 + h_rel_err.GetNbinsX() ):
                  print h_sys[k].GetBinContent(ib)
                  h_rel_err.SetBinContent(ib, h_rel_err.GetBinContent(ib) + h_sys[k].GetBinContent(ib)**2 )

            # In case one wants to add uncertainties to specific backgrounds (like x-sec), that can be done here
            if True:
                for ib in range(1 + h_rel_err.GetNbinsX() ):
                    counts = [ shapeHists[x].GetBinContent(ib) for x in mc ]
                    totalCount = sum(counts)
                    print "Count in bin %s: %.2f"%(ib, totalCount)
                    shapeUnc = [ 0 ]
                    print rare_mc
                    print rare_mc.name
                    shapeUnc.append( (0.50*shapeHists[rare_mc].GetBinContent(ib))**2 )
                    shapeUnc.append( (0.11*shapeHists[WZ_mc].GetBinContent(ib))**2 )
                    shapeUnc.append( (0.30*shapeHists[non_mc].GetBinContent(ib))**2 )
                    shapeUnc.append( (0.10*shapeHists[TTX_mc].GetBinContent(ib))**2 )
                    shapeUnc.append( (0.10*shapeHists[TZQ_mc].GetBinContent(ib))**2 )
                    shapeUnc.append( (0.10*shapeHists[TTZ_mc].GetBinContent(ib))**2 ) # mockup for PDF and scale
                    shapeUnc.append( (0.025*(totalCount))**2 )
                    #shapeUnc.append( (0.5*(totalCount))**2 )
                    h_rel_err.SetBinContent(ib, h_rel_err.GetBinContent(ib) + sum( shapeUnc ) )

            # take sqrt
            for ib in range( 1 + h_rel_err.GetNbinsX() ):
                h_rel_err.SetBinContent(ib, sqrt( h_rel_err.GetBinContent(ib) ) )

            # Divide
            h_rel_err.Divide(h_summed[None])

            plot = plot_mc[None]
            if args.normalizeBinWidth: plot.name += "_normalizeBinWidth"
            signal_histos = plot_data.histos[1:]
            data_histo    = plot_data.histos[0][0]
            for h in plot_data.histos[0][1:]:
                data_histo.Add(h)

            data_histo.style = styles.errorStyle( ROOT.kBlack )
            plot.histos += [[ data_histo ]]
            for h in signal_histos: plot.histos += [h]
            #plot_data.stack[0][0].texName = data_sample.texName if mode != "all" else data_sample[0].texName 
            plot.stack += [[ plot_data.stack[0][0] ]]
            for i, signal in enumerate(signals):
                plot_data.stack[i+1][0].texName = signal.texName
                plot_data.stack[i+1][0].style   = signal.style
                plot.stack += [[ plot_data.stack[i+1][0] ]]

            boxes = []
            ratio_boxes = []
            for ib in range(1, 1 + h_rel_err.GetNbinsX() ):
                val = h_summed[None].GetBinContent(ib)
                if val<0: continue
                sys = h_rel_err.GetBinContent(ib)
                box = ROOT.TBox( h_rel_err.GetXaxis().GetBinLowEdge(ib),  max([0.03, (1-sys)*val]), h_rel_err.GetXaxis().GetBinUpEdge(ib), max([0.03, (1+sys)*val]) )
                box.SetLineColor(ROOT.kBlack)
                box.SetFillStyle(3444)
                box.SetFillColor(ROOT.kBlack)
                r_box = ROOT.TBox( h_rel_err.GetXaxis().GetBinLowEdge(ib),  max(0.1, 1-sys), h_rel_err.GetXaxis().GetBinUpEdge(ib), min(1.9, 1+sys) )
                r_box.SetLineColor(ROOT.kBlack)
                r_box.SetFillStyle(3444)
                r_box.SetFillColor(ROOT.kBlack)

                boxes.append( box )
                ratio_boxes.append( r_box )

                ratio = {'yRange':(0.1,1.9), 'drawObjects':ratio_boxes}
                   
            #print "plot.histos[0][pos_top].Integral()", pos_top,plot.histos 
            #print "plot.histos[0][pos_top].Integral()", plot.histos[0][pos_top].Integral()    
            for log in [False, True]:
                plotDir = os.path.join(plot_directory, 'systematicsPlots', str(args.year), args.plot_directory, mode + ("_log" if log else "") + "_scaled", args.selection)
                if args.showOnly: plotDir = os.path.join(plotDir, "only_" + args.showOnly)
                plotting.draw(plot,
                    plot_directory = plotDir,
                    ratio = ratio,
                    legend = (0.50,0.88-0.04*sum(map(len, plot.histos)),0.95,0.88),
                    logX = False, logY = log, sorting = True,
                    yRange = (0.03, "auto"),
                    #drawObjects = drawObjects( True, top_sf[None], lumi_scale ) + boxes,
                    drawObjects = drawObjects( True, 1, lumi_scale ) + boxes,
                    copyIndexPHP = True
                )
