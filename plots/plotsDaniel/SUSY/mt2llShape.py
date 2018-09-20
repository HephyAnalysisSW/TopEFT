#!/usr/bin/env python

'''
Use 4l events to varify the modelling of the mt2ll/mt2blbl shape in ttZ(2l,2nu)
'''
#
# Standard imports and batch mode
#
import ROOT, os
import itertools
import copy

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

import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v19/dilep/"

dirs = {}
dirs['TTZToLLNuNu']   = ["TTZToLLNuNu_ext"]
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TTZToLLNuNu  = Sample.fromDirectory(name="TTZToLLNuNu", treeName="Events", isData=False, color=ROOT.kRed+1, texName="ttZ", directory=directories['TTZToLLNuNu'])

read_variables =    ["weight/F", 'reweightLeptonSF_tight_4l/F', 'reweightLeptonTrackingSF_tight_4l/F', 'reweightTrigger_tight_4l/F',
                    #"jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I]", "njet/I","nJetSelected/I",
                    #"lep[mediumMuonId/I,pt/F,eta/F,phi/F,pdgId/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,lostHits/I,convVeto/I,dxy/F,dz/F,hadronicOverEm/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,mvaTTV/F]", "nlep/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I,jetPtRatiov2/F]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", "met_genPhi/F", "met_genPt/F",
                    "genZ_pt/F", "genZ_phi/F", "genZ_eta/F",
                    "Z1_l1_index_4l/I", "Z1_l2_index_4l/I", "nonZ1_l1_index_4l/I", "nonZ1_l2_index_4l/I", "Z2_l1_index_4l/I", "Z2_l2_index_4l/I",
                    "nonZ_l1_index/I", "nonZ_l2_index/I",
                    "Z1_phi_4l/F","Z1_pt_4l/F", "Z1_mass_4l/F", "Z1_eta_4l/F","Z1_lldPhi_4l/F", "Z1_lldR_4l/F", "Z1_cosThetaStar_4l/F","Higgs_mass/F",
                    "Z2_phi_4l/F","Z2_pt_4l/F", "Z2_mass_4l/F", "Z2_eta_4l/F", "Z2_cosThetaStar_4l/F",
                    ]

variables = map( TreeVariable.fromString, read_variables )
#variables += [VectorTreeVariable.fromString('lep[pt/F,eta/F,phi/F,jetPtRatiov2/F,pdgId/I]')]

rand = ROOT.TRandom3(10**6+1)

def getMT2ll( event ):
    l1 = ROOT.TLorentzVector()
    l2 = ROOT.TLorentzVector()
    event.lep_pt[event.nonZ1_l1_index_4l]
    l1.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l1_index_4l], event.lep_eta[event.nonZ1_l1_index_4l], event.lep_phi[event.nonZ1_l1_index_4l], 0 )
    l2.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l2_index_4l], event.lep_eta[event.nonZ1_l2_index_4l], event.lep_phi[event.nonZ1_l2_index_4l], 0 )
    mt2Calc.setLeptons(l1.Pt(), l1.Eta(), l1.Phi(), l2.Pt(), l2.Eta(), l2.Phi())

    #print event.nonZ1_l1_index_4l, event.nonZ1_l2_index_4l, event.Z1_l1_index_4l, event.Z1_l2_index_4l

    met         = ROOT.TLorentzVector()
    met.SetPtEtaPhiM( event.met_pt, 0, event.met_phi, 0)

    genZ        = ROOT.TLorentzVector()
    genZ.SetPtEtaPhiM( event.genZ_pt, event.genZ_eta, event.genZ_phi, 0)


    response    = .99
    Z           = ROOT.TLorentzVector()
    Z.SetPtEtaPhiM( event.Z1_pt_4l*response, event.Z1_eta_4l, event.Z1_phi_4l, 0) #mass missing?!

    # smear the Z with some resolution. 20% resolution assumed for now.
    #if Z.Pt()>200:
    #    rd = rand.Gaus(0,0.25)
    #elif Z.Pt()>100:
    #    rd = rand.Gaus(0,0.25)
    #else:
    #    rd = rand.Gaus(0,0.25)
    #rd = rand.Gaus(0,0.20)
    #Z_pt = (1+rd)*Z.Pt()*0.95
    rd = rand.Gaus(0,20)
    Z_pt = (rd+Z.Pt())*0.95
    #Z_px = Z_pt*math.cos(Z.Phi())
    #Z_py = Z_pt*math.sin(Z.Phi())
    smearZ = ROOT.TLorentzVector()
    smearZ.SetPtEtaPhiM( Z_pt, event.Z1_eta_4l, event.Z1_phi_4l, 0)
    
    #print met.Phi(), Z.Phi()

    newMet = Z + met
    newMetSmear = met + smearZ

    mt2Calc.setMet(newMet.Pt(), newMet.Phi())
    dl_mt2ll_Z = mt2Calc.mt2ll()
    
    mt2Calc.setMet(newMetSmear.Pt(), newMet.Phi()) # phi doesn't change anyway
    dl_mt2ll_Z_smear = mt2Calc.mt2ll()
    
    event.newMet_pt     = newMet.Pt()
    event.newMet_phi    = newMet.Phi()
    
    event.newMetSmeared_pt  = newMetSmear.Pt()
    event.dl_mt2ll_Z        = dl_mt2ll_Z
    event.dl_mt2ll_Z_smear  = dl_mt2ll_Z_smear
    
    event.dPhi_nonZ_l1_newMet = deltaPhi(newMet.Phi(), l1.Phi())
    event.dPhi_nonZ_l2_newMet = deltaPhi(newMet.Phi(), l2.Phi())

    return 1#newMet.Pt(), newMetSmear.Pt(), dl_mt2ll_Z, dl_mt2ll_Z_smear, newMet.Phi()


quadlepSelection    = cutInterpreter.cutString('quadlep-lepSelQuad-njet1p-btag1p-onZ1-offZ2-min_mll12')
quadlepSelection += "&&lep_pt[nonZ1_l1_index_4l]>40&&lep_pt[nonZ1_l2_index_4l]>20"
#dilepSelection      = cutInterpreter.cutString('dilepOS-njet3p-btag1p-offZ') # almost analysis like, no met cuts

#dilepSelection += '&&(abs(lep_pdgId[0])!=(lep_pdgId[1]))'

dilepSelection      = cutInterpreter.cutString('lepSelDY-njet3p-btag1p')
dilepSelection += '&&nlep==2&&(nElectrons_tight_4l==1&&nMuons_tight_4l==1)'
dilepSelection += '&&(abs(genZ_daughter_flavor)==12||abs(genZ_daughter_flavor)==14||abs(genZ_daughter_flavor)==16)'
#dilepSelection = 'nlep==2&&(abs(lep_pdgId[0])!=(lep_pdgId[1]))'

sample = TTZToLLNuNu
dilepS  = copy.deepcopy(TTZToLLNuNu)
quadlepS= copy.deepcopy(TTZToLLNuNu)
dilep   = copy.deepcopy(TTZToLLNuNu)
quadlep = copy.deepcopy(TTZToLLNuNu)


#binning = [0,30,60,100,140,240,340]
binning = [0,50,100,150,200,340]
metBinning = [10,0,400]
phiBinning = [10,-3.2, 3.2]
absPhiBinning = [10,0,3.2]

print dilepSelection

dilep_mt2ll = sample.get1DHistoFromDraw('dl_mt2ll', binning, selectionString=dilepSelection, weightString='weight', binningIsExplicit=True)#, addOverFlowBin='upper')
dilep_met   = sample.get1DHistoFromDraw('met_pt', metBinning, selectionString=dilepSelection, weightString='weight', binningIsExplicit=False, addOverFlowBin='upper')
dilep_metPhi= sample.get1DHistoFromDraw('met_phi', phiBinning, selectionString=dilepSelection, weightString='weight', binningIsExplicit=False)
dilep_phi   = sample.get1DHistoFromDraw('met_phi', absPhiBinning, selectionString=dilepSelection, weightString='weight', binningIsExplicit=False)


#raise NotImplementedError

quadlep_mt2ll = dilep_mt2ll.Clone()
quadlep_met = dilep_met.Clone()
quadlep_metPhi = dilep_metPhi.Clone()
quadlep_metOrig = dilep_met.Clone()

# lepton/met dphi
dPhiHist = dilep_phi.Clone()
dPhiHist.Reset()
dilep_dPhi_metL1    = dPhiHist.Clone()
dilep_dPhi_metL2    = dPhiHist.Clone()
quadlep_dPhi_metL1  = dPhiHist.Clone()
quadlep_dPhi_metL2  = dPhiHist.Clone()

quadlep_mt2ll.Reset()
quadlep_met.Reset()
quadlep_metPhi.Reset()

quadlep_genPt   = TTZToLLNuNu.get1DHistoFromDraw("genZ_pt", selectionString=cutInterpreter.cutString('quadlep-lepSelQuad-njet1p-btag1p-onZ1-offZ2-min_mll12')+'&&genZ_pt>0', binning=[25,0,500], weightString='weight',addOverFlowBin='upper')
dilep_genPt     = TTZToLLNuNu.get1DHistoFromDraw("genZ_pt", selectionString=cutInterpreter.cutString('dilep-lepSelDY-looseVetoDL-njet2p-btag1p-offZ-min_mll12')+'&&genZ_pt>0', binning=[25,0,500], weightString='weight',addOverFlowBin='upper')
dilep_genPt.style         = styles.lineStyle( ROOT.kRed+1, width=2, errors=True )
quadlep_genPt.style       = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )

texNameDilepTTZ = "t#bar{t}Z, Z#rightarrow#nu#nu, 2l"
texNameQuadlepTTZ = "t#bar{t}Z, Z#rightarrowll, 4l, modified E_{T}^{miss}"
texNameQuadlepTTZOrig = "t#bar{t}Z, Z#rightarrowll, 4l"



dilep_genPt.legendText        = texNameDilepTTZ
quadlep_genPt.legendText      = texNameQuadlepTTZ

dilep_genMet    = TTZToLLNuNu.get1DHistoFromDraw("met_genPt", selectionString=dilepSelection, binning=[25,0,500], weightString='weight',addOverFlowBin='upper')
quadlep_genMet  = dilep_genMet.Clone()
quadlep_genMet.Reset()

dilep_genMet.style         = styles.lineStyle( ROOT.kRed+1, width=2, errors=True )
quadlep_genMet.style       = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )

dilep_genMet.legendText        = texNameDilepTTZ
quadlep_genMet.legendText      = texNameQuadlepTTZ



quadlepS.setSelectionString([quadlepSelection])
quadlepS.texName = texNameQuadlepTTZ
reader = quadlepS.treeReader( variables = variables )
reader.start()

while reader.run():
    r = reader.event
    weight = r.weight * r.reweightLeptonSF_tight_4l * r.reweightTrigger_tight_4l
    met = r.met_pt
    
    getMT2ll( r )
    #if newMetSmear >= 120:
    #    if mt2ll_Z_smear > 340: mt2ll_Z_smear = 339
    #    if newMetSmear > 400: newMetSmear = 399
    #    quadlep_mt2ll.Fill(mt2ll_Z_smear, weight*150)
    #    quadlep_met.Fill(newMetSmear, weight*150)
    #    quadlep_metOrig.Fill(met, weight*150)
    if r.newMet_pt >= 0:
        #if r.dl_mt2ll_Z > 340: r.dl_mt2ll_Z = 339
        if met > 400: met = 399
        if r.newMet_pt > 400: r.newMet_pt = 399
        quadlep_mt2ll.Fill(r.dl_mt2ll_Z, weight*150)
        quadlep_met.Fill(r.newMet_pt, weight*150)
        quadlep_metOrig.Fill(met, weight*150)
        quadlep_metPhi.Fill(r.newMet_phi, weight*150) 

        quadlep_dPhi_metL1.Fill(r.dPhi_nonZ_l1_newMet, weight*150)
        quadlep_dPhi_metL2.Fill(r.dPhi_nonZ_l2_newMet, weight*150)

        genMetVec   = ROOT.TLorentzVector()
        genZVec     = ROOT.TLorentzVector()
        genMetVec.SetPtEtaPhiM(r.met_genPt, 0, r.met_genPhi, 0)
        genZVec.SetPtEtaPhiM(r.genZ_pt, 0, r.genZ_phi, 0)
        genMet = (genZVec+genMetVec).Pt()
        quadlep_genMet.Fill(genMet, weight*150)

dilepS.setSelectionString([dilepSelection])
dilepS.texName = texNameDilepTTZ
reader2 = dilepS.treeReader( variables = variables )
reader2.start()

while reader2.run():
    r = reader2.event
    weight = r.weight * r.reweightLeptonSF_tight_4l * r.reweightTrigger_tight_4l
    met_pt = r.met_pt
    met_phi = r.met_phi
    
    l1_phi = r.lep_phi[r.nonZ1_l1_index_4l]
    l2_phi = r.lep_phi[r.nonZ1_l2_index_4l]

    dilep_dPhi_metL1.Fill(deltaPhi(met_phi, l1_phi), weight*150)
    dilep_dPhi_metL2.Fill(deltaPhi(met_phi, l2_phi), weight*150)


    
dilep_mt2ll.style         = styles.lineStyle( ROOT.kRed+1, width=2, errors=True )
quadlep_mt2ll.style       = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )

dilep_mt2ll.legendText        = texNameDilepTTZ
quadlep_mt2ll.legendText      = texNameQuadlepTTZ

dilep_met.style         = styles.lineStyle( ROOT.kRed+1, width=2, errors=True )
quadlep_met.style       = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )
quadlep_metOrig.style   = styles.lineStyle( ROOT.kBlue+1, width=2, errors=True )

dilep_met.legendText        = texNameDilepTTZ
quadlep_met.legendText      = texNameQuadlepTTZ
quadlep_metOrig.legendText  = texNameQuadlepTTZOrig

dilep_metPhi.legendText        = texNameDilepTTZ
quadlep_metPhi.legendText      = texNameQuadlepTTZ
dilep_metPhi.style         = styles.lineStyle( ROOT.kRed+1, width=2, errors=True )
quadlep_metPhi.style       = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )

dilep_dPhi_metL1.legendText        = texNameDilepTTZ
quadlep_dPhi_metL1.legendText      = texNameQuadlepTTZ
dilep_dPhi_metL1.style         = styles.lineStyle( ROOT.kRed+1, width=2, errors=True )
quadlep_dPhi_metL1.style       = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )

dilep_dPhi_metL2.legendText        = texNameDilepTTZ
quadlep_dPhi_metL2.legendText      = texNameQuadlepTTZ
dilep_dPhi_metL2.style         = styles.lineStyle( ROOT.kRed+1, width=2, errors=True )
quadlep_dPhi_metL2.style       = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )



def drawObjects( ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Simulation'),
      (0.75, 0.95, 'MC (13 TeV)' )
    ]
    return [tex.DrawLatex(*l) for l in lines]

plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/stopsDileptonLegacy/TTZstudies/mt2ll_lepSelUpdate/"

for log in [True, False]:
    
    postFix = '_log' if log else ''

    plots = [[dilep_mt2ll], [quadlep_mt2ll]]
    plotting.draw(
        Plot.fromHisto("dl_mt2ll"+postFix,
                    plots,
                    texX = "M_{T2}(ll) (GeV)"
                ),
        plot_directory = plot_directory,
        logX = False, logY = log, sorting = False,
        drawObjects = drawObjects(),
        scaling = {0:1},
        ratio = {'histos':[(1,0)]},
        copyIndexPHP = True
        )

    plots = [[dilep_genPt], [quadlep_genPt]]
    plotting.draw(
        Plot.fromHisto("gen_Zpt"+postFix,
                    plots,
                    texX = "p_{T}(Z) (gen) (GeV)"
                ),
        plot_directory = plot_directory,
        logX = False, logY = log, sorting = False,
        drawObjects = drawObjects(),
        scaling = {0:1},
        ratio = {'histos':[(1,0)]},
        copyIndexPHP = True
        )

    
    plots = [[dilep_met], [quadlep_met], [quadlep_metOrig]]
    
    plotting.draw(
        Plot.fromHisto("met_pt"+postFix,
                    plots,
                    texX = "E_{T}^{miss} (GeV)"
                ),
        plot_directory = plot_directory,
        logX = False, logY = log, sorting = False,
        drawObjects = drawObjects(),
        scaling = {0:1},
        ratio = {'histos':[(1,0)], 'yRange': (0.01, 2.99)},
        copyIndexPHP = True
        )
    
    plots = [[dilep_metPhi], [quadlep_metPhi]]
    plotting.draw(
        Plot.fromHisto("met_phi"+postFix,
                    plots,
                    texX = "#phi(E_{T}^{miss})"
                ),
        plot_directory = plot_directory,
        logX = False, logY = log, sorting = False,
        drawObjects = drawObjects(),
        scaling = {0:1},
        ratio = {'histos':[(1,0)]},
        copyIndexPHP = True
        )

    plots = [[dilep_dPhi_metL1], [quadlep_dPhi_metL1]]
    plotting.draw(               
        Plot.fromHisto("dPhi_metL1"+postFix,
                    plots,
                    texX = "#Delta#phi(l1, E_{T}^{miss})"
                ),
        plot_directory = plot_directory,
        logX = False, logY = log, sorting = False,
        drawObjects = drawObjects(),
        scaling = {0:1},
        ratio = {'histos':[(1,0)]},
        copyIndexPHP = True
        )

    plots = [[dilep_dPhi_metL2], [quadlep_dPhi_metL2]]
    plotting.draw(
        Plot.fromHisto("dPhi_metL2"+postFix,
                    plots,
                    texX = "#Delta#phi(l2, E_{T}^{miss})"
                ),
        plot_directory = plot_directory,
        logX = False, logY = log, sorting = False,
        drawObjects = drawObjects(),
        scaling = {0:1},
        ratio = {'histos':[(1,0)]},
        copyIndexPHP = True
        )

    plots = [[dilep_genMet], [quadlep_genMet]]
    plotting.draw(
        Plot.fromHisto("met_genPt"+postFix,
                    plots,
                    texX = "E_{T}^{miss} (gen) (GeV)"
                ),
        plot_directory = plot_directory,
        logX = False, logY = log, sorting = False,
        drawObjects = drawObjects(),
        scaling = {0:1},
        ratio = {'histos':[(1,0)]},
        copyIndexPHP = True
        )


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

def drawPlots(plots, dataMCScale):
  for log in [False, True]:
    #ext = "_small" if small else ""
    ext = "_log" if log else ""
    plot_directory_ = plot_directory
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      extensions_ = ["pdf", "png", "root"]

      plotting.draw(plot,
        plot_directory = plot_directory_,
        extensions = extensions_,
        ratio = {'yRange':(0.1,1.9)},
        logX = False, logY = log, sorting = False,
        scaling = {1:0},
        yRange = (0.03, "auto") if log else (0.001, "auto"),
        legend = [ (0.15,0.87-0.03*sum(map(len, plot.histos)),0.9,0.87), 2],
        drawObjects = drawObjects( False , dataMCScale , 1 ),
        copyIndexPHP = True,
      )

dilep.setSelectionString(dilepSelection)
quadlep.setSelectionString(quadlepSelection)

dilep.style = styles.lineStyle(ROOT.kRed+1, width=2, errors=True)
quadlep.style = styles.lineStyle(ROOT.kGreen+1, width=2, errors=True)

stack = Stack(dilep, quadlep)

weight_ = lambda event, sample: event.weight

Plot.setDefaults(stack = stack, weight = staticmethod(weight_), selectionString = '(1)', addOverFlowBin='upper')

plots = []

plots.append(Plot(
     name = 'lnonZ1_pt',
     texX = 'p_{T}(l_{1,non-Z}) (GeV)', texY = 'Number of Events / 20 GeV',
     attribute = lambda event, sample:event.lep_pt[event.nonZ1_l1_index_4l],
     #event, sample:event.lep_pt[0], #event.lep_pt[event.nonZ1_l1_index_4l]
     binning=[15,0,300],
))

plots.append(Plot(
     name = 'lnonZ1_phi',
     texX = '#phi(l_{1,non-Z}) (GeV)', texY = 'Number of Events / 20 GeV',
     attribute = lambda event, sample:event.lep_phi[event.nonZ1_l1_index_4l],
     #event, sample:event.lep_pt[0], #event.lep_pt[event.nonZ1_l1_index_4l]
     binning=[10,-3.2,3.2],
))

plots.append(Plot(
     name = 'lnonZ1_eta',
     texX = '#eta(l_{1,non-Z}) (GeV)', texY = 'Number of Events / 20 GeV',
     attribute = lambda event, sample:event.lep_eta[event.nonZ1_l1_index_4l],
     #event, sample:event.lep_pt[0], #event.lep_pt[event.nonZ1_l1_index_4l]
     binning=[10,-2.5,2.5],
))

plots.append(Plot(
     name = 'lnonZ2_pt',
     texX = 'p_{T}(l_{2,non-Z}) (GeV)', texY = 'Number of Events / 20 GeV',
     attribute = lambda event, sample:event.lep_pt[event.nonZ1_l2_index_4l],
     #event, sample:event.lep_pt[0], #event.lep_pt[event.nonZ1_l1_index_4l]
     binning=[15,0,150],
))

plots.append(Plot(
     name = 'lnonZ2_phi',
     texX = '#phi(l_{2,non-Z}) (GeV)', texY = 'Number of Events / 20 GeV',
     attribute = lambda event, sample:event.lep_phi[event.nonZ1_l2_index_4l],
     #event, sample:event.lep_pt[0], #event.lep_pt[event.nonZ1_l1_index_4l]
     binning=[10,-3.2,3.2],
))

plots.append(Plot(
     name = 'lnonZ2_eta',
     texX = '#eta(l_{2,non-Z}) (GeV)', texY = 'Number of Events / 20 GeV',
     attribute = lambda event, sample:event.lep_eta[event.nonZ1_l2_index_4l],
     #event, sample:event.lep_pt[0], #event.lep_pt[event.nonZ1_l1_index_4l]
     binning=[10,-2.5,2.5],
))


plotting.fill(plots, read_variables = read_variables, sequence = [])

dataMCScale = 1
drawPlots(plots, dataMCScale)

