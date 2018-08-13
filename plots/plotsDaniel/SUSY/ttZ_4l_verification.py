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

#
# Make samples, will be searched for in the postProcessing directory
#

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v17/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v18/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v19/dilep/"

dirs = {}
dirs['TTZ']         = ['TTZToLLNuNu_ext','TTZToQQ', 'TTZToLLNuNu_m1to10']#, 'TTZToQQ']
dirs['TTZToLLNuNu'] = ['TTZToLLNuNu_m1to10', 'TTZToLLNuNu_ext']
dirs['TTZToQQ']     = ['TTZToQQ']

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

# Define samples
TTZ         = Sample.fromDirectory(name="TTZ", treeName="Events", isData=False, color=color.TTZ, texName="t#bar{t}Z,Z to inv.", directory=directories['TTZ'])

quadlepSelection    = cutInterpreter.cutString('quadlep-lepSelQuad-njet1p-btag1p-onZ1-offZ2-min_mll12') # offZ2 in cutinterpreter doesn't do anything
quadlepSelection   += "&&lep_pt[nonZ1_l1_index_4l]>40&&lep_pt[nonZ1_l2_index_4l]>20"

dilepSelection      = cutInterpreter.cutString('lepSelDY-njet3p-btag1p')
dilepSelection += '&&nlep==2&&nLeptons_tight_4l==2&&(nElectrons_tight_4l==1&&nMuons_tight_4l==1)'
#dilepSelection += '&&nlep==2&&nLeptons_tight_4l==2&&((nElectrons_tight_4l==1&&nMuons_tight_4l==1)||(nElectrons_tight_4l==2&&abs(Z1_mass_4l-91.2)>10)||(nMuons_tight_4l==2&&abs(Z1_mass_4l-91.2)>10))'
dilepSelection += '&&genZ_pt>=0'
#dilepSelection += '&&(abs(genZ_daughter_flavor)==12||abs(genZ_daughter_flavor)==14||abs(genZ_daughter_flavor)==16)'

invisibleSelection  = '(abs(genZ_daughter_flavor)==12||abs(genZ_daughter_flavor)==14||abs(genZ_daughter_flavor)==16)'
leptonicSelection   = '(abs(genZ_daughter_flavor)==11||abs(genZ_daughter_flavor)==13)'
tauSelection        = '(abs(genZ_daughter_flavor)==15)'
hadronicSelection   = '(abs(genZ_daughter_flavor)<7)'





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

#scaling = { i+1:0 for i in range(len(signals)) }

def drawPlots(plots, mode, dataMCScale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.plot_directory, mode + ("_log" if log else ""), args.selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      if not args.noData: 
        if mode == "all": plot.histos[1][0].legendText = "Data"
        if mode == "SF":  plot.histos[1][0].legendText = "Data (SF)"
      extensions_ = ["pdf", "png", "root"] if mode == 'all' else ['png']

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


#
# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I]", "njet/I","nJetSelected/I",
                    "lep[mediumMuonId/I,pt/F,eta/F,phi/F,pdgId/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,lostHits/I,convVeto/I,dxy/F,dz/F,hadronicOverEm/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,mvaTTV/F]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "Z1_l1_index_4l/I", "Z1_l2_index_4l/I", "nonZ1_l1_index_4l/I", "nonZ1_l2_index_4l/I", "Z2_l1_index_4l/I", "Z2_l2_index_4l/I", 
                    "Z1_phi_4l/F","Z1_pt_4l/F", "Z1_mass_4l/F", "Z1_eta_4l/F","Z1_lldPhi_4l/F", "Z1_lldR_4l/F", "Z1_cosThetaStar_4l/F","Higgs_mass/F",
                    "Z2_phi_4l/F","Z2_pt_4l/F", "Z2_mass_4l/F", "Z2_eta_4l/F", "Z2_cosThetaStar_4l/F",
                    ]

variables = map( TreeVariable.fromString, read_variables )

offZ2 = "&&abs(Z2_mass_4l-91.2)>20"
def getLeptonSelection( mode ):
    if   mode=="mumumumu":  return "nMuons_tight_4l==4&&nElectrons_tight_4l==0" + offZ2
    elif mode=="mumumue":   return "nMuons_tight_4l==3&&nElectrons_tight_4l==1"
    elif mode=="mumuee":    return "nMuons_tight_4l==2&&nElectrons_tight_4l==2" + offZ2
    elif mode=="mueee":     return "nMuons_tight_4l==1&&nElectrons_tight_4l==3"
    elif mode=="eeee":      return "nMuons_tight_4l==0&&nElectrons_tight_4l==4" + offZ2
    elif mode=='all':       return "nMuons_tight_4l+nElectrons_tight_4l==4"

modes = ["mumumumu","mumumue","mumuee","mueee","eeee"]

def getMT2ll_fromZ( event ):
    l1 = ROOT.TLorentzVector()
    l2 = ROOT.TLorentzVector()
    l1.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l1_index_4l], event.lep_eta[event.nonZ1_l1_index_4l], event.lep_phi[event.nonZ1_l1_index_4l], 0 )
    l2.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l2_index_4l], event.lep_eta[event.nonZ1_l2_index_4l], event.lep_phi[event.nonZ1_l2_index_4l], 0 )
    mt2Calc.setLeptons(l1.Pt(), l1.Eta(), l1.Phi(), l2.Pt(), l2.Eta(), l2.Phi())

    met         = ROOT.TLorentzVector()
    met.SetPtEtaPhiM( event.met_pt, 0, event.met_phi, 0)

    Z           = ROOT.TLorentzVector()
    Z.SetPtEtaPhiM( event.Z1_pt_4l, event.Z1_eta_4l, event.Z1_phi_4l, 0)

    newMet = met+Z

    mt2Calc.setMet(newMet.Pt(), newMet.Phi())
    event.dl_mt2ll_Z = mt2Calc.mt2ll()
    event.met_pt_Z = newMet.Pt()


def getMT2ll_tight_4l( event ):
    l1 = ROOT.TLorentzVector()
    l2 = ROOT.TLorentzVector()
    l1.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l1_index_4l], event.lep_eta[event.nonZ1_l1_index_4l], event.lep_phi[event.nonZ1_l1_index_4l], 0 )
    l2.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l2_index_4l], event.lep_eta[event.nonZ1_l2_index_4l], event.lep_phi[event.nonZ1_l2_index_4l], 0 )
    mt2Calc.setLeptons(l1.Pt(), l1.Eta(), l1.Phi(), l2.Pt(), l2.Eta(), l2.Phi())

    met         = ROOT.TLorentzVector()
    met.SetPtEtaPhiM( event.met_pt, 0, event.met_phi, 0)

    mt2Calc.setMet(met.Pt(), met.Phi())
    event.dl_mt2ll_tight_4l = mt2Calc.mt2ll()

logger.info("Getting a template histogram.")
binning = [0,50,100,150,200,340]
metBinning = [5,0,400]

mt2ll_hist  = TTZ.get1DHistoFromDraw('dl_mt2ll', binning, selectionString=dilepSelection, weightString='weight', binningIsExplicit=True, addOverFlowBin='upper')
met_hist    = TTZ.get1DHistoFromDraw('met_pt', metBinning, selectionString=dilepSelection, weightString='weight', binningIsExplicit=False, addOverFlowBin='upper')

hists = {}
met_hists = {}

quadlep_samples = [Run2016, rare, TTX, ZZ]
dilep_samples   = [TTZ]

tr = triggerSelector(2016)
lumi_scale = 35.9

logger.info("Now working on 4l samples.")

for s in quadlep_samples:
    logger.info("Sample: %s", s.name)
    hists[s.name] = mt2ll_hist.Clone()
    hists[s.name].Reset()
    hists[s.name].legendText = s.texName
    met_hists[s.name] = met_hist.Clone()
    met_hists[s.name].Reset()
    met_hists[s.name].legendText = s.texName

    # selection for data or MC. Trigger and filters and stuff!
    for mode in modes:
        logger.info("Working on mode %s", mode)
        if s.isData:
            s.setSelectionString([getFilterCut(isData=True, year=2016), quadlepSelection, getLeptonSelection(mode)])
        else:
            s.setSelectionString([getFilterCut(isData=False, year=2016), quadlepSelection, tr.getSelection("MC"), getLeptonSelection(mode)])
        
        reader = s.treeReader( variables = variables )
        reader.start()

        while reader.run():
            r = reader.event
            
            getMT2ll_fromZ(r)
            if r.dl_mt2ll_Z > binning[-1]: r.dl_mt2ll_Z = binning[-1]-1
            if r.met_pt_Z > metBinning[-1]: r.met_pt_Z = metBinning[-1]-1
            weight = r.weight*lumi_scale if not s.isData else r.weight
            hists[s.name].Fill(r.dl_mt2ll_Z, weight)
            met_hists[s.name].Fill(r.met_pt_Z, weight)

        del reader

logger.info("Now working on 2l samples.")

for s in dilep_samples:
    logger.info("Sample: %s", s.name)
    hists[s.name] = mt2ll_hist.Clone()
    hists[s.name].Reset()
    hists[s.name].legendText = s.texName

    met_hists[s.name] = met_hist.Clone()
    met_hists[s.name].Reset()
    met_hists[s.name].legendText = s.texName

    # selection for data or MC. Trigger and filters and stuff!
    s.setSelectionString([getFilterCut(isData=False, year=2016), dilepSelection, invisibleSelection, tr.getSelection("MC")])

    reader = s.treeReader( variables = variables )
    reader.start()

    while reader.run():
        r = reader.event

        getMT2ll_tight_4l(r)
        if r.dl_mt2ll_tight_4l > binning[-1]: r.dl_mt2ll_tight_4l = binning[-1]-1
        if r.met_pt > metBinning[-1]: r.met_pt_Z = metBinning[-1]-1
        hists[s.name].Fill(r.dl_mt2ll_tight_4l, r.weight*lumi_scale)
        met_hists[s.name].Fill(r.met_pt, r.weight*lumi_scale)
    
    del reader

logger.info("Getting scaling...")

data_yield = hists['Run2016'].Integral()
other_yield = 0.
for s in quadlep_samples:
    if not s.isData:
        y = hists[s.name].Integral()
        logger.info("Process %s has yield: %.2f", s, y)
        other_yield += y

# scale TTZ 
TTZ_scale = (data_yield-other_yield)/hists['TTZ'].Integral()

logger.info("Scale for dilep ttZ sample: %.2f", TTZ_scale)

hists['TTZ'].Scale(TTZ_scale)
met_hists['TTZ'].Scale(TTZ_scale)


########## now just plot I guess

for name in hists.keys():
    #hists[name].legendText = name
    if not name == 'Run2016':
        hists[name].style = styles.fillStyle(getattr(color, name))
        met_hists[name].style = styles.fillStyle(getattr(color, name))
    else:
        hists[name].style = styles.errorStyle(ROOT.kBlack)
        met_hists[name].style = styles.errorStyle(ROOT.kBlack)

logger.info("Plotting.")

for log in [True, False]:

    postFix = '_log' if log else ''

    plots = [[hists['TTZ'], hists['ZZ'], hists['TTX'], hists['rare']], [hists['Run2016']]]
    plotting.draw(
        Plot.fromHisto("dl_mt2ll"+postFix,
                    plots,
                    texX = "M_{T2}(ll) (GeV)"
                ),
        plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/stopsDileptonLegacy/TTZstudies/ttZ_4l/",
        logX = False, logY = log, sorting = False,
        drawObjects = drawObjects(True, 1.0, lumi_scale),
        #scaling = {0:1},
        ratio = {'histos':[(1,0)], 'yRange':(0.1,1.9)},
        legend = [ (0.55,0.7,0.9,0.9), 1],
        copyIndexPHP = True
        )

    plots = [[met_hists['TTZ'], met_hists['ZZ'], met_hists['TTX'], met_hists['rare']], [met_hists['Run2016']]]
    plotting.draw(
        Plot.fromHisto("met_pt"+postFix,
                    plots,
                    texX = "E_{T}^{miss} (GeV)"
                ),
        plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/stopsDileptonLegacy/TTZstudies/ttZ_4l/",
        logX = False, logY = log, sorting = False,
        drawObjects = drawObjects(True, 1.0, lumi_scale),
        #scaling = {0:1},
        ratio = {'histos':[(1,0)], 'yRange':(0.1,1.9)},
        legend = [ (0.55,0.7,0.9,0.9), 1],
        copyIndexPHP = True
        )



##
## Loop over channels
##
#yields     = {}
#allPlots   = {}
#allModes   = ['mumumumu','mumumue','mumuee', 'mueee', 'eeee']
#for index, mode in enumerate(allModes):
#    yields[mode] = {}
#    logger.info("Working on mode %s", mode)
#    if not args.noData:
#        data_sample = Run2016 if args.year == 2016 else Run2017
#        data_sample.texName = "data"
#
#        data_sample.setSelectionString([getFilterCut(isData=True, year=args.year), getLeptonSelection(mode)])
#        data_sample.name           = "data"
#        data_sample.read_variables = ["evt/I","run/I"]
#        data_sample.style          = styles.errorStyle(ROOT.kBlack)
#        lumi_scale                 = data_sample.lumi/1000
#
#    if args.noData: lumi_scale = 35.9 if args.year == 2016 else 41.0
#    weight_ = lambda event, sample: event.weight
#
#    if args.year == 2016:
#        mc             = [ TTZtoLLNuNu, TTX, rare, ZZ ]
#    else:
#        mc             = [ TTZtoLLNuNu_17, TTX_17, rare_17, ZZ_17 ]
#
#    for sample in mc: sample.style = styles.fillStyle(sample.color)
#
#    for sample in mc + signals:
#      sample.scale          = lumi_scale
#      sample.read_variables = ['reweightBTagCSVv2_SF/F', 'reweightBTagDeepCSV_SF/F', 'reweightPU36fb/F', 'reweightTrigger_tight_4l/F', 'reweightLeptonTrackingSF_tight_4l/F', 'nTrueInt/F', 'reweightPU36fb/F', 'reweightLeptonSF_tight_4l/F']#, 'reweightLeptonSF_tight_4l/F']
#      
#      if args.year == 2016:
#          sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightTrigger_tight_4l*event.reweightLeptonTrackingSF_tight_4l*event.reweightPU36fb*event.reweightLeptonSF_tight_4l #*nTrueInt36fb_puRW(event.nTrueInt)
#      else:
#          sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightTrigger_tight_4l*event.reweightPU36fb*event.reweightLeptonSF_tight_4l #*event.reweightLeptonSF_tight_4l #*nTrueInt36fb_puRW(event.nTrueInt)
#      tr = triggerSelector(args.year)
#      sample.setSelectionString([getFilterCut(isData=False, year=args.year), getLeptonSelection(mode), tr.getSelection("MC")])
#
#    if not args.noData:
#      stack = Stack(mc, data_sample)
#    else:
#      stack = Stack(mc)
#
#    stack.extend( [ [s] for s in signals ] )
#
#    if args.small:
#        for sample in stack.samples:
#            sample.reduceFiles( to = 1 )
#
#    # Use some defaults
#    Plot.setDefaults(stack = stack, weight = weight_, selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='both')
#
#    plots = []
#    
#    plots.append(Plot(
#      name = 'yield', texX = 'yield', texY = 'Number of Events',
#      attribute = lambda event, sample: 0.5 + index,
#      binning=[5, 0, 5],
#    ))
#    
#    plots.append(Plot(
#      name = 'nVtxs', texX = 'vertex multiplicity', texY = 'Number of Events',
#      attribute = TreeVariable.fromString( "nVert/I" ),
#      binning=[50,0,50],
#    ))
#    
#    plots.append(Plot(
#        texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
#        attribute = TreeVariable.fromString( "met_pt/F" ),
#        binning=[400/20,0,400],
#    ))
#    
#    plots.append(Plot(
#        texX = 'H_{T} (GeV)', texY = 'Number of Events / 20 GeV',
#        attribute = TreeVariable.fromString( "ht/F" ),
#        binning=[800/20,0,800],
#    ))
#    
#    plots.append(Plot(
#        texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
#        attribute = TreeVariable.fromString( "met_phi/F" ),
#        binning=[10,-pi,pi],
#    ))
#    
#    plots.append(Plot(
#        texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 20 GeV',
#        attribute = TreeVariable.fromString( "Z1_pt_4l/F" ),
#        binning=[20,0,400],
#    ))
#    
#    plots.append(Plot(
#        name = 'Z1_pt_coarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 50 GeV',
#        attribute = TreeVariable.fromString( "Z1_pt_4l/F" ),
#        binning=[16,0,800],
#    ))
#    
#    plots.append(Plot(
#        name = 'Z1_pt_superCoarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events',
#        attribute = TreeVariable.fromString( "Z1_pt_4l/F" ),
#        binning=[3,0,600],
#    ))
#    
#    plots.append(Plot(
#        name = 'Z1_pt_analysis', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 100 GeV',
#        attribute = TreeVariable.fromString( "Z1_pt_4l/F" ),
#        binning=[4,0,400],
#    ))
#    
#    plots.append(Plot(
#        name = "invM_3l",
#        texX = 'M(3l) (GeV)', texY = 'Number of Events',
#        attribute = lambda event, sample:event.threelmass,
#        binning=[25,0,500],
#    ))
#    
#    plots.append(Plot(
#        texX = '#Delta#phi(ll)', texY = 'Number of Events',
#        attribute = TreeVariable.fromString( "Z1_lldPhi_4l/F" ),
#        binning=[10,0,pi],
#    ))
#
#    # plots of lepton variables
#
#    plots.append(Plot(
#        name = "lZ1_pt",
#        texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
#        attribute = lambda event, sample:event.lep_pt[event.Z1_l1_index_4l],
#        binning=[30,0,300],
#    ))
#
#    plots.append(Plot(
#        name = "lZ1_eta",
#        texX = 'eta(l_{1,Z})', texY = 'Number of Events',
#        attribute = lambda event, sample:event.lep_eta[event.Z1_l1_index_4l],
#        binning=[40,-4.,4.],
#    ))
#
#    plots.append(Plot(
#        name = "lZ1_phi",
#        texX = '#phi(l_{1,Z})', texY = 'Number of Events',
#        attribute = lambda event, sample:event.lep_phi[event.Z1_l1_index_4l],
#        binning=[40,-3.2,3.2],
#    ))
#
#    plots.append(Plot(
#        name = "lZ1_pdgId",
#        texX = 'PDG ID (l_{1,Z})', texY = 'Number of Events',
#        attribute = lambda event, sample:event.lep_pdgId[event.Z1_l1_index_4l],
#        binning=[30,-15,15],
#    ))
#
#    # lepton 2    
#    plots.append(Plot(
#        name = "lZ2_pt",
#        texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
#        attribute = lambda event, sample:event.lep_pt[event.Z1_l2_index_4l],
#        binning=[20,0,200],
#    ))
#
#
#    plots.append(Plot(
#        name = "lZ2_eta",
#        texX = 'eta(l_{2,Z})', texY = 'Number of Events',
#        attribute = lambda event, sample:event.lep_eta[event.Z1_l2_index_4l],
#        binning=[40,-4.,4.],
#    ))
#
#    plots.append(Plot(
#        name = "lZ2_phi",
#        texX = '#phi(l_{2,Z})', texY = 'Number of Events',
#        attribute = lambda event, sample:event.lep_phi[event.Z1_l2_index_4l],
#        binning=[40,-3.2,3.2],
#    ))
#
#    plots.append(Plot(
#        name = "lZ2_pdgId",
#        texX = 'PDG ID (l_{2,Z})', texY = 'Number of Events',
#        attribute = lambda event, sample:event.lep_pdgId[event.Z1_l2_index_4l],
#        binning=[30,-15,15],
#    ))
#    
#    # lepton 3
#    plots.append(Plot(
#        name = 'lnonZ1_pt',
#        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 10 GeV',
#        attribute = lambda event, sample:event.lep_pt[event.nonZ1_l1_index_4l],
#        binning=[30,0,300],
#    ))
#
#    plots.append(Plot(
#        name = "lnonZ1_eta",
#        texX = 'eta(l_{1,extra})', texY = 'Number of Events',
#        attribute = lambda event, sample:event.lep_eta[event.nonZ1_l1_index_4l],
#        binning=[40,-4.,4.],
#    ))
#
#    plots.append(Plot(
#        name = "lnonZ1_phi",
#        texX = '#phi(l_{1,extra})', texY = 'Number of Events',
#        attribute = lambda event, sample:event.lep_phi[event.nonZ1_l1_index_4l],
#        binning=[40,-3.2,3.2],
#    ))
#
#    plots.append(Plot(
#        name = "lnonZ1_pdgId",
#        texX = 'PDG ID (l_{1,extra})', texY = 'Number of Events',
#        attribute = lambda event, sample:event.lep_pdgId[event.nonZ1_l1_index_4l],
#        binning=[30,-15,15],
#    ))
#
#    # other plots
#
#
#    plots.append(Plot(
#        texX = 'M(ll) (GeV)', texY = 'Number of Events / 2 GeV',
#        attribute = TreeVariable.fromString( "Z1_mass_4l/F" ),
#        binning=[20,70,110],
#    ))
#
#    plots.append(Plot(
#        texX = 'M(ll) 2nd OS pair (GeV)', texY = 'Number of Events / 8 GeV',
#        attribute = TreeVariable.fromString( "Z2_mass_4l/F" ),
#        binning=[20,40,200],
#    ))
#    
#    plots.append(Plot(
#        texX = 'M(ZZ) (GeV)', texY = 'Number of Events / 10 GeV',
#        attribute = TreeVariable.fromString( "Higgs_mass/F" ),
#        binning=[22,80,300],
#    ))
#    
#    plots.append(Plot(
#        texX = 'M_{T2}(ll) Z estimated (GeV)', texY = 'Number of Events',
#        name = "mt2ll_Z_estimated",
#        attribute = lambda event, sample: event.dl_mt2ll_Z,
#        binning=[4,0,320],
#    ))
#    
#    plots.append(Plot(
#      texX = 'N_{jets}', texY = 'Number of Events',
#      attribute = TreeVariable.fromString( "nJetSelected/I" ), #nJetSelected
#      binning=[8,-0.5,7.5],
#    ))
#    
#    plots.append(Plot(
#      texX = 'N_{b-tag}', texY = 'Number of Events',
#      attribute = TreeVariable.fromString( "nBTag/I" ),
#      binning=[4,-0.5,3.5],
#    ))
#    
#    plots.append(Plot(
#      texX = 'N_{l, loose}', texY = 'Number of Events',
#      name = 'nLepLoose', attribute = lambda event, sample: event.nlep,
#      binning=[5,2.5,7.5],
#    ))
#
#    plots.append(Plot(
#      texX = 'p_{T}(leading l) (GeV)', texY = 'Number of Events / 20 GeV',
#      name = 'lep1_pt', attribute = lambda event, sample: event.lep_pt[0],
#      binning=[400/20,0,400],
#    ))
#
#    plots.append(Plot(
#      texX = 'p_{T}(subleading l) (GeV)', texY = 'Number of Events / 10 GeV',
#      name = 'lep2_pt', attribute = lambda event, sample: event.lep_pt[1],
#      binning=[200/10,0,200],
#    ))
#
#    plots.append(Plot(
#      texX = 'p_{T}(trailing l) (GeV)', texY = 'Number of Events / 10 GeV',
#      name = 'lep3_pt', attribute = lambda event, sample: event.lep_pt[2],
#      binning=[150/10,0,150],
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
#
#    plots.append(Plot(
#        name = "LP", texX = 'L_{P}', texY = 'Number of Events / 0.1',
#        attribute = lambda event, sample:event.Lp,
#        binning=[20,-1,1],
#    ))
#    
#    plots.append(Plot(
#        name = "Z1_cosThetaStar", texX = 'cos#theta(Z1,l-)', texY = 'Number of Events / 0.2',
#        attribute = lambda event, sample:event.Z1_cosThetaStar_4l,
#        binning=[10,-1,1],
#    ))
#    
#    plots.append(Plot(
#        name = "Z1_cosThetaStar_coarse", texX = 'cos#theta(Z1,l-)', texY = 'Number of Events / 0.2',
#        attribute = lambda event, sample:event.Z1_cosThetaStar_4l,
#        binning=[5,-1,1],
#    ))
#    
#    plots.append(Plot(
#        name = "Z2_cosThetaStar", texX = 'cos#theta(Z2,l-)', texY = 'Number of Events / 0.2',
#        attribute = lambda event, sample:event.Z2_cosThetaStar_4l,
#        binning=[10,-1,1],
#    ))
#    
#    plotting.fill(plots, read_variables = read_variables, sequence = sequence)
#
#    # Get normalization yields from yield histogram
#    for plot in plots:
#      if plot.name == "yield":
#        for i, l in enumerate(plot.histos):
#          for j, h in enumerate(l):
#            yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
#            h.GetXaxis().SetBinLabel(1, "#mu#mu#mu#mu")
#            h.GetXaxis().SetBinLabel(2, "#mu#mu#mue")
#            h.GetXaxis().SetBinLabel(3, "#mu#muee")
#            h.GetXaxis().SetBinLabel(4, "#mueee")
#            h.GetXaxis().SetBinLabel(5, "eeee")
#    if args.noData: yields[mode]["data"] = 0
#
#    yields[mode]["MC"] = sum(yields[mode][s.name] for s in mc)
#    dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
#
#    drawPlots(plots, mode, dataMCScale)
#    allPlots[mode] = plots
#
## Add the different channels into SF and all
#for mode in ["comb1","comb2","comb3","all"]:
#    yields[mode] = {}
#    for y in yields[allModes[0]]:
#        try:    yields[mode][y] = sum(yields[c][y] for c in ['eeee','mueee','mumuee', 'mumumue', 'mumumumu'])
#        except: yields[mode][y] = 0
#    dataMCScale = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
#    
#    for plot in allPlots['mumumumu']:
#        if mode=="comb1":
#            tmp = allPlots['mumumue']
#        elif mode=="comb2":
#            tmp = allPlots['mumuee']
#        elif mode=="comb3":
#            tmp = allPlots['mueee']
#        else:
#            tmp = allPlots['eeee']
#        for plot2 in (p for p in tmp if p.name == plot.name):
#            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
#                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
#                    if i==k:
#                        j.Add(l)
#    
#    if mode == "all": drawPlots(allPlots['mumumumu'], mode, dataMCScale)
#
#logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )

