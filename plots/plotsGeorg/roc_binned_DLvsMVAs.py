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

#parser
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
    argParser.add_argument('--sampleSize',      action='store', type=str, choices=['small','medium','full'],         required = True, help="small sample or full sample?")
    argParser.add_argument('--binned',          action='store', type=str, choices=['pt','eta','nTrueInt'],         required = True, help="Which variable for binning?")

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
MVAList.append({"Name":"LeptonMVA_TTH",  "Type":"MVA_Id",  "Var":"lep_mvaTTH",           "plotColor":ROOT.kGray+1,     "lineWidth":2})
MVAList.append({"Name":"DeepLepton",     "Type":"DL_Id",   "Var":"prob_lep_isPromptId",  "plotColor":ROOT.kGreen+2,    "lineWidth":2})

binnedList={}
binnedList.update({"pt":       {"VarName":"|pt|",                                           "Var":"lep_pt",                                             "abs":1, "cuts":[0, 250],      "bins":50, "binsEB":5 }})
binnedList.update({"eta":      {"VarName":"|etaSc|" if options.flavour=='ele' else "|eta|", "Var":"lep_etaSc" if options.flavour=='ele' else "lep_eta", "abs":1, "cuts":[0, 2.5],      "bins":50, "binsEB":5 }})
binnedList.update({"nTrueInt": {"VarName":"nTrueInt",                                       "Var":"nTrueInt",                                           "abs":0, "cuts":[0, 55],       "bins":55, "binsEB":5 }})

logY=0

relIsoCuts=[1.0]

ptCuts=[]
if options.binned=='pt':
    ptCuts.append({"Name":"pt10to250","lower_limit":10, "upper_limit":250         })
else:
    ptCuts.append({"Name":"pt25toInf","lower_limit":25, "upper_limit":float("Inf")})
    ptCuts.append({"Name":"pt10to25", "lower_limit":10, "upper_limit":25          })

####################################
# loop over samples and draw plots #
####################################

for leptonFlavour in leptonFlavourList:

    for relIsoCut in relIsoCuts:

        for ptCut in ptCuts:    

            colorList=[]
            lineWidthList=[]
            
            #Initialize Mulitgraph
            c=ROOT.TCanvas()
            if logY==1:
                c.SetLogy()
            mg=ROOT.TMultiGraph()
            g=[]
            ng=0
            binWidth = (binnedList[options.binned]["cuts"][1]-binnedList[options.binned]["cuts"][0])/binnedList[options.binned]["bins"]

            for plot in MVAList:
                
                colorList.append(plot["plotColor"])
                lineWidthList.append(plot["lineWidth"])

                # reader class
                readerData=[[] for i in xrange(binnedList[options.binned]["bins"])]
                reader = leptonFlavour["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
                reader.start()
                while reader.run():
                    if abs(reader.event.lep_pdgId)==leptonFlavour["pdgId"] and reader.event.lep_pt>=ptCut["lower_limit"] and reader.event.lep_pt<=ptCut["upper_limit"]:
                        cut_val = abs(getattr(reader.event, binnedList[options.binned]["Var"])) 
                        if cut_val >= binnedList[options.binned]["cuts"][0] and cut_val <  binnedList[options.binned]["cuts"][1]:
                            
                            j=int(math.ceil(cut_val/(binnedList[options.binned]["cuts"][1]-binnedList[options.binned]["cuts"][0])*binnedList[options.binned]["bins"]))-1


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

                #calculate cut value for eB<=0.01 on average for e.g. n=2 data bins 
                for i in xrange(int(binnedList[options.binned]["bins"]/binnedList[options.binned]["binsEB"])):
                    binReaderData = [readerData[k] for k in xrange(i*binnedList[options.binned]["binsEB"],(i+1)*binnedList[options.binned]["binsEB"])]
                    eBreaderData  = []
                    for dataset in binReaderData:
                        for datapoint in dataset:
                            eBreaderData.append(datapoint) 

                    prange = [pval*0.0001 for pval in xrange(8500 if plot['Type']=='DL_Id' else 5000,10000)]
                    eBValMin=1.1
                    for pval in prange:
                        eBVal=eB(pval,eBreaderData)
                        if eBVal<eBValMin:
                            eBValMin=eBVal
                            cutVal=pval 
                        #print pval, xval
                        if eBValMin<=0.01 and not eBValMin==0.:
                            break
                    print cutVal, eBValMin
                    for dataset in binReaderData:
                        j += 1
                        if not len(dataset)==0:
                            x.append(j*binWidth)
                            y_eS.append(eS(cutVal,dataset))
                            y_eB.append(eB(cutVal,dataset)*10)
                            print j*binWidth, cutVal, y_eB[-1], y_eS[-1]

                #old bin-wise calculation of cut value
                #for dataset in readerData:
                #    #print j+1, len(dataset)
                #    j += 1
                #    prange=[1] if plot["Type"]=="POG_Id" else [pval*0.0001 for pval in range(9000,10000)]
                #    for pval in prange:
                #        xval=eB(pval,dataset)
                #        p=pval 
                #        #print pval, xval
                #        if xval<=0.01:
                #            break
                #    if not len(dataset)==0:
                #        x.append(j*5)
                #        y_eS.append(eS(p,dataset))
                #        y_eB.append(xval)
                #        print j*5, p, xval, y_eS[-1]

                #Draw Graphs
                n=len(x)
                g.append(ROOT.TGraph(n,x,y_eS))
                gname=("eS "+plot["Name"]+" (eB<=0.01)")
                g[ng].SetName(gname)
                g[ng].SetTitle(gname)
                g[ng].SetLineColor( 0 )
                #g[ng].SetLineWidth(lineWidthList[ng])
                g[ng].SetMarkerColor(colorList[ng])
                g[ng].SetMarkerStyle( 9 ) #
                g[ng].SetFillStyle(0)
                g[ng].SetFillColor(0)
                #g[ng].SetMarkerSize(0)
                g[ng].SetMarkerSize(0.5)
                #g[ng].Draw("C")
                g[ng].Draw("P")
                #nmaxtext.DrawLatex(x[nmax],y[nmax],"mvaId=%1.2f" %p[nmax])
                mg.Add(g[ng])

                #Draw eB plots
                #Draw Graphs
                n=len(x)
                graph=ROOT.TGraph(n,x,y_eB)
                gname=("eB x 10 "+plot["Name"]+" (for plotted eS)")
                graph.SetName(gname)
                graph.SetTitle(gname)
                #graph.SetLineStyle( 2 )
                graph.SetLineColor( 0 )
                #graph.SetLineWidth(lineWidthList[ng])
                graph.SetMarkerColor(colorList[ng])
                graph.SetMarkerStyle( 4 )
                graph.SetFillStyle( 0 )
                graph.SetFillColor( 0 )
                graph.SetMarkerSize( 0.5 )
                graph.Draw("P")
                #nmaxtext.DrawLatex(x[nmax],y[nmax],"mvaId=%1.2f" %p[nmax])
                mg.Add(graph)

                ng += 1

            #Draw Multigraph
            mg.Draw("AP")
            #mg.SetTitle(leptonFlavour["sample"].texName+(" - TrainData" if isTrainData else " - TestData"))
            mg.GetXaxis().SetTitle(binnedList[options.binned]["VarName"])
            mg.GetYaxis().SetTitle('eS,eB')
            if logY==0:
                mg.GetYaxis().SetRangeUser(0.0,1.02)
            if options.binned=='eta':
                if ptCut['Name']=="pt25toInf":
                    ya = 0.25
                else:
                    ya = 0.45
            else:
                ya = 0.35
            yb = ya + 0.25
            c.BuildLegend(0.55,ya,0.9,yb)
            drawObjects(isTestData, options.flavour, options.sampleSelection, ptCut['Name'], relIsoCut )
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
            c.Print(os.path.join(directory, 'roc_binned_'+options.binned+"_relIsoCut="+str(relIsoCut)+'_'+ptCut['Name']+'.png'))
