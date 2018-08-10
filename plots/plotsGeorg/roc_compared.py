###########
# imports #
###########

# Standard imports
import ROOT
import os
from array import array
from copy import deepcopy
from multiprocessing import Pool
from functools import partial

# RootTools
from RootTools.core.standard import *

# User specific 
from TopEFT.Tools.user import plot_directory
plot_directory_=os.path.join(plot_directory, 'DeepLepton')
plot_directory=plot_directory_

# plot samples definitions
from def_plot_samples import plot_plotList, plot_samples, plot_samples_iso, roc_plot_variables, eS, eB

###################
# define plotlist #
###################

plotListMuo=[]
plotListMuo.append({"LeptonFlavour":"Muo", "Date":"20180729",            "isTrainData":0, "isIsolationTraining":0 ,"TrainingName":"std_PF_withoutSV",     "Variable":"prob_lep_isPromptId", "plotColor":ROOT.kRed,   "lineWidth":2})
plotListMuo.append({"LeptonFlavour":"Muo", "Date":"20180731",            "isTrainData":0, "isIsolationTraining":0 ,"TrainingName":"std_PFandSV",          "Variable":"prob_lep_isPromptId", "plotColor":ROOT.kRed+1, "lineWidth":2})
plotListMuo.append({"LeptonFlavour":"Muo", "Date":"20180808_std_PfAndSv","isTrainData":0, "isIsolationTraining":0 ,"TrainingName":"std_PFandSV_moreVars", "Variable":"prob_lep_isPromptId", "plotColor":ROOT.kRed+2, "lineWidth":2})

plotListEle=[]
plotListEle.append({"LeptonFlavour":"Ele", "Date":"20180730","isTrainData":0,             "isIsolationTraining":0 ,"TrainingName":"MVA_Fall17noIso",      "Variable":"lep_mvaIdFall17noIso", "plotColor":ROOT.kGray, "lineWidth":2})
plotListEle.append({"LeptonFlavour":"Ele", "Date":"20180730","isTrainData":0,             "isIsolationTraining":0 ,"TrainingName":"std_PF_withoutSV",     "Variable":"prob_lep_isPromptId", "plotColor":ROOT.kRed,   "lineWidth":2})
plotListEle.append({"LeptonFlavour":"Ele", "Date":"20180731","isTrainData":0,             "isIsolationTraining":0 ,"TrainingName":"std_PFandSV",          "Variable":"prob_lep_isPromptId", "plotColor":ROOT.kRed+1, "lineWidth":2})
plotListEle.append({"LeptonFlavour":"Ele", "Date":"20180808_std_PfAndSv","isTrainData":0, "isIsolationTraining":0 ,"TrainingName":"std_PFandSV_moreVars", "Variable":"prob_lep_isPromptId", "plotColor":ROOT.kRed+2, "lineWidth":2})

plotList=[
            plotListMuo,
            plotListEle
         ]

##################
# load variables #
##################

# variables to read
variables=roc_plot_variables()

#########################
# define plot structure #
#########################

pt_cuts=[]
pt_cuts.append({"Name":"pt15to25","lower_limit":15, "upper_limit":25})
pt_cuts.append({"Name":"pt25toInf","lower_limit":25, "upper_limit":float("Inf")})

cutList=[]
cutList.append({"Name":"relIso", "VarName":"relIso03", "Var":"lep_relIso03", "cuts":[0.1,0.2,0.3,0.4,0.5], "operator":"<="})

logY=1

####################################
# loop over samples and draw plots #
####################################

#define lists
for plotFlavour in plotList:

    colorList=[]
    lineWidthList=[]
        
    for plot in plotFlavour:
        colorList.append(plot["plotColor"])
        lineWidthList.append(plot["lineWidth"])

    readerData=[]
    plotLegend=[]

    for i in xrange(len(pt_cuts)):

        readerData.append([])
        plotLegend.append([])
            
        for var in cutList:
            for j in xrange(len(var["cuts"])):
                
                readerData[i].append([])
                plotLegend[i].append([])

                for k in xrange(len(plotFlavour)): 
                    readerData[i][j].append([])
                    plotLegend[i][j].append([])
                    legendString=plotFlavour[k]["TrainingName"]+", "+var["VarName"]+var["operator"]+str(var["cuts"][j])
                    plotLegend[i][j][k]=legendString

    #reader part
    i=0
    j=0
    k=0
    for plot in plotFlavour:

        print (plot["LeptonFlavour"],plot["Date"],plot["isTrainData"])
        #load sample
        if plot["isIsolationTraining"]:
            samples=plot_samples_iso(plot["LeptonFlavour"],plot["Date"],plot["isTrainData"]) 
        else:
            samples=plot_samples(plot["LeptonFlavour"],plot["Date"],plot["isTrainData"]) 
        print samples
        isTrainData=samples["isTrainData"]  #1=true, 0=false
        plotDate=samples["plotDate"]

        # reader class
        reader = samples["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
        # loop
        reader.start()
        
        while reader.run():
            for pt_cut in pt_cuts:
                for var in cutList:
                    for cut in var["cuts"]:
                        if reader.event.lep_pt>=pt_cut["lower_limit"] and reader.event.lep_pt<=pt_cut["upper_limit"]:
                            if (getattr(reader.event,var["Var"]) <= cut if var["operator"]=="<=" else getattr(reader.event,var["Var"]) >= cut):
                                #print i, j, k, reader.event.lep_pt, reader.event.lep_relIso03, reader.event.lep_isPromptId, getattr(reader.event, plot["Variable"])
                                readerData[i][j][k].append([reader.event.lep_isPromptId, getattr(reader.event, plot["Variable"])])            
                        j+=1
                i+=1
                j=0
            i=0
        k+=1


    #plot Graphs
    for i in xrange(len(pt_cuts)):

        for var in cutList:
            for j in xrange(len(var["cuts"])):

                #Draw TGraph
                c=ROOT.TCanvas()
                if logY: c.SetLogy()
                mg=ROOT.TMultiGraph()
                g=[]
                ng=0

                #calculate eS and eB
                for dataset in readerData[i][j]:
                    p=array('d')
                    x=array('d')
                    y=array('d')

                    prange=[pval*0.01 for pval in xrange(-100,100)]
                    for pval in prange:
                        x.append(eS(pval, dataset))
                        y.append(eB(pval, dataset)) if logY else y.append(1-eB(pval, dataset))
                    
                    #parallelize calculations 
                    #if __name__ == '__main__':
                    #    pool = Pool(processes=4)
                    #    eS_p=partial(eS,rocdataset=dataset)
                    #    x=array('d', pool.map(eS_p, [pval for pval in prange]))
                    #    eB_p=partial(eB,rocdataset=dataset)
                    #    y=array('d', pool.map(eB_p if logY else 1-eB_p, [pval for pval in prange]))
                    
                    gname=plotLegend[i][j][ng]
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
                mg.SetTitle(pt_cut["Name"]+" "+samples["sample"].texName+(" - TrainData" if isTrainData else " - TestData"))
                mg.GetXaxis().SetTitle('eS')
                mg.GetXaxis().SetLimits(0.597, 1.003)
                mg.GetYaxis().SetTitle('eB' if logY else '1-eB')
                mg.GetYaxis().SetRangeUser(0.0009, 1.01) if logY else mg.GetYaxis().SetLimits(0.0, 1.0)
                #c.BuildLegend(0.12,0.90,0.5,0.7) if logY else c.BuildLegend()
                c.BuildLegend()
                directory=(os.path.join(plot_directory, "ROC_compared_20180808"))
                if not os.path.exists(directory):
                    os.makedirs(directory)
                c.Print(os.path.join(directory, plot["LeptonFlavour"]+("_TrainData_" if isTrainData else "_TestData_")+'roc_compared_'+pt_cuts[i]["Name"]+'_cut_'+var["Name"]+'='+str(var["cuts"][j])+'.png'))
