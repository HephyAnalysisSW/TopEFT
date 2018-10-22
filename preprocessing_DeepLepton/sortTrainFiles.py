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

    argParser.add_argument('--version',         action='store', type=str, choices=['v1','v1_small'],                required = True, help="Version for output directory")
    argParser.add_argument('--year',            action='store', type=int, choices=[2016,2017],                      required = True, help="Which year?")
    argParser.add_argument('--flavour',         action='store', type=str, choices=['ele','muo'],                    required = True, help="Which Flavour?")
    argParser.add_argument('--ptSelection',     action='store', type=str, choices=['pt_10_to_inf', 'pt_15_to_inf', 'noPtSelection'], required = True, help="Which pt selection?")
    argParser.add_argument('--sampleSelection', action='store', type=str, choices=['SlDlTTJetsVsQCD', 'DYVsQCD', 'TestSample'],   required = True, help="Which sample selection?")

    argParser.add_argument('--nJobs',           action='store', nargs='?', type=int, default=1, help="Maximum number of simultaneous jobs.")
    argParser.add_argument('--job',             action='store',            type=int, default=0, help="Run only job i")

    return argParser

options = get_parser().parse_args()

#some helper functions
def printData(data):
    for row in data:
        print row

def getKey(item):
    return float(item[2])

def varList(pfCandId):

    #define related variables of PF candidates
    pfCandVarList = [
    'pfCand_'+pfCandId+'_pdgId',
    'pfCand_'+pfCandId+'_pt',
    'pfCand_'+pfCandId+'_eta',
    'pfCand_'+pfCandId+'_phi',
    'pfCand_'+pfCandId+'_mass',
    'pfCand_'+pfCandId+'_puppiWeight',
    'pfCand_'+pfCandId+'_hcalFraction',
    'pfCand_'+pfCandId+'_fromPV',
    'pfCand_'+pfCandId+'_dxy_pf',
    'pfCand_'+pfCandId+'_dz_pf',
    'pfCand_'+pfCandId+'_dzAssociatedPV',
    'pfCand_'+pfCandId+'_deltaR',
    'pfCand_'+pfCandId+'_ptRel',
                    ]

    return pfCandVarList

#define PF candidates for loop
pfCandIdList = [
                'neutral',
                'charged',
                'photon',
                'electron',
                'muon',
               ]

#define paths
TrainFilePath = '/afs/hephy.at/data/gmoertl01/DeepLepton/trainfiles'
inputPath     = os.path.join(TrainFilePath, options.version, str(options.year), options.flavour, options.ptSelection, options.sampleSelection)
outputPath    = os.path.join(TrainFilePath, options.version, str(options.year), options.flavour, options.ptSelection, options.sampleSelection+'_ptRelSorted')

if not os.path.exists( outputPath ):
    os.makedirs( outputPath )

#get file list
inputFileList  = os.listdir(inputPath)
removeFileList = []
for inputFile in inputFileList:
    if '.root' not in inputFile:
        removeFileList.append(inputFile)
for inputFile in removeFileList:
    inputFileList.remove(inputFile)

print inputFileList
print 'total files: ', len(inputFileList)

nJobFiles = int(len(inputFileList)/options.nJobs)
jobFileList = []

for i in xrange(nJobFiles):
    jobFileList.append(inputFileList[options.job*nJobFiles+i])

inputFileList = jobFileList

print 'selected files in this job: ', inputFileList

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

        #add branches
        for pfCandVar in pfCandVarList:
            name = pfCandVar+'_ptRelSorted'
            varName = name+'[npfCand_'+pfCandId+']/F'
            vars()[name] = array('f', np.tile(0.0, 100)) #important: maximum length of pf cands per pf cand flavour per lepton
            oFileTree.Branch(name , vars()[name], varName )
            

    #loop over all entries
    #for i in xrange(5):
    for i in xrange(nEntries):
        iFileTree.GetEntry(i)

        for pfCandId in pfCandIdList:
            pfCandVarList = varList(pfCandId)
            npfCand = 'npfCand_'+pfCandId

            #check if number of leaves matches number of PF candidates
            ptRel = oFileTree.GetLeaf('pfCand_'+pfCandId+'_ptRel')
            npf   = oFileTree.GetLeaf(npfCand).GetValue()
            if ptRel.GetLen() != npf:
                print 'Wrong number of PF candidates!'

            #collect ptRel  + indices (entry, leaf, ptRel)
            ptRelData = []
            for j in xrange(ptRel.GetLen()):
                ptRelData.append([i, j, ptRel.GetValue(j)])
           
            #reorder leaf indices by ptRel, entry indices remain the same
            ptRelData=sorted(ptRelData, key=getKey, reverse=True)


            for pfCandVar in pfCandVarList:
                name = pfCandVar+'_ptRelSorted'
                pfVar = oFileTree.GetLeaf(pfCandVar)

                #fill pTRel sorted vars()[name] in branches
                k=0
                for instance in ptRelData:
                    vars()[name][k]=pfVar.GetValue(instance[1])
                    k +=1
                #print vars()[name]

        iFileTree.CopyAddresses(oFileTree)
        oFileTree.Fill() 

    print '%i of %i Entries processed for %s' %(i+1, nEntries, inputFile)

    #save and close files
    iFile.Close()
    oFile.Write(os.path.join(outputPath,inputFile),oFile.kOverwrite)
    oFile.Close()



