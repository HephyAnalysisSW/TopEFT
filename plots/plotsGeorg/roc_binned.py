###########
# imports #
###########

# Standard imports
import ROOT
import os
from array import array
from copy import deepcopy
import math

# RootTools
from RootTools.core.standard import *

# User specific 
from TopEFT.Tools.user import plot_directory
plot_directory_=os.path.join(plot_directory, 'DeepLepton')
plot_directory=plot_directory_

# plot samples definitions
from def_plot_samples import plot_samples, roc_plot_variables, eS, eB

##############################
# load samples and variables #
##############################

#define samples for electorns and muons
samples=plot_samples()
sampleEle=samples["ele"]
sampleMuo=samples["muo"]
PlotTrainData=samples["plottraindata"]  #1=true, 0=false
ElectronDate=samples["eledate"]
MuonDate=samples["muodate"]
logY=1

# variables to read
variables=roc_plot_variables()

#########################
# define plot structure #
#########################

leptonFlavourList=[]
leptonFlavourList.append({"Name":"Electron", "ShortName":"ele", "pdgId":11, "sample":sampleEle})
leptonFlavourList.append({"Name":"Muon", "ShortName":"muo", "pdgId":13, "sample":sampleMuo})

MVAList=[]
MVAList.append({"Name":"MVA_Fall17noIso", "Var":"lep_mvaIdFall17noIso", "plotColor":ROOT.kGray, "lineWidth":1})
MVAList.append({"Name":"DeepLeptonSummer18", "Var":"prob_lep_isPromptId", "plotColor":ROOT.kRed, "lineWidth":2})

binnedList=[]
binnedList.append({"Name":"pt", "VarName":"|pt|", "Var":"lep_pt", "abs":1, "cuts":[0, 250], "bins":50})

####################################
# loop over samples and draw plots #
####################################

for leptonFlavour in leptonFlavourList:
    if leptonFlavour["Name"]=="Muon":
        MVAList=[]
        MVAList.append({"Name":"DeepLeptonSummer18", "Var":"prob_lep_isPromptId", "plotColor":ROOT.kRed, "lineWidth":2})
    
    for binVar in binnedList:

        colorList=[]
        lineWidthList=[]
        
        #Initialize Mulitgraph
        c=ROOT.TCanvas()
        c.SetLogy()
        mg=ROOT.TMultiGraph()
        g=[]
        ng=0

        for MVA in MVAList:
            
            colorList.append(MVA["plotColor"])
            lineWidthList.append(MVA["lineWidth"])

            # reader class
            readerData=[[] for i in xrange(binVar["bins"])]
            reader = leptonFlavour["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
            reader.start()
            while reader.run():
                if abs(reader.event.lep_pdgId)==leptonFlavour["pdgId"]:
                    cut_val = getattr(reader.event, binVar["Var"]) 
                    if cut_val >= binVar["cuts"][0] and cut_val <  binVar["cuts"][1]:
                        j=int(math.ceil(cut_val/(binVar["cuts"][1]-binVar["cuts"][0])*binVar["bins"]))-1
                        readerData[j].append([reader.event.lep_isPromptId, getattr(reader.event, MVA["Var"])])
                        #print "j=%i, pt=%f" %(j, reader.event.lep_pt)
                        #print "i=%i,j=%i,  pt=%f" %(i,j, reader.event.lep_pt)
            
            j=0
            x=array('d')
            y=array('d')
            for dataset in readerData:
                #print j+1, len(dataset)
                j += 1
                prange=[pval*0.001 for pval in range(950,1000)]
                for pval in prange:
                    xval=eB(pval,dataset)
                    p=pval 
                    #print pval, xval
                    if xval<=0.01:
                        break
                if not len(dataset)==0:
                    x.append(j*5)
                    y.append(eS(p,dataset))

            #Draw Graphs
            n=len(x)
            g.append(ROOT.TGraph(n,x,y))
            gname=(MVA["Name"]+": "+binVar["Var"]+", "+"eB<=0.01")
            g[ng].SetName(gname)
            g[ng].SetTitle(gname)
            g[ng].SetLineColor(colorList[ng])
            g[ng].SetLineWidth(lineWidthList[ng])
            g[ng].SetMarkerColor(colorList[ng])
            #g[ng].SetMarkerStyle( 5 )
            g[ng].SetFillStyle(0)
            g[ng].SetFillColor(0)
            g[ng].SetMarkerSize(0)
            g[ng].Draw("C")
            #nmaxtext.DrawLatex(x[nmax],y[nmax],"mvaId=%1.2f" %p[nmax])
            mg.Add(g[ng])
            ng += 1

        #Draw Multigraph
        mg.Draw("AC")
        mg.SetTitle(leptonFlavour["sample"].texName+(" - TrainData" if PlotTrainData else " - TestData"))
        mg.GetXaxis().SetTitle('pt')
        mg.GetYaxis().SetTitle('eS')
        #mg.GetYaxis().SetRangeUser(0.0,1.0)
        c.BuildLegend()
        directory=(os.path.join(plot_directory, ElectronDate if leptonFlavour["Name"]=="Electron" else MuonDate, leptonFlavour["Name"]))
        if not os.path.exists(directory):
            os.makedirs(directory)
        c.Print(os.path.join(directory, 'roc_binned_'+binVar["Name"]+'.png'))
