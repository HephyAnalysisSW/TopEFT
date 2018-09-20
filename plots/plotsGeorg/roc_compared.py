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
from def_plot_samples import *

###################
# define plotlist #
###################

plotListMuo=[]
#plotListMuo.append({"Flavour":"Muo", "Type":"DL_Id",  "Date":"20180729",            "isTrainData":0, "IsoTrained":0 ,"Name":"std_PF_withoutSV",     "Var":"prob_lep_isPromptId", "plotColor":ROOT.kGreen,   "lineWidth":2})
#plotListMuo.append({"Flavour":"Muo", "Type":"DL_Id",  "Date":"20180731",            "isTrainData":0, "IsoTrained":0 ,"Name":"std_PFandSV",          "Var":"prob_lep_isPromptId", "plotColor":ROOT.kGreen+1, "lineWidth":2})
plotListMuo.append({"Flavour":"Muo", "Type":"DL_Id",  "Date":"20180808_std_PfAndSv","isTrainData":0, "IsoTrained":0 ,"Name":"DeepLepton_std",       "Var":"prob_lep_isPromptId", "plotColor":ROOT.kGreen+2, "lineWidth":2})
plotListMuo.append({"Flavour":"Muo", "Type":"POG_Id", "Date":"20180808_std_PfAndSv","isTrainData":0, "IsoTrained":0 ,"Name":"POG_muoId_loose",      "Var":"lep_pfMuonId",        "plotColor":ROOT.kGray+1,  "lineWidth":4})
plotListMuo.append({"Flavour":"Muo", "Type":"POG_Id", "Date":"20180808_std_PfAndSv","isTrainData":0, "IsoTrained":0 ,"Name":"POG_muoId_medium",     "Var":"lep_tightId",         "plotColor":ROOT.kBlack,   "lineWidth":4})

plotListEle=[]
plotListEle.append({"Flavour":"Ele", "Type":"MVA_Id", "Date":"20180808_std_PfAndSv", "isTrainData":0, "IsoTrained":0 ,"Name":"MVA_Fall17noIso",      "Var":"lep_mvaIdFall17noIso", "plotColor":ROOT.kGray,    "lineWidth":2})
#plotListEle.append({"Flavour":"Ele", "Type":"DL_Id",  "Date":"20180730",             "isTrainData":0, "IsoTrained":0 ,"Name":"std_PF_withoutSV",     "Var":"prob_lep_isPromptId",  "plotColor":ROOT.kGreen,   "lineWidth":2})
#plotListEle.append({"Flavour":"Ele", "Type":"DL_Id",  "Date":"20180731",            "isTrainData":0,  "IsoTrained":0 ,"Name":"std_PFandSV",          "Var":"prob_lep_isPromptId",  "plotColor":ROOT.kGreen+1, "lineWidth":2})
plotListEle.append({"Flavour":"Ele", "Type":"DL_Id",  "Date":"20180808_std_PfAndSv", "isTrainData":0, "IsoTrained":0 ,"Name":"DeepLepton_std",       "Var":"prob_lep_isPromptId",  "plotColor":ROOT.kGreen+2, "lineWidth":2})
plotListEle.append({"Flavour":"Ele", "Type":"POG_Id", "Date":"20180808_std_PfAndSv", "isTrainData":0, "IsoTrained":0 ,"Name":"POG_eleId80x_veto",    "ValElePOGId":1,              "plotColor":ROOT.kGray,    "lineWidth":1})
plotListEle.append({"Flavour":"Ele", "Type":"POG_Id", "Date":"20180808_std_PfAndSv", "isTrainData":0, "IsoTrained":0 ,"Name":"POG_eleId80x_loose",   "ValElePOGId":2,              "plotColor":ROOT.kGray+1,  "lineWidth":1})
plotListEle.append({"Flavour":"Ele", "Type":"POG_Id", "Date":"20180808_std_PfAndSv", "isTrainData":0, "IsoTrained":0 ,"Name":"POG_eleId80x_medium",  "ValElePOGId":3,              "plotColor":ROOT.kGray+2,  "lineWidth":1})
plotListEle.append({"Flavour":"Ele", "Type":"POG_Id", "Date":"20180808_std_PfAndSv", "isTrainData":0, "IsoTrained":0 ,"Name":"POG_eleId80x_tight",   "ValElePOGId":4,              "plotColor":ROOT.kBlack,   "lineWidth":1})

plotList=[
            plotListMuo,
            plotListEle
         ]

##################
# load variables #
##################

# variables to read
variables=roc_plot_variables()

###############
# define cuts #
###############

pt_cuts=[]
pt_cuts.append({"Name":"pt10to25","lower_limit":10, "upper_limit":25})
pt_cuts.append({"Name":"pt25toInf","lower_limit":25, "upper_limit":float("Inf")})

relIsoCuts   = [0.4,0.2,0.1,0.05,1.0]

logY=1

####################################
# loop over samples and draw plots #
####################################

#define lists
for plotFlavour in plotList:

    colorList=[]
    lineWidthList=[]
    plotTypeList=[]
        
    for plot in plotFlavour:
        colorList.append(plot["plotColor"])
        lineWidthList.append(plot["lineWidth"])
        plotTypeList.append(plot["Type"])

    readerData=[]
    plotLegend=[]

    for i in xrange(len(pt_cuts)):

        readerData.append([])
        plotLegend.append([])
            
        for j in xrange(len(relIsoCuts)):
            
            readerData[i].append([])
            plotLegend[i].append([])

            for k in xrange(len(plotFlavour)): 
                readerData[i][j].append([])
                plotLegend[i][j].append([])
                legendString=plotFlavour[k]["Name"]+("_IP" if plotFlavour[k]["Type"]=="POG_Id" else "")
                plotLegend[i][j][k]=legendString

    #reader part
    i=0
    j=0
    k=0
    for plot in plotFlavour:

        print (plot["Flavour"],plot["Date"],plot["isTrainData"])
        #load sample
        if plot["IsoTrained"]:
            samples=plot_samples_iso(plot["Flavour"],plot["Date"],plot["isTrainData"]) 
        else:
            samples=plot_samples(plot["Flavour"],plot["Date"],plot["isTrainData"]) 
        print samples
        isTrainData=samples["isTrainData"]  #1=true, 0=false
        plotDate=samples["plotDate"]

        # reader class
        reader = samples["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
        # loop
        reader.start()
        
        while reader.run():
            for pt_cut in pt_cuts:
                for relIsoCut in relIsoCuts:
                    if reader.event.lep_pt>=pt_cut["lower_limit"] and reader.event.lep_pt<=pt_cut["upper_limit"]:
                        #print i, j, k, reader.event.lep_pt, reader.event.lep_relIso03, reader.event.lep_isPromptId, getattr(reader.event, plot["Variable"])

                        #check if lepton passes relIso and Impact Parameter cuts
                        passIsoId = passIso(relIsoCut, reader.event.lep_relIso03)
                        passIPId  = passIP(reader.event.lep_pdgId, reader.event.lep_etaSc, reader.event.lep_dxy, reader.event.lep_dz)

                        if passIsoId:
                            #Electron WPs (incl Iso cut and IP cuts)
                            if plot["Type"]=="POG_Id" and plot["Flavour"]=="Ele":
                                leptonVarDict={
                                                "etaSc": reader.event.lep_etaSc,
                                                "full5x5_sigmaIetaIeta": reader.event.lep_full5x5_sigmaIetaIeta,
                                                "abs(dEtaInSeed)": abs(reader.event.lep_dEtaInSeed),
                                                "abs(dPhiIn)": abs(reader.event.lep_dPhiScTrkIn),
                                                "H/E": reader.event.lep_hadronicOverEm,
                                                "abs(1/E-1/p)": abs(reader.event.lep_eInvMinusPInv),
                                                "missingInnerHits": reader.event.lep_lostHits,
                                                "conversionVeto": reader.event.lep_convVeto
                                               }
                                elePOGId  = getElePOGId(leptonVarDict)
                                readerData[i][j][k].append([reader.event.lep_isPromptId, 1 if (elePOGId>=plot["ValElePOGId"] and passIPId) else 0])
                            #Muon WP (incl Iso cut and IP cuts)
                            if plot["Type"]=="POG_Id" and plot["Flavour"]=="Muo":
                                readerData[i][j][k].append([reader.event.lep_isPromptId, 1 if (getattr(reader.event, plot["Var"])==1 and passIPId) else 0])
                            #Lepton MVAs (nonIso)
                            if plot["Type"]=="MVA_Id":
                                readerData[i][j][k].append([reader.event.lep_isPromptId, getattr(reader.event, plot["Var"])])
                            #DeepLepton
                            if plot["Type"]=="DL_Id":
                                readerData[i][j][k].append([reader.event.lep_isPromptId, getattr(reader.event, plot["Var"])])
                    
                    j+=1
                i+=1
                j=0
            i=0
        k+=1


    #plot Graphs
    for i in xrange(len(pt_cuts)):
        for j in xrange(len(relIsoCuts)):

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

                prange=[1] if plotTypeList[ng]=="POG_Id" else [pval*0.01 for pval in xrange(-100,100)]
                for pval in prange:
                    x.append(eS(pval, dataset))
                    y.append(eB(pval, dataset)) if logY else y.append(1-eB(pval, dataset))

                if plotTypeList[ng]=="POG_Id":
                    print x, y
                
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
                if plotTypeList[ng]=="MVA_Id" or plotTypeList[ng]=="DL_Id":
                    g[ng].SetLineWidth(lineWidthList[ng])
                g[ng].SetLineColor(0 if plotTypeList[ng]=="POG_Id" else colorList[ng])
                g[ng].SetMarkerSize(1 if plotTypeList[ng]=="POG_Id" else 0)
                g[ng].SetMarkerColor(colorList[ng])
                if plotTypeList[ng]=="POG_Id":
                    g[ng].SetMarkerStyle( 8 )
                g[ng].SetFillStyle(0)
                g[ng].SetFillColor(0)
                g[ng].Draw("P" if plotTypeList[ng]=="POG_Id" else "C")
                #nmaxtext.DrawLatex(x[nmax],y[nmax],"mvaId=%1.2f" %p[nmax])
                mg.Add(g[ng])
                ng += 1
            mg.Draw("ACP")
            #mg.SetTitle(pt_cut["Name"]+" "+samples["sample"].texName+(" - TrainData" if isTrainData else " - TestData"))
            mg.GetXaxis().SetTitle('eS')
            mg.GetXaxis().SetLimits(0.597, 1.003)
            mg.GetYaxis().SetTitle('eB' if logY else '1-eB')
            mg.GetYaxis().SetRangeUser(0.0009, 1.01) if logY else mg.GetYaxis().SetLimits(0.0, 1.0)
            #c.BuildLegend(0.12,0.90,0.5,0.7) if logY else c.BuildLegend()
            c.BuildLegend()
            drawObjects(isTrainData, samples["leptonType"], 'TTJets+QCD', pt_cuts[i]["Name"], relIsoCuts[j] )
            drawObjectsSmall(isTrainData, samples["leptonType"], 'TTJets+QCD', pt_cuts[i]["Name"], relIsoCuts[j] )
            directory=(os.path.join(plot_directory, "ROC_compared_20180808"))
            if not os.path.exists(directory):
                os.makedirs(directory)
            c.Print(os.path.join(directory, plot["Flavour"]+("_TrainData_" if isTrainData else "_TestData_")+'roc_compared_'+pt_cuts[i]["Name"]+'_relIsoCut='+str(relIsoCuts[j])+'.png'))
