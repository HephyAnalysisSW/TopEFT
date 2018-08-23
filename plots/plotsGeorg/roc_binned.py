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
from def_plot_samples import *


#################
# load plotlist #
#################

plotList=plot_plotList()

for plot in plotList:

##############################
# load samples and variables #
##############################

    #define samples for electorns and muons
    if plot[3]=="iso":
        samples=plot_samples_iso(plot[0],plot[1],plot[2]) 
    else:
        samples=plot_samples(plot[0],plot[1],plot[2])

    # variables to read
    variables=roc_plot_variables()

#########################
# define plot structure #
#########################

    leptonFlavourList=[]
    MVAList=[]

    if samples["leptonType"]=="Ele":
        sampleEle=samples["sample"]
        leptonFlavourList.append({"Name":"Electron", "ShortName":"ele", "pdgId":11, "sample":sampleEle})
        #MVAList.append({"Name":"MVA_Fall17noIso",     "Type":"MVA_Id", "Var":"lep_mvaIdFall17noIso", "plotColor":ROOT.kGray,   "lineWidth":1})
        MVAList.append({"Name":"POG_eleId80x_veto",   "Type":"POG_Id", "ValElePOGId":1,              "plotColor":ROOT.kGray,   "lineWidth":1})
        MVAList.append({"Name":"POG_eleId80x_loose",  "Type":"POG_Id", "ValElePOGId":2,              "plotColor":ROOT.kGray+1, "lineWidth":1})
        MVAList.append({"Name":"POG_eleId80x_medium", "Type":"POG_Id", "ValElePOGId":3,              "plotColor":ROOT.kGray+2, "lineWidth":1})
        MVAList.append({"Name":"POG_eleId80x_tight",  "Type":"POG_Id", "ValElePOGId":4,              "plotColor":ROOT.kBlack,  "lineWidth":1})
        MVAList.append({"Name":"DeepLeptonSummer18",  "Type":"DL_Id",  "Var":"prob_lep_isPromptId",  "plotColor":ROOT.kRed,    "lineWidth":2})
        
    if samples["leptonType"]=="Muo":
        sampleMuo=samples["sample"]
        leptonFlavourList.append({"Name":"Muon", "ShortName":"muo", "pdgId":13, "sample":sampleMuo})
        MVAList.append({"Name":"POG_muoId_loose",     "Type":"POG_Id", "Var":"lep_pfMuonId",        "plotColor":ROOT.kGray,   "lineWidth":1})
        MVAList.append({"Name":"POG_muoId_loose_ip",  "Type":"POG_Id", "Var":"lep_pfMuonId",        "plotColor":ROOT.kGray+1, "lineWidth":1})
        MVAList.append({"Name":"POG_muoId_medium",    "Type":"POG_Id", "Var":"lep_mediumMuonId",    "plotColor":ROOT.kGray+2, "lineWidth":1})
        MVAList.append({"Name":"POG_muoId_medium_ip", "Type":"POG_Id", "Var":"lep_mediumMuonId",    "plotColor":ROOT.kBlack,  "lineWidth":1})
        MVAList.append({"Name":"DeepLeptonSummer18",  "Type":"MVA_Id", "Var":"prob_lep_isPromptId", "plotColor":ROOT.kRed,    "lineWidth":2})
        
    binnedList=[]
    binnedList.append({"Name":"pt", "VarName":"|pt|", "Var":"lep_pt", "abs":1, "cuts":[0, 250], "bins":50})

    isTrainData=samples["isTrainData"]  #1=true, 0=false
    plotDate=samples["plotDate"]
    logY=0
    
    relIsoCuts=[0.1]

####################################
# loop over samples and draw plots #
####################################

    for leptonFlavour in leptonFlavourList:

        for relIsoCut in relIsoCuts:
        
            for binVar in binnedList:

                colorList=[]
                lineWidthList=[]
                
                #Initialize Mulitgraph
                c=ROOT.TCanvas()
                if logY==1:
                    c.SetLogy()
                mg=ROOT.TMultiGraph()
                g=[]
                ng=0

                for plot in MVAList:
                    
                    colorList.append(plot["plotColor"])
                    lineWidthList.append(plot["lineWidth"])

                    # reader class
                    readerData=[[] for i in xrange(binVar["bins"])]
                    reader = leptonFlavour["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
                    reader.start()
                    while reader.run():
                        if abs(reader.event.lep_pdgId)==leptonFlavour["pdgId"]:
                            cut_val = getattr(reader.event, binVar["Var"]) 
                            if cut_val >= binVar["cuts"][0] and cut_val <  binVar["cuts"][1]:
                                
                                j=int(math.ceil(cut_val/(binVar["cuts"][1]-binVar["cuts"][0])*binVar["bins"]))-1


                                #check if lepton passes relIso and Impact Parameter cuts
                                passIsoId = passIso(relIsoCut, reader.event.lep_relIso03)
                                passIPId  = passIP(reader.event.lep_pdgId, reader.event.lep_etaSc, reader.event.lep_dxy, reader.event.lep_dz)

                                if passIsoId:
                                
                                    #Electron WPs (incl Iso cut and IP cuts)
                                    if plot["Type"]=="POG_Id" and samples["leptonType"]=="Ele":
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
                                        readerData[j].append([reader.event.lep_isPromptId, 1 if (elePOGId>=plot["ValElePOGId"] and passIPId) else 0])
                                    #Muon WP (incl Iso cut and IP cuts)
                                    if plot["Type"]=="POG_Id" and samples["leptonType"]=="Muo":
                                        readerData[j].append([reader.event.lep_isPromptId, 1 if (getattr(reader.event, plot["Var"])==1 and passIPId) else 0])
                                    #Lepton MVAs (nonIso)
                                    if plot["Type"]=="MVA_Id":
                                        readerData[j].append([reader.event.lep_isPromptId, getattr(reader.event, plot["Var"])])
                                    #DeepLepton
                                    if plot["Type"]=="DL_Id":
                                        readerData[j].append([reader.event.lep_isPromptId, getattr(reader.event, plot["Var"])])

                    #Draw eS plots
                    j=0
                    x    = array('d')
                    y_eS = array('d')
                    y_eB = array('d')
                    for dataset in readerData:
                        #print j+1, len(dataset)
                        j += 1
                        prange=[1] if plot["Type"]=="POG_Id" else [pval*0.001 for pval in range(500,1000)]
                        for pval in prange:
                            xval=eB(pval,dataset)
                            p=pval 
                            #print pval, xval
                            if xval<=0.01:
                                break
                        if not len(dataset)==0:
                            x.append(j*5)
                            y_eS.append(eS(p,dataset))
                            y_eB.append(xval)

                    #Draw Graphs
                    n=len(x)
                    g.append(ROOT.TGraph(n,x,y_eS))
                    gname=("eS "+plot["Name"]+" relIsoCut="+str(relIsoCut) if plot["Type"]=="POG_Id" else "eS "+plot["Name"]+" (eB<=0.01)"+" relIsoCut="+str(relIsoCut))
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

                    #Draw eB plots
                    #Draw Graphs
                    n=len(x)
                    graph=ROOT.TGraph(n,x,y_eB)
                    gname=("eB "+plot["Name"]+" relIsoCut="+str(relIsoCut) if plot["Type"]=="POG_Id" else "eB "+plot["Name"]+" (for plotted eS)"+" relIsoCut="+str(relIsoCut))
                    graph.SetName(gname)
                    graph.SetTitle(gname)
                    graph.SetLineStyle( 2 )
                    graph.SetLineColor(colorList[ng])
                    graph.SetLineWidth(lineWidthList[ng])
                    graph.SetMarkerColor(colorList[ng])
                    #graph.SetMarkerStyle( 5 )
                    graph.SetFillStyle( 0 )
                    graph.SetFillColor( 0 )
                    graph.SetMarkerSize( 0 )
                    graph.Draw("C")
                    #nmaxtext.DrawLatex(x[nmax],y[nmax],"mvaId=%1.2f" %p[nmax])
                    mg.Add(graph)

                    ng += 1

                #Draw Multigraph
                mg.Draw("AC")
                #mg.SetTitle(leptonFlavour["sample"].texName+(" - TrainData" if isTrainData else " - TestData"))
                mg.GetXaxis().SetTitle('pt')
                mg.GetYaxis().SetTitle('eS,eB')
                if logY==0:
                    mg.GetYaxis().SetRangeUser(0.0,1.02)
                c.BuildLegend(0.55,0.15,0.9,0.4)
                drawObjects(isTrainData, samples["leptonType"], 'TTJets+QCD', 'pt0to250', relIsoCut )
                drawObjectsSmall(isTrainData, samples["leptonType"], 'TTJets+QCD', 'pt0to250', relIsoCut ) 
                directory=(os.path.join(plot_directory, leptonFlavour["Name"], plotDate))
                if not os.path.exists(directory):
                    os.makedirs(directory)
                c.Print(os.path.join(directory,("TrainData" if isTrainData else "TestData")+ '_roc_binned_'+binVar["Name"]+" relIsoCut="+str(relIsoCut)+'.png'))
