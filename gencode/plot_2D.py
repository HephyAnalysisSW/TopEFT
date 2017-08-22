import ROOT,os
from TopEFT.gencode.EFT import *
from TopEFT.gencode.user import plot_directory
import itertools

ROOT.gROOT.LoadMacro('scripts/tdrstyle.C')
ROOT.setTDRStyle()

model = 'HEL_UFO'

nonZeroCouplings = ("cuW", "cuB")

n = 5

cuB = [ i*0.3/n for i in range(-n,n+1) ]

# this is the workaround
couplingPairs = [a for a in itertools.permutations(cuB,2)] + zip(cuB,cuB)
couplingPairs = [(round(a[0],2), round(a[1],2)) for a in couplingPairs]


config = configuration(model)

HEL_couplings = couplings()
HEL_couplings.addBlock("newcoup", HEL_couplings_newcoup)
#HEL_couplings.setCoupling(coup,0)

styles = {"ttZ": {"marker": 20, "color": ROOT.kCyan+2}, "ttW": {"marker": 21, "color":ROOT.kRed+1}, "ttH": {"marker":22, "color":ROOT.kGreen+2}}

ttZ = process("ttZ", 1, config)
ttW = process("ttW", 1, config)
ttH = process("ttH", 1, config)

processes = [ttH,ttZ,ttW]
#processes = [ttH]

for p in processes:
    p.addCoupling(HEL_couplings)
    p.couplings.setCoupling(nonZeroCouplings[0], 0.0)
    p.couplings.setCoupling(nonZeroCouplings[1], 0)
    print "Checking SM x-sec:"
    p.SMxsec = p.getXSec()
    if p.SMxsec.val == 0: p.SMxsec = u_float(1)

hists = []
fits = []
cans = []
pads = []
m = 0

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11)


for p in processes:
    #hists.append(ROOT.TGraph(len(couplingValues)))
    #hists.append(ROOT.TH1F(p.process,"",len(couplingValues),min(couplingValues),max([abs(min(couplingValues)),max(couplingValues)])))
    hists.append(ROOT.TH2F(p.process,p.process,len(cuB),min(cuB),max(cuB),len(cuB),min(cuB),max(cuB)))
    #hists[-1].SetMarkerColor(styles[p.process]["color"])
    #hists[-1].SetLineColor(styles[p.process]["color"])
    #hists[-1].SetLineWidth(1)

    #hists[-1].SetMarkerStyle(styles[p.process]["marker"])
    hists[-1].GetXaxis().SetTitle("c_{uW}")
    hists[-1].GetYaxis().SetTitle("c_{uB}")
    for i,cv0 in enumerate(cuB):
        for j,cv1 in enumerate(cuB):
            print cv0, cv1
            p.couplings.setCoupling(nonZeroCouplings[0], round(cv0,2))
            p.couplings.setCoupling(nonZeroCouplings[1], round(cv1,2))
            ratio = p.getXSec()/p.SMxsec
            hists[-1].SetBinContent(i+1,j+1,ratio.val)
        #hists[-1].SetBinError(i+1,ratio.sigma)
    hists[-1].SetStats(0)
#    hists[-1].Draw(printCmd)
#    printCmd = "e1p same"
    

    cans.append(ROOT.TCanvas("can_%s"%p.process,"",700,700))
    pads.append(ROOT.TPad("pad_%s"%p.process,"",0.,0.,1.,1.))
    pads[-1].SetRightMargin(0.15)
    pads[-1].SetTopMargin(0.06)
    pads[-1].Draw()
    pads[-1].cd()
    
    hists[-1].Draw("colz")

    latex1.DrawLatex(0.16,0.96,'CMS #bf{#it{Simulation} %s}'%p.process)
    latex1.DrawLatex(0.65,0.96,'#bf{%sLO (13TeV)}'%model.replace('_',' ').replace('UFO',''))

    plotDir = '/'.join([plot_directory,model,"xsec_2D/"])
    if not os.path.isdir(plotDir):
        os.makedirs(plotDir)
    
    for e in [".png",".pdf",".root"]:
        cans[-1].Print(plotDir+p.process+'_'+nonZeroCouplings[0]+'_'+nonZeroCouplings[1]+e)


