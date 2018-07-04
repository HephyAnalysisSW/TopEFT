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


#from TopEFT.samples.heppy_dpm_samples import *
#DY_HT2500 = Fall17_heppy_mapper.from_heppy_samplename("DYJetsToLL_M50_HT2500toInf")
#DY_LO = Fall17_heppy_mapper.from_heppy_samplename("DYJetsToLL_M50_LO")


#from TopEFT.samples.private_dpm_samples import *
#TT_l_from_t = Fall17_heppy_mapper.from_heppy_samplename(Fall17_heppy_mapper.heppy_sample_names[0])

T2tt_1200   = Sample.fromDirectory(name='T2tt_1200', treeName='Events', isData=False, color=color.TTJets, texName='T2tt (1200,100)', directory=['/afs/hephy.at/data/dspitzbart01/gen/T2tt_mStop1200'])
T2tt_1500   = Sample.fromDirectory(name='T2tt_1500', treeName='Events', isData=False, color=color.TTJets, texName='T2tt (1500,100)', directory=['/afs/hephy.at/data/dspitzbart01/gen/T2tt_mStop1500'])
T1tttt_2000 = Sample.fromDirectory(name='T1tttt_2000', treeName='Events', isData=False, color=color.TTJets, texName='T1tttt (2000,100)', directory=['/afs/hephy.at/data/dspitzbart01/gen/T1tttt_mGlu2000'])
T1tttt_2000_CP1 = Sample.fromDirectory(name='T1tttt_2000_CP1', treeName='Events', isData=False, color=color.TTJets, texName='T1tttt CP1 (2000,100)', directory=['/afs/hephy.at/data/dspitzbart01/gen/T1tttt_mGlu2000_CP1'])
T1tttt_1000 = Sample.fromDirectory(name='T1tttt_1000', treeName='Events', isData=False, color=color.TTJets, texName='T1tttt (1000,100)', directory=['/afs/hephy.at/data/dspitzbart01/gen/T1tttt_mGlu1000'])
T1tttt_1000_CP1 = Sample.fromDirectory(name='T1tttt_1000_CP1', treeName='Events', isData=False, color=color.TTJets, texName='T1tttt CP1 (1000,100)', directory=['/afs/hephy.at/data/dspitzbart01/gen/T1tttt_mGlu1000_CP1'])

# binning
#binning = [50,0,1500]
#binning = [25,0,1500]
#binning = [20,0,20]
#binning = [20, 1000, 5000]
binning = [20, 500, 3500]

weight = "(1)"
#weight = "abs(LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[578])"

sample = T1tttt_2000
sample_CP1 = T1tttt_2000_CP1
#sample = DY_LO

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
# LO
#h_all  = sample.get1DHistoFromDraw( "met_pt", selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = weight )
#h_neg  = sample.get1DHistoFromDraw( "met_pt", selectionString = "genWeight<0", binning = binning,  addOverFlowBin = 'upper', weightString = weight )
#h_all  = sample.get1DHistoFromDraw( var, selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = weight )
#h_neg  = sample.get1DHistoFromDraw( var, selectionString = "LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[9]<0", binning = binning,  addOverFlowBin = 'upper', weightString = weight )
h_all  = sample.get1DHistoFromDraw( var, selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = "LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[9]" )
h_neg  = sample.get1DHistoFromDraw( var , selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = "LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[1077]" )
#h_nnlo  = sample.get1DHistoFromDraw( var , selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = "LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[1077]" )
#h_neg  = sample.get1DHistoFromDraw( var , selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = "LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[972]" )
#h_nnlo.style = styles.lineStyle( ROOT.kRed,  width=2, errors=True )
h_neg.style = styles.lineStyle( ROOT.kBlue, width=2, errors=True )
h_all.style = styles.lineStyle( ROOT.kGreen+1, width=2, errors=True )

# get the variations
replicas = range(10,110) #NNPDF3.1nnlo
#replicas = range(476,576) #PDF4LHC15 nlo
#replicas = range(121,221) #NNPDF3.1nlo
#replicas = range(579,679) #PDF4LHC15 nnlo

alphaS = [110,111]
#alphaS = [576,577]
#alphaS = [221,222]
#alphaS = [679,680]

variations = []
for rep in replicas:
    print "Working on replica %s"%rep
    variations.append(sample.get1DHistoFromDraw( var, selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = "LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[%s]"%rep ))

variations_as = []
for aS in alphaS:
    variations_as.append(sample.get1DHistoFromDraw( var, selectionString = "(1)", binning = binning,  addOverFlowBin = 'upper', weightString = "LHEEventProduct_externalLHEProducer__SIM.obj.weights_.wgt[%s]"%aS ))

# loop over all bins
unc = []
for b in range(21):
    v = []
    v_rel = []
    central = h_all.GetBinContent(b+1)
    print b,central
    delta = 0.
    for var in variations:
        varied = var.GetBinContent(b+1)
        delta += (varied-central)**2
        if central>0:
            v_rel.append(abs(varied-central)/central)
        else:
            v_rel.append(0)
        v.append(varied)
    v = sorted(v)
    print v
    print max(v_rel), min(v_rel)
    ## replicas
    #u = {'up':v[84*len(variations)/100-1]-central, 'down':central-v[max(0,16*len(variations)/100-1)]}
    # hessian
    if central>0:
        u = {'up':sqrt(delta), 'down':sqrt(delta), 'rel':sqrt(delta)/central}
    else:
        u = {'up':sqrt(delta), 'down':sqrt(delta), 'rel':0.}

    u['alphaS'] = 1.5*(variations_as[0].GetBinContent(b+1) - variations_as[1].GetBinContent(b+1))/2.
    u['up']     = sqrt(u['up']**2 + u['alphaS']**2)
    u['down']   = sqrt(u['down']**2 + u['alphaS']**2)
    
    print u
    unc.append(u)

central = h_all.Integral()
delta = 0
for var in variations:
    varied = var.Integral()
    delta += (varied-central)**2

print "Total relative uncertainty", delta/central


boxes = []
for ib in range(1, 1 + h_all.GetNbinsX() ):
    val = h_all.GetBinContent(ib)
    
    # uncertainty box in main histogram
    box = ROOT.TBox( h_all.GetXaxis().GetBinLowEdge(ib),  max([0.00, val-unc[ib-1]['down']]), h_all.GetXaxis().GetBinUpEdge(ib), max([0.00, val+unc[ib-1]['up']]) )
    box.SetLineColor(ROOT.kBlack)
    box.SetFillStyle(3444)
    box.SetFillColor(ROOT.kBlack)
    
    boxes.append( box )

#raise NotImplementedError

#h_central.legendText = "t#bar{t}Z (LO)"
#h_all.legendText = "NNPDF3.1 nnlo"
h_all.legendText = "NNPDF3.1 nnlo CP5"
h_neg.legendText = "NNPDF3.1 lo CP1"
#h_nnlo.legendText = "NNPDF3.1 lo CP5"

#h_all.legendText = "all weights"
#h_neg.legendText = "neg weights"

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

plots = [[ h_all ], [ h_neg ]]#, [h_nnlo]]

plotting.draw(
    Plot.fromHisto("%s_nJe30_NNPDF31_lo_tune"%sample.name,
                plots,
                #texX = "E_{T}^{miss} (GeV)"
                #texX = "N_{jet}"
                texX = "H_{T} (GeV)"
            ),
    plot_directory = "/afs/hephy.at/user/d/dspitzbart/www/MG/weights/",
    logX = False, logY = True, #sorting = True, 
    #yRange = (0.0008,3.),
    #yRange = (0.03, 150.),
    #yRange = (0.03, [0.001,0.5]),
    #ratio = {'yRange': (0.0, 0.7),'texY':'neg. frac.'},
    ratio = {'yRange': (0.2, 1.5),'texY':'lo/nnlo'},
    #ratio = {'yRange': (0.5, 1.5)},
    scaling = {1:0, 2:0},
    drawObjects = drawObjects() + boxes,
    copyIndexPHP = True
)

