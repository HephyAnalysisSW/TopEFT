###########
# imports #
###########

# Standard imports
import ROOT
import os
from array import array
from copy import deepcopy

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
MVAList.append({"Name":"MVA_Fall17noIso", "Var":"lep_mvaIdFall17noIso", "plotColor":[ROOT.kGray,ROOT.kGray+1,ROOT.kGray+2,ROOT.kGray+3,ROOT.kGray+4], "lineWidth":1})
MVAList.append({"Name":"DeepLeptonSummer18", "Var":"prob_lep_isPromptId", "plotColor":[ROOT.kRed,ROOT.kRed+1,ROOT.kRed+2,ROOT.kRed+3,ROOT.kRed+4], "lineWidth":2})

pt_cuts=[]
pt_cuts.append({"Name":"pt15to25","lower_limit":15, "upper_limit":25})
pt_cuts.append({"Name":"pt25toInf","lower_limit":25, "upper_limit":float("Inf")})

cutList=[]
cutList.append({"Name":"relIso", "VarName":"relIso03", "Var":"lep_relIso03", "cuts":[0.1,0.2,0.3,0.4,0.5], "operator":"<="})

####################################
# loop over samples and draw plots #
####################################

for leptonFlavour in leptonFlavourList:
    if leptonFlavour["Name"]=="Muon":
        MVAList=[]
        MVAList.append({"Name":"DeepLeptonSummer18", "Var":"prob_lep_isPromptId", "plotColor":[ROOT.kRed,ROOT.kRed+1,ROOT.kRed+2,ROOT.kRed+3,ROOT.kRed+4], "lineWidth":2})

    for pt_cut in pt_cuts:
    
        for var in cutList:
            readerdata=[]
            plotLegend=[]
            
            colorList=[]
            lineWidthList=[]
            
            #Draw TGraph
            c=ROOT.TCanvas()
            if logY: c.SetLogy()
            mg=ROOT.TMultiGraph()
            g=[]
            ng=0
             
            for MVA in MVAList:
                i=0
                for cut in var["cuts"]:
                    legendString=MVA["Name"]+" |pdgId|="+str(leptonFlavour["pdgId"])+", "+var["VarName"]+var["operator"]+str(cut)
                    plotLegend.append(legendString)
                    colorList.append(MVA["plotColor"][i])
                    lineWidthList.append(MVA["lineWidth"])
                    readerdata.append([])
                    i += 1

            # reader class
            reader = leptonFlavour["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
            # loop
            reader.start()

            while reader.run():
                j=0
                for MVA in MVAList:
                    for cut in var["cuts"]:
                        if abs(reader.event.lep_pdgId)==leptonFlavour["pdgId"] and (reader.event.lep_pt>=pt_cut["lower_limit"] and reader.event.lep_pt<=pt_cut["upper_limit"]):
                            if (getattr(reader.event,var["Var"]) <= cut if var["operator"]=="<=" else getattr(reader.event,var["Var"]) >= cut):
                                readerdata[j].append([reader.event.lep_isPromptId, getattr(reader.event, MVA["Var"])])            
                                #print "pdgId %i, pt %f" %(reader.event.lep_pdgId, reader.event.lep_pt)
                        j += 1

            #calculate eS and eB
            for dataset in readerdata:
                p=array('d')
                x=array('d')
                y=array('d')

                prange=[pval*0.01 for pval in xrange(-100,100)]
                for pval in prange:
                    x.append(eS(pval, dataset))
                    y.append(eB(pval, dataset)) if logY else y.append(1-eB(pval, dataset))

                gname=plotLegend[ng]
                n=len(x)
                g.append(ROOT.TGraph(n,x,y))
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
            mg.Draw("AC")
            mg.SetTitle(pt_cut["Name"]+" "+leptonFlavour["sample"].texName+(" - TrainData" if PlotTrainData else " - TestData"))
            mg.GetXaxis().SetTitle('eS')
            mg.GetXaxis().SetLimits(0.597, 1.003)
            mg.GetYaxis().SetTitle('eB' if logY else '1-eB')
            mg.GetYaxis().SetRangeUser(0.0009, 1.01) if logY else mg.GetYaxis().SetLimits(0.0, 1.0)
            #c.BuildLegend(0.12,0.90,0.5,0.7) if logY else c.BuildLegend()
            c.BuildLegend()
            directory=(os.path.join(plot_directory, leptonFlavour["Name"], ElectronDate if leptonFlavour["Name"]=="Electron" else MuonDate))
            if not os.path.exists(directory):
                os.makedirs(directory)
            c.Print(os.path.join(directory, ("TrainData" if PlotTrainData else "TestData")+'_roc_'+pt_cut["Name"]+'_cut_'+var["Name"]+'.png'))
