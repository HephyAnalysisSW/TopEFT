# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

# TopEFT
from TopEFT.Tools.PickleCache import PickleCache
from TopEFT.Tools.user import results_directory, plot_directory
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, writeObjToFile, getObjFromFile

from array import array

ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--leg',                    action='store',         nargs='?',              choices=["E","M"],     default='E', help="electron or muon?")
    argParser.add_argument('--Run2017',                action='store_true',          help="2017 data?")
    argParser.add_argument('--channel',                action='store', choices = ["dilep", "trilep"], default = "trilep",          help="Which channel?")

    return argParser

options = get_parser().parse_args()

# 2016 MC samples for shapes
postProcessing_directory = "TopEFT_PP_v14/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *

# 2017 MC samples for shapes
data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = 'TopEFT_PP_2017_Fall17_v2/trilep'
from TopEFT.samples.cmgTuples_Fall17_94X_mAODv2_postProcessed import *

# Define stuff for plotting
binning = [0,10,20,30,40,50,60,70,80,100,120,150,200]
if options.Run2017:
    binning = [0,10,20,30,40,50,60,70,80,100,120,150,200]
    #binning = [0,10,20,30,40,60,80,100,120,150,200]

#binning = [0,1,2,3,4]

if options.channel == "dilep":
    presel = "nlep==2&&lep_pt[0]>40&&lep_pt[1]>20&&met_pt>40&&sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))>20"
else:
    presel  = 'nlep==3&&lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10&&abs(Z_mass-90.2)<10'

# loop over 3 leptons. Too tired to think of something nicer
#for i in range(3):
#for i in range(1):
for i in range(2):

    if options.Run2017:
        
        if options.channel == "dilep":
            MC = TTW_17
            DataCanvas  = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/MET_Run2017/turnOn_3l_MET_HTMHT_JetHT_altBinning/2l/lep_pt[%s]_MET_Run2017_comp.root"%i, "can")
            MCCanvas    = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/TTLep_pow_17/turnOn_3l_MET_HTMHT_JetHT_altBinning/2l/lep_pt[%s]_TTLep_pow_17_comp.root"%i, "can")
        else:
            MC = TTZtoLLNuNu_17
            #DataCanvas  = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/MET_Run2017/turnOn_3l_MET_HTMHT_JetHT_altBinning/3pl/lep_pt[%s]_MET_Run2017_comp.root"%i, "can")
            #MCCanvas    = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/TTZtoLLNuNu_17/turnOn_3l_MET_HTMHT_JetHT_altBinning/3pl/lep_pt[%s]_TTZtoLLNuNu_17_comp.root"%i, "can")
            DataCanvas  = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/MET_Run2017/turnOn_3l_MET_HTMHT_JetHT_altBinning/3pl/nGoodElectrons_MET_Run2017_comp.root", "can")
            MCCanvas    = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/TTZtoLLNuNu_17/turnOn_3l_MET_HTMHT_JetHT_altBinning/3pl/nGoodElectrons_TTZtoLLNuNu_17_comp.root", "can")
    
    else:
    
        if options.channel == "dilep":
            MC = TTW
            DataCanvas  = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/MET_Run2016/turnOn_3l_MET_HTMHT_JetHT_altBinning/2l/lep_pt[%s]_MET_Run2016_comp.root"%i, "can")
            MCCanvas    = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/TTLep_pow/turnOn_3l_MET_HTMHT_JetHT_altBinning/2l/lep_pt[%s]_TTLep_pow_comp.root"%i, "can")
        else:
            MC = TTZ_LO
            #DataCanvas  = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/MET_Run2016/turnOn_3l_MET_HTMHT_JetHT/3pl/lep_pt[%s]_MET_Run2016_comp.root"%i, "can")
            #MCCanvas    = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/TTZ_LO/turnOn_3l_MET_HTMHT/3pl/lep_pt[%s]_TTZ_LO_comp.root"%i, "can")
            DataCanvas  = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/MET_Run2016/turnOn_3l_MET_HTMHT_JetHT_altBinning/3pl/nGoodElectrons_MET_Run2016_comp.root", "can")
            MCCanvas    = getObjFromFile("/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/TTZ_LO/turnOn_3l_MET_HTMHT_JetHT_altBinning/3pl/nGoodElectrons_TTZ_LO_comp.root", "can")
    
    # get the histogram with highest efficiencies ( == most ORed triggers)
    indexData   = 0
    maxEffData  = 0
    indexMC     = 0
    maxEffMC    = 0

    for j in range(4,7):
        if DataCanvas.GetListOfPrimitives()[j].GetEfficiency(5) > maxEffData:
            maxEffData = DataCanvas.GetListOfPrimitives()[j].GetEfficiency(5)
            indexData = j
        if MCCanvas.GetListOfPrimitives()[j].GetEfficiency(5) > maxEffMC:
            maxEffMC = MCCanvas.GetListOfPrimitives()[j].GetEfficiency(5)
            indexMC = j

    if not indexData == 6:
        print "Weird"

    indexData = 6#6
    indexMC = 6#6
    
    DataHist    = DataCanvas.GetListOfPrimitives()[indexData]
    DataHist.SetLineColor(ROOT.kBlue)
    DataHist.SetMarkerColor(ROOT.kBlue)
    DataHist.SetMarkerStyle(21)
    MCHist      = MCCanvas.GetListOfPrimitives()[indexMC]
    
    shapeHist   = MC.get1DHistoFromDraw("lep_pt[%s]"%i, binning, selectionString=presel, weightString="weight", binningIsExplicit=True, addOverFlowBin='upper', isProfile=False)
    #shapeHist   = MC.get1DHistoFromDraw("nGoodElectrons", binning, selectionString=presel, weightString="weight", binningIsExplicit=True, addOverFlowBin='upper', isProfile=False)
    if i == 0:
        shapeHist.Scale(15/shapeHist.Integral(),"width")
        #shapeHist.Scale(0.5/shapeHist.Integral(),"width")
    elif i ==1:
        shapeHist.Scale(7/shapeHist.Integral(),"width") #10
    else:
        shapeHist.Scale(5/shapeHist.Integral(),"width")
    shapeHist.SetMaximum(1.02)
    shapeHist.SetMinimum(0.80)
    shapeHist.GetXaxis().SetRangeUser(0.1,200)
    shapeHist.SetFillColorAlpha(ROOT.kGray, 0.6)

    numHist     = shapeHist.Clone()
    denomHist   = shapeHist.Clone()
    oneHist     = shapeHist.Clone()
    # shifting shape to 0.8    
    for j in range(len(binning)):
        oneHist.SetBinContent(j+1, 1)
        shapeHist.SetBinContent(j+1, shapeHist.GetBinContent(j+1)+0.8)
        numHist.SetBinContent(j+1, DataHist.GetEfficiency(j+1))
        denomHist.SetBinContent(j+1, MCHist.GetEfficiency(j+1))

    # get asymmetric errors for correct error propagation
    from TopEFT.Tools.asym_float import *

    numHist.GetYaxis().SetTitle("efficiency")
    numHist.Divide(denomHist)
    scaleFactors = [ ]
    
    for j in range(len(binning)):
        effData = asym_float(DataHist.GetEfficiency(j+1), DataHist.GetEfficiencyErrorUp(j+1), DataHist.GetEfficiencyErrorLow(j+1))
        effMC = asym_float(MCHist.GetEfficiency(j+1), MCHist.GetEfficiencyErrorUp(j+1), MCHist.GetEfficiencyErrorLow(j+1))
        scaleFactors.append(effData/effMC) if effMC > 0 else scaleFactors.append(asym_float(0))

    ratioSyst = ROOT.TGraphAsymmErrors(oneHist)
    ratioAsym = ROOT.TGraphAsymmErrors(numHist)
    for j in range(len(binning)):
        ratioAsym.SetPointError(j, 0.,0.,scaleFactors[j].down, scaleFactors[j].up)
        print binning[j]
        x_err = (binning[j+1]-binning[j])/2. if j < len(binning)-1 else 0
        ratioSyst.SetPointError(j, x_err,x_err,0.02, 0.02)

    canNew = ROOT.TCanvas("canNew","can", 700,700)
    #canNew.SetLogx()
    
    pad1=ROOT.TPad("pad1","MyTitle",0.,0.3,1.,1.)
    pad1.SetLeftMargin(0.1)
    pad1.SetBottomMargin(0.01)
    pad1.SetTopMargin(0.08)
    pad1.Draw()
    #pad1.SetLogx()
    pad1.cd()

    shapeHist.Draw("hist")
    DataHist.Draw("same")
    MCHist.Draw("same")

    leg2 = ROOT.TLegend(0.52,0.55,0.95,0.67)
    leg2.SetFillColor(ROOT.kWhite)
    leg2.SetShadowColor(ROOT.kWhite)
    leg2.SetBorderSize(0)
    leg2.SetTextSize(0.035)
    leg2.SetTextFont(42)

    leg2.AddEntry(DataHist,  "Run 2017MET+HTMHT+JetHT PD") if options.Run2017 else leg2.AddEntry(DataHist,    "Run2016 MET+HTMHT+JetHT PD")
    if options.channel == "dilep":
        leg2.AddEntry(MCHist,    "t#bar{t} Fall17 MC") if options.Run2017 else leg2.AddEntry(MCHist,    "t#bar{t} Summer16 MC")
        leg2.AddEntry(shapeHist, "Lepton spectrum, ttW MC", 'f')
    else:
        leg2.AddEntry(MCHist,    "ttZ Fall17 MC") if options.Run2017 else leg2.AddEntry(MCHist,    "ttZ Summer16 MC")
        leg2.AddEntry(shapeHist, "Lepton spectrum, ttZ MC", 'f')

    leg2.Draw()
    
    canNew.cd()

    extraText = "Preliminary"
    latex1 = ROOT.TLatex()
    latex1.SetNDC()
    latex1.SetTextSize(0.04)
    latex1.SetTextAlign(11) # align right
    latex1.DrawLatex(0.10,0.95,'CMS #bf{#it{'+extraText+'}}')
    if options.Run2017:
        latex1.DrawLatex(0.72,0.95,"#bf{%sfb^{-1}} (13TeV)"%"41.9")
    else:
        latex1.DrawLatex(0.72,0.95,"#bf{%sfb^{-1}} (13TeV)"%"35.9")
    
    pad2=ROOT.TPad("pad2","datavsMC",0.,0.,1.,.3)
    pad2.SetLeftMargin(0.1)
    pad2.SetBottomMargin(0.3)
    pad2.SetTopMargin(0.01)
    #pad2.SetLogx()
    pad2.Draw()
    pad2.cd()

    numHist.SetMaximum(1.06)
    numHist.SetMinimum(0.94)

    numHist.SetLineColor(ROOT.kBlack)
    numHist.GetXaxis().SetMoreLogLabels()
    numHist.GetXaxis().SetNoExponent()
    numHist.GetXaxis().SetTitleSize(0.13)
    numHist.GetXaxis().SetLabelSize(0.11)
    numHist.GetXaxis().SetLabelOffset(0.02)
    numHist.GetYaxis().SetTitleSize(0.145)
    numHist.GetYaxis().SetLabelSize(0.13)
    numHist.GetYaxis().SetTitleOffset(0.32)
    numHist.GetYaxis().SetNdivisions(504)

    numHist.GetXaxis().SetTitle("p_{T}(l) (GeV)")
    #numHist.GetXaxis().SetLabelSize(0.18)
    #numHist.GetXaxis().SetBinLabel(1, "mmm")
    #numHist.GetXaxis().SetBinLabel(2, "emm")
    #numHist.GetXaxis().SetBinLabel(3, "eem")
    #numHist.GetXaxis().SetBinLabel(4, "eee")
    #numHist.GetXaxis().SetTitle("N_{e}")
    numHist.GetYaxis().SetTitle("Data/MC")

    one = ROOT.TF1("one","1",0,200)
    one.SetLineColor(ROOT.kRed)

    ratioSyst.SetFillColor(ROOT.kGray+1)
    ratioSyst.SetFillStyle(3444)
    ratioSyst.SetLineWidth(3)
    ratioSyst.SetLineColor(ROOT.kGray+1)
    ratioSyst.SetMarkerColor(ROOT.kGray+1)
    ratioSyst.SetMarkerStyle(0)
    ratioSyst.SetMarkerSize(0)
    
    numHist.SetMarkerSize(0)
    numHist.SetLineWidth(0)
    numHist.Draw("e1p")
    one.Draw("same")
    ratioSyst.Draw("2 same")
    ratioAsym.Draw("e1p same")


    plotDir = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/trigger/2l_OR_combined_altBinning/"
    
    name = "lep_pt[%s]_Run2017"%i if options.Run2017 else "lep_pt[%s]_Run2016"%i
    #name = "nElectrons_Run2017" if options.Run2017 else "nElectrons_Run2016"
    
    for e in ['.png', '.pdf', '.root']:
        canNew.Print(plotDir+name+e)
    

