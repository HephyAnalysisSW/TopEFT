#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option("--selectRegion",         dest="selectRegion",          default=None, type="int",    action="store",      help="select region?")
parser.add_option("--small",                action='store_true', help="small?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
parser.add_option('--overwrite',            dest="overwrite", default = False, action = "store_true", help="Overwrite existing output files, bool flag set to True  if used")
parser.add_option('--regionsXSec',          dest="regionsXSec", default = False, action = "store_true", help="Use nJet and nBTag binning")
(options, args) = parser.parse_args()

# Standard imports
import ROOT
import os
import sys
import pickle
import math

# Analysis
from TopEFT.Analysis.SetupHelpers       import channel, trilepChannels, allTrilepChannels, singlelepChannels, allSinglelepChannels
from TopEFT.Analysis.regions            import noRegions, regionsA, regionsE, regionsReweight, regionsReweight4l, regions4l, regions4lB
from TopEFT.Analysis.estimators         import *
from TopEFT.Analysis.DataObservation    import DataObservation
from TopEFT.Analysis.FakeEstimate       import FakeEstimate
from TopEFT.Analysis.run.SignalReweightingTemplate import *
from TopEFT.Analysis.run.WZReweightingTemplate import *
from TopEFT.Tools.u_float           import u_float
from TopEFT.Tools.resultsDB         import resultsDB
from TopEFT.Analysis.Region         import Region

#RootTools
from RootTools.core.standard import *

from TopEFT.samples.color import color
from TopEFT.Tools.cutInterpreter    import cutInterpreter

import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   options.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None)


def getCouplingFromName(name, coupling):
    name = name.lower()
    coupling = coupling.lower()
    if coupling in name:
        l = name.split('_')
        return float(l[l.index(coupling)+1].replace('p','.').replace('m','-'))
    else:
        return 0.


data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"

## 2016 ##
postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
from TopEFT.samples.cmgTuples_ttZ0j_Summer16_mAODv2_postProcessed import *

postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_07Aug17_postProcessed import *

## 2017 ##
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *
postProcessing_directory = "TopEFT_PP_2017_mva_v21/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *

from TopEFT.Analysis.Setup          import Setup

from TopEFT.samples.gen_fwlite_benchmarks import *

year = 2016

## 3l setup ##
setup3l                 = Setup(year, nLeptons=3)
estimators3l            = estimatorList(setup3l)
setup3l.estimators      = estimators3l.constructEstimatorList(["WZ", "TTX", "XG", "rare", "ZZ"])# if not args.WZamc else estimators3l.constructEstimatorList(["WZ_amc", "TTX", "TTW", "ZG", "rare", "ZZ"])
setup3l.reweightRegions = regionsReweight
setup3l.channels        = [channel(-1,-1)] # == 'all'
setup3l.regions         = regionsE
setup3l.year            = year
setup3l.default_sys['reweight'] = []

## 4l setup ##
setup4l                 = Setup(year=year, nLeptons=4)
setup4l.parameters.update({'nJets':(1,-1), 'nBTags':(1,-1), 'zMassRange':20, 'zWindow2':"offZ"})
estimators4l            = estimatorList(setup4l)
setup4l.estimators      = estimators4l.constructEstimatorList(["ZZ", "rare","TTX"])
setup4l.reweightRegions = regionsReweight4l
setup4l.channels        = [channel(-1,-1)] # == 'all'
setup4l.regions         = regions4lB
setup4l.year            = year
setup4l.default_sys['reweight'] = []

setups = [setup3l, setup4l]

reweightCache   = os.path.join( results_directory, 'SignalReweightingTemplate_v3' )

allPairings = [
    (ttZ0j_ll,                                                              ewkDM_ttZ_ll_gen), 
    (ttZ0j_ll_DC2A_0p200000_DC2V_0p200000,                                  ewkDM_ttZ_ll_gen_DC2A_0p200000_DC2V_0p200000),
    (ttZ0j_ll_DC1A_1p000000,                                                ewkDM_ttZ_ll_gen_DC1A_1p000000),
    (ttZ0j_ll_DC1A_0p500000_DC1V_0p500000,                                  ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_0p500000),
    (ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000,                                 ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_m1p000000),
    (ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700,     ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700),
    (ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700,    ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700),
    (ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000,                   ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000),
    (ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700,    ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700),
    (ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700,   ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700),
    (ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000,                  ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000),
    (ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000,                  ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000),
    (ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000,                   ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000)
    ]

for s in allPairings:

    target_reco = s[0]
    target_gen  = s[1]

    modification_dict = {}
    
    nonZeroCouplings = ["DC1A","DC1V","DC2A","DC2V"]
    
    # for safety, set all couplings to 0.
    modification_dict["DC1A"]   = 0.
    modification_dict["DC1V"]   = 0.
    modification_dict["DC2A"]   = 0.
    modification_dict["DC2V"]   = 0.
    
    for coup in nonZeroCouplings:
        try:
            modification_dict[coup] = getCouplingFromName(target_reco.name, coup)
            logger.info("The following coupling is set to non-zero value: %s: %s", coup, modification_dict[coup])
        except ValueError:
            logger.info("The following coupling is kept at zero: %s: %s", coup, modification_dict[coup])
            continue
    
    #for s in ewkDM_all:
    #    if s.name == "ewkDM_%s"%target_reco.name.replace('0j',''):
    #        target_gen = s
    #        print "Found gen sample"
    
    #SM_reco = TTZtoLLNuNu
    SM_reco = ttZ0j_ll
    
    reco_selection = 'nJetSelected>=3&&nBTag>=1&&min_dl_mass>=12&&abs(Z_mass - 91.1876)<=10&&Z_fromTight>0&&nLeptons_tight_3l==3&&Sum$((lep_tight_3l*(lep_pt - lep_ptCorr) + lep_ptCorr)>40&&lep_tight_3l>0)>0&&Sum$((lep_tight_3l*(lep_pt - lep_ptCorr) + lep_ptCorr)>20&&lep_tight_3l>0)>1&&Sum$((lep_tight_3l*(lep_pt - lep_ptCorr) + lep_ptCorr)>10&&lep_tight_3l>0)>2&&!(nLeptons_tight_4l>=4)'
    
    norm_source     = SM_reco.getYieldFromDraw(reco_selection, "weight")
    norm_target     = target_reco.getYieldFromDraw(reco_selection, "weight")
    
    norm = norm_source['val']/norm_target['val']
    
    print "Norm", norm
    
    allRegions = setup3l.regions + setup4l.regions
    
    
    hists = {}
    Nbins = len(allRegions)
    
    for p in ["signal", "signal_reweight"]:
        hists[p] = ROOT.TH1F(p, "", Nbins, 0, Nbins)
    
    
    ibin = 1
    for setup in setups:
        signal      = MCBasedEstimate(name=SM_reco.name, sample=SM_reco, cacheDir=setup.defaultCacheDir())
    
        FS_signal   = MCBasedEstimate(name=target_reco.name, sample=target_reco, cacheDir=setup.defaultCacheDir())
        
        for r in setup.regions:
            print r
            for channel in setup.channels:
                print channel.name
                
                # reweighted
                #source_gen = ewkDM_central #ewkDM_ttZ_ll_gen
                source_gen = ewkDM_ttZ_ll_gen
                signalReweighting = SignalReweighting( source_sample = source_gen, target_sample = target_gen, cacheDir = reweightCache)
                f = signalReweighting.cachedReweightingFunc( setup.genSelection )
                sig = signal.reweight2D(r, channel, setup, f)
                hists['signal_reweight'].SetBinContent(ibin, sig.val)
                hists['signal_reweight'].SetBinError(ibin, sig.sigma)
                hists['signal_reweight'].GetXaxis().SetBinLabel(ibin, "%i"%(ibin))
                
                print sig.val, sig.sigma
    
                ## off-Z is wrong when not using simple getYieldFromDraw. Careful!!
                reco_sig = FS_signal.cachedEstimate(r, channel, setup)
                hists['signal'].SetBinContent(ibin, reco_sig.val*norm)
                hists['signal'].SetBinError(ibin, reco_sig.sigma*norm)
                hists['signal'].GetXaxis().SetBinLabel(ibin, "%i"%(ibin))
                ibin += 1
                #reco_sig_alt = target_reco.getYieldFromDraw('&&'.join([setup.preselection("MC")['cut'], r.cutString()]), setup.weightString()+'*35.9')
                
    
    hists['signal'].style           = styles.errorStyle(ROOT.kBlack, markerSize=1)
    hists['signal_reweight'].style  = styles.lineStyle(ROOT.kRed+1, width=2, errors=True)
    hists['signal'].legendText      = "BSM full sim."
    hists['signal_reweight'].legendText = "SM reweighted"
    
    print "Total norm", hists['signal_reweight'].Integral()/hists['signal'].Integral()
    
    def drawObjects( isData=False, lumi=36. ):
        tex = ROOT.TLatex()
        tex.SetNDC()
        tex.SetTextSize(0.04)
        tex.SetTextAlign(11) # align right
        lines = [
          (0.15, 0.95, 'CMS Simulation') if not isData else (0.15, 0.95, 'CMS Preliminary'),
          (0.75, 0.95, '%sfb^{-1} (13 TeV)'%int(lumi) )
        ]
        return [tex.DrawLatex(*l) for l in lines]
    
    def drawLabelsLower( regions ):
        tex = ROOT.TLatex()
        tex.SetNDC()
        tex.SetTextSize(0.04)
        tex.SetTextFont(42)
        tex.SetTextAngle(0)
        tex.SetTextAlign(23) # align right
        min = 0.15
        max = 0.95
        diff = (max-min) / len(regions)
    
        lines  = [(min+6*diff, 0.80, "N_{b}=1"),        (min+13.5*diff, 0.80, "N_{b}#geq1"),      (min+21*diff, 0.80, "N_{b}#geq1"),      (min+28.5*diff, 0.80, "N_{b}#geq1")]
        lines += [(min+6*diff, 0.85, "N_{jet}#geq3"),   (min+13.5*diff, 0.85, "N_{jet}#geq1"),    (min+21*diff, 0.85, "N_{jet}#geq3"),    (min+28.5*diff, 0.85, "N_{jet}#geq1")]
        lines += [(min+6*diff, 0.90, "N_{lep}=3"),      (min+13.5*diff, 0.90, "N_{lep}=4"),       (min+21*diff, 0.90, "N_{lep}=3"),       (min+28.5*diff, 0.90, "N_{lep}=4")]
    
        return [tex.DrawLatex(*l) for l in lines]
    
    
    def drawLabels( regions ):
        tex = ROOT.TLatex()
        tex.SetNDC()
        tex.SetTextSize(0.028)
        if len(regions)>12:
            tex.SetTextAngle(90)
        else:
            tex.SetTextAngle(0)
        tex.SetTextAlign(12) # align right
        min = 0.15
        max = 0.95
        diff = (max-min) / len(regions)
        y_pos = 0.50 if len(regions)>12 else 0.85
        x_pos = 2.50 if len(regions)>12 else 0.25
        if len(regions) > 12:
            lines =  [(min+(3*i+x_pos)*diff, y_pos,  r.texStringForVar('Z_pt'))   for i, r in enumerate(regions[:-3][::3])]
        else:
            lines =  [(min+(3*i+x_pos)*diff, y_pos,  r.texStringForVar('Z_pt'))   for i, r in enumerate(regions[::3])]
        return [tex.DrawLatex(*l) for l in lines]
    
    def drawDivisions(regions):
        min = 0.15
        max = 0.95
        diff = (max-min) / len(regions)
        lines = []
        lines2 = []
        line = ROOT.TLine()
    #   line.SetLineColor(38)
        line.SetLineWidth(1)
        line.SetLineStyle(2)
        lines = [ (min+3*i*diff,  0.1, min+3*i*diff, 0.75) if min+3*i*diff<0.74 else (min+3*i*diff,  0.1, min+3*i*diff, 0.85) for i in range(1,10) ]
        return [line.DrawLineNDC(*l) for l in lines] + [tex.DrawLatex(*l) for l in []] + [tex2.DrawLatex(*l) for l in lines2]
    
    drawObjects = drawObjects( isData=False, lumi=round(35.9,0)) + drawLabelsLower(allRegions) + drawLabels(allRegions) + drawDivisions(allRegions)
    
    plots_SR    =  [ [hists["signal_reweight"]], [hists["signal"]] ]
    
    from TopEFT.Tools.user              import plot_directory
    
    scaling = {1:0}
    
    plotting.draw(
        Plot.fromHisto("reweightingClosure_"+target_gen.name,
                    plots_SR,
                    texX = "Signal region",
                    texY = "Number of events"
                ),
        plot_directory = os.path.join(plot_directory, "reweightingClosure"),
        logX = False, logY = False, sorting = False,
        #legend = (0.74,0.80-0.010*8, 0.95, 0.80),
        legend = [ (0.15,0.9-0.06*sum(map(len, plots_SR)),0.4,0.9), 1],
        widths = {'x_width':700, 'y_width':600},
        #yRange = (0.03, [0.001,0.5]),
        ratio = {'yRange': (0.81, 1.19), 'texY':"FullSim/reweight"},
        drawObjects = drawObjects,
        scaling = scaling,
        copyIndexPHP = True,
    )


logger.info("All done.")

