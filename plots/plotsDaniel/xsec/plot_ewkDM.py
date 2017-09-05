''' Make 2D plot of xsec with variied couplings
'''

# Standard imports
import ROOT
import os
import itertools
import ctypes

# TopEFT imports
from TopEFT.Generation.Configuration import Configuration
from TopEFT.Generation.Process       import Process
from TopEFT.tools.u_float         import u_float
from TopEFT.tools.user            import plot_directory

# Logging
import TopEFT.tools.logger as logger
logger = logger.get_logger("CRITICAL", logFile = None)

# Plot style
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()
ROOT.gStyle.SetNumberContours(255)

# Function for Delaunay triangulated 2D graph
def toGraph2D(name,title,length,x,y,z):
    result = ROOT.TGraph2D(length)
    result.SetName(name)
    result.SetTitle(title)
    for i in range(length):
        #print x[i],y[i],z[i]
        result.SetPoint(i,x[i],y[i],z[i])
    h = result.GetHistogram()
    h.SetMinimum(min(z))
    #print min(z)
    h.SetMaximum(max(z))
    #print max(z)
    c = ROOT.TCanvas()
    result.Draw()
    del c
    #res = ROOT.TGraphDelaunay(result)
    return result

interpolate         = True
drawContours        = True
model_name          = 'ewkDM'
nZC_latex           = ("#DeltaC_{1,V}", "#DeltaC_{1,A}", "#DeltaC_{2,V}", "#DeltaC_{2,A}")
processes           = ["ttZ","ttH","ttW"]

nonZeroCouplings    = ("DC1V","DC1A","DC2V","DC2A")
#dc1v = [ i*1.3/4 for i in range(-4,3) ]
#dc1a = [ i*1.3/4 for i in range(-2,5) ]
#dc2v = [ i*0.3/6 for i in range(-5,7) ]
#dc2a = [ i*0.3/6 for i in range(-5,7) ]
dc1v = [ i*1.0/2 for i in range(-2,3) ]
dc1a = dc2v = dc2a = dc1v
couplingValues = [dc1v,dc1a,dc2v,dc2a]
nDim = len(nonZeroCouplings)

# prepare the grid with all points
couplingGrid = [ a for a in itertools.product(*couplingValues) ]

# zip with coupling names
allCombinations =  [ zip(nonZeroCouplings, a) for a in couplingGrid ]
allCombinationsFlat = []
for comb in allCombinations:
    allCombinationsFlat.append([item for sublist in comb for item in sublist])


contours = {'ttZ': [0.74,0.87,1.15,1.3], 'ttW': [0.58,0.79,1.23,1.46], 'ttH':[0.33,0.67,1.33,1.67]}

n = 2
#points          = [ round(i*1.0/n,2) for i in range(-n,n+1) ]
points = {"DC1V":dc1v, "DC1A":dc1a, "DC2V":dc2v, "DC2A":dc2a}
combinations    = [ a for a in itertools.combinations(nonZeroCouplings,2) ]

hists   = []
cans    = []
pads    = []
SM_xsec = {}

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11)

logger.info("Model:        %s", model_name)

for proc in processes:
    logger.info("Starting with process %s", proc)
    config = Configuration( model_name = model_name )
    p = Process(process = proc, nEvents = 50000, config = config)
    SM_xsec[proc] = p.xsec(modified_couplings = {})
    
    logger.info("SM x-sec: %s", SM_xsec[proc])
    
    for comb in combinations:
        logger.info("Making 2D plots for %s",comb)
        fixedPoints = list(nonZeroCouplings)
        subDir = "{}_vs_{}".format(comb[0],comb[1])
        if interpolate:
            subDir += "_interpolated"
        for c in comb: fixedPoints.remove(c)

        for v in points[fixedPoints[0]]:
            for w in points[fixedPoints[1]]:
                fileName = "{}={:.2f}_{}={:.2f}".format(fixedPoints[0],v,fixedPoints[1],w)
                nameStr = "_".join([proc, subDir, fileName])
                filePath = os.path.join(plot_directory,model_name,"2D_scans",proc,subDir)

                x_list = []
                y_list = []
                z_list = []             
                
                for x in points[comb[0]]:
                    for y in points[comb[1]]:
                        modified_couplings = { fixedPoints[0]:v, fixedPoints[1]:w, comb[0]:x, comb[1]:y }
    
                        #logger.info("Couplings:    %s", ", ".join( [ "%s=%5.4f" % c for c in modified_couplings.items()] ))
                        
                        # Create configuration class
                        config = Configuration( model_name = model_name )
                        
                        p = Process(process = proc, nEvents = 50000, config = config)
                        if p.hasXSec(modified_couplings = modified_couplings):
                            logger.debug("Couplings:    %s", ", ".join( [ "%s=%5.4f" % c for c in modified_couplings.items()] ))
                            xsec_val = p.xsec(modified_couplings = modified_couplings)
                            ratio = xsec_val/SM_xsec[proc]
                            x_list.append(x)
                            y_list.append(y)
                            z_list.append(ratio.val)
                        else:
                            ratio = u_float(-1.)

                        config.cleanup()
                if interpolate:
                    a = toGraph2D(nameStr,nameStr,len(x_list),x_list,y_list,z_list)
                    xmin = min(x_list)
                    xmax = max(x_list)
                    ymin = min(y_list)
                    ymax = max(y_list)
                    bin_size_x = (abs(xmax)+abs(xmin))/(3*len(points[comb[0]]))
                    bin_size_y = (abs(ymax)+abs(ymin))/(3*len(points[comb[1]]))
                    nxbins = max(1, min(500, int((xmax-xmin+bin_size_x/100.)/bin_size_x))) + 1
                    nybins = max(1, min(500, int((ymax-ymin+bin_size_y/100.)/bin_size_y))) + 1
                    a.SetNpx(nxbins)
                    a.SetNpy(nybins)
                    hists.append(a.GetHistogram().Clone())
                else:
                    a = ROOT.TH2F(nameStr, nameStr, len(points[comb[0]]), min(x_list), max(x_list)+0.001, len(points[comb[1]]), min(y_list), max(y_list)+0.001)
                    for i,x in enumerate(x_list):
                        bin_x = a.GetXaxis().FindBin(x_list[i])
                        bin_y = a.GetYaxis().FindBin(y_list[i])
                        a.SetBinContent(bin_x, bin_y, z_list[i])
                    hists.append(a.Clone())

                cans.append(ROOT.TCanvas(nameStr,"",500,500))

                hists[-1].GetXaxis().SetTitle(comb[0].replace("DC","#DeltaC_{").replace("V",",V}").replace("A",",A}"))
                hists[-1].GetXaxis().SetNdivisions(505)
                hists[-1].GetYaxis().SetTitle(comb[1].replace("DC","#DeltaC_{").replace("V",",V}").replace("A",",A}"))
                hists[-1].GetYaxis().SetNdivisions(505)
                hists[-1].GetYaxis().SetTitleOffset(1.0)
                hists[-1].GetZaxis().SetTitle("#sigma_{NP+SM}/#sigma_{SM}")
                hists[-1].GetZaxis().SetTitleOffset(1.2)
                hists[-1].SetStats(0)
                
                if drawContours:    
                    histsForCont = hists[-1].Clone()
                    contDict = {}
                    for i, cont in enumerate(contours[proc]):
                        contour = [cont]
                        c_contlist = ((ctypes.c_double)*(len(contour)))(*contour)
                        histsForCont.SetContour(len(c_contlist),c_contlist)
                        histsForCont.Draw("contzlist")
                        cans[-1].Update()
                        conts = ROOT.gROOT.GetListOfSpecials().FindObject("contours")
                        contDict[cont] = conts.At(0).Clone()
                        if i == 0 or i == 3:
                            for c in contDict[cont]:
                                c.SetLineColor(ROOT.kRed)
                        else:
                            for c in contDict[cont]:
                                c.SetLineColor(ROOT.kOrange)
                        for c in contDict[cont]:
                            c.SetLineWidth(2)
                            c.SetLineStyle(7)
                
                pads.append(ROOT.TPad(nameStr,"",0.,0.,1.,1.))
                pads[-1].SetRightMargin(0.20)
                pads[-1].SetLeftMargin(0.14)
                pads[-1].SetTopMargin(0.11)
                pads[-1].Draw()
                pads[-1].cd()

                hists[-1].Draw("colz")

                if drawContours:
                    for cont in contDict.keys():#[cont_m1, cont_p1]:
                        for c in contDict[cont]:
                            c.Draw("same")


                latex1.DrawLatex(0.14,0.96,'CMS #bf{#it{Simulation}}')
                latex1.DrawLatex(0.14,0.92,'#bf{%s, couplings: %s}'%(p.process, fileName.replace('_',', ').replace("DC","#DeltaC_{").replace("V",",V}").replace("A",",A}")))
                latex1.DrawLatex(0.79,0.96,'#bf{MC (13TeV)}')
                
                if not os.path.isdir( filePath ):
                    os.makedirs( filePath )

                f = os.path.join( filePath, fileName )
                for e in [".png",".pdf",".root"][:1]:
                    cans[-1].Print(f+e)

