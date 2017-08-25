''' Make 2D plot of xsec with variied couplings
'''

# Standard imports
import ROOT
import os

# TopEFT imports
from TopEFT.gencode.EFT import *
from TopEFT.tools.user import plot_directory, results_directory
from TopEFT.tools.niceColorPalette import niceColorPalette
import itertools

# Plot style
ROOT.gROOT.LoadMacro('scripts/tdrstyle.C')
ROOT.setTDRStyle()
ROOT.gStyle.SetNumberContours(255)

#niceColorPalette(255)

#model = 'HEL_UFO'
model = 'TopEffTh'

#nonZeroCouplings = ("cuW", "cuB")
nonZeroCouplings = ("IC3phiq", "ICtW")

n = 5

#cuB = [ i*0.3/n for i in range(-n,n+1) ]
cuB = [ i*10.0/n for i in range(-n,n+1) ]

# this is the workaround
couplingPairs = [a for a in itertools.permutations(cuB,2)] + zip(cuB,cuB)
couplingPairs = [(round(a[0],2), round(a[1],2)) for a in couplingPairs]

config = configuration(model)

HEL_couplings = couplings()
#HEL_couplings.addBlock("newcoup", HEL_couplings_newcoup)
HEL_couplings.addBlock("dim6", TOP_EFT_couplings_dim6)
HEL_couplings.addBlock("fourfermion", TOP_EFT_couplings_fourfermion)

#HEL_couplings.setCoupling(coup,0)

styles = {"ttZ": {"marker": 20, "color": ROOT.kCyan+2}, "ttW": {"marker": 21, "color":ROOT.kRed+1}, "ttH": {"marker":22, "color":ROOT.kGreen+2}}

ttZ = process("ttZ", 1, config)
ttW = process("ttW", 1, config)
ttH = process("ttH", 1, config)

processes = [ttH,ttZ,ttW]
#processes = [ttH]

for p in processes:
    p.addCoupling(HEL_couplings)
    p.couplings.setCoupling("Lambda",1000.)
    p.couplings.setCoupling(nonZeroCouplings[0], 0.)
    p.couplings.setCoupling(nonZeroCouplings[1], 0.)
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

def toGraph2D(name,title,length,x,y,z):
    result = ROOT.TGraph2D(length)
    result.SetName(name)
    result.SetTitle(title)
    for i in range(length):
        result.SetPoint(i,x[i],y[i],z[i])
    h = result.GetHistogram()
    h.SetMinimum(min(z))
    h.SetMaximum(max(z))
    c = ROOT.TCanvas()
    result.Draw()
    del c
    #res = ROOT.TGraphDelaunay(result)
    return result


for p in processes:
    x = []
    y = []
    z = []

    #hists.append(ROOT.TH2F(p.process,p.process,len(cuB)*3,min(cuB)-0.03,max(cuB)+0.03,len(cuB)*3,min(cuB)-0.03,max(cuB)+0.03))
    for i,cv0 in enumerate(cuB):
        for j,cv1 in enumerate(cuB):
            p.couplings.setCoupling(nonZeroCouplings[0], round(cv0,2))
            p.couplings.setCoupling(nonZeroCouplings[1], round(cv1,2))
            ratio = p.getXSec()/p.SMxsec
            #bin_x = hists[-1].GetXaxis().FindBin(cv0)
            #bin_y = hists[-1].GetYaxis().FindBin(cv1)
            #hists[-1].SetBinContent(bin_x,bin_y,ratio.val)
            #hists[-1].SetBinContent(i+1,j+1,ratio.val)

            x.append(cv0)
            y.append(cv1)
            z.append(ratio.val)
            
    a = toGraph2D(p.process,p.process,len(x),x,y,z)
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    bin_size = 0.05 # 0.01
    nxbins = max(1, min(500, int((xmax-xmin+bin_size/100.)/bin_size)))
    nybins = max(1, min(500, int((ymax-ymin+bin_size/100.)/bin_size)))
    print nxbins,nybins
    a.SetNpx(nxbins)
    a.SetNpy(nybins)
    hists.append(a.GetHistogram().Clone())
    #hists[-1].GetXaxis().SetTitle("c_{uW}")
    #hists[-1].GetYaxis().SetTitle("c_{uB}")
    hists[-1].GetXaxis().SetTitle("c_{#phiq}")
    hists[-1].GetYaxis().SetTitle("c_{tW}")
    hists[-1].GetZaxis().SetTitle("#sigma_{NP+SM}/#sigma_{SM}")   
    hists[-1].SetStats(0)
    

    cans.append(ROOT.TCanvas("can_%s"%p.process,"",700,700))
    pads.append(ROOT.TPad("pad_%s"%p.process,"",0.,0.,1.,1.))
    pads[-1].SetRightMargin(0.20)
    pads[-1].SetLeftMargin(0.15)
    pads[-1].SetTopMargin(0.06)
    pads[-1].Draw()
    pads[-1].cd()
    
    hists[-1].Draw("colz")

    latex1.DrawLatex(0.15,0.95,'CMS #bf{#it{Simulation} %s}'%p.process)
    latex1.DrawLatex(0.55,0.95,'#bf{%sLO (13TeV)}'%model.replace('_',' ').replace('UFO',''))

    plotDir = '/'.join([plot_directory,model,"xsec_2D_int/"])
    if not os.path.isdir(plotDir):
        os.makedirs(plotDir)
    
    for e in [".png",".pdf",".root"]:
        cans[-1].Print(plotDir+p.process+'_'+nonZeroCouplings[0]+'_'+nonZeroCouplings[1]+e)

    #hists[-1].SetMaximum(110)
    #hists[-1].SetMinimum(0.09)
    hists[-1].SetMaximum(5)
    hists[-1].SetMinimum(0.09)
    pads[-1].SetLogz()
    for e in [".png",".pdf",".root"]:
        cans[-1].Print(plotDir+p.process+'_'+nonZeroCouplings[0]+'_'+nonZeroCouplings[1]+'_log'+e)
