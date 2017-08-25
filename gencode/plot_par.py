
# Standard imports
import ROOT
import os

# TopEFT
from TopEFT.tools.EFT  import *
from TopEFT.tools.user import plot_directory

# Logger
import logging
logger = logging.getLogger(__name__)

ROOT.gROOT.LoadMacro('scripts/tdrstyle.C')
ROOT.setTDRStyle()

model = 'HEL_UFO'

#coup = 'cuW'
#couplingValues = [ i*0.077/15 for i in range(-15,15) ]

#coup = 'cuG'
#couplingValues = [ i*0.007/15 for i in range(-15,15) ]

coup = 'cuB'
couplingValues = [ i*0.3/15 for i in range(-15,15) ]


config = configuration(model)

HEL_couplings = couplings()
HEL_couplings.addBlock("newcoup", HEL_couplings_newcoup)
HEL_couplings.setCoupling(coup,0)

styles = {"ttZ": {"marker": 20, "color": ROOT.kCyan+2}, "ttW": {"marker": 21, "color":ROOT.kRed+1}, "ttH": {"marker":22, "color":ROOT.kGreen+2}}

ttZ = process("ttZ", 1, config)
ttW = process("ttW", 1, config)
ttH = process("ttH", 1, config)

processes = [ttH,ttZ,ttW]

for p in processes:
    p.addCoupling(HEL_couplings)
    p.couplings.setCoupling(coup, 0.0)
    logger.info( "Checking SM x-sec:" )
    p.SMxsec = p.getXSec()
    if p.SMxsec.val == 0: p.SMxsec = u_float(1)

hists = []
fits = []
m = 0

for p in processes:
    #hists.append(ROOT.TGraph(len(couplingValues)))
    #hists.append(ROOT.TH1F(p.process,"",len(couplingValues),min(couplingValues),max([abs(min(couplingValues)),max(couplingValues)])))
    hists.append(ROOT.TH1F(p.process,p.process,len(couplingValues),min(couplingValues),max(couplingValues)))
    hists[-1].SetMarkerColor(styles[p.process]["color"])
    hists[-1].SetLineColor(styles[p.process]["color"])
    hists[-1].SetLineWidth(1)

    hists[-1].SetMarkerStyle(styles[p.process]["marker"])
    hists[-1].GetXaxis().SetTitle(coup)
    hists[-1].GetYaxis().SetTitle("#sigma_{NP+SM}/#sigma_{SM}")
    for i,cv in enumerate(couplingValues):
        p.couplings.setCoupling(coup, cv)
        ratio = p.getXSec()/p.SMxsec
        hists[-1].SetBinContent(i+1,ratio.val)
        hists[-1].SetBinError(i+1,ratio.sigma)
    hists[-1].SetStats(0)
#    hists[-1].Draw(printCmd)
#    printCmd = "e1p same"
    
    # Do the fits
    fits.append(ROOT.TF1("f_%s"%p.process, "[0] + [1]*x + [2]*x**2", 0, len(couplingValues)))
    fits[-1].SetParameters(2,-1)
    fits[-1].SetLineWidth(2)
    fits[-1].SetLineStyle(1)
    fits[-1].SetLineColor(styles[p.process]["color"])
    hists[-1].Fit("f_%s"%p.process, "S")
    m = hists[-1].GetMaximum() if hists[-1].GetMaximum() > m else m

can = ROOT.TCanvas("can","",700,700)
printCmd = "e1p"
for h in hists:
    h.SetMinimum(0)
    h.SetMaximum(m)
    h.Draw(printCmd)
    printCmd = "e1p same"


leg = ROOT.TLegend(0.85,0.82,0.98,0.95)
leg.SetFillColor(ROOT.kWhite)
leg.SetShadowColor(ROOT.kWhite)
leg.SetBorderSize(1)
leg.SetTextSize(0.035)

for h in hists:
    leg.AddEntry(h)

leg.Draw()

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11)

latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{Simulation}}')
latex1.DrawLatex(0.65,0.96,'#bf{%sLO (13TeV)}'%model.replace('_',' ').replace('UFO',''))

plotDir = os.path.join( plot_directory,model,"xsec")
if not os.path.isdir(plotDir):
    os.makedirs(plotDir)

for e in [".png",".pdf",".root"]:
    can.Print(plotDir+coup+e)
