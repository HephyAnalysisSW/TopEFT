''' Make 2D plot of xsec with variied couplings
'''

# Standard imports
import ROOT
import os
import itertools
import ctypes

# TopEFT imports
from TopEFT.gencode.Configuration import Configuration
from TopEFT.gencode.Process       import Process
from TopEFT.tools.u_float         import u_float
from TopEFT.tools.user            import plot_directory

# Logging
import TopEFT.tools.logger as logger
logger = logger.get_logger("CRITICAL", logFile = None)

# Plot style
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/gencode/scripts/tdrstyle.C')
ROOT.setTDRStyle()
ROOT.gStyle.SetNumberContours(255)

# Function for Delaunay triangulated 2D graph
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

interpolate         = True
drawContours        = True
model_name          = 'ewkDM'
nonZeroCouplings    = ("DC1V","DC1A","DC2V","DC2A")
nZC_latex           = ("#DeltaC_{1,V}", "#DeltaC_{1,A}", "#DeltaC_{2,V}", "#DeltaC_{2,A}")
processes           = ["ttZ","ttH","ttW"]

contours = {'ttZ': [0.74,0.87,1.15,1.3], 'ttW': [0.58,0.79,1.23,1.46], 'ttH':[0.33,0.67,1.33,1.67]}

n = 2
points          = [ round(i*1.0/n,2) for i in range(-n,n+1) ]
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
    config = Configuration( model_name = model_name, modified_couplings = {} )
    p = Process(process = proc, nEvents = 50000, config = config)
    SM_xsec[proc] = p.xsec()
    
    logger.info("SM x-sec: %s", SM_xsec[proc])
    
    for comb in combinations:

        logger.info("Making 2D plots for %s",comb)
        fixedPoints = list(nonZeroCouplings)
        subDir = "{}_vs_{}".format(comb[0],comb[1])
        if interpolate:
            subDir += "_interpolated"
        for c in comb: fixedPoints.remove(c)

        for v in points:
            for w in points:
                fileName = "{}={:.2f}_{}={:.2f}".format(fixedPoints[0],v,fixedPoints[1],w)
                nameStr = "_".join([proc, subDir, fileName])
                filePath = os.path.join(plot_directory,model_name,"2D_scans",proc,subDir)

                x_list = []
                y_list = []
                z_list = []             
                
                for x in points:
                    for y in points:
                        modified_couplings = { fixedPoints[0]:v, fixedPoints[1]:w, comb[0]:x, comb[1]:y }
    
                        #logger.info("Couplings:    %s", ", ".join( [ "%s=%5.4f" % c for c in modified_couplings.items()] ))
                        
                        # Create configuration class
                        config = Configuration( model_name = model_name, modified_couplings = modified_couplings )
                        
                        p = Process(process = proc, nEvents = 50000, config = config)
                        if p.hasXSec():
                            logger.debug("Couplings:    %s", ", ".join( [ "%s=%5.4f" % c for c in modified_couplings.items()] ))
                            xsec_val = p.xsec()
                            ratio = xsec_val/SM_xsec[proc]
                        else:
                            ratio = u_float(-1.)
                        x_list.append(x)
                        y_list.append(y)
                        z_list.append(ratio.val)

                        config.cleanup()
                
                if interpolate:
                    a = toGraph2D(nameStr,nameStr,len(x_list),x_list,y_list,z_list)

                    xmin = min(x_list)
                    xmax = max(x_list)
                    ymin = min(y_list)
                    ymax = max(y_list)
                    bin_size = 0.125
                    nxbins = max(1, min(500, int((xmax-xmin+bin_size/100.)/bin_size)))
                    nybins = max(1, min(500, int((ymax-ymin+bin_size/100.)/bin_size)))
                    #print nxbins,nybins
                    a.SetNpx(nxbins)
                    a.SetNpy(nybins)
                    hists.append(a.GetHistogram().Clone())
                else:
                    a = ROOT.TH2F(nameStr, nameStr, len(points), min(x_list), max(x_list), len(points), min(y_list), max(y_list))
                    k = 0
                    for i in range(len(points)):
                        for j in range(len(points)):
                            a.SetBinContent(i+1, j+1, z_list[k])
                            k += 1
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
                    c_contlist = ((ctypes.c_double)*(len(contours[proc])))(*contours[proc])
                    histsForCont.SetContour(len(c_contlist),c_contlist)
                    histsForCont.Draw("contzlist")
                    cans[-1].Update()
                    conts = ROOT.gROOT.GetListOfSpecials().FindObject("contours")
                    cont_m2 = conts.At(0).Clone()
                    cont_m1 = conts.At(1).Clone()
                    cont_p1 = conts.At(2).Clone()
                    cont_p2 = conts.At(3).Clone()
                
                pads.append(ROOT.TPad(nameStr,"",0.,0.,1.,1.))
                pads[-1].SetRightMargin(0.20)
                pads[-1].SetLeftMargin(0.14)
                pads[-1].SetTopMargin(0.11)
                pads[-1].Draw()
                pads[-1].cd()

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
                latex1.DrawLatex(0.14,0.92,'#bf{%s, couplings: %s}'%(p.process, fileName.replace('_',', ').replace("DC","#DeltaC_{").replace("V",",V}").replace("A",",A}")))
                latex1.DrawLatex(0.79,0.96,'#bf{MC (13TeV)}')
                
                if not os.path.isdir( filePath ):
                    os.makedirs( filePath )

                f = os.path.join( filePath, fileName )
                for e in [".png",".pdf",".root"][:1]:
                    cans[-1].Print(f+e)

