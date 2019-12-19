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

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--noData',             action='store_true', default=False,           help='also plot data?')
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--plot_directory',     action='store',      default='analysisPlots_3l_2016')
argParser.add_argument('--selection',          action='store',      default='trilep-Zcand-lepSelTTZ-min_mll12-njet1p-btag0-onZ')
argParser.add_argument('--normalize',           action='store_true', default=False,             help="Normalize yields" )
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
if args.noData:                       args.plot_directory += "_noData"
if args.WZpowheg:                     args.plot_directory += "_WZpowheg"
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
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
      (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
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
	    logX = False, logY = log, sorting = False, #True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = scaling if args.normalize else {},
	    legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
	    drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale ) if not args.normalize else drawObjects( not args.noData, 1.0 , lumi_scale ),
        copyIndexPHP = True,
      )

# define 3l selections
def getLeptonSelection( mode ):
    if   mode=="mumumu": return "nMuons_tight_3l==3&&nElectrons_tight_3l==0"
    elif mode=="mumue":  return "nMuons_tight_3l==2&&nElectrons_tight_3l==1"
    elif mode=="muee":   return "nMuons_tight_3l==1&&nElectrons_tight_3l==2"
    elif mode=="eee":    return "nMuons_tight_3l==0&&nElectrons_tight_3l==3"
    elif mode=='all':    return "nMuons_tight_3l+nElectrons_tight_3l==3"

# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I]", "njet/I","nJetSelected/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I", 
                    "Z_phi/F","Z_pt/F", "Z_mass/F", "Z_eta/F","Z_lldPhi/F", "Z_lldR/F"
                    ]
sequence = []

def getDPhiZLep( event, sample ):
    event.dPhiZLep = deltaPhi(event.lep_phi[event.nonZ_l1_index], event.Z_phi)

def getDPhiZJet( event, sample ):
    event.dPhiZJet = deltaPhi(event.jet_phi[0], event.Z_phi) if event.njet>0 and event.Z_mass>0 else float('nan') #nJetSelected

sequence += [ getDPhiZLep, getDPhiZJet] #,getJets ]

def getSelectedJets( event, sample ):
    jetVars     = ['eta','pt','phi','btagCSV','DFbb', 'DFb', 'id']
    event.selectedJets  = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'njet'))) if ( abs(event.jet_eta[i])<=2.4 and event.jet_pt[i] > 30 and event.jet_id[i])] #nJetSelected
sequence += [ getSelectedJets ]

#def getJets( event, sample ):
#    jetVars     = ['eta','pt','phi','btagCSV']
#    event.jets_sortbtag  = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'nJetSelected')))] #nJetSelected
#    event.jets_sortbtag.sort( key = lambda l:-l['btagCSV'] )
#
#def getAllJets( event, sample ):
#    jetVars     = ['eta','pt','btagCSV']
#    event.allJets = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'njet')))]
#
#def getForwardJets( event, sample ):
#    event.nJetForward30  = len([j for j in event.allJets if (j['pt']>30 and abs(j['eta'])>2.4) ])
#    event.nJetForward40  = len([j for j in event.allJets if (j['pt']>40 and abs(j['eta'])>2.4) ])
#    event.nJetForward50  = len([j for j in event.allJets if (j['pt']>50 and abs(j['eta'])>2.4) ])
#    event.nJetForward60  = len([j for j in event.allJets if (j['pt']>60 and abs(j['eta'])>2.4) ])
#    event.nJetForward70  = len([j for j in event.allJets if (j['pt']>70 and abs(j['eta'])>2.4) ])
#
#def getForwardJets_eta3( event, sample ):
#    event.nJetForward30_eta3  = len([j for j in event.allJets if (j['pt']>30 and abs(j['eta'])>3.0) ])
#    event.nJetForward40_eta3  = len([j for j in event.allJets if (j['pt']>40 and abs(j['eta'])>3.0) ])
#    event.nJetForward50_eta3  = len([j for j in event.allJets if (j['pt']>50 and abs(j['eta'])>3.0) ])
#    event.nJetForward60_eta3  = len([j for j in event.allJets if (j['pt']>60 and abs(j['eta'])>3.0) ])
#    event.nJetForward70_eta3  = len([j for j in event.allJets if (j['pt']>70 and abs(j['eta'])>3.0) ])
#
#def getForwardJetEta( event, sample ):
#    event.forwardJets = [j for j in event.allJets if j['btagCSV']<0.8484 ]
#    event.forwardJet1_eta = -999
#    event.forwardJet1_pt  = -999
#    event.forwardJet2_eta = -999
#    event.forwardJet2_pt  = -999
#    if len(event.forwardJets) > 0:
#        event.forwardJet1_eta = abs(event.forwardJets[0]['eta'])
#        event.forwardJet1_pt  = event.forwardJets[0]['pt']
#    
#        if len(event.forwardJets) > 1:
#            event.forwardJet2_eta = abs(event.forwardJets[1]['eta'])
#            event.forwardJet2_pt  = event.forwardJets[1]['pt']

#sequence += [ getAllJets, getForwardJets, getForwardJets_eta3, getForwardJetEta]

MW = 80.385
Mt = 172.5

#def getCPVars( event, sample ):
#    lepton  = ROOT.TVector3()
#    bjets = []
#    nonbjets = []
#    maxBJets = 2
#    bjetCounter = 0
#    mt_had = 0
#    mw_had = 0
#    
#    # get the bjet and non-bjet collection
#    for j in event.selectedJets:
#        jet = ROOT.TLorentzVector()
#        jet.SetPtEtaPhiM(j['pt'], j['eta'], j['phi'], 0)
#
#        # get the 2 hardest b jets
#        if j['btagCSV'] > 0.8484 and bjetCounter < 2:
#            bjetCounter += 1
#            bjets.append(jet)
#        else:
#            nonbjets.append(jet)
#
#    # do a chi2 minimization to get the hadronic and leptonic top quarks. mjj and mbjj are not independent - is this still valid?
#    chi2min = float('Inf')
#
#    jetcombinations = [ x for x in itertools.combinations(range(len(nonbjets)),2) ]
#    for i, b in enumerate(bjets):
#        for j, jetComb in enumerate(itertools.combinations(nonbjets,2)):
#            mbjj = ( b + jetComb[0] + jetComb[1] ).M()
#            mjj  = ( jetComb[0] + jetComb[1] ).M()
#            x = (mjj - MW)**2/MW + (mbjj - Mt)**2/Mt
#            if x < chi2min:
#                chi2min = x
#                hadTopJetIndices = (i, jetcombinations[j][0], jetcombinations[j][1])
#                leptonicTopJetIndex = 1 - i
#                mt_had = mbjj
#                mw_had = mjj
#
#    # asign the b quarks accordingly
#    leptonCharge = -event.lep_pdgId[event.nonZ_l1_index]/abs(event.lep_pdgId[event.nonZ_l1_index])
#    if leptonCharge > 0:
#        b       = bjets[leptonicTopJetIndex]
#        bbar    = bjets[hadTopJetIndices[0]]
#    else:
#        b       = bjets[hadTopJetIndices[0]]
#        bbar    = bjets[leptonicTopJetIndex]
#
#    # also get the highest pt jet from the hadronic W, as well as the lepton and met
#    jet         = nonbjets[hadTopJetIndices[1]]
#    lepton      = ROOT.TLorentzVector()
#    met         = ROOT.TLorentzVector()
#    lepton.SetPtEtaPhiM( event.lep_pt[event.nonZ_l1_index], event.lep_eta[event.nonZ_l1_index], event.lep_phi[event.nonZ_l1_index], 0)
#    met.SetPtEtaPhiM( event.met_pt, 0, event.met_phi, 0)
#    
#    event.mt_had = mt_had
#    event.mw_had = mw_had
#    event.mt_lep = (lepton + met + bjets[leptonicTopJetIndex]).M()
#    event.mw_lep = (lepton + met).M()
#    event.chi2min = chi2min
#    
#    # calculate the observables listed in arxiv:1611.08931
#    b3      = ROOT.TVector3(b.X(), b.Y(), b.Z())
#    bbar3   = ROOT.TVector3(bbar.X(), bbar.Y(), bbar.Z())
#    jet3    = ROOT.TVector3(jet.X(), jet.Y(), jet.Z())
#    lepton3 = ROOT.TVector3(lepton.X(), lepton.Y(), lepton.Z())
#
#    O2 = (b3 + bbar3) * (lepton3.Cross(jet3))
#
#    O4 = (b3 - bbar3) * (lepton3.Cross(jet3))
#    O4 = O4*leptonCharge
#        
#    O7 = (b3 -bbar3).Z() * (b3.Cross(bbar3)).Z()
#    
#    event.O2 = int(O2/abs(O2))
#    event.O4 = int(O4/abs(O4))
#    event.O7 = int(O7/abs(O7))
#    
#    # to get O3, we need to boost in the b-bbar system
#    bbbarsystem = (b + bbar).BoostVector()
#    lepton.Boost(-bbbarsystem)
#    b.Boost(-bbbarsystem)
#    jet.Boost(-bbbarsystem)
#    
#    b3      = ROOT.TVector3(b.X(), b.Y(), b.Z())
#    jet3    = ROOT.TVector3(jet.X(), jet.Y(), jet.Z())
#    lepton3 = ROOT.TVector3(lepton.X(), lepton.Y(), lepton.Z())
#    
#    O3 = b3 * (lepton3.Cross(jet3))
#    O3 = O3*leptonCharge
#    
#    event.O3 = int(O3/abs(O3))
#    
#    #print event.O2, event.O3, event.O4, event.O7

#sequence += [ getCPVars ]

def getL( event, sample):

    # get the lepton and met
    lepton  = ROOT.TLorentzVector()
    met     = ROOT.TLorentzVector()
    lepton.SetPtEtaPhiM(event.lep_pt[event.nonZ_l1_index], event.lep_eta[event.nonZ_l1_index], event.lep_phi[event.nonZ_l1_index], 0)
    met.SetPtEtaPhiM(event.met_pt, 0, event.met_phi, 0)

    # get the W boson candidate
    W   = lepton + met
    
    # calculate Lp
    event.Lp = ( W.Px()*lepton.Px() + W.Py()*lepton.Py() ) / (W.Px()**2 + W.Py()**2 )

    event.deltaPhi_Wl = acos( ( W.Px()*lepton.Px() + W.Py()*lepton.Py() ) / sqrt( (W.Px()**2 + W.Py()**2 ) * ( lepton.Px()**2 + lepton.Py()**2 ) ) )

sequence.append( getL )

def getCosThetaStar( event, sample ):
    # get the negative-charge lepton from Z
    lm_index = event.Z_l1_index if event.lep_pdgId[event.Z_l1_index] > 0 else event.Z_l2_index
    
    # get the Z and lepton vectors
    Z   = ROOT.TVector3()
    l   = ROOT.TVector3()

    # set the values
    Z.SetPtEtaPhi(event.Z_pt,               event.Z_eta,                event.Z_phi)
    l.SetPtEtaPhi(event.lep_pt[lm_index],   event.lep_eta[lm_index],    event.lep_phi[lm_index])

    # get cos(theta)
    cosTheta = Z*l / (sqrt(Z*Z) * sqrt(l*l))
    
    # get beta and gamma
    gamma   = sqrt(1+event.Z_pt**2/event.Z_mass**2 * cosh(event.Z_eta)**2 )
    beta    = sqrt( 1 - 1/gamma**2 )
    
    cosThetaStar = (-beta + cosTheta) / (1 - beta*cosTheta)
    event.cosThetaStar = cosThetaStar

sequence.append( getCosThetaStar )

def getM3l( event, sample ):
    # get the invariant mass of the 3l system
    l = []
    for i in range(3):
        l.append(ROOT.TLorentzVector())
        l[i].SetPtEtaPhiM(event.lep_pt[i], event.lep_eta[i], event.lep_phi[i],0)
    event.threelmass = (l[0] + l[1] + l[2]).M()

sequence.append( getM3l )

def getWpt( event, sample):

    # get the lepton and met
    lepton  = ROOT.TLorentzVector()
    met     = ROOT.TLorentzVector()
    lepton.SetPtEtaPhiM(event.lep_pt[event.nonZ_l1_index], event.lep_eta[event.nonZ_l1_index], event.lep_phi[event.nonZ_l1_index], 0)
    met.SetPtEtaPhiM(event.met_pt, 0, event.met_phi, 0)

    # get the W boson candidate
    W   = lepton + met
    event.W_pt = W.Pt()

sequence.append( getWpt )

def getLooseLeptonMult( event, sample ):
    leptons = [getObjDict(event, 'lep_', ['eta','pt','phi','charge', 'pdgId', 'sourceId','mediumMuonId'], i) for i in range(len(event.lep_pt))]
    lepLoose = [ l for l in leptons if l['pt'] > 10 and ((l['mediumMuonId'] and abs(l['pdgId'])==13) or abs(l['pdgId'])==11)  ]
    event.nLepLoose = len(lepLoose)

sequence.append( getLooseLeptonMult )

#MVA
from Analysis.TMVA.Reader   import Reader
from TopEFT.MVA.MVA_TWZ     import mva_variables, bdt1, bdt2, mlp1, mlp2, mlp3
from TopEFT.MVA.MVA_TWZ     import sequence as mva_sequence
from TopEFT.MVA.MVA_TWZ     import read_variables as mva_read_variables
from TopEFT.Tools.user      import mva_directory

sequence.extend( mva_sequence )
read_variables.extend( mva_read_variables )

#reader = Reader(
#    mva_variables    = mva_variables,
#    weight_directory = "/afs/hephy.at/work/t/ttschida/public/CMSSW_9_4_6_patch1/src/TopEFT/MVA/python/weights/",
#    label            = "Test")

reader_TTZ = Reader(
    mva_variables     = mva_variables,
    weight_directory  = "/afs/hephy.at/work/t/ttschida/public/CMSSW_9_4_6_patch1/src/TopEFT/MVA/python/weights/TTZ/",
    label             = "Test")

reader_WZ  = Reader(
    mva_variables     = mva_variables,
    weight_directory  = "/afs/hephy.at/work/t/ttschida/public/CMSSW_9_4_6_patch1/src/TopEFT/MVA/python/weights/WZ/",
    label             = "Test")

def makeDiscriminator( mva ):
    def _getDiscriminator( event, sample ):
        kwargs = {name:func(event,None) for name, func in mva_variables.iteritems()}
#        setattr( event, mva['name'], reader.evaluate(mva['name'], **kwargs))
        setattr( event, "TTZ_"+mva['name'], reader_TTZ.evaluate(mva['name'], **kwargs))
        setattr( event, "WZ_"+mva['name'], reader_WZ.evaluate(mva['name'], **kwargs))
        #print mva['name'], getattr( event, mva['name'] )
    return _getDiscriminator

def discriminator_getter(name):
    def _disc_getter( event, sample ):
        return getattr( event, name )
    return _disc_getter
    
mvas = [ bdt1, bdt2, mlp1, mlp2, mlp3 ]
for mva in mvas:
#    reader.addMethod(method=mva)
    reader_TTZ.addMethod(method=mva)
    reader_WZ.addMethod(method=mva)
    sequence.append( makeDiscriminator(mva) )

#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['mumumu','mumue','muee', 'eee']
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

    if args.noData: lumi_scale = 35.9
    lumi_scale = 300
    weight_ = lambda event, sample: event.weight

    TTZ_mc = TTZtoLLNuNu

    if args.WZpowheg:
        mc             = [ TWZ, TTZ_mc , TTX, WZ_powheg, rare, ZZ, nonpromptMC, Xgamma ]
    else:
        #mc             = [ TWZ, TTZ_mc , TTX, WZ_amcatnlo, rare, ZZ, nonpromptMC, Xgamma ]
        mc             = [ yt_TWZ_filter, TTZ_mc, TTX_rare_TWZ, TZQ, WZ_amcatnlo, rare, ZZ, nonpromptMC ]#, Xgamma ]
    for sample in mc: sample.style = styles.fillStyle(sample.color)

    for sample in mc:
      sample.scale          = lumi_scale
      #if args.WZpowheg and sample in [WZ_powheg]:
      #  sample.scale          = lumi_scale * 4.666/4.42965 # get same x-sec as amc@NLO
      #sample.read_variables = ['reweightTopPt/F','reweightDilepTriggerBackup/F','reweightLeptonSF/F','reweightBTag_SF/F','reweightPU36fb/F', 'nTrueInt/F', 'reweightLeptonTrackingSF/F']
      #sample.weight         = lambda event, sample: event.reweightTopPt*event.reweightBTag_SF*event.reweightLeptonSF*event.reweightDilepTriggerBackup*event.reweightPU36fb*event.reweightLeptonTrackingSF
      sample.read_variables = ['reweightBTagCSVv2_SF/F', 'reweightBTagDeepCSV_SF/F', 'reweightPU36fb/F', 'reweightLeptonSFSyst_tight_3l/F', 'reweightLeptonTrackingSF_tight_3l/F', 'reweightTrigger_tight_3l/F', "Z_pt/F"]
      sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightPU36fb*event.reweightLeptonSFSyst_tight_3l*event.reweightLeptonTrackingSF_tight_3l*event.reweightTrigger_tight_3l
      tr = triggerSelector(2016)
      sample.setSelectionString([getFilterCut(isData=False), getLeptonSelection(mode), tr.getSelection("MC")])

    yt_TWZ_filter.scale = lumi_scale * 1.07314

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

#    for mva in mvas:
#        plots.append(Plot(
#            texX = mva['name'], texY = 'Number of Events',
#            name = mva['name'], attribute = discriminator_getter(mva['name']),
#            binning=[25, 0, 1],
#        ))

#    for mva in mvas:
#        plots.append(Plot(
#            texX = mva['name']+"_coarse", texY = 'Number of Events',
#            name = mva['name'], attribute = discriminator_getter(mva['name']),
#            binning=[10, 0, 1],
#        ))

    for mva in mvas:
        plots.append(Plot(
            texX = 'TTZ_'+mva['name'], texY = 'Number of Events',
            name = 'TTZ_'+mva['name'], attribute = discriminator_getter('TTZ_'+mva['name']),
            binning=[25, 0, 1],
        ))

    for mva in mvas:
        plots.append(Plot(
            texX = 'TTZ_'+mva['name']+'_coarse', texY = 'Number of Events',
            name = 'TTZ_'+mva['name']+'_coarse', attribute = discriminator_getter('TTZ_'+mva['name']),
            binning=[10, 0, 1],
        ))

    for mva in mvas:
        plots.append(Plot(
            texX = 'WZ_'+mva['name'], texY = 'Number of Events',
            name = 'WZ_'+mva['name'], attribute = discriminator_getter('WZ_'+mva['name']),
            binning=[25, 0, 1],
        ))

    for mva in mvas:
        plots.append(Plot(
            texX = 'WZ_'+mva['name']+'_coarse', texY = 'Number of Events',
            name = 'WZ_'+mva['name']+'_coarse', attribute = discriminator_getter('WZ_'+mva['name']),
            binning=[10, 0, 1],
        ))


    plots.append(Plot(
        texX = 'TTZ mlp2 WZ bdt1', texY = 'Number of Events',
        name = 'TTZ_mlp2_WZ_bdt1', attribute = lambda event, sample: event.TTZ_mlp2 if event.WZ_bdt1 > 0.8 else -1,
        binning=[25, 0, 1],
    ))

    plots.append(Plot(
        texX = 'TTZ mlp2 WZ bdt1_coarse', texY = 'Number of Events',
        name = 'TTZ_mlp2_WZ_bdt1_coarse', attribute = lambda event, sample: event.TTZ_mlp2 if event.WZ_bdt1 > 0.8 else -1,
        binning=[10, 0, 1],
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
        binning=[20,0,400],
    ))
    
    plots.append(Plot(
        name = "W_pt",
        texX = 'p_{T}(W) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.W_pt,
        binning=[20,0,400],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_coarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 50 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[16,0,800],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_superCoarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[3,0,600],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_analysis', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 100 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[4,0,400],
    ))
    
    plots.append(Plot(
        name = "invM_3l",
        texX = 'M(3l) (GeV)', texY = 'Number of Events',
        attribute = lambda event, sample:event.threelmass,
        binning=[25,0,500],
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
    
    #plots.append(Plot(
    #    name = "O2_sign",
    #    texX = 'O2/|O2|', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.O2,
    #    binning=[2,-2,2],
    #))

    #plots.append(Plot(
    #    name = "O3_sign",
    #    texX = 'O3/|O3|', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.O3,
    #    binning=[2,-2,2],
    #))

    #plots.append(Plot(
    #    name = "O4_sign",
    #    texX = 'O4/|O4|', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.O4,
    #    binning=[2,-2,2],
    #))

    #plots.append(Plot(
    #    name = "O7_sign",
    #    texX = 'O7/|O7|', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.O7,
    #    binning=[2,-2,2],
    #))
    #
    #plots.append(Plot(
    #    name = "mt_had",
    #    texX = 'M(had. top)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.mt_had,
    #    binning=[20,0,300],
    #))
    #
    #plots.append(Plot(
    #    name = "mt_lep",
    #    texX = 'M(lep. top)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.mt_lep,
    #    binning=[20,0,300],
    #))

    #plots.append(Plot(
    #    name = "mw_had",
    #    texX = 'M(had. W)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.mw_had,
    #    binning=[20,0,200],
    #))

    #plots.append(Plot(
    #    name = "mw_lep",
    #    texX = 'M(lep. W)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.mw_lep,
    #    binning=[20,0,200],
    #))
    #
    #plots.append(Plot(
    #    name = "chi2min",
    #    texX = 'min(#chi^2)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.chi2min,
    #    binning=[20,0,200],
    #))

    
    #plots.append(Plot(
    #    name = "nForwardJet_Pt30_eta3",
    #    texX = 'nJet p_{T}(j)>30 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward30_eta3,
    #    binning=[10,0,10],
    #))
    #
    #plots.append(Plot(
    #    name = "nForwardJet_Pt40_eta3",
    #    texX = 'nJet p_{T}(j)>40 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward40_eta3,
    #    binning=[10,0,10],
    #))

    #plots.append(Plot(
    #    name = "nForwardJet_Pt50_eta3",
    #    texX = 'nJet p_{T}(j)>50 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward50_eta3,
    #    binning=[10,0,10],
    #))

    #plots.append(Plot(
    #    name = "nForwardJet_Pt60_eta3",
    #    texX = 'nJet p_{T}(j)>60 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward60_eta3,
    #    binning=[10,0,10],
    #))

    #plots.append(Plot(
    #    name = "nForwardJet_Pt70_eta3",
    #    texX = 'nJet p_{T}(j)>70 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward70_eta3,
    #    binning=[10,0,10],
    #))
    
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
        name = "lZ1_pt_coarse",
        texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 40 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning=[10,0,400],
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
        binning=[20,0,200],
    ))
    
    plots.append(Plot(
        name = "lZ2_pt_coarse",
        texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning=[10,0,200],
    ))
    
    plots.append(Plot(
        name = 'lZ2_pt_ext', texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning=[20,0,400],
    ))
    
    plots.append(Plot(
        name = 'lnonZ1_pt',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[15,0,300],
    ))

    plots.append(Plot(
        name = 'lnonZ1_pt_coarse',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 60 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[3,0,180],
    ))

    plots.append(Plot(
        name = 'lnonZ1_pt_ext',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 30 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[6,0,180],
    ))

    plots.append(Plot(
        name = 'lnonZ1_charge',
        texX = 'Charge(l_{1,extra})', texY = 'Number of Events',
        attribute = lambda event, sample:-event.lep_pdgId[event.nonZ_l1_index]/abs(event.lep_pdgId[event.nonZ_l1_index]),
        binning=[2,-1,1],
    ))

    plots.append(Plot(
        name = 'lnonZ1_eta',
        texX = '#eta(l_{1,extra})', texY = 'Number of Events',
        attribute = lambda event, sample: event.lep_eta[event.nonZ_l1_index],
        binning=[20,-3,3],
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
      binning=[5,2.5,7.5],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(leading l) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'lep1_pt', attribute = lambda event, sample: event.lep_pt[0],
      binning=[400/20,0,400],
    ))

    plots.append(Plot(
      texX = 'p_{T}(subleading l) (GeV)', texY = 'Number of Events / 10 GeV',
      name = 'lep2_pt', attribute = lambda event, sample: event.lep_pt[1],
      binning=[200/10,0,200],
    ))

    plots.append(Plot(
      texX = 'p_{T}(trailing l) (GeV)', texY = 'Number of Events / 10 GeV',
      name = 'lep3_pt', attribute = lambda event, sample: event.lep_pt[2],
      binning=[150/10,0,150],
    ))
    
    #plots.append(Plot(
    #  texX = 'p_{T}(Z l+) (GeV)', texY = 'Number of Events / 10 GeV',
    #  name = 'lZp_pt', attribute = lambda event, sample: event.lZp_pt,
    #  binning=[20,0,200],
    #))
    #
    #plots.append(Plot(
    #  texX = 'p_{T}(Z l-) (GeV)', texY = 'Number of Events / 10 GeV',
    #  name = 'lZm_pt', attribute = lambda event, sample: event.lZm_pt,
    #  binning=[20,0,200],
    #))
    
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

    ##if len(event.forwardJets)>0:
    #plots.append(Plot(
    #  texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 10 GeV',
    #  name = 'forwardJet1_pt', attribute = lambda event, sample: event.forwardJet1_pt,
    #  binning=[30,0,300],
    #))

    #plots.append(Plot(
    #  texX = '#eta(leading jet) (GeV)', texY = 'Number of Events',
    #  name = 'forwardJet1_eta', attribute = lambda event, sample: event.forwardJet1_eta,
    #  binning=[20,0.,5.],
    #))
    #
    ##if len(event.forwardJets)>1:
    #plots.append(Plot(
    #  texX = 'p_{T}(sub-leading jet) (GeV)', texY = 'Number of Events / 10 GeV',
    #  name = 'forwardJet2_pt', attribute = lambda event, sample: event.forwardJet2_pt,
    #  binning=[30,0,300],
    #))

    #plots.append(Plot(
    #  texX = '#eta(sub-leading jet) (GeV)', texY = 'Number of Events',
    #  name = 'forwardJet2_eta', attribute = lambda event, sample: event.forwardJet2_eta,
    #  binning=[20,0.,5.],
    #))


    #plots.append(Plot(
    #  texX = 'p_{T}(leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
    #  name = 'bjet1_pt', attribute = lambda event, sample: event.b1_pt,
    #  binning=[20,0,400],
    #))

    #plots.append(Plot(
    #  texX = 'p_{T}(2nd leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
    #  name = 'bjet2_pt', attribute = lambda event, sample: event.b2_pt,
    #  binning=[20,0,400],
    #))
    #
    #plots.append(Plot(
    #    name = "top_cand1_pt", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 30 GeV',
    #    attribute = lambda event, sample:event.top1_pt,
    #    binning=[20,0,600],
    #))

    #plots.append(Plot(
    #    name = "top_cand1_pt_coarse", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 200 GeV',
    #    attribute = lambda event, sample:event.top1_pt,
    #    binning=[3,0,600],
    #))
    #
    #plots.append(Plot(
    #    name = "top_cand1_pt_2bin", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 200 GeV',
    #    attribute = lambda event, sample:event.top1_pt,
    #    binning=[2,0,400],
    #))

    #plots.append(Plot(
    #    name = "top_cand1_mass", texX = 'M(t cand1) (GeV)', texY = 'Number of Events / 15 GeV',
    #    attribute = lambda event, sample:event.top1_mass,
    #    binning=[20,0,300],
    #))

    #plots.append(Plot(
    #    name = "top_cand1_phi", texX = '#phi(t cand1)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.top1_phi,
    #    binning=[10,-pi,pi],
    #))

    #plots.append(Plot(
    #    name = "top_cand2_pt", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 30 GeV',
    #    attribute = lambda event, sample:event.top2_pt,
    #    binning=[20,0,600],
    #))
    #
    #plots.append(Plot(
    #    name = "top_cand2_pt_coarse", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 200 GeV',
    #    attribute = lambda event, sample:event.top2_pt,
    #    binning=[3,0,600],
    #))

    #plots.append(Plot(
    #    name = "top_cand2_mass", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 15 GeV',
    #    attribute = lambda event, sample:event.top2_mass,
    #    binning=[20,0,300],
    #))

    #plots.append(Plot(
    #    name = "top_cand2_phi", texX = '#phi(t cand1)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.top2_phi,
    #    binning=[10,-pi,pi],
    #))

    #plots.append(Plot(
    #    name = "mt_1", texX = 'M_{T}(var 1) (GeV)', texY = 'Number of Events / 20 GeV',
    #    attribute = lambda event, sample:event.mt_1,
    #    binning=[20,50,450],
    #))

    #plots.append(Plot(
    #    name = "mt_1_coarse", texX = 'M_{T}(var 1) (GeV)', texY = 'Number of Events / 100 GeV',
    #    attribute = lambda event, sample:event.mt_1,
    #    binning=[5,50,550],
    #))

    #plots.append(Plot(
    #    name = "mt_2", texX = 'M_{T}(var 2) (GeV)', texY = 'Number of Events / 20 GeV',
    #    attribute = lambda event, sample:event.mt_2,
    #    binning=[20,50,450],
    #))

    #plots.append(Plot(
    #    name = "mt_2_coarse", texX = 'M_{T}(var 2) (GeV)', texY = 'Number of Events / 100 GeV',
    #    attribute = lambda event, sample:event.mt_2,
    #    binning=[5,50,550],
    #))

    #plots.append(Plot(
    #    name = "minMLepB", texX = 'min M(l, b-jet) (GeV)', texY = 'Number of Events / 10 GeV',
    #    attribute = lambda event, sample:event.minMLepB,
    #    binning=[15,0,300],
    #))
    
    #plots.append(Plot(
    #    name = "LP_superCoarse", texX = 'L_{P}', texY = 'Number of Events / 0.6',
    #    attribute = lambda event, sample:event.Lp,
    #    binning=[3,-0.6,1.2],
    #))
    
    plots.append(Plot(
        name = "LP_coarse", texX = 'L_{P}', texY = 'Number of Events / 0.2',
        attribute = lambda event, sample:event.Lp,
        binning=[10,-1,1],
    ))
    
    plots.append(Plot(
        name = "LP", texX = 'L_{P}', texY = 'Number of Events / 0.1',
        attribute = lambda event, sample:event.Lp,
        binning=[20,-1,1],
    ))
    
    plots.append(Plot(
        name = "LP_wide", texX = 'L_{P}', texY = 'Number of Events / 0.2',
        attribute = lambda event, sample:event.Lp,
        binning=[25,-2,3],
    ))

    #plots.append(Plot(
    #    name = "deltaPhi_Wl", texX = '#Delta#phi_{W,l}', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.deltaPhi_Wl,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "deltaPhi_Wl_coarse", texX = '#Delta#phi_{W,l}', texY = 'Number of Events / 0.8',
    #    attribute = lambda event, sample:event.deltaPhi_Wl,
    #    binning=[4,0,3.2],
    #))
    #
    #plots.append(Plot(
    #    name = "deltaPhi_tl", texX = '#Delta#phi_{t,l}', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.deltaPhi_tl,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "deltaPhi_tl_coarse", texX = '#Delta#phi_{t,l}', texY = 'Number of Events / 0.8',
    #    attribute = lambda event, sample:event.deltaPhi_tl,
    #    binning=[4,0,3.2],
    #))
    
    #plots.append(Plot(
    #    name = "deltaPhi_tl_topRF", texX = '#Delta#phi_{t,l} in t RF', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.deltaPhi_tl_topRF,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "deltaPhi_tl_topRF_coarse", texX = '#Delta#phi_{t,l} in t RF', texY = 'Number of Events / 0.8',
    #    attribute = lambda event, sample:event.deltaPhi_tl_topRF,
    #    binning=[4,0,3.2],
    #))
    #
    #plots.append(Plot(
    #    name = "deltaR_tl_topRF", texX = '#DeltaR_{t,l} in t RF', texY = 'Number of Events / 0.4',
    #    attribute = lambda event, sample:event.deltaR_tl_topRF,
    #    binning=[10,0,4],
    #))

    #plots.append(Plot(
    #    name = "deltaR_tl_topRF_coarse", texX = '#DeltaR_{t,l} in t RF', texY = 'Number of Events / 1.',
    #    attribute = lambda event, sample:event.deltaR_tl_topRF,
    #    binning=[4,0,4],
    #))

    #plots.append(Plot(
    #    name = "deltaEta_tl_topRF", texX = '#Delta#eta_{t,l} in t RF', texY = 'Number of Events / 0.4',
    #    attribute = lambda event, sample:event.deltaEta_tl_topRF,
    #    binning=[10,0,4],
    #))

    #plots.append(Plot(
    #    name = "deltaEta_tl_topRF_coarse", texX = '#Delta#eta_{t,l} in t RF', texY = 'Number of Events / 1.',
    #    attribute = lambda event, sample:event.deltaEta_tl_topRF,
    #    binning=[4,0,4],
    #))

    #plots.append(Plot(
    #    name = "dPhi_Zl1", texX = '#Delta#phi_{Z,l1}', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.dPhi_Zl1,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "dPhi_Zl2", texX = '#Delta#phi_{Z,l2}', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.dPhi_Zl2,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "dEta_Zl1", texX = '#Delta#eta_{Z,l1}', texY = 'Number of Events / 0.25',
    #    attribute = lambda event, sample:event.dEta_Zl1,
    #    binning=[16,0,4],
    #))

    #plots.append(Plot(
    #    name = "dEta_Zl2", texX = '#Delta#eta_{Z,l2}', texY = 'Number of Events / 0.25',
    #    attribute = lambda event, sample:event.dEta_Zl2,
    #    binning=[16,0,4],
    #))
    
    plots.append(Plot(
        name = "cosThetaStar", texX = 'cos#theta(l-)', texY = 'Number of Events / 0.2',
        attribute = lambda event, sample:event.cosThetaStar,
        binning=[10,-1,1],
    ))
    
    plots.append(Plot(
        name = "cosThetaStar_coarse", texX = 'cos#theta(l-)', texY = 'Number of Events / 0.4',
        attribute = lambda event, sample:event.cosThetaStar,
        binning=[5,-1,1],
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

