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
from RootTools.core.Sample import *

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

    #argParser.add_argument('--nJobs',        action='store', type=int,    nargs='?',         default=1,                   help="Maximum number of simultaneous jobs.")
    #argParser.add_argument('--job',          action='store', type=int,                       default=0,                   help="Run only job i")

    return argParser

options = get_parser().parse_args()


###################
# define plotlist #
###################
isTestData = options.isTestData

leptonFlavours = [{'FullName':'Electron' if options.flavour=='ele' else 'Muon', 'Name':options.flavour, 'pdgId': 11 if options.flavour=='ele' else 13, 'TrainDates': [], 'plotTestData': isTestData}]
#Flavour Plots


##previous results
#if options.flavour=='ele':
#    leptonFlavours[0]['TrainDates'].append({'Date': 20180913,         'TrainType': options.trainingType, 'SampleSize': options.sampleSize, 'Plots': [
#                                                                                                         {'Name': 'DeepLepton_excluded_JetBTagCSVs', 'MVAType': 'DL_Id',  'Var': 'prob_lep_isPromptId', 'Color':ROOT.kGreen+1, 'lineWidth': 2},
#                                                                                                         ]})


#acutal results
leptonFlavours[0]['TrainDates'].append({'Date': options.trainingDate, 'TrainType': options.trainingType, 'SampleSize': options.sampleSize, 'Plots': [
                                                                                                     {'Name': 'LeptonMVA_TTV',       'MVAType': 'MVA_Id', 'Var': 'lep_mvaTTV',          'Color':ROOT.kGray,    'lineWidth': 2},
                                                                                                     {'Name': 'LeptonMVA_TTH',       'MVAType': 'MVA_Id', 'Var': 'lep_mvaTTH',          'Color':ROOT.kGray+1,  'lineWidth': 2},
                                                                                                     {'Name': 'DeepLepton',          'MVAType': 'DL_Id',  'Var': 'prob_lep_isPromptId', 'Color':ROOT.kGreen+2, 'lineWidth': 2},
                                                                                                     ]})
##################
# load variables #
##################

# variables to read
variables=roc_plot_variables()

###############
# define cuts #
###############

ptCuts=[]
ptCuts.append({"Name":"pt25toInf","lower_limit":25, "upper_limit":float("Inf")})
ptCuts.append({"Name":"pt10to25","lower_limit":10, "upper_limit":25})

relIsoCuts = [1.0,0.4,0.2,0.1,0.05]

logY=1

####################################
# loop over samples and draw plots #
####################################

#define lists
for leptonFlavour in leptonFlavours:

    colorList     =[]
    lineWidthList =[]
    plotTypeList  =[]

    for trainDate in leptonFlavour['TrainDates']:
        for plot in trainDate['Plots']:

            colorList.append(plot['Color'])
            lineWidthList.append(plot['lineWidth'])
            plotTypeList.append(plot['MVAType'])
        
    readerData    =[]
    plotLegend    =[]

    for i in xrange(len(ptCuts)):

        readerData.append([])
        plotLegend.append([])
            
        for j in xrange(len(relIsoCuts)):
            
            readerData[i].append([])
            plotLegend[i].append([])

            k=0
            for trainDate in leptonFlavour['TrainDates']:
                for plot in trainDate['Plots']:

                    readerData[i][j].append([])
                    plotLegend[i][j].append([])
                    legendString        = plot["Name"]
                    plotLegend[i][j][k] = legendString
                    k += 1

    #reader part
    i = 0
    j = 0
    k = 0
    k_act = 0

    for trainDate in leptonFlavour['TrainDates']:
        #load sample
        samples=plot_samples_v2(options.version, options.year, options.flavour, options.trainingDate, options.isTestData, options.ptSelection, options.sampleSelection, options.sampleSize) 
        #amples=plot_samples_v2(options.version, options.year, options.flavour, trainDate['Date'], options.isTestData, options.ptSelection, options.sampleSelection, options.sampleSize) 
        print samples["sample"]

        # reader class
        reader = samples["sample"].treeReader(  map( TreeVariable.fromString, variables ) )
        # loop
        reader.start()
        
        while reader.run():
            for plot in trainDate['Plots']:
                for ptCut in ptCuts:
                    for relIsoCut in relIsoCuts:

                        if reader.event.lep_pt>=ptCut["lower_limit"] and reader.event.lep_pt<=ptCut["upper_limit"] and reader.event.lep_relIso03 <= relIsoCut:
                            #print i, j, k, reader.event.lep_pt, reader.event.lep_relIso03, reader.event.lep_isPromptId, getattr(reader.event, plot["Variable"])
                            readerData[i][j][k].append([reader.event.lep_isPromptId, getattr(reader.event, plot["Var"])])
                    
                        j += 1
                    i += 1
                    j = 0
                k += 1
                i = 0
            k = k_act
        k_act += len(trainDate['Plots'])

    #plot Graphs
    for i in xrange(len(ptCuts)):
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

                if plotTypeList[ng]=='MVA_Id':
                    prange = [pval*0.01 for pval in xrange(-100,80)]
                    for pval in xrange(801,990):
                        prange.append(pval*0.001)
                    for pval in xrange(9901,10000):
                        prange.append(pval*0.0001)
                else:
                    prange = [pval*0.01 for pval in xrange(0,90)]
                    for pval in xrange(901,990):
                        prange.append(pval*0.001)
                    for pval in xrange(9901,10000):
                        prange.append(pval*0.0001)

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
            #mg.SetTitle(pt_cut["Name"]+" "+samples["sample"].texName+(" - TrainData" if isTestData else " - TestData"))
            mg.GetXaxis().SetTitle('eS')
            mg.GetXaxis().SetLimits(0.597, 1.003)
            mg.GetYaxis().SetTitle('eB' if logY else '1-eB')
            mg.GetYaxis().SetRangeUser(0.0009, 1.01) if logY else mg.GetYaxis().SetLimits(0.0, 1.0)
            c.BuildLegend(0.12,0.7,0.5,0.9) if logY else c.BuildLegend()
            #c.BuildLegend()
            drawObjects(isTestData, options.flavour, options.sampleSelection, ptCuts[i]["Name"], relIsoCuts[j] )
            #drawObjectsSmall(isTestData, samples["leptonFlavour"], 'TTJets+QCD', ptCuts[i]["Name"], relIsoCuts[j] )
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
            c.Print(os.path.join(directory, 'roc_compared_'+ptCuts[i]["Name"]+'_relIso<='+str(relIsoCuts[j])+'.png'))
