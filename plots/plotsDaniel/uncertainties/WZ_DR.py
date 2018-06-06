''' Analysis script for 1D 2l plots (RootTools)
'''

#Standard imports
import ROOT
from math import sqrt, cos, sin, pi, acos
import itertools,os
import copy

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
args = argParser.parse_args()


#RootTools
from RootTools.core.standard import *
from TopEFT.Tools.user import data_directory

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_v14/trilep/"

from TopEFT.samples.color           import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter
from TopEFT.Tools.helpers import closestOSDLMassToMZ, checkRootFile, writeObjToFile, deltaR, bestDRMatchInCollection, deltaPhi, mZ, cosThetaStar, getGenZ, getGenPhoton, getGenB, getSortedZCandidates, getMinDLMass
from TopEFT.Tools.objectSelection import getGoodBJets, getGoodJets, isBJet, isAnalysisJet, getGoodPhotons, getGenPartsAll, getAllJets, getJets
import TopEFT.Tools.logger as logger

import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

def getGenBs(genparts):
     allBs = []
     for g in genparts:
         if abs(g['pdgId']) == 5 and abs(g['motherId']) != 5: allBs.append(g)
     return allBs


data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v7/trilep/"

dirs = {}
dirs['WZTo3LNu_amcatnlo']   = ["WZTo3LNu_amcatnlo"]
dirs['WZTo3LNu']     = ['WZTo3LNu_comb']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

WZ_amc  = Sample.fromDirectory(name="WZTo3LNu_amcatnlo", treeName="Events", isData=False, color=color.TTJets, texName="WZ MG (NLO)", directory=directories['WZTo3LNu_amcatnlo'])
WZ_pow = Sample.fromDirectory(name="WZTo3LNu_powheg", treeName="Events", isData=False, color=color.TTJets, texName="WZ powheg (NLO)", directory=directories['WZTo3LNu'])

### DY dilep samples (older processing...) ###
data_directory = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v2/dilep/"

dirs = {}
dirs['DYJetsToLL_M50_LO_ext_comb']   = ["DYJetsToLL_M50_LO_ext_comb"]
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

DYJetsToLL_M50_LO_ext_comb  = Sample.fromDirectory(name="DYJetsToLL_M50_LO_ext_comb", treeName="Events", isData=False, color=color.TTJets, texName="DY (LO)", directory=directories['DYJetsToLL_M50_LO_ext_comb'])

## selections and plotting

selection = cutInterpreter.cutString('trilep-Zcand-lepSelTTZ-njet3p-btag1p-onZ')
WZselection = cutInterpreter.cutString('trilep-Zcand-lepSelTTZ-njet2p-btag2p-onZ')
DYselection = cutInterpreter.cutString('njet2p-btag2p-onZ')
DYselection += "&&Sum$(lep_pt>40&&lep_tight>0)>0 && Sum$(lep_pt>20&&lep_tight>0)>1 && Z_pt > 100 "#&& Sum$(jet_pt>30&&abs(jet_eta)<2.4&&jet_id>0&&jet_btagDeepCSV>0.6324&&jet_hadronFlavour==5)>=2"

trueVar = "jet_hadronFlavour"
#trueVar = "jet_mcFlavour"

#oneTrueB = "Sum$(jet_btagDeepCSV>0.6324&&abs(%s)==5)==1"
#moreTrueB = "Sum$(jet_btagDeepCSV>0.6324&&abs(%s)==5)>1"
oneTrueB = "Sum$(abs(%s)==5)==1"%trueVar
moreTrueB = "Sum$(abs(%s)==5)>1"%trueVar
trueCs = "Sum$(abs(%s)==4)>=1"%trueVar
onlyTrueB = "(Sum$(jet_btagDeepCSV>0.6324)==Sum$(jet_btagDeepCSV>0.6324&&abs(%s)==5))"%trueVar

oneFakeB = "Sum$(jet_btagDeepCSV>0.6324&&abs(%s)!=5)==1"%trueVar
moreFakeB = "Sum$(jet_btagDeepCSV>0.6324&&abs(%s)!=5)>1"%trueVar
#onlyFakeB = "(Sum$(jet_btagDeepCSV>0.6324)==Sum$(jet_btagDeepCSV>0.6324&&abs(%s)!=5))"%trueVar
onlyFakeB = "Sum$(abs(%s)==5)==0"%trueVar
onlyFakeB_noC = "Sum$(abs(%s)==5)==0&&Sum$(abs(%s)==4)==0"%(trueVar, trueVar)


#weight_central  = "weight*reweightBTagDeepCSV_SF*reweightPU36fb*reweightTrigger_tight_3l*reweightLeptonTrackingSF_tight_3l*35.9"
weight_central  = "weight*reweightBTagDeepCSV_SF*reweightPU36fb"
reweight        = weight_central #+ "*((Sum$(abs(%s)==5)>0)*%s+(Sum$(abs(%s)==5)==0))"%(trueVar,'0.5',trueVar)

#sample = WZ_pow
sample = DYJetsToLL_M50_LO_ext_comb

jetVars = ['eta','pt','phi','btagDeepCSV', 'hadronFlavour']

variables = map( TreeVariable.fromString, ["run/I", "lumi/I", "evt/I", "Z_pt/F", "cosThetaStar/F", "weight/F", "met_pt/F", "Z_mass/F", "nJetSelected/I", "nBTag/I", 'Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I', 'nonZ_l2_index/I', 'njet/I'])
variables += map( TreeVariable.fromString, ['reweightPU36fb/F', 'reweightBTagDeepCSV_SF/F' ] )
#variables += [VectorTreeVariable.fromString('lep[pt/F,ptCorr/F,eta/F,phi/F,FO_3l/I,tight_3l/I,FO_SS/I,tight_SS/I,jetPtRatiov2/F,pdgId/I]')]
variables += [VectorTreeVariable.fromString('lep[pt/F,eta/F,phi/F,tight/I,jetPtRatiov2/F,pdgId/I]')]
variables += [VectorTreeVariable.fromString('jet[pt/F,eta/F,phi/F,btagDeepCSV/F,hadronFlavour/I]')]
variables += [VectorTreeVariable.fromString('genPartAll[eta/F,pt/F,phi/F,mass/F,charge/I,status/I,pdgId/I,motherId/I,grandmotherId/I,nDaughters/I,daughterIndex1/I,daughterIndex2/I,nMothers/I,motherIndex1/I,motherIndex2/I,isPromptHard/I]',nMax=400)]
variables += map(TreeVariable.fromString, ['ngenPartAll/I','run/I','evt/I','lumi/I'])

h_DR_reco = ROOT.TH1F("deltaR_reco","", 20,0,4.)
h_DR_true = ROOT.TH1F("deltaR_true","", 20,0,4.)
h_DR_true_fromG = ROOT.TH1F("deltaR_true_fromG","", 20,0,4.)

sample.setSelectionString([DYselection])
reader = sample.treeReader( variables = variables )
reader.start()
while reader.run():
    r = reader.event
    # get all jets
    jets = getJets(r, jetVars=jetVars, jetColl="jet")
    # get jets with hadronFlavour == 5
    #trueBJets = [ j for j in jets if abs(j['hadronFlavour'])==5 ]
    #recoBJets = [ j for j in jets if j['btagDeepCSV']>0.6324 ]
    trueBJets = [ j for j in jets if (abs(j['hadronFlavour'])==5 and j['btagDeepCSV']>0.6324) ]
    recoBJets = [ j for j in jets if (abs(j['hadronFlavour'])<5 and j['btagDeepCSV']>0.6324) ]
    
    bjets = recoBJets
    
    gPart = getGenPartsAll(r)
    bs = getGenBs(gPart)
    
    bsFromG = [ b for b in bs if abs(b['motherId']) == 21 ]
    
    if len(recoBJets)>1:
        minDR = 999.
        comb = itertools.combinations(recoBJets, 2)
        for c in comb:
            dR = deltaR(c[0], c[1])
            if dR < minDR: minDR = dR
        
        minDR = 3.9 if minDR > 4 else minDR
        h_DR_reco.Fill(minDR, r.weight)

    if len(trueBJets)>1:
        minDR = 999.
        comb = itertools.combinations(trueBJets, 2)
        for c in comb:
            dR = deltaR(c[0], c[1])
            if dR < minDR: minDR = dR

        minDR = 3.9 if minDR > 4 else minDR
        h_DR_true.Fill(minDR, r.weight)
        if len(bsFromG) > 1:
            h_DR_true_fromG.Fill(minDR, r.weight)
            #print
            #for b in bsFromG:
            #    print "b from G"
            #    print b['motherIndex1'], b['motherIndex2']
            #    print gPart[b['motherIndex1']]['pdgId'],    gPart[b['motherIndex2']]['pdgId']
            #    print gPart[b['motherIndex1']]['pt'],       gPart[b['motherIndex2']]['pt']


h_DR_true.style         = styles.lineStyle( ROOT.kGreen+1, width=2 )
h_DR_reco.style         = styles.lineStyle( ROOT.kOrange+1, width=2 )
h_DR_true_fromG.style         = styles.lineStyle( ROOT.kBlue+1, width=2 )

h_DR_true.legendText        = "true b-jets"
h_DR_reco.legendText        = "fake b-jets"
h_DR_true_fromG.legendText  = "true b-jets from g"

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

plots = [[ h_DR_true ], [h_DR_reco], [h_DR_true_fromG]]

plotting.draw(
    Plot.fromHisto("DY_dR_2b_true_fake_trueFromG_Zpt100",
                plots,
                texX = "#DeltaR(b-jets)"
            ),
    plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/WZ/",
    logX = False, logY = False, sorting = True, 
    drawObjects = drawObjects(),
    copyIndexPHP = True
)

