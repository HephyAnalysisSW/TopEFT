# Standard imports
import ROOT
import os
import sys
import importlib
import random
import numpy as np
from array import array

# RootTools
from RootTools.core.Sample import *

# TopEFT
from TopEFT.Tools.user import skim_output_directory as input_directory
from TopEFT.Tools.user import trainingFiles_directory as output_directory
#from TopEFT.postprocessing.deepLeptonSamplesForTraining import deepLeptonSignalSamples, deepLeptonBackgroundSamples

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
    argParser.add_argument('--ptSelection',     action='store', type=str, choices=['pt_10_to_inf', 'pt_15_to_inf'],         required = True, help="Which pt selection?")
    argParser.add_argument('--sampleSelection', action='store', type=str, choices=['SlDlTTJetsVsQCD', 'DYVsQCD'],      required = True, help="Which sample selection?")
    argParser.add_argument('--trainingType',    action='store', type=str, choices=['std','iso'],            required = True, help="Standard or Isolation Training?")
    argParser.add_argument('--sampleSize',      action='store', type=str, choices=['small','medium','large','full'],         required = True, help="small sample or full sample?")

    return argParser

#some helper functions
def printData(data):
    for row in data:
        print row

def getKey(item):
    return float(item[2])

def varList(pfCandId):

    #define related variables of PF candidates
    pfCandVarList = [
    #'pfCand_'+pfCandId+'_pdgId',
    #'pfCand_'+pfCandId+'_pt',
    #'pfCand_'+pfCandId+'_eta',
    #'pfCand_'+pfCandId+'_phi',
    #'pfCand_'+pfCandId+'_mass',
    #'pfCand_'+pfCandId+'_puppiWeight',
    #'pfCand_'+pfCandId+'_hcalFraction',
    #'pfCand_'+pfCandId+'_fromPV',
    #'pfCand_'+pfCandId+'_dxy_pf',
    #'pfCand_'+pfCandId+'_dz_pf',
    #'pfCand_'+pfCandId+'_dzAssociatedPV',
    #'pfCand_'+pfCandId+'_deltaR',
    'pfCand_'+pfCandId+'_ptRel',
                    ]

    return pfCandVarList

#define PF candidates for loop
pfCandIdList = [
                #'neutral',
                'charged',
                #'photon',
                #'electron',
                #'muon',
               ]

#define paths
inputPath  = '/afs/hephy.at/data/gmoertl01/lepton/trainfiles/v1_small/2016/ele/pt_10_to_inf/DYVsQCD'
outputPath = '/afs/hephy.at/data/gmoertl01/lepton/trainfiles/v1_small/2016/ele/pt_10_to_inf/DYVsQCD/ptRelSorted/'

#get file list
#inputPath = os.path.join(inputPath, options.version, options.flavour, options.ptSelection, options.sampleSelection)
inputFileList = os.listdir(inputPath)
for inputFile in inputFileList:
    if not '.root' in inputFile:
        inputFileList.remove(inputFile) 

print inputFileList

#Loop over input files
for inputFile in inputFileList:
    iFile     = ROOT.TFile.Open(os.path.join(inputPath,inputFile), 'read')
    iFileTree = iFile.Get('tree')
    nEntries  = iFileTree.GetEntries()

    #clone tree
    oFile     = ROOT.TFile.Open(os.path.join(outputPath,inputFile), 'recreate')
    oFileTree = iFileTree.CloneTree(0)


    #Loop over PF candidate ID
    for pfCandId in pfCandIdList:
        pfCandVarList = varList(pfCandId)
        npfCand = 'npfCand_'+pfCandId

        #add branches
        for pfCandVar in pfCandVarList:
            name = pfCandVar+'_ptRelSorted'
            values = array('f', np.tile(0.0, 100))
            varName = 'values[npfCand_charged]/F'
            oFileTree.Branch(name , values, varName )
            

        #loop over all entries
        for i in xrange(2):
            iFileTree.GetEntry(i)

            #check if number of leaves matches number of PF candidates
            leaf = oFileTree.GetLeaf('pfCand_'+pfCandId+'_ptRel')
            npf  = oFileTree.GetLeaf(npfCand).GetValue()
            if leaf.GetLen() != npf:
                print 'Wrong number of PF candidates!'

            #collect ptRel values + indices (entry, leaf, ptRel)
            leafData = []
            for j in xrange(leaf.GetLen()):
                leafData.append([i, j, leaf.GetValue(j)])
           
            #reorder leaf indices by ptRel, entry indices remain the same
            leafData=sorted(leafData, key=getKey, reverse=True)

            #fill pTRel sorted values in branches
            k=0
            for instance in leafData:
                values[k]=instance[2]
                k +=1
            print values

            iFileTree.CopyAddresses(oFileTree)
            oFileTree.Fill() 


    #save and close files
    iFile.Close()
    oFile.Write()
    oFile.Close()



