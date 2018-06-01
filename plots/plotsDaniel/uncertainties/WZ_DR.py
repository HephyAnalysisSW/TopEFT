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
from TopEFT.Tools.helpers           import deltaR, deltaR2
from TopEFT.Tools.objectSelection   import getJets
import TopEFT.Tools.logger as logger

import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)


data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v7/trilep/"

dirs = {}
dirs['WZTo3LNu_amcatnlo']   = ["WZTo3LNu_amcatnlo"]
dirs['WZTo3LNu']     = ['WZTo3LNu_comb']
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

WZ_amc  = Sample.fromDirectory(name="WZTo3LNu_amcatnlo", treeName="Events", isData=False, color=color.TTJets, texName="WZ MG (NLO)", directory=directories['WZTo3LNu_amcatnlo'])
WZ_pow = Sample.fromDirectory(name="WZTo3LNu_powheg", treeName="Events", isData=False, color=color.TTJets, texName="WZ powheg (NLO)", directory=directories['WZTo3LNu'])


selection = cutInterpreter.cutString('trilep-Zcand-lepSelTTZ-njet3p-btag1p-onZ')
WZselection = cutInterpreter.cutString('trilep-Zcand-lepSelTTZ-njet2p-btag2p-onZ')

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


weight_central  = "weight*reweightBTagDeepCSV_SF*reweightPU36fb*reweightTrigger_tight_3l*reweightLeptonTrackingSF_tight_3l*35.9"
reweight        = weight_central #+ "*((Sum$(abs(%s)==5)>0)*%s+(Sum$(abs(%s)==5)==0))"%(trueVar,'0.5',trueVar)

sample = WZ_pow

jetVars = ['eta','pt','phi','btagDeepCSV', 'hadronFlavour']

variables = map( TreeVariable.fromString, ["run/I", "lumi/I", "evt/I", "Z_pt/F", "cosThetaStar/F", "weight/F", "met_pt/F", "Z_mass/F", "nJetSelected/I", "nBTag/I", 'Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I', 'nonZ_l2_index/I', 'njet/I'])
variables += map( TreeVariable.fromString, ['reweightPU36fb/F', 'reweightBTagDeepCSV_SF/F' ] )
variables += [VectorTreeVariable.fromString('lep[pt/F,ptCorr/F,eta/F,phi/F,FO_3l/I,tight_3l/I,FO_SS/I,tight_SS/I,jetPtRatiov2/F,pdgId/I]')]
variables += [VectorTreeVariable.fromString('jet[pt/F,eta/F,phi/F,btagDeepCSV/F,hadronFlavour/I]')]

h_DR_reco = ROOT.TH1F("deltaR_reco","", 20,0,4.)
h_DR_true = ROOT.TH1F("deltaR_true","", 20,0,4.)


sample.setSelectionString([WZselection])
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


h_DR_true.style         = styles.lineStyle( ROOT.kGreen+1, width=2 )
h_DR_reco.style         = styles.lineStyle( ROOT.kOrange+1, width=2 )

h_DR_true.legendText        = "true b-jets"
h_DR_reco.legendText        = "fake b-jets"


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

plots = [[ h_DR_true ], [h_DR_reco]]

plotting.draw(
    Plot.fromHisto("WZ_dR_2b_true_fake",
                plots,
                texX = "#DeltaR(b-jets)"
            ),
    plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/WZ/",
    logX = False, logY = False, sorting = True, 
    drawObjects = drawObjects(),
    copyIndexPHP = True
)

