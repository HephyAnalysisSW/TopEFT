
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
from TopEFT.Tools.user            import plot_directory, mva_directory
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, deltaR, deltaR2
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.cutInterpreter  import cutInterpreter
from TopEFT.Tools.triggerSelector import triggerSelector

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--noData',             action='store_true', default=False,           help='also plot data?')
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--sorting',                                 action='store_true',     help='Sort MCs?', )
argParser.add_argument('--plot_directory',     action='store',      default='TTW_dim6top_nonprompt')
argParser.add_argument('--selection',          action='store',      default='SSdilep-lepSelTTW-njet2p-btag1p-met30')
argParser.add_argument('--normalize',           action='store_true', default=False,             help="Normalize yields" )
argParser.add_argument('--nominalSignal',      action='store_true', default=False,             help="Use the nominal signal sample?" )
argParser.add_argument('--WZpowheg',           action='store_true', default=False,             help="Use WZ powheg sample" )
args = argParser.parse_args()

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"
if args.sorting:                      args.plot_directory += "_sorting"
if args.noData:                       args.plot_directory += "_noData"
if args.WZpowheg:                     args.plot_directory += "_WZpowheg"
if args.nominalSignal:                args.plot_directory += "_nominalSignal"
if args.normalize: args.plot_directory += "_normalize"
#
# Make samples, will be searched for in the postProcessing directory
#
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *

#
# Text on the plots
#
def drawObjects( plotData, dataMCScale, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'Simulation'), 
      (0.45, 0.95, 'L=%i fb^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.45, 0.95, 'L=%i fb^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

scaling = { 1:0 }

def drawPlots(plots, mode, dataMCScale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.plot_directory, mode + ("_log" if log else ""), args.selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      postFix = " (legacy)"
      if not args.noData: 
        if mode == "all": plot.histos[1][0].legendText = "Data" + postFix
        if mode == "SF":  plot.histos[1][0].legendText = "Data (SF)" + postFix
      extensions_ = ["pdf", "png", "root"] if mode == 'all' else ['png']

      plotting.draw(plot,
        plot_directory = plot_directory_,
        extensions = extensions_,
        ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
        logX = False, logY = log, sorting = args.sorting, #True,
        yRange = (0.8, "auto") if log else (0.001, "auto"),
        scaling = scaling if args.normalize else {},
        legend = [ (0.19,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
        drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale ) if not args.normalize else drawObjects( not args.noData, 1.0 , lumi_scale ),
        copyIndexPHP = True,
)

# define 2l selections
def getLeptonSelection( mode ):
    if   mode=="mumu": return "abs(lep_pdgId[0])==13&&abs(lep_pdgId[1])==13"
    elif mode=="mue":  return "(abs(lep_pdgId[0])*abs(lep_pdgId[1]))==143"
    elif mode=="ee":   return "abs(lep_pdgId[0])==11&&abs(lep_pdgId[1])==11"
    elif mode=='all':  return "nlep==2"

# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I]", "njet/I","nJetSelected/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    ]
sequence = []

def getSelectedJets( event, sample ):
    jetVars     = ['eta','pt','phi','btagCSV','DFbb', 'DFb', 'id']
    event.selectedJets  = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'njet'))) if ( abs(event.jet_eta[i])<=2.4 and event.jet_pt[i] > 30 and event.jet_id[i])] #nJetSelected
sequence += [ getSelectedJets ]

def getM2l( event, sample ):
    # get the invariant mass of the 2l system
    l = []
    for i in range(2):
        l.append(ROOT.TLorentzVector())
        l[i].SetPtEtaPhiM(event.lep_pt[i], event.lep_eta[i], event.lep_phi[i],0)
    event.mll = (l[0] + l[1]).M()
    if event.mll < 12 and abs(event.mll-91.1876)>15: 
        event.weight = 0
sequence.append( getM2l )

def getLooseLeptonMult( event, sample ):
    leptons = [getObjDict(event, 'lep_', ['eta','pt','phi','charge', 'pdgId', 'sourceId','mediumMuonId'], i) for i in range(len(event.lep_pt))]
    lepLoose = [ l for l in leptons if l['pt'] > 10 and ((l['mediumMuonId'] and abs(l['pdgId'])==13) or abs(l['pdgId'])==11)  ]
    event.nLepLoose = len(lepLoose)
sequence.append( getLooseLeptonMult )

def find_flavor_sign_bin( event, sample ):    
    event.flavor_bin = -1
    if   event.lep_pdgId[0] == -13 and event.lep_pdgId[1] == -13:                 event.flavor_bin = 0
    elif event.lep_pdgId[0]*event.lep_pdgId[1] == 143 and event.lep_pdgId[0] < 0: event.flavor_bin = 1
    elif event.lep_pdgId[0] == -11 and event.lep_pdgId[1] == -11:                 event.flavor_bin = 2
    elif event.lep_pdgId[0] ==  13 and event.lep_pdgId[1] ==  13:                 event.flavor_bin = 3
    elif event.lep_pdgId[0]*event.lep_pdgId[1] == 143 and event.lep_pdgId[0] > 0: event.flavor_bin = 4
    elif event.lep_pdgId[0] ==  11 and event.lep_pdgId[1] ==  11:                 event.flavor_bin = 5
sequence.append( find_flavor_sign_bin )

#MVA
from Analysis.TMVA.Reader   import Reader
from TopEFT.MVA.MVA_TTW     import mva_variables, bdt1, bdt2, bdt3, bdt4, mlp1, mlp2, mlp3
from TopEFT.MVA.MVA_TTW     import sequence as mva_sequence
from TopEFT.MVA.MVA_TTW     import read_variables as mva_read_variables
from TopEFT.Tools.user      import mva_directory

sequence.extend( mva_sequence )
read_variables.extend( mva_read_variables )

#reader = Reader(
#    mva_variables    = mva_variables,
#    weight_directory = "/afs/hephy.at/work/t/ttschida/public/CMSSW_9_4_6_patch1/src/TopEFT/MVA/python/weights/",
#    label            = "Test")

reader_nonprompt = Reader(
    mva_variables     = mva_variables,
    weight_directory  = os.path.join( mva_directory, "TTW"),
    label             = "Test")

def makeDiscriminator( mva ):
    def _getDiscriminator( event, sample ):
        kwargs = {name:func(event,None) for name, func in mva_variables.iteritems()}
#        setattr( event, mva['name'], reader.evaluate(mva['name'], **kwargs))
        setattr( event, "nonprompt_"+mva['name'], reader_nonprompt.evaluate(mva['name'], **kwargs))
        #print mva['name'], getattr( event, mva['name'] )
    return _getDiscriminator

def discriminator_getter(name):
    def _disc_getter( event, sample ):
        return getattr( event, name )
    return _disc_getter

mvas = [ bdt1, bdt2, bdt3, bdt4, mlp1, mlp2, mlp3 ]
#mvas = [ mlp2 ]
for mva in mvas:
    reader_nonprompt.addMethod(method=mva)
    sequence.append( makeDiscriminator(mva) )

#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['mumu','mue','ee']
for index, mode in enumerate(allModes):
    yields[mode] = {}
    if not args.noData:
        data_sample = Run2016
        data_sample.texName = "data (legacy)"
        data_sample.setSelectionString([getFilterCut(isData=True), getLeptonSelection(mode)])
        data_sample.name           = "data"
        data_sample.read_variables = ["evt/I","run/I"]
        data_sample.style          = styles.errorStyle(ROOT.kBlack)
        lumi_scale                 = data_sample.lumi/1000

#    lumi_scale = 300
    lumi_scale = 35.9
    weight_ = lambda event, sample: event.weight

    TTZ_mc = TTZtoLLNuNu
    tWZ_sample = TWZ if args.nominalSignal else yt_TWZ_filter

    if args.WZpowheg:
        mc             = [ tWZ_sample, TTZ_mc , TTX, WZ_powheg, rare, ZZ, nonprompt_TWZ_3l, Xgamma ]
    else:
        #mc             = [ TWZ, TTZ_mc , TTX, WZ_amcatnlo, rare, ZZ, nonprompt_TWZ_3l, Xgamma ]
#        mc             = [ tWZ_sample, TTZ_mc, TTX_rare_TWZ, TZQ, WZ_amcatnlo, rare, ZZ, nonprompt_TWZ_3l ]#, Xgamma ]
#        mc             = [ yt_TWW, dim6top_TTW, TTZ_mc, TTX_rare_TWZ, WZ_amcatnlo, rare, nonprompt_TWZ_3l ]
        mc              = [ dim6top_TTW, TTZ_mc, nonprompt_TWZ_3l, WZ_amcatnlo, TTX_rare_TWZ, rare ]

    # specifications
    TTZtoLLNuNu.texName = "t#bar{t}Z" 
   # TZQ.color           = ROOT.kRed - 9
    dim6top_TTW.color = ROOT.kRed

    for sample in mc: sample.style = styles.fillStyle(sample.color)
    
    for sample in mc:
      sample.scale          = lumi_scale
      #if args.WZpowheg and sample in [WZ_powheg]:
      #  sample.scale          = lumi_scale * 4.666/4.42965 # get same x-sec as amc@NLO
      #sample.read_variables = ['reweightTopPt/F','reweightDilepTriggerBackup/F','reweightLeptonSF/F','reweightBTag_SF/F','reweightPU36fb/F', 'nTrueInt/F', 'reweightLeptonTrackingSF/F']
      #sample.weight         = lambda event, sample: event.reweightTopPt*event.reweightBTag_SF*event.reweightLeptonSF*event.reweightDilepTriggerBackup*event.reweightPU36fb*event.reweightLeptonTrackingSF

      # dilep reweight?
      sample.read_variables = ['reweightBTagCSVv2_SF/F', 'reweightBTagDeepCSV_SF/F', 'reweightPU36fb/F', 'reweightLeptonSFSyst_tight_3l/F', 'reweightLeptonTrackingSF_tight_3l/F', 'reweightTrigger_tight_3l/F', "Z_pt/F"]
      sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightPU36fb*event.reweightLeptonSFSyst_tight_3l*event.reweightLeptonTrackingSF_tight_3l*event.reweightTrigger_tight_3l
      tr = triggerSelector(2016)
      sample.setSelectionString([getFilterCut(isData=False), getLeptonSelection(mode), tr.getSelection("MC")])

    if not args.noData:
      stack = Stack(mc, data_sample)
    else:
      stack = Stack(mc)

    if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 1 )

    # Use some defaults
    Plot.setDefaults(stack = stack, weight = staticmethod(weight_), selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper')

    plots = []

    plots.append(Plot(
      name = 'yield', texX = 'yield', texY = 'Number of Events',
      attribute = lambda event, sample: 0.5 + index,
      binning=[4, 0, 4],
    ))

    plots.append(Plot(
      name = 'flavor', texX = '', texY = 'Number of Events',
      attribute = lambda event, sample: 0.5 + event.flavor_bin,
      binning=[6, 0, 6],
    ))

    for mva in mvas:
        plots.append(Plot(
            texX = 'nonprompt_'+mva['name'], texY = 'Number of Events',
            name = 'nonprompt_'+mva['name'], attribute = discriminator_getter('nonprompt_'+mva['name']),
            binning=[25, 0, 1],
        ))

    for mva in mvas:
        plots.append(Plot(
            texX = 'nonprompt_'+mva['name']+'_coarse', texY = 'Number of Events',
            name = 'nonprompt_'+mva['name']+'_coarse', attribute = discriminator_getter('nonprompt_'+mva['name']),
            #binning=[10, 0, 1],
            binning=Binning.fromThresholds([0, 0.2, 0.4, 0.6, 1.0]),
        ))

    plots.append(Plot(
        texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 30 GeV',
        attribute = TreeVariable.fromString( "met_pt/F" ),
        binning=[300/30,0,300]
    ))

    plots.append(Plot(
        texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_phi/F" ),
        binning=[10,-pi,pi],
    ))

    plots.append(Plot(
        texX = 'H_{T} (GeV)', texY = 'Number of Events / 50 GeV',
        attribute = TreeVariable.fromString( "ht/F" ),
        binning=[1000/50,0,1000],
    ))

    plots.append(Plot(
      texX = 'N_{jets}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nJetSelected/I" ), #nJetSelected
      binning=[8,-0.5,7.5],
    ))

    plots.append(Plot(
      texX = 'N_{b-tag}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nBTag/I" ), #nJetSelected
      binning=[4,-0.5,3.5],
    ))

    plots.append(Plot(
      texX = 'N_{l, loose}', texY = 'Number of Events',
      name = 'nLepLoose', attribute = lambda event, sample: event.nLepLoose,
      binning=[5,0.5,5.5],
    ))

#    def set_ndiv(h):
#        h.GetXaxis().SetNdivisions(2)
#        h.GetXaxis().SetBinLabel( 1, "N_{lep}=1")
#        h.GetXaxis().SetBinLabel( 2, "N_{lep}=2")
#        h.GetXaxis().SetBinLabel( 3, "N_{lep}=3")

#    plots.append(Plot(
#      texX = '', texY = 'Number of Events',
#      name = 'nLepLoose_1To3', attribute = lambda event, sample: event.nLepLoose,
#      binning=[3,1,4],
#    ))
#    plots[-1].histModifications = [set_ndiv]

    plots.append(Plot(
      texX = 'p_{T}(leading l) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'lep1_pt', attribute = lambda event, sample: event.lep_pt[0],
      binning=[400/20,0,400],
    ))

    plots.append(Plot(
      texX = 'pdgId(leading l) (GeV)', texY = 'Number of Events',
      name = 'lep1_pdgId', attribute = lambda event, sample: event.lep_pdgId[0],
      binning=[30,-15,15],
    ))

    plots.append(Plot(
      texX = 'p_{T}(subleading l) (GeV)', texY = 'Number of Events / 10 GeV',
      name = 'lep2_pt', attribute = lambda event, sample: event.lep_pt[1],
      binning=[120/10,0,120],
    ))

    plots.append(Plot(
      texX = 'pdgId(subleading l) (GeV)', texY = 'Number of Events',
      name = 'lep2_pdgId', attribute = lambda event, sample: event.lep_pdgId[1],
      binning=[30,-15,15],
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
      if plot.name == "flavor":
        for i, l in enumerate(plot.histos):
          for j, h in enumerate(l):
            h.GetXaxis().SetBinLabel(1, "#mu^{#plus} #mu^{#plus}")
            h.GetXaxis().SetBinLabel(2, "#mu^{#plus} e^{#plus}")
            h.GetXaxis().SetBinLabel(3, "e^{#plus} e^{#plus}")
            h.GetXaxis().SetBinLabel(4, "#mu^{#minus} #mu^{#minus}")
            h.GetXaxis().SetBinLabel(5, "#mu^{#minus} e^{#minus}")
            h.GetXaxis().SetBinLabel(6, "e^{#minus} e^{#minus}")
    if args.noData: yields[mode]["data"] = 0

    yields[mode]["MC"] = sum(yields[mode][s.name] for s in mc)
    dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    drawPlots(plots, mode, dataMCScale)
    allPlots[mode] = plots

# Add the different channels into SF and all
for mode in ["comb1","all"]:
    yields[mode] = {}
    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in ['ee','mue','mumu'])
        except: yields[mode][y] = 0
    dataMCScale = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
    
    for plot in allPlots['mumu']:
        if mode=="comb1":
            tmp = allPlots['mue']
        else:
            tmp = allPlots['ee']
        for plot2 in (p for p in tmp if p.name == plot.name):
            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
                    if i==k:
                        j.Add(l)
    
    if mode == "all": drawPlots(allPlots['mumu'], mode, dataMCScale)

logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )

