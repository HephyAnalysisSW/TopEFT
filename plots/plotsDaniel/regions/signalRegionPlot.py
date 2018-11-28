'''
Get a signal region plot from the cardfiles
'''

#!/usr/bin/env python
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--noMultiThreading",     dest="noMultiThreading",      default = False,             action="store_true", help="noMultiThreading?")
parser.add_option("--selectWeight",         dest="selectWeight",       default=None,                action="store",      help="select weight?")
parser.add_option("--PDFset",               dest="PDFset",              default="NNPDF30", choices=["NNPDF30", "PDF4LHC15_nlo_100"], help="select the PDF set")
parser.add_option("--selectRegion",         dest="selectRegion",          default=None, type="int",    action="store",      help="select region?")
parser.add_option("--sample",               dest='sample',  action='store', default='TTZ_NLO_16',    choices=["TTZ_LO_16", "TTZ_NLO_16", "TTZ_NLO_17"], help="which sample?")
parser.add_option("--small",                action='store_true', help="small?")
parser.add_option("--combine",              action='store_true', help="Combine results?")
parser.add_option('--logLevel',             dest="logLevel",              default='INFO',              action='store',      help="log level?", choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'])
parser.add_option('--signal',               action="store_true")
parser.add_option('--blinded',              action="store_true")
parser.add_option('--WZreweight',           action="store_true")
parser.add_option('--overwrite',            dest="overwrite", default = False, action = "store_true", help="Overwrite existing output files, bool flag set to True  if used")
parser.add_option('--postFit',              dest="postFit", default = False, action = "store_true", help="Apply pulls?")
parser.add_option('--bestFit',              dest="bestFit", default = False, action = "store_true", help="Apply pulls to signal?")
parser.add_option('--expected',             action = "store_true", help="Run expected?")
parser.add_option("--year",                 action='store',      default=2016, type="int", help='Which year?')
(options, args) = parser.parse_args()

# Standard imports
import ROOT
import os
import sys
import pickle
import math

# Analysis
from TopEFT.Analysis.regions        import regionsE, noRegions, regions4l, regions4lB
from TopEFT.Tools.u_float           import u_float
from TopEFT.Analysis.Region         import Region
from TopEFT.Tools.infoFromCards     import *
from TopEFT.Tools.user              import plot_directory
from TopEFT.samples.color           import color
from TopEFT.Tools.getPostFit        import *

from RootTools.core.standard import *
# logger
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   options.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(options.logLevel, logFile = None)

# regions like in the cards
regions = regionsE + regions4lB
regions += regions
#regions = regionsE

# processes (and names) like in the card
processes = [
    ('signal', 't#bar{t}Z'),
    ('WZ', 'WZ'),
    ('ZZ', 'ZZ'),
    ('nonPromptDD', 'non-prompt'),
    ('TTX', 't(#bar{t})X'),
#    ('TTW', 't#bar{t}W'),
    ('XG', 'X#gamma'),
    ('rare', 'rare'),
    ]

# uncertainties like in the card
postfix = "_%s"%options.year
uncertainties = ['PU'+postfix, 'JEC'+postfix, 'btag_heavy'+postfix, 'btag_light'+postfix, 'trigger'+postfix, 'leptonSFSyst', 'leptonTracking', 'eleSFStat'+postfix, 'muSFStat'+postfix, 'scale', 'scale_sig', 'PDF', 'nonprompt', 'WZ_xsec', 'WZ_bb', 'WZ_powheg', 'WZ_njet', 'XG_xsec', 'ZZ_xsec', 'rare', 'ttX', 'Lumi'+postfix] #tzq removed

Nbins = len(regions)

isData = True if not options.expected else False
if options.year == 2016:
    lumiStr = 35.9
elif options.year == 2017:
    lumiStr = 41.9
else:
    lumiStr = 0.

if options.combine:
    lumiStr = 35.92+41.53

#cardName = "ewkDM_ttZ_ll"
cardName = "dim6top_LO_ttZ_ll"
#cardName_signal = "ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m1p200000"
#cardName_signal = "ewkDM_ttZ_ll_DC2A_0p150000_DC2V_m0p150000"
#cardName_signal = "ewkDM_ttZ_ll_DC2A_0p250000_DC2V_m0p150000"
#cardName_signal = "ewkDM_ttZ_ll_DC1V_m1p000000"
cardName_signal = "dim6top_LO_ttZ_ll_cpQM_m4p000000_cpt_m2p000000" ## best-fit right now
#cardName_signal = "dim6top_LO_ttZ_ll_cpQM_0p000000_cpt_m17p500000"
#subDir = "nbtag0-njet1p"
subDir = ""
WZreweight = "" if not options.WZreweight else "WZreweight_"
expected = "" if not options.expected else "expected_"
#cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_%s_xsec_shape_lowUnc/%s/ewkDM_dipoles/"%(options.year,subDir)
#cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_20167_xsec_shape_lowUnc/%s/ewkDM_currents/"%subDir
#cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_%s_xsec_shape_lowUnc_allChannelsV8/%s/ewkDM_dipoles/"%(options.year,subDir)
#cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_%s_xsec_shape_lowUnc_%sSRandCR/%s/ewkDM_dipoles/"%(options.year,WZreweight,subDir)
cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_%s_xsec_shape_lowUnc_%s%sSRandCR/%s/dim6top_LO_currents/"%(options.year,expected,WZreweight,subDir)

if options.combine:
    cardDir = cardDir.replace('2016', 'COMBINED')

#cardName = "ewkDM_ttZ_ll_DC1A_0p900000_DC1V_0p900000"
#cardDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_shape_lowUnc/ewkDM_currents/"
cardFile = "%s/%s.txt"%(cardDir, cardName)
cardFile_signal = "%s/%s.txt"%(cardDir, cardName_signal)


logger.info("Plotting from cardfile %s"%cardFile)

hists = {}
allProcesses = processes + [('total','')] + [('observed','Data (%s)'%options.year)] + [('BSM','signal')]
for process,tex in allProcesses:
    hists[process] = ROOT.TH1F(process,"", Nbins, 0, Nbins)

years = [2016,2017] if options.combine else [options.year]

for i, r in enumerate(regions):
    #i = i+15
    totalYield          = 0.
    backgroundYield     = 0.
    totalUncertainty    = 0.
    backgroundUncertainty = 0.

    if options.postFit:
        suffix = '_bestfit' if options.bestFit else '_r1'
        postFitResults = getPrePostFitFromMLF(cardFile.replace('.txt','_FD%s.root'%suffix)) #r1

    for p,tex in processes:

        pYield = u_float(0,0)
        preYield = u_float(0,0)
        pError = 0
        
        for year in years:

            postfix  = '_%s'%year
            prefix   = 'dc_%s_'%year if options.combine else ''
            binName  = prefix+'Bin%s'%i
            logger.info("Working on bin %s, process %s, year %s.", binName, p, year)
            proc = "%s_%s"%(p,year) if p in ["WZ","ZZ","TTX","rare","XG"] else p
            res      = getEstimateFromCard(cardFile, proc, binName, postfix=postfix)

            if options.postFit:
                tmpYield    = u_float(0,0)
                # postfit: all uncertainties already taken care of
                if proc in postFitResults['results']['shapes_fit_s'][binName].keys():
                    tmpYield    = postFitResults['results']['shapes_fit_s'][binName][proc]
                    pYield     += tmpYield
                    preYield   += postFitResults['results']['shapes_prefit'][binName][proc]
                    tmpError    = tmpYield.sigma
                    #print "Stat error"
                    #print tmpError

                    if tmpError/tmpYield.val > 10:
                        tmpError = tmpYield.val
                    pError += tmpError**2
                else: pYield += u_float(0,0)
                if tmpYield.val>0:
                    logger.info("Yield for year %s: %s", year, tmpYield.val)
            else:
                # prefit: get all the uncertainties later
                logger.info("Yield for year %s: %s", year, res.val)
                pYield      += res
                pError      += pYield.sigma**2

            #if not p == "signal":
            #    backgroundYield += pYield

            #totalYield += pYield

            if not options.postFit:
                postfix = "_%s"%year
                uncertainties = ['PU'+postfix, 'JEC'+postfix, 'btag_heavy'+postfix, 'btag_light'+postfix, 'trigger'+postfix, 'leptonSFSyst', 'leptonTracking', 'eleSFStat'+postfix, 'muSFStat'+postfix, 'scale', 'scale_sig', 'PDF', 'nonprompt', 'WZ_xsec', 'WZ_bb', 'WZ_powheg', 'WZ_njet', 'XG_xsec', 'ZZ_xsec', 'rare', 'ttX', 'Lumi'+postfix]
                for u in uncertainties:
                    try:
                        unc = getPreFitUncFromCard(cardFile, proc, u, binName, )
                    except:
                        logger.debug("No uncertainty %s for process %s"%(u, p))
                    if unc > 0:
                        pError += (unc*pYield.val)**2

            
            totalUncertainty += pError
            if not p == "signal":
                backgroundUncertainty += pError
            
        
        if not p == "signal":
            backgroundYield += pYield
        
        totalYield += pYield

        if pYield.val > 0:
            logger.info("Final yield: %s +/- %s", pYield.val, pError)
        hists[p].SetBinContent(i+1, pYield.val)
        hists[p].SetBinError(i+1,0)
        hists[p].legendText = tex
        if not p == 'total':
           hists[p].style = styles.fillStyle( getattr(color, p.replace('_2016','')), lineColor=getattr(color,p.replace('_2016','')), errors=False )

        if options.postFit:
            if preYield.val > 0 and pYield.val > 0:
                SF = pYield/u_float(preYield.val,0)
                logger.info("Scale factor: %s +/- %s", round(SF.val,3), round(SF.sigma,3))
        

    hists['total'].SetBinContent(i+1, totalYield.val)
    totalUncertainty = math.sqrt(totalUncertainty)
    logger.info("Total background yield: %s +/- %s", totalYield.val, totalUncertainty)
    hists['total'].SetBinError(i+1, totalUncertainty)

    ## signals ##
    if options.signal:# and i>14:
        pYield = 0
        for year in years:
            postfix  = '_%s'%year
            prefix   = 'dc_%s_'%year if options.combine else '' 
            binName  = prefix+'Bin%s'%i
            res      = getEstimateFromCard(cardFile_signal, "signal", binName, postfix=postfix)
            pYield += res.val
            pError = 0

            # loop over all uncertainties
            postfix = "_%s"%year
            uncertainties = ['PU', 'JEC', 'JER', 'btag_heavy'+postfix, 'btag_light'+postfix, 'trigger'+postfix, 'leptonSFSyst', 'leptonTracking', 'eleSFStat'+postfix, 'muSFStat'+postfix, 'scale', 'scale_sig', 'PDF', 'nonprompt', 'WZ_xsec', 'WZ_bb', 'WZ_powheg', 'WZ_njet', 'XG_xsec', 'ZZ_xsec', 'rare', 'ttX', 'Lumi'+postfix]
            for u in uncertainties:
                try:
                    unc = getPreFitUncFromCard(cardFile_signal, "signal", u, binName, )
                except:
                    logger.debug("No uncertainty %s for process %s"%(u, p))
                if unc > 0:
                    pError += (unc*pYield)**2
        hists['BSM'].SetBinContent(i+1, pYield + backgroundYield.val)
        hists['BSM'].SetBinError(i+1, math.sqrt(pError + backgroundUncertainty))
        hists['BSM'].legendText = "EFT best-fit"
        #hists['BSM'].legendText = "c_{#varphit}=-17.5"


## data ##
for i, r in enumerate(regions):
    #i = i+15
    pYield = 0
    for year in years:
        postfix  = '_%s'%options.year
        prefix   = 'dc_%s_'%year if options.combine else ''
        binName  = prefix+"Bin%s"%i
        res      = getObservationFromCard(cardFile, binName)
        pYield  += res.val
    if not (options.blinded and i>14):
        hists['observed'].SetBinContent(i+1, pYield)
        if not isData:
            hists['observed'].legendText = 'Total SM'
        else:
            hists['observed'].legendText = 'Data (%s)'%options.year if not options.combine else 'Data (2016+2017)'
    
## manually calculate the chi2 (no correlations).
chi2SM  = 0
chi2BSM = 0
totalExp = 0
totalObs = 0
nDOF = 0
for i, r in enumerate(regions):
    print "Region %s"%(i+1)
    print "SM"
    print hists['total'].GetBinContent(i+1)
    print (hists['observed'].GetBinContent(i+1) - hists['total'].GetBinContent(i+1))
    print hists['total'].GetBinError(i+1)
    print hists['observed'].GetBinContent(i+1)/hists['total'].GetBinContent(i+1)
    print "Chi2", ( ((hists['observed'].GetBinContent(i+1) - hists['total'].GetBinContent(i+1))**2) / (hists['total'].GetBinError(i+1)**2) )
    print "BSM"
    print hists['BSM'].GetBinContent(i+1)
    print hists['observed'].GetBinContent(i+1) - hists['BSM'].GetBinContent(i+1)
    print hists['BSM'].GetBinError(i+1)
    print hists['observed'].GetBinContent(i+1)/hists['BSM'].GetBinContent(i+1)
    print "Chi2", (hists['observed'].GetBinContent(i+1) - hists['BSM'].GetBinContent(i+1))**2/hists['BSM'].GetBinError(i+1)**2
    print
    totalExp += hists['total'].GetBinContent(i+1)
    totalObs += hists['observed'].GetBinContent(i+1)
    if hists['total'].GetBinContent(i+1) > 10:# or True:
        chi2SM += ( ((hists['observed'].GetBinContent(i+1) - hists['total'].GetBinContent(i+1))**2) / (hists['total'].GetBinError(i+1)**2) )
        nDOF +=1
    if options.signal and hists['BSM'].GetBinContent(i+1) > 10:# or True:
        chi2BSM += (hists['observed'].GetBinContent(i+1) - hists['BSM'].GetBinContent(i+1))**2/hists['BSM'].GetBinError(i+1)**2

    if i == 14:
        print "Intermediate Chi2 values:"
        print chi2SM
        print chi2BSM

print "Chi-squared for SM:", chi2SM
print "Chi-squared for BSM:", chi2BSM
print "nDOF:", len(regions)
print "nDOF (red):", nDOF
print "Total Obs/Exp:", totalObs/totalExp


## get the covariance matrix
# combineCards.py mycard.txt -S > myshapecard.txt
# text2workspace.py myshapecard.txt
# combine -M MaxLikelihoodFit --saveShapes --saveWithUnc --numToysForShape 5000 --saveOverall myshapecard.root

## calculate the chi2 with R^T*Cov^(-1)*R where R is the residual vector



#hists['observed'].SetBinErrorOption(ROOT.TH1.kPoisson)
hists['observed'].style = styles.errorStyle( ROOT.kBlack, markerSize = 1. )

if options.signal:
    hists['BSM'].style = styles.lineStyle( ROOT.kRed+1, width=3, dashed=True)

boxes = []
ratio_boxes = []
for ib in range(1, 1 + hists['total'].GetNbinsX() ):
    val = hists['total'].GetBinContent(ib)
    if val<0: continue
    sys = hists['total'].GetBinError(ib)
    if val > 0:
        sys_rel = sys/val
    else:
        sys_rel = 1.
    
    # uncertainty box in main histogram
    box = ROOT.TBox( hists['total'].GetXaxis().GetBinLowEdge(ib),  max([0.006, val-sys]), hists['total'].GetXaxis().GetBinUpEdge(ib), max([0.006, val+sys]) )
    box.SetLineColor(ROOT.kGray+1)
    box.SetFillStyle(3244)
    box.SetFillColor(ROOT.kGray+1)
    
    # uncertainty box in ratio histogram
    r_box = ROOT.TBox( hists['total'].GetXaxis().GetBinLowEdge(ib),  max(0.1, 1-sys_rel), hists['total'].GetXaxis().GetBinUpEdge(ib), min(1.9, 1+sys_rel) )
    r_box.SetLineColor(ROOT.kGray+1)
    r_box.SetFillStyle(3244)
    r_box.SetFillColor(ROOT.kGray+1)

    boxes.append( box )
    hists['total'].SetBinError(ib, 0)
    ratio_boxes.append( r_box )

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
    y_pos = 0.6 if len(regions)>12 else 0.85
    x_pos = 0.90 if len(regions)>12 else 0.25
    if len(regions) > 12:
        lines =  [(min+(3*i+x_pos)*diff, y_pos,  r.texStringForVar('Z_pt'))   for i, r in enumerate(regions[:-3][::3])]
    else:
        lines =  [(min+(3*i+x_pos)*diff, y_pos,  r.texStringForVar('Z_pt'))   for i, r in enumerate(regions[::3])]
    return [tex.DrawLatex(*l) for l in lines] 

def drawLabels2( regions ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.028)
    tex.SetTextAngle(0)
    tex.SetTextAlign(12) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / len(regions)
    lines =  [(min+(3*i+0.90)*diff, 0.900,  "N_{l}=3")   for i, r in enumerate(regions[:-3][::3])]
    lines += [(min+(12+0.90)*diff, 0.900,  "N_{l}=4")]
    lines +=  [(min+(3*i+0.90)*diff, 0.860,  "N_{b-tag}#geq1")   for i, r in enumerate(regions[:-3][::3])]
    lines += [(min+(12+0.90)*diff, 0.860,  "N_{b-tag}#geq1")]
    lines +=  [(min+(3*i+0.90)*diff, 0.820,  "N_{j}#geq3")   for i, r in enumerate(regions[:-3][::3])]
    lines += [(min+(12+0.90)*diff, 0.820,  "N_{j}#geq2")]
    return [tex.DrawLatex(*l) for l in lines] if len(regions)>12 else []

def drawLabelsLower( regions ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.09)
    tex.SetTextFont(42)
    tex.SetTextAngle(0)
    tex.SetTextAlign(23) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / len(regions)
    
    lines  = [(min+6*diff, 0.10, "N_{b}=0"),        (min+13.5*diff, 0.10, "N_{b}#geq0"),      (min+21*diff, 0.10, "N_{b}#geq1"),      (min+28.5*diff, 0.10, "N_{b}#geq1")]
    lines += [(min+6*diff, 0.21, "N_{jet}#geq1"),   (min+13.5*diff, 0.21, "N_{jet}#geq0"),    (min+21*diff, 0.21, "N_{jet}#geq3"),    (min+28.5*diff, 0.21, "N_{jet}#geq1")]
    lines += [(min+6*diff, 0.32, "N_{lep}=3"),      (min+13.5*diff, 0.32, "N_{lep}=4"),       (min+21*diff, 0.32, "N_{lep}=3"),       (min+28.5*diff, 0.32, "N_{lep}=4")]

    return [tex.DrawLatex(*l) for l in lines]

def drawHeadlineLower( regions ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.10)
    tex.SetTextFont(42)
    tex.SetTextAngle(0)
    tex.SetTextAlign(23) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / len(regions)

    lines  = [(min+8*diff, 0.415, "Control Region"),        (min+23*diff, 0.415, "Signal Region")]

    return [tex.DrawLatex(*l) for l in lines]


def drawDivisionsLower(regions):
    min = 0.15
    max = 0.95
    diff = (max-min) / len(regions)
    lines = []
    lines2 = []
    line = ROOT.TLine()
#   line.SetLineColor(38)
    line.SetLineWidth(1)
    line.SetLineStyle(2)
    #lines = [ (min+3*i*diff,  0.01, min+3*i*diff, 0.45) for i in range(1,10) ]
    lines = [ (min +0*diff, 0.01, min +0*diff, 0.50), (min +12*diff, 0.01, min +12*diff, 0.32), (min +15*diff, 0.01, min +15*diff, 1.0), (min +27*diff, 0.01, min +27*diff, 0.32), (min +30*diff, 0.01, min +30*diff, 0.50)]
    return [line.DrawLineNDC(*l) for l in lines] + [tex.DrawLatex(*l) for l in []] + [tex2.DrawLatex(*l) for l in lines2]


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
    lines = [ (min+3*i*diff,  0.013, min+3*i*diff, 0.93) if min+3*i*diff<0.74 else (min+3*i*diff,  0.013, min+3*i*diff, 0.52) for i in range(1,10) ]
    return [line.DrawLineNDC(*l) for l in lines] + [tex.DrawLatex(*l) for l in []] + [tex2.DrawLatex(*l) for l in lines2]


def drawBinNumbers(numberOfBins):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.13 )
    tex.SetTextAlign(23) # align right
    min = 0.15
    max = 0.95
    diff = (max-min) / numberOfBins
    lines = [(min+(i+0.5)*diff, 0.35 ,  str(i)) for i in range(numberOfBins)]
    return [tex.DrawLatex(*l) for l in lines]

def drawObjects( isData=False, lumi=36. ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Simulation') if not isData else (0.15, 0.95, 'CMS #bf{#it{Preliminary}}'),
      (0.75, 0.95, '%sfb^{-1} (13 TeV)'%lumi )
    ]
    return [tex.DrawLatex(*l) for l in lines]

def setBinLabels( hist ):
    for i in range(1, hist.GetNbinsX()+1):
        if i < 16:
            hist.GetXaxis().SetBinLabel(i, "%s"%i)
        else:
            hist.GetXaxis().SetBinLabel(i, "%s"%(i-15))

drawObjects = drawObjects( isData=isData, lumi=round(lumiStr,1)) + boxes + drawDivisions( regions )# + drawLabels( regions ) + drawLabels2( regions ) + drawDivisions( regions )# + drawBinNumbers( len(regions) )

bkgHists = []
for p,tex in processes:
    if p is not "total" and p is not 'observed':
        bkgHists.append(hists[p])

for p,tex in allProcesses:
    setBinLabels(hists[p])

#histos =  bkgHists  + [hists["total"]]
if options.signal:
    plots = [ bkgHists, [hists['BSM']], [hists['observed']] ]
else:
    plots = [ bkgHists, [hists['observed']]]
if subDir:
    subDir = "%s_"%subDir

plotName = "%s%s_signalRegions_incl4l_dataV2_%s%s%s"%(subDir,cardName,expected,WZreweight,options.year if not options.combine else "COMBINED")
if options.postFit:
    plotName += "_postFit"
if options.blinded:
    plotName += "_blinded"
if options.bestFit:
    plotName += "_bestFit"

plotting.draw(
    Plot.fromHisto(plotName,
                plots,
                texX = ""
            ),
    plot_directory = os.path.join(plot_directory, "signalRegions_v2"),
    logX = False, logY = True, sorting = False, 
    #legend = (0.75,0.80-0.010*32, 0.95, 0.80),
    legend = (0.74,0.54, 0.95, 0.89),
    widths = {'x_width':1000, 'y_width':600},
    #yRange = (0.3,3000.),
    #yRange = (0.03, [0.001,0.5]),
    ratio = {'yRange': (0.51, 1.49), 'drawObjects':ratio_boxes + drawLabelsLower( regions ) +drawHeadlineLower( regions ) + drawDivisionsLower(regions), 'histModifications':[], 'texY':'Data/Pred', 'histos':[(2,0),(1,0)] if options.signal else [(1,0)]} ,
    drawObjects = drawObjects,
    copyIndexPHP = True,
)

