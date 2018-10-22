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
from TopEFT.Tools.WeightInfo      import WeightInfo

from plot_helpers                 import *
from plotParameter_ttG            import ttG1lPlots, ttG1lSequence, ttG2lPlots, ttG2lSequence, ttGVariables

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--signal',             action='store',      default=None,            nargs='?', choices=[None, "ewkDM", "ttZ01j"], help="Add signal to plot")
argParser.add_argument('--lepSelection',       action='store',      default='dilept',        nargs='?', choices=["dilept", "semilept"], help="dileptonic or semi-leptonic ttgamma channel?")
argParser.add_argument('--onlyTTG',            action='store_true', default=False,           help="Plot only ttG")
argParser.add_argument('--noData',             action='store_true', default=False,           help='also plot data?')
argParser.add_argument('--small',              action='store_true',                          help='Run only on a small subset of the data?', )
argParser.add_argument('--TTG_LO',             action='store_true',                          help='Use LO TTG?', )
argParser.add_argument('--reweightPtGToSM',    action='store_true',                          help='Reweight Pt(gamma) to the SM for all the signals?', )
argParser.add_argument('--plot_directory',     action='store',      default='80X_mva_v17')
argParser.add_argument('--selection',          action='store',      default='trilep-Zcand-lepSelTTZ-min_mll12-njet1p-btag0-onZ')
argParser.add_argument('--normalize',          action='store_true', default=False,           help="Normalize yields" )
argParser.add_argument('--WZpowheg',           action='store_true', default=False,           help="Use WZ powheg sample" )
argParser.add_argument('--reweightWZ',         action='store_true', default=False,           help="Reweight to WZ powheg sample?" )
argParser.add_argument('--parameters',         action='store',      default = [],            type=str, nargs='+', help = "argument parameters")
argParser.add_argument('--order',              action='store',      default=2,               type=int, help='Polynomial order of weight string (e.g. 2)')
args = argParser.parse_args()

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

# modify plot directory
args.plot_directory = "TTGamma2l/" + args.plot_directory if args.lepSelection == "dilept" else "TTGamma1l/" + args.plot_directory
if args.small:                        args.plot_directory += "_small"
if args.noData:                       args.plot_directory += "_noData"
if args.signal:                       args.plot_directory += "_signal_"+args.signal
if args.onlyTTG:                      args.plot_directory += "_onlyTTG"
if args.TTG_LO:                       args.plot_directory += "_TTG_LO"
if args.WZpowheg:                     args.plot_directory += "_WZpowheg"
if args.reweightWZ:                   args.plot_directory += "_WZreweight"
if args.normalize:                    args.plot_directory += "_normalize"
if args.reweightPtGToSM:              args.plot_directory += "_reweightPtGToSM"

#
# Make samples, will be searched for in the postProcessing directory
#
# Import MC samples
data_directory           = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v20/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

# Import data samples
data_directory           = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v20/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *

# define signal samples
signals = []
if args.signal == "dim6Top":
    data_directory           = '/afs/hephy.at/data/rschoefbeck02/cmgTuples/'
    postProcessing_directory = "TopEFT_PP_v12/trilep/"
    from TopEFT.samples.cmgTuples_ttZ0j_Summer16_mAODv2_postProcessed import *
    
    SM                = ttZ0j_ll
    SM.style          = styles.lineStyle( ROOT.kBlack, width=3, errors = True )
    SM.params         = {}
    SM.read_variables = [VectorTreeVariable.fromString('p[C/F]', nMax=2000)]

    w = WeightInfo( SM.reweight_pkl )
    w.set_order( args.order )

    samplesWC = []
    if len(args.parameter) != 0:
        colors = [ ROOT.kMagenta+1, ROOT.kOrange, ROOT.kBlue, ROOT.kCyan+1, ROOT.kGreen+1, ROOT.kRed, ROOT.kViolet, ROOT.kYellow+2 ]
     
        coeffs = args.parameters[::2]
        str_vals = args.parameters[1::2]
        vals = list( map( float, str_vals ) )
        for i, (coeff, val, str_val) in enumerate(zip(coeffs, vals, str_vals)):
            samplesWC.append( copy.deepcopy( SM ) )
            samplesWC[-1].texName    = coeff
            samplesWC[-1].name       = coeff
            samplesWC[-1].params     = {coeff:val}
            samplesWC[-1].style      = styles.lineStyle( colors[i], width=2, errors = True )
            samplesWC.read_variables = [VectorTreeVariable.fromString('p[C/F]', nMax=2000)]

    signals = [SM] + samplesWC

# scaling signals
scaling = { i+1:0 for i in range(len(signals)) }

# reweighting 
if args.reweightPtGToSM:
    #attention ttgamma
    sel_string = "&&".join([getFilterCut(isData=False), get3LeptonSelection('all'), cutInterpreter.cutString(args.selection)])
    #attention ttgamma
    TTG_ptG = TTZtoLLNuNu.get1DHistoFromDraw("photon_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
    scaleFactor = TTG_ptG.Integral()
    if scaleFactor == 0: scaleFactor = 1.
    TTG_ptG.Scale(1./scaleFactor)

    def get_reweight( var, histo, params=None ):

        def reweight(event, sample):
            i_bin = histo.FindBin(getattr( event, var ) )
            return histo.GetBinContent(i_bin)*w.get_weight_func( **params )( event, sample )/event.p_C[0] if params is not None else histo.GetBinContent(i_bin)

        return reweight

    for signal in signals:
        logger.info( "Computing PtG reweighting for signal %s", signal.name )
        signal_ptG = signal.get1DHistoFromDraw("photon_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
        scaleFactor = signal_ptG.Integral()
        if scaleFactor == 0: scaleFactor = 1.
        signal_ptG.Scale(1./scaleFactor)

        signal.reweight_ptG_histo = TTG_ptG.Clone()
        signal.reweight_ptG_histo.Divide(signal_ptG)

        signal.weight = get_reweight( "photon_pt", signal.reweight_ptG_histo, **signal.params if args.signal == "dim6Top" else None )

elif args.signal == "dim6Top":
    def get_reweight( params ):

        def reweight(event, sample):
            return w.get_weight_func( **params )( event, sample ) / event.p_C[0]

        return reweight

    for signal in signals:
        logger.info( "Computing weights for signal %s", signal.name )
        signal.weight = get_reweight( **signal.params )


#
# Read variables and sequences
#
read_variables = ttGVariables()
sequence       = ttG2lSequence() if args.lepSelection == "dilept" else ttG1lSequence()

#scale WZ samples to MC generators
WZ_amcatnlo.Z_pt_histo    = WZ_amcatnlo.get1DHistoFromDraw("Z_pt", [10,0,500], selectionString= cutInterpreter.cutString(args.selection), addOverFlowBin='upper')
scaleFactor = WZ_amcatnlo.Z_pt_histo.Integral()
if scaleFactor == 0: scaleFactor = 1.
WZ_amcatnlo.Z_pt_histo.Scale(1./scaleFactor)
WZ_powheg.Z_pt_histo      = WZ_powheg.get1DHistoFromDraw("Z_pt", [10,0,500], selectionString= cutInterpreter.cutString(args.selection), addOverFlowBin='upper')
scaleFactor = WZ_powheg.Z_pt_histo.Integral()
if scaleFactor == 0: scaleFactor = 1.
WZ_powheg.Z_pt_histo.Scale(1./scaleFactor)

ZptRW = get_powheg_reweight( WZ_powheg.Z_pt_histo, WZ_amcatnlo.Z_pt_histo )

#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['mumu','mue', 'ee'] if args.lepSelection == "dilept" else ['mu', 'e']

#
# Set data sample
#
if not args.noData:
    data_sample                = Run2016
    data_sample.texName        = "data"# (legacy)"
    data_sample.name           = "data"
    data_sample.read_variables = ["evt/I","run/I"]
    data_sample.style          = styles.errorStyle(ROOT.kBlack)

if args.lepSelection == "dilept":
    addVariables = ['reweightBTagCSVv2_SF/F', 'reweightBTagDeepCSV_SF/F', 'reweightPU36fb/F']#, 'reweightLeptonSF_tight_2l/F', 'reweightLeptonTrackingSF_tight_2l/F', 'reweightTrigger_tight_2l/F', "photon_pt/F"]
else:
    addVariables = ['reweightBTagCSVv2_SF/F', 'reweightBTagDeepCSV_SF/F', 'reweightPU36fb/F']#, 'reweightLeptonSF_tight_2l/F', 'reweightLeptonTrackingSF_tight_1l/F', 'reweightTrigger_tight_1l/F', "photon_pt/F"]

for index, mode in enumerate(allModes):
    yields[mode] = {}

    if not args.noData:
        data_sample.setSelectionString( [ getFilterCut(isData=True), get2LeptonSelection(mode) if args.lepSelection == "dilept" else get1LeptonSelection(mode) ] )
        lumi_scale = data_sample.lumi/1000.
    else:
        lumi_scale = 35.9

    weight_ = lambda event, sample: event.weight

    # attention ttgamma
    TTG_mc = TTG_LO if args.TTG_LO else TTG

    if args.onlyTTG:
        mc = [ TTG_mc ]
    else:
        mc = [ TTG_mc, nonpromptMC, TTX_noTTG, WZ_powheg if args.WZpowheg else WZ_amcatnlo, ZZ, rare, WGToLNuG, ZGTo2LG ]
        # mc = [ TTG_mc , TTW, TTX, WZ_powheg if args.WZpowheg else WZ_amcatnlo, rare, ZZ, nonpromptMC, ZGTo2LG ]
        # dilept: ttbar, Zgamma, DY, single-t+tW, ttZ, ttW, ttH, ttVV, tZq, tHq, tHW, tWZ, diboson, triboson, Wgamma
        # semilept: ttbar, Zgamma, DY, single-t+tW, ttZ, ttW, (ttH), (ttVV), (tZq), (tHq), (tHW), (tWZ), diboson, (triboson), Wgamma, QCD (mu/e enriched)

    for sample in mc:
        sample.style = styles.fillStyle(sample.color)

    for sample in mc + signals:
        sample.scale = lumi_scale
        #attention ttgamma
        if args.lepSelection == "dilept":
            weightFunction = lambda event, sample_: event.reweightBTagDeepCSV_SF*event.reweightPU36fb#*event.reweightLeptonSF_tight_2l*event.reweightLeptonTrackingSF_tight_2l*event.reweightTrigger_tight_2l
        else:
            weightFunction = lambda event, sample_: event.reweightBTagDeepCSV_SF*event.reweightPU36fb#*event.reweightLeptonSF_tight_1l*event.reweightLeptonTrackingSF_tight_1l*event.reweightTrigger_tight_1l

        if sample in [WZ_amcatnlo] and args.reweightWZ:
            # reweight bg sample WZ if args.reweightWZ
            sample.read_variables = addVariables
            sample.weight         = lambda event, sample_: weightFunction( event, sample_ ) * ZptRW(event.Z_pt)

        elif sample in signals and args.signal == "dim6Top":
            # add weight to dim6Top weight function
            sample.read_variables += addVariables
            sample.weight          = lambda event, sample_: sample.weight( event, sample_ ) * weightFunction( event, sample_ )

        elif sample in signals and args.reweightPtGToSM:
            # add weight to reweightPtZToSM weight function
            sample.read_variables = addVariables
            sample.weight         = lambda event, sample_: sample.weight( event, sample_ ) * weightFunction( event, sample_ )

        else:
            sample.read_variables = addVariables
            sample.weight         = weightFunction

        tr = triggerSelector(2016)
        sample.setSelectionString( [getFilterCut(isData=False), get2LeptonSelection(mode) if args.lepSelection == "dilept" else get1LeptonSelection(mode), tr.getSelection("MC")] )

    if not args.noData:
        stack = Stack( mc, data_sample )
    else:
        stack = Stack( mc )

    stack.extend( [ [s] for s in signals ] )

    if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 1 )

    # Use some defaults
    Plot.setDefaults( stack = stack, weight = staticmethod( weight_ ), selectionString = cutInterpreter.cutString( args.selection ), addOverFlowBin='upper' )

    # get list of plots
    plots = ttG2lPlots( index ) if args.lepSelection == "dilept" else ttG1lPlots( index )

    plotting.fill( plots, read_variables = read_variables, sequence = sequence )

    # Get normalization yields from yield histogram
    for plot in plots:
      if plot.name == "yield":
        for i, l in enumerate(plot.histos):
          for j, h in enumerate(l):
            yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
            if args.lepSelection == "dilept":
                h.GetXaxis().SetBinLabel(1, "#mu#mu")
                h.GetXaxis().SetBinLabel(2, "#mue")
                h.GetXaxis().SetBinLabel(3, "ee")
            else:
                h.GetXaxis().SetBinLabel(1, "#mu")
                h.GetXaxis().SetBinLabel(2, "e")
    if args.noData: yields[mode]["data"] = 0

    yields[mode]["MC"] = sum( yields[mode][s.name] for s in mc )
    dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    drawPlots( plots, mode, dataMCScale, lumi_scale, args.selection, args.plot_directory, args.noData, args.normalize )
    allPlots[mode] = plots


# Add the different channels into SF and all
for i, mode in enumerate(allModes[1:]):
    yields[mode] = {}
    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in allModes)
        except: yields[mode][y] = 0

    dataMCScale = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    for plot in allPlots[allModes[0]]:
        # iterate through all plots but not the one with the first mode in list
        # add all plots to the first mode
        for plot2 in (p for p in allPlots[mode] if p.name == plot.name):
            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
                    if i==k:
                        j.Add(l)

#draw first mode with added plots ("all"-plot)    
drawPlots( allPlots[allModes[0]], "all", dataMCScale, lumi_scale, args.selection, args.plot_directory, args.noData, args.normalize )

logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )

