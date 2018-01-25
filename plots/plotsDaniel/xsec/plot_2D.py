''' Make 2D plot of xsec with variied couplings
'''

# Standard imports
import ROOT
import os
import ctypes

# TopEFT imports
from TopEFT.Generation.Configuration import *
from TopEFT.Generation.Process import *
from TopEFT.Tools.user import plot_directory, results_directory
from TopEFT.Tools.niceColorPalette import niceColorPalette
import itertools

# Logger
import logging
logger = logging.getLogger(__name__)

# Plot style
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()
ROOT.gStyle.SetNumberContours(255)

#model_name = 'HEL_UFO'
#model_name = 'TopEffTh'
#model_name = 'ewkDM'
#model_name = 'ewkDMGZ'
model_name = 'dim6top_LO'

#nonZeroCouplings = ("cuW", "cuB")
#nonZeroCouplings = ("IC3phiq", "ICtW")
#nonZeroCouplings = ("DC2V","DC2A")
#nonZeroCouplings = ("DVG","DAG")
#nonZeroCouplings = ("cuW", "cuB")
#dc2v = [ i*0.10/10 for i in range(-10,11) ]
#dc2a = [ i*0.30/10 for i in range(-10,11) ]

nonZeroCouplings = ("ctZ", "ctZI")
dc2v = [ i*2./5 for i in range(-5,6) ]
dc2a = [ i*2./5 for i in range(-5,6) ]

couplingValues = [dc2v,dc2a]

# prepare the grid with all points
couplingGrid = [ a for a in itertools.product(*couplingValues) ]

# zip with coupling names
allCombinations =  [ zip(nonZeroCouplings, a) for a in couplingGrid ]
allCombinationsFlat = []
for comb in allCombinations:
    allCombinationsFlat.append([item for sublist in comb for item in sublist])

#processes = [ "ttZ", "ttH", "ttW" ]
contours = {'ttZ': [0.74,0.87,1.15,1.3], 'ttZ_ll': [0.74,0.87,1.15,1.3], 'ttW': [0.58,0.79,1.23,1.46], 'ttH':[0.33,0.67,1.33,1.67], 'ttgamma':[0.33,0.67,1.33,1.67]}
#contours = {'ttZ': [0.74,0.87,1.20,1.3], 'ttW': [0.58,0.79,1.23,1.46], 'ttH':[0.33,0.67,1.33,1.67], 'ttgamma':[0.33,0.67,1.33,1.67]}


processes = [ "ttZ_ll" ]


drawContours = True
SM_xsec = {}
hists = []
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


for proc in processes[:1]:
    
    found = 0
    
    logger.info("Starting with process %s", proc)
    config = Configuration( model_name = model_name )
    p = Process(process = proc, nEvents = 50000, config = config)
    print "getting x-sec"
    SM_xsec[proc] = p.xsec(modified_couplings = {})

    x = []
    y = []
    z = []
    
    print "looping"
    for coup in allCombinationsFlat:
        coupling_names  = coup[::2]
        coupling_values = map(float,coup[1::2])

        modified_couplings = {c:v for c,v in zip( coupling_names, coupling_values ) }
        
        config = Configuration( model_name = model_name )
        p = Process(process = proc, nEvents = 50000, config = config)

        
        ratio = p.xsec(modified_couplings = modified_couplings, skip=True)/SM_xsec[proc]
        #print coupling_values
        if ratio.val > 0:
            found += 1
            #print "Found"
            x.append(coupling_values[0])
            y.append(coupling_values[1])
            z.append(ratio.val)
            
    print "plotting from %s points"%found
    a = toGraph2D(proc, proc, len(x), x, y, z)
    xmin = min( x )
    xmax = max( x )
    ymin = min( y )
    ymax = max( y )
    bin_size_x = 0.01/3 # 0.01
    bin_size_y = 0.02/3
    nxbins = max(1, min(500, int((xmax-xmin+bin_size_x/100.)/bin_size_x)))
    nybins = max(1, min(500, int((ymax-ymin+bin_size_y/100.)/bin_size_y)))
    #print nxbins,nybins
    a.SetNpx(nxbins)
    a.SetNpy(nybins)
    hists.append(a.GetHistogram().Clone())
    hists[-1].GetXaxis().SetTitle(coupling_names[0].replace("DC","C_{").replace("V",",V}").replace("A",",A}"))
    hists[-1].GetXaxis().SetNdivisions(505)
    hists[-1].GetYaxis().SetTitle(coupling_names[1].replace("DC","C_{").replace("V",",V}").replace("A",",A}"))
    hists[-1].GetYaxis().SetNdivisions(505)
    hists[-1].GetYaxis().SetTitleOffset(1.0)
    hists[-1].GetZaxis().SetTitle("#sigma_{NP+SM}/#sigma_{SM}")
    hists[-1].GetZaxis().SetTitleOffset(1.2)
    hists[-1].SetStats(0)
    hists[-1].Smooth()

    cans.append(ROOT.TCanvas("can_%s"%proc,"",700,700))

    if drawContours:
        histsForCont = hists[-1].Clone()
        c_contlist = ((ctypes.c_double)*(len(contours[proc])))(*contours[proc])
        histsForCont.SetContour(len(c_contlist),c_contlist)
        histsForCont.Draw("contzlist")
        cans[-1].Update()
        conts = ROOT.gROOT.GetListOfSpecials().FindObject("contours")
        cont_m2 = conts.At(0).Clone()
        cont_m1 = conts.At(1).Clone()
        cont_p1 = conts.At(2).Clone()
        cont_p2 = conts.At(3).Clone()
    
    pads.append(ROOT.TPad("pad_%s"%proc,"",0.,0.,1.,1.))
    pads[-1].SetRightMargin(0.20)
    pads[-1].SetLeftMargin(0.14)
    pads[-1].SetTopMargin(0.11)
    pads[-1].Draw()
    pads[-1].cd()
    
    hists[-1].SetMaximum(1.95) #1.95
    hists[-1].SetMinimum(0.95)

    hists[-1].Draw("colz")

    if drawContours:
        for conts in [cont_m1, cont_p1]:
            for cont in conts:
                cont.SetLineColor(ROOT.kRed)
                cont.SetLineWidth(2)
                cont.SetLineStyle(7)
                cont.Draw("same")
        for conts in [cont_m2, cont_p2]:
            for cont in conts:
                cont.SetLineColor(ROOT.kOrange)
                cont.SetLineWidth(2)
                cont.SetLineStyle(7)
                cont.Draw("same")


    latex1.DrawLatex(0.14,0.96,'CMS #bf{#it{Simulation}}')
    latex1.DrawLatex(0.14,0.92,'#bf{%s}'%proc)
    #latex1.DrawLatex(0.14,0.92,'#bf{%s, couplings: #DeltaC_{1,V}=0.00, #DeltaC_{1,A}=0.00}'%proc)
    latex1.DrawLatex(0.79,0.96,'#bf{MC (13TeV)}')

    plotDir = os.path.join( plot_directory,model_name,"simple_2D_scans_v2/" )
    if not os.path.isdir(plotDir):
        os.makedirs(plotDir)
    
    for e in [".png",".pdf",".root"]:
        cans[-1].Print(plotDir+proc+'_'+nonZeroCouplings[0]+'_'+nonZeroCouplings[1]+e)

    hists[-1].SetMaximum(1.95)
    hists[-1].SetMinimum(0.95)
    pads[-1].SetLogz()
    for e in [".png",".pdf",".root"]:
        cans[-1].Print(plotDir+proc+'_'+nonZeroCouplings[0]+'_'+nonZeroCouplings[1]+'_log'+e)
