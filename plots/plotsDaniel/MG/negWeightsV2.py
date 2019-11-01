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


from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter
import TopEFT.Tools.logger as logger

import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

T2tt_1500_NNLOPDF_CP5   = Sample.fromDirectory(name='T2tt_1500_NNLOPDF_CP5', treeName='Events', isData=False, color=color.TTJets, texName='T2tt (1500,100)', directory=['/afs/hephy.at/data/dspitzbart01/gen/T2tt_mStop1500_NNLOPDF_update_CP5_v2'])

T1tttt_2000_NNLOPDF_CP5   = Sample.fromDirectory(name='T1tttt_2000_NNLOPDF_CP5', treeName='Events', isData=False, color=color.TTJets, texName='T2tt (1500,100)', directory=['/afs/hephy.at/data/dspitzbart01/gen/T1tttt_mGl2000_NNLOPDF_update_CP5_v2'])

sample = T2tt_1500_NNLOPDF_CP5

#sample.reduceFiles(to = 1)

# binning
#binning = [50,0,1500]
#binning = [25,0,2500]
#binning = [12,2,14]
#binning = [20, 1000, 5000]
binning = [20, 500, 3500]
#binning = [20, 1000, 5000]

weight = "(1)"
#weight = "abs(LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[578])"

met = "recoGenMETs_genMetTrue__SIM.obj.pt()"
njet = "Sum$(recoGenJets_ak4GenJets__SIM.obj.pt()>30&&abs(recoGenJets_ak4GenJets__SIM.obj.eta()<2.4))"
ht = "Sum$((recoGenJets_ak4GenJets__SIM.obj.pt()>30&&abs(recoGenJets_ak4GenJets__SIM.obj.eta()<2.4))*recoGenJets_ak4GenJets__SIM.obj.pt())"

var = ht


# central weight index for different PDF sets
CT14_nnlo   = 223
CT14_nlo    = 282
PDF4LHC_nlo = 475
PDF4LHC_nnlo= 578
NNPDF31_lo  = 1077 # as 0130
NNPDF30_lo  = 1078 # 1079 actually (as 0130)
NNPDF30_nlo = 972
NNPDF31_nnlo= 9
NNPDF31_nlo = 120


print "Working on central values"

## plots for T2tt. everything super dirty ##
h_NNLO_update   = sample.get1DHistoFromDraw( var, selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = "LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[9]" )

h_NNLO_update.style = styles.lineStyle( ROOT.kGreen+1, width=3, errors=True )

#h_all.Scale(1/h_all.Integral())

# get the variations
replicas = range(10,110) #NNPDF3.1nnlo
#replicas = replicas[:10]
#replicas = range(476,576) #PDF4LHC15 nlo
#replicas = range(121,221) #NNPDF3.1nlo
#replicas = range(579,679) #PDF4LHC15 nnlo

#alphaS = [110,111]
#alphaS = [576,577]
#alphaS = [221,222]
#alphaS = [679,680]

variations = []
variationsNLO = []
for rep in replicas:
    print "Working on replica %s"%rep

    #v_LO = T2tt_1500_LOPDF_CP2.get1DHistoFromDraw( var, selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = "LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[%s]"%rep )
    #variations.append(v_LO)

    v = sample.get1DHistoFromDraw( var, selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = "(LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[%s]>0)*LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[%s]"%(rep,rep) )
    variationsNLO.append(v)

variationsNLO.sort( key = lambda x: x.Integral() )

h_NNLO_central = h_NNLO_update.Clone()

from numpy import median

inclusive = True

uncNLO = []
for b in range(binning[0]+1):

    if inclusive:
        central = (variationsNLO[49].GetBinContent(b+1) + variationsNLO[50].GetBinContent(b+1))/2.
        h_NNLO_central.SetBinContent(b+1,central)
        ## replicas
        u = {'up': variationsNLO[83].GetBinContent(b+1), 'central':central, 'down': variationsNLO[15].GetBinContent(b+1)}

    else:
        v = []
        for var in variationsNLO:
            varied = var.GetBinContent(b+1)# / scaleFactor

            ## positivity prescription
            if varied > 0:
                v.append(varied)
            else:
                v.append(0)
        v = sorted(v)

        ## redefine central as median of all variations
        central = median(v)

        u = {'up': v[84*len(variations)/100-1], 'central':central, 'down': v[16*len(variations)/100-1]}

    print u
    uncNLO.append(u)


h_NNLO_central.style = styles.lineStyle( ROOT.kGreen+1, width=1, errors=False )

boxesNLO = []
ratioBoxes = []
for ib in range(1, 1 + h_NNLO_update.GetNbinsX() ):
    val = h_NNLO_update.GetBinContent(ib)

    # uncertainty box in main histogram
    box = ROOT.TBox( h_NNLO_update.GetXaxis().GetBinLowEdge(ib),  max([0.00, uncNLO[ib-1]['down']]), h_NNLO_update.GetXaxis().GetBinUpEdge(ib), max([0.00, uncNLO[ib-1]['up']]) )
    box.SetLineColor(ROOT.kBlack)
    box.SetFillStyle(3005)
    box.SetFillColor(ROOT.kGreen+1)

    boxesNLO.append( box )

    ratioBox = ROOT.TBox( h_NNLO_update.GetXaxis().GetBinLowEdge(ib),  max([0.20, uncNLO[ib-1]['down']/h_NNLO_update.GetBinContent(ib)]), h_NNLO_update.GetXaxis().GetBinUpEdge(ib), min([max([0.00, uncNLO[ib-1]['up']/h_NNLO_update.GetBinContent(ib)]), 1.5]) )
    ratioBox.SetLineColor(ROOT.kBlack)
    ratioBox.SetFillStyle(3005)
    ratioBox.SetFillColor(ROOT.kGreen+1)
    
    ratioBoxes.append(ratioBox)
    

h_NNLO_update.legendText = "NNPDF3.1 NNLOpos, CP5"

h_NNLO_central.legendText = "NNPDF3.1 NNLOpos, median"


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

plots = [[ h_NNLO_update ], [h_NNLO_central]]

ROOT.gStyle.SetHatchesSpacing(0.3)
ROOT.gStyle.SetHatchesLineWidth(2)

plotting.draw(
    Plot.fromHisto("%s_ht30_NNPDF31_NNLOPDF_pos_inclusiveAlt"%sample.name,
                plots,
                #texX = "E_{T}^{miss} (GeV)"
                #texX = "N_{jet}"
                texX = "H_{T} (GeV)"
            ),
    plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/MG/weights_update/",
    logX = False, logY = True, #sorting = True, 
    ratio = {'yRange': (0.2, 1.5),'texY':'median/central', 'histos':[(1,0)], 'drawObjects':ratioBoxes},
    drawObjects = drawObjects() + boxesNLO,
    copyIndexPHP = True
)

