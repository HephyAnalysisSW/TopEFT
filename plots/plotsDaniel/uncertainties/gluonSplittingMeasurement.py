''' Analysis script for 1D 2l plots (RootTools)
'''

#Standard imports
import ROOT
from math import sqrt, cos, sin, pi, acos
import itertools,os
import copy

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--small',               action='store_true', help="For testing")
argParser.add_argument('--noData',              action='store_true', help="Omit data")
argParser.add_argument('--logLevel',            action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
args = argParser.parse_args()


#RootTools
from RootTools.core.standard import *
from TopEFT.Tools.user import data_directory

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_v14/trilep/"

from TopEFT.samples.color           import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter
from TopEFT.Tools.helpers           import deltaR, deltaR2, deltaPhi
from TopEFT.Tools.objectSelection   import getJets
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.triggerSelector import triggerSelector
from TopEFT.Tools.user            import plot_directory

import TopEFT.Tools.logger as logger

import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)


data_directory = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v2/dilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *

dirs = {}
dirs['DY_HT_LO'] = ['DYJetsToLL_M50_LO_ext_comb_lheHT70','DYJetsToLL_M50_HT70to100', 'DYJetsToLL_M50_HT100to200_comb', 'DYJetsToLL_M50_HT200to400_comb', 'DYJetsToLL_M50_HT400to600_comb', 'DYJetsToLL_M50_HT600to800', 'DYJetsToLL_M50_HT800to1200', 'DYJetsToLL_M50_HT1200to2500', 'DYJetsToLL_M50_HT2500toInf']
dirs['top']      = ['TTLep_pow'] + ['TToLeptons_sch_amcatnlo', 'T_tch_powheg', 'TBar_tch_powheg']
dirs['TTX']      = ['TTZToLLNuNu_ext', 'TTWToLNu_ext_comb', "TTGJets_comb", "TTHnobb_pow", "TTTT", "tWll", "tZq_ll_ext"]
dirs['boson']    = ['ZZ_comb','WZ_comb', 'WWW', 'WWZ', 'WZZ', 'ZZZ', "ZGTo2LG_ext", "WGToLNuG"]

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

# Define samples
DY_HT_LO = Sample.fromDirectory(name="DY_HT_LO", treeName="Events", isData=False, color=ROOT.kBlue+1, texName="DY HT (LO)", directory=directories['DY_HT_LO'])
Top      = Sample.fromDirectory(name="Top", treeName="Events", isData=False, color=color.TTJets, texName="t/t#bar{t}", directory=directories['top'])
TTX      = Sample.fromDirectory(name="TTX", treeName="Events", isData=False, color=color.TTZ, texName="t/t#bar{t}X", directory=directories['TTX'])
boson    = Sample.fromDirectory(name="boson", treeName="Events", isData=False, color=color.WZ, texName="VV/VVV", directory=directories['boson'])

Data    = Run2016

flavorSelection = "((nGoodElectrons==2&&nGoodMuons==0)||(nGoodElectrons==0&&nGoodMuons==2))"
selection = "Sum$(lep_pt>40&&lep_tight>0)>0&&Sum$(lep_pt>20&&lep_tight>0)>1 && abs(Z_mass-91.2)<10 && nBTag>=2 && nJetSelected>=2 && Z_pt>100"
tr = triggerSelector(2016)

selection     = "&&".join([flavorSelection, selection])

## Sequence
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I,btagDeepCSV/F]", "njet/I","nJetSelected/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I",
                    "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I",
                    "Z_phi/F","Z_pt/F", "Z_mass/F", "Z_eta/F","Z_lldPhi/F", "Z_lldR/F"
                    ]

jetVars = ['eta','pt','phi','btagDeepCSV', 'hadronFlavour']

def getGenBs(genparts):
     allBs = []
     for g in genparts:
         if abs(g['pdgId']) == 5 and abs(g['motherId']) != 5: allBs.append(g)
     return allBs

def getBJetDR( event, sample ):
    jets = getJets(event, jetVars=jetVars, jetColl="jet")
    trueBJets = [ j for j in jets if abs(j['hadronFlavour'])==5 ]
    bjets = [ j for j in jets if j['btagDeepCSV']>0.6324 ]

    minDR = -1
    mindPhi = -1
    if len(bjets)>1:
        minDR = 999.
        mindPhi = 4.
        comb = itertools.combinations(bjets, 2)
        for c in comb:
            dR = deltaR(c[0], c[1])
            dPhi = deltaPhi(c[0]['phi'], c[1]['phi'])
            if dR < minDR:
                minDR = dR
                mindPhi = dPhi
                l1  = ROOT.TLorentzVector()
                l2  = ROOT.TLorentzVector()
                l1.SetPtEtaPhiM( c[0]['pt'], c[0]['eta'], c[0]['phi'], 0)
                l2.SetPtEtaPhiM( c[1]['pt'], c[1]['eta'], c[1]['phi'], 0)
                M = (l1 + l2).M()
    event.bjet_dR = minDR
    event.bjet_dPhi = mindPhi
    event.bjet_invMass = M
    return
    ##

def getGenBs( event, sample ):
    gPart = getGenPartsAll(event)
    bs = getGenBs(gPart)
    nBFromGlu = len( [ b for b in bs if (abs(b['motherId'])<5 or abs(b['motherId'])==2212 or abs(b['motherId'])==21) ] )

    event.nBFromGlu = nBFromGlu

sequence = [getBJetDR]

## Plotting
lumi_scale = 35.9
noData = args.noData
small = args.small

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
    ext = "_small" if small else ""
    ext += "_log" if log else ""
    plot_directory_ = os.path.join(plot_directory, 'gluonSplitting', 'test_Zpt100_nBTag2p%s'%ext)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      extensions_ = ["pdf", "png", "root"]

      plotting.draw(plot,
        plot_directory = plot_directory_,
        extensions = extensions_,
        ratio = {'yRange':(0.1,1.9)} if not noData else None,
        logX = False, logY = log, sorting = False,
        yRange = (0.03, "auto") if log else (0.001, "auto"),
        legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
        drawObjects = drawObjects( not noData, dataMCScale , lumi_scale ),
        copyIndexPHP = True,
      )

# Samples
DY_HT_LO.read_variables = [VectorTreeVariable.fromString('jet[hadronFlavour/I]') ] 

DY_twoTrueBsFromG = copy.deepcopy(DY_HT_LO)
DY_twoTrueBsFromG.color = ROOT.kYellow+1
DY_twoTrueBsFromG.texName = "DY (LO), N_{true b-jets}#geq2, from g"

DY_twoTrueBsFromP = copy.deepcopy(DY_HT_LO)
DY_twoTrueBsFromP.color = ROOT.kOrange+8
DY_twoTrueBsFromP.texName = "DY (LO), N_{true b-jets}#geq2, from p"

DY_twoTrueBsFromQ = copy.deepcopy(DY_HT_LO)
DY_twoTrueBsFromQ.color = ROOT.kRed-3
DY_twoTrueBsFromQ.texName = "DY (LO), N_{true b-jets}#geq2, from q"

DY_twoTrueBsElse = copy.deepcopy(DY_HT_LO)
DY_twoTrueBsElse.color = ROOT.kRed+3
DY_twoTrueBsElse.texName = "DY (LO), N_{true b-jets}#geq2, else"

DY_oneTrueBs = copy.deepcopy(DY_HT_LO)
DY_oneTrueBs.color = ROOT.kGreen+1
DY_oneTrueBs.texName = "DY (LO), N_{true b-jets}=1"

DY_fakeBs = copy.deepcopy(DY_HT_LO)
DY_fakeBs.color = ROOT.kGreen+3
DY_fakeBs.texName = "DY (LO), N_{true b-jets}=0"


mc = [DY_twoTrueBsElse, DY_twoTrueBsFromG, DY_twoTrueBsFromP, DY_twoTrueBsFromQ, DY_oneTrueBs, DY_fakeBs,TTX,boson, Top]
for s in mc:
    s.setSelectionString([getFilterCut(isData=False), tr.getSelection("MC")])
    s.read_variables = ['reweightPU36fb/F', 'reweightBTagDeepCSV_SF/F']
    s.weight         = lambda event, s: event.reweightBTagDeepCSV_SF*event.reweightPU36fb
    s.style = styles.fillStyle(s.color)
    s.scale = lumi_scale

nBFromG = "Sum$(abs(genPartAll_pdgId)==5&&abs(genPartAll_motherId)>5&&(abs(genPartAll_motherId)==21))"
nBFromP = "Sum$(abs(genPartAll_pdgId)==5&&abs(genPartAll_motherId)>5&&(abs(genPartAll_motherId)==2212))"
nBFromQ = "Sum$(abs(genPartAll_pdgId)==5&&abs(genPartAll_motherId)<5)"

DY_twoTrueBsFromG.addSelectionString(["Sum$(jet_pt>30&&abs(jet_eta)<2.4&&jet_id>0&&jet_btagDeepCSV>0.6324&&jet_hadronFlavour==5)>=2 && %s>=2"%nBFromG])
DY_twoTrueBsFromP.addSelectionString(["Sum$(jet_pt>30&&abs(jet_eta)<2.4&&jet_id>0&&jet_btagDeepCSV>0.6324&&jet_hadronFlavour==5)>=2 && %s>=2 && %s<2"%(nBFromP,nBFromG)])
DY_twoTrueBsFromQ.addSelectionString(["Sum$(jet_pt>30&&abs(jet_eta)<2.4&&jet_id>0&&jet_btagDeepCSV>0.6324&&jet_hadronFlavour==5)>=2 && %s>=2 && %s<2 && %s<2"%(nBFromQ,nBFromP,nBFromG)])
DY_twoTrueBsElse.addSelectionString(["Sum$(jet_pt>30&&abs(jet_eta)<2.4&&jet_id>0&&jet_btagDeepCSV>0.6324&&jet_hadronFlavour==5)>=2 && %s<2 && %s<2 && %s<2"%(nBFromG,nBFromQ,nBFromP)])
DY_oneTrueBs.addSelectionString(["Sum$(jet_pt>30&&abs(jet_eta)<2.4&&jet_id>0&&jet_btagDeepCSV>0.6324&&jet_hadronFlavour==5)==1"])
DY_fakeBs.addSelectionString(["Sum$(jet_pt>30&&abs(jet_eta)<2.4&&jet_id>0&&jet_btagDeepCSV>0.6324&&jet_hadronFlavour==5)==0"])


Data.setSelectionString([getFilterCut(isData=True)])
Data.style          = styles.errorStyle(ROOT.kBlack)

if small:
    for s in mc + [Data]:
        s.reduceFiles( to = 1 )

stack = Stack(mc, Data)

weight_ = lambda event, sample: event.weight

Plot.setDefaults(stack = stack, weight = weight_, selectionString = selection, addOverFlowBin='upper')

plots = []

plots.append(Plot(
  name = 'dl_mass', texX = 'M(ll) (GeV)', texY = 'Number of Events',
  attribute = TreeVariable.fromString( "Z_mass/F" ),
  binning=[21,80.70,101.70],
))

plots.append(Plot(
  name = 'nBTag', texX = 'N_{b-tag}', texY = 'Number of Events',
  attribute = TreeVariable.fromString( "nBTag/I" ),
  binning=[4,-0.5,3.5],
))

plots.append(Plot(
  name = 'nJetSelected', texX = 'N_{jets}', texY = 'Number of Events',
  attribute = TreeVariable.fromString( "nJetSelected/I" ),
  binning=[8,-0.5,7.5],
))

plots.append(Plot(
    name = 'bjet_dR',
    texX = '#DeltaR(b-tagged jets)', texY = 'Number of Events',
    attribute = lambda event, sample:event.bjet_dR,
    binning=[20,0,4],
))

plots.append(Plot(
    name = 'bjet_dPhi',
    texX = '#Delta#Phi(b-tagged jets)', texY = 'Number of Events',
    attribute = lambda event, sample:event.bjet_dPhi,
    binning=[16,0,3.2],
))

plots.append(Plot(
    name = 'bjet_invMass',
    texX = 'M(bb)', texY = 'Number of Events',
    attribute = lambda event, sample:event.bjet_invMass,
    binning=[50,0,400],
))

plots.append(Plot(
    texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "met_pt/F" ),
    binning=[400/20,0,400],
))

plots.append(Plot(
    texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 20 GeV',
    attribute = TreeVariable.fromString( "Z_pt/F" ),
    binning=[20,0,400],
))

plots.append(Plot(
    name = "cosThetaStar", texX = 'cos#theta(l*)', texY = 'Number of Events / 0.2',
    attribute = TreeVariable.fromString( "cosThetaStar/F" ),
    binning=[10,-1,1],
))


plotting.fill(plots, read_variables = read_variables, sequence = sequence)

dataMCScale = 1
drawPlots(plots, dataMCScale)

