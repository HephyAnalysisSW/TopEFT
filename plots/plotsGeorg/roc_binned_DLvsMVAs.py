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

#rser
def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--version',         action='store', type=str, choices=['v1'],                   required = True, help="Version for output directory")
    argParser.add_argument('--year',            action='store', type=int, choices=[2016,2017],              required = True, help="Which year?")
    argParser.add_argument('--flavour',         action='store', type=str, choices=['ele','muo'],            required = True, help="Which Flavour?")
    argParser.add_argument('--trainingDate',    action='store', type=int, default=0,                                         help="Which Training Date? 0 for no Training Date.")
    argParser.add_argument('--isTestData',      action='store', type=int, choices=[0,1],                    required = True, help="Which Training Date? 0 for no Training Date.")
    argParser.add_argument('--ptSelection',     action='store', type=str, choices=['pt_10_to_inf'],         required = True, help="Which pt selection?")
    argParser.add_argument('--sampleSelection', action='store', type=str, choices=['SlDlTTJetsVsQCD'],      required = True, help="Which sample selection?")
    argParser.add_argument('--trainingType',    action='store', type=str, choices=['std','iso'],            required = True, help="Standard or Isolation Training?")
    argParser.add_argument('--sampleSize',      action='store', type=str, choices=['small','full'],         required = True, help="small sample or full sample?")

    #argParser.add_argument('--nJobs',        action='store', type=int,    nargs='?',         default=1,                   help="Maximum number of simultaneous jobs.")
    #argParser.add_argument('--job',          action='store', type=int,                       default=0,                   help="Run only job i")

    return argParser

options = get_parser().parse_args()

##############################
# load samples and variables #
##############################

#define samples for electorns and muons
samples=plot_samples_v2(options.version, options.year, options.flavour, options.trainingDate, options.isTestData, options.ptSelection, options.sampleSelection, options.sampleSize)

# variables to read
variables=roc_plot_variables()

#########################
# define plot structure #
#########################

isTestData=options.isTestData  #1=true, 0=false

leptonFlavourList=[]
leptonFlavourList.append({"Name":"Electron" if options.flavour=='ele' else "Muon", "Flavour":options.flavour, "pdgId":11 if options.flavour=='ele' else 13, "sample":samples["sample"]})

MVAList=[]
MVAList.append({"Name":"LeptonMVA_TTV",  "Type":"MVA_Id",  "Var":"lep_mvaTTV",           "plotColor":ROOT.kGray,       "lineWidth":2})
MVAList.append({"Name":"LeptonMVA_TTH",  "Type":"MVA_Id",  "Var":"lep_mvaTTH",           "plotColor":ROOT.kGray,       "lineWidth":2})
MVAList.append({"Name":"DeepLepton",     "Type":"DL_Id",   "Var":"prob_lep_isPromptId",  "plotColor":ROOT.kGreen+2,    "lineWidth":2})
    
binnedList=[]
binnedList.append({"Name":"pt", "VarName":"|pt|", "Var":"lep_pt", "abs":1, "cuts":[0, 250], "bins":50})

logY=0

relIsoCuts=[1.0]

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
                            
                                #Lepton MVAs
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
            drawObjects(isTestData, options.flavour, options.sampleSelection, 'pt10to250', relIsoCut )
            #drawObjectsSmall(isTestData, options.flavour, 'SLDL_TTJets+QCD', 'pt10to250', relIsoCut ) 
            directory=(os.path.join(
                                    plot_directory,
                                    str(options.year), 
                                    options.flavour, 
                                    options.sampleSelection, 
                                    str(options.trainingDate), 
                                    'TestData' if isTestData else 'TrainData'
                                   ))
            if not os.path.exists(directory):
                os.makedirs(directory)
            c.Print(os.path.join(directory, 'roc_binned_'+binVar["Name"]+" relIsoCut="+str(relIsoCut)+'.png'))
