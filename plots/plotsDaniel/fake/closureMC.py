''' Analysis script for 1D 2l plots (RootTools)
'''

#Standard imports
import ROOT
from math import sqrt, cos, sin, pi, acos
import itertools,os
import copy
from operator import mul


import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
args = argParser.parse_args()


#RootTools
from RootTools.core.standard import *

from TopEFT.Tools.user              import data_directory
from TopEFT.samples.color           import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.helpers import getObjDict, getCollection, getObjFromFile


#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--plot_directory',      action='store',      default='94X_nonpromptClosure')
argParser.add_argument('--selection',           action='store',      default='njet0p-btag0p')
argParser.add_argument('--year',                action='store',      default=2017,   type=int,  help="Which year?" )
args = argParser.parse_args()

# Logger
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

# Samples
data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_mva_v7/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2016_mva_v7/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *

data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2017_mva_v7/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v7/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *

postProcessing_directory = "TopEFT_PP_2017_mva_v8/trilep/"
dirs = {}
dirs['DY']   = ["DYJetsToLL_M50_ext"]
dirs['TTbar']   = ["TTLep_pow"]
directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

DY  = Sample.fromDirectory(name="DY", treeName="Events", isData=False, color=color.DY, texName="DY", directory=directories['DY'])
TT  = Sample.fromDirectory(name="TT", treeName="Events", isData=False, color=0, texName="t#bar{t}", directory=directories['TTbar'])


sample = TT
#sample = DY_HT_LO_17 if args.year == 2017 else DY_HT_LO
#sample = TTLep_pow_17 if args.year == 2017 else TTLep_pow


# Trigger
from TopEFT.Tools.triggerSelector import triggerSelector
tr = triggerSelector(args.year)



# Event selection
nonpromptSelection  = "nLeptons_FO_3l>=3    && Sum$((lep_tight_3l*(lep_pt - lep_ptCorr) + lep_ptCorr)>40&&lep_FO_3l>0)>0&&Sum$((lep_tight_3l*(lep_pt - lep_ptCorr) + lep_ptCorr)>20&&lep_FO_3l>0)>1&&Sum$((lep_tight_3l*(lep_pt - lep_ptCorr) + lep_ptCorr)>10&&lep_FO_3l>0)>2 && !(nLeptons_tight_4l>=4) && nLeptons_tight_3l<3"
promptSelection     = "nLeptons_tight_3l==3 && nLeptons_FO_3l_genPrompt<=2 && Sum$(lep_pt>40&&lep_tight_3l>0)>0&&Sum$(lep_pt>20&&lep_tight_3l>0)>1&&Sum$(lep_pt>10&&lep_tight_3l>0)>2 && !(nLeptons_tight_4l>=4)"
#np_sel_string       = "&&".join([getFilterCut(isData=False, year=args.year), tr.getSelection("MC"), nonpromptSelection, cutInterpreter.cutString(args.selection), "abs(Z_mass - 91.2)<10"])
#sel_string          = "&&".join([getFilterCut(isData=False, year=args.year), tr.getSelection("MC"), promptSelection, cutInterpreter.cutString(args.selection), "abs(Z_mass - 91.2)<10 && Z_fromTight>0"])
np_sel_string       = "&&".join([getFilterCut(isData=False, year=args.year), tr.getSelection("MC"), nonpromptSelection, cutInterpreter.cutString(args.selection)])
sel_string          = "&&".join([getFilterCut(isData=False, year=args.year), tr.getSelection("MC"), promptSelection, cutInterpreter.cutString(args.selection)])


# weights
weight_central = "weight*reweightPU36fb*reweightBTagDeepCSV_SF*41.2"

# preparation for looper
loose_ID = "FO_3l"
tight_ID = "tight_3l"
nLeptons = 3

variables = map( TreeVariable.fromString, ["run/I", "lumi/I", "evt/I", "Z_pt/F", "cosThetaStar/F", "weight/F", "met_pt/F", "Z_mass/F", "nJetSelected/I", "nBTag/I", 'Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I', 'nonZ_l2_index/I', 'met_pt/F', 'nMuons_FO_3l/I'])
if not sample.isData: variables += map( TreeVariable.fromString, ['reweightPU36fb/F', 'reweightBTagDeepCSV_SF/F' ] )
variables += [VectorTreeVariable.fromString('lep[pt/F,ptCorr/F,eta/F,phi/F,FO_3l/I,tight_3l/I,FO_SS/I,tight_SS/I,jetPtRatiov2/F,pdgId/I]')]

# Get histograms directly from MC
plotvars = ["Z_mass", "nJetSelected", "met_pt", "nBTag", "nMuons_FO_3l", "lep_pt_trail"]
hists = {}
hists_pred = {}

hists["Z_mass"]     = sample.get1DHistoFromDraw( "Z_mass", selectionString = sel_string, binning = [20,80,100],  addOverFlowBin = 'upper', weightString = weight_central )
hists["met_pt"]     = sample.get1DHistoFromDraw( "met_pt", selectionString = sel_string, binning = [20,0,200],  addOverFlowBin = 'upper', weightString = weight_central )
hists["nJetSelected"]     = sample.get1DHistoFromDraw( "nJetSelected", selectionString = sel_string, binning = [8,0,8],  addOverFlowBin = 'upper', weightString = weight_central )
hists["nBTag"]     = sample.get1DHistoFromDraw( "nBTag", selectionString = sel_string, binning = [4,0,4],  addOverFlowBin = 'upper', weightString = weight_central )
hists["nMuons_FO_3l"] = sample.get1DHistoFromDraw( "nMuons_tight_3l", selectionString = sel_string, binning = [4,0,4],  addOverFlowBin = 'upper', weightString = weight_central )
hists["lep_pt_trail"] = sample.get1DHistoFromDraw( "lep_pt[2]", selectionString = sel_string, binning = [10,0,100],  addOverFlowBin = 'upper', weightString = weight_central )

# Run the tree reader for cases with more complicated plots
hists["lep_pt_trail"].Reset()
sample.setSelectionString(sel_string)
reader = sample.treeReader( variables = variables )
reader.start()
while reader.run():
    nLep = len([ l for l in reader.event.lep_pt if l > 0])
    lep = [getObjDict(reader.event, "lep"+'_', ["pt", "ptCorr", "eta", "phi", "FO_3l", "FO_SS", "tight_3l", "tight_SS", "pdgId","jetPtRatiov2"], i) for i in range(nLep) ]

    # get the relevant leptons
    lep = [ l for l in lep if l[tight_ID] ]

    if len(lep) != nLeptons: print "bug"
    allweights = ["weight", "reweightPU36fb", "reweightBTagDeepCSV_SF"]

    if sample.isData:
        weight = 1
    else:
        weights = [ getattr( reader.event, w ) for w in allweights ]
        weight = reduce(mul, weights, 1)
    
    hists["lep_pt_trail"].Fill(lep[2]['pt'], ( weight * 41.2 ))




for var in plotvars:
    hists_pred[var] = hists[var].Clone()
    hists_pred[var].Reset()


# Get the nonprompt prediction
muFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/muFR_all.root")
elFile = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Tools/data/FRData/elFR_all.root")
muMap = getObjFromFile(muFile, "passed")
elMap = getObjFromFile(elFile, "passed")

sample.setSelectionString(np_sel_string)
reader = sample.treeReader( variables = variables )
reader.start()
while reader.run():
    nLep = len([ l for l in reader.event.lep_pt if l > 0])
    lep = [getObjDict(reader.event, "lep"+'_', ["pt", "ptCorr", "eta", "phi", "FO_3l", "FO_SS", "tight_3l", "tight_SS", "pdgId","jetPtRatiov2"], i) for i in range(nLep) ]

    # get the relevant leptons
    lep = [ l for l in lep if l[loose_ID] ]

    # get tight and loose separately
    looseNotTight   = [ l for l in lep if not l[tight_ID] ]
    tight           = [ l for l in lep if l[tight_ID] ]
    nLooseNotTight  = len( looseNotTight )
    nTight          = len( tight )

    # Really get ALL possible combinations.
    allCombinations = itertools.combinations(tight+looseNotTight, nLeptons)

    for comb in allCombinations:
        FR = 1.
        nLooseNotTight = 0
        pts = [ l['pt'] if l[tight_ID] else l['ptCorr'] for l in comb ]
        pts = sorted(pts, reverse=True)
        for l in comb:
            if l[tight_ID]:
                continue
            else:
                if abs(l['pdgId']) == 11: FRmap = elMap
                elif abs(l['pdgId']) == 13: FRmap = muMap
                else: raise NotImplementedError
                ptCut = 45. if sample.isData else 99.
                ptCorrected = l['ptCorr'] if l['ptCorr'] < ptCut else (ptCut-1)
                #print ptCorrected
                FR_from_map = FRmap.GetBinContent(FRmap.FindBin(ptCorrected, abs(l['eta'])))
                if sample.isData:
                    FR *= FR_from_map/(1-FR_from_map)
                else:
                    FR *= FR_from_map
                nLooseNotTight += 1

        FR *= (-1)**(nLooseNotTight+1)

        allweights = ["weight", "reweightPU36fb", "reweightBTagDeepCSV_SF"]

        if sample.isData:
            weight = 1
        else:
            weights = [ getattr( reader.event, w ) for w in allweights ]
            weight = reduce(mul, weights, 1)

        for var in plotvars:
            if not var == "lep_pt_trail":
                hists_pred[var].Fill(getattr(reader.event, var), ( weight * FR * 41.2 ))
            else:
                hists_pred[var].Fill(pts[2], ( weight * FR * 41.2 ))


def drawObjects( ):
        tex = ROOT.TLatex()
        tex.SetNDC()
        tex.SetTextSize(0.04)
        tex.SetTextAlign(11) # align right
        lines = [
          (0.15, 0.95, 'CMS Simulation'),
          (0.65, 0.95, '%s MC (13 TeV)'%args.year )
        ]
        return [tex.DrawLatex(*l) for l in lines]

texX = {
    "Z_mass": "M(ll) (GeV)",
    "met_pt": "E_{T}^{miss} (GeV)",
    "nJetSelected": "N_{jet}",
    "nBTag": "N_{b-tag}",
    "nMuons_FO_3l": "N_{#mu}",
    "lep_pt_trail": "p_{T}(trailing l) (GeV)",
    }

for var in plotvars:
    hists[var].style      = styles.errorStyle( ROOT.kBlack )
    hists_pred[var].style = styles.fillStyle( ROOT.kBlue-1 )
    
    
    hists[var].legendText = sample.texName
    hists_pred[var].legendText = "prediction"
    
    plots = [[ hists_pred[var] ], [hists[var]] ]
    
    print plots
    plotting.draw(
        Plot.fromHisto("%s_%s"%(sample.name, var),
                    plots,
                    texX = texX[var]
                ),
        plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/nonprompt/",
        logX = False, logY = False, sorting = True,
        #yRange = (0.008,3.),
        ratio = {'yRange': (0.1, 2.4), 'texX':'MC/pred'},
        drawObjects = drawObjects(),
        copyIndexPHP = True
    )


