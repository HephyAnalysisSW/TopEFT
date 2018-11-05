# Standard imports
import ROOT
import os

import numpy

#nJobs = 60
#
#for i in len(nJobs):
#    
#    prefix='modulo_'+str(i)+'_trainfile_'
#    n=15
#
#    #ascending order
#    #for i in xrange(1,n+1):
#    #    print prefix+str(i)+".root"
#
#    #random order of files
#    fileNo=numpy.arange(n)
#    numpy.random.shuffle(fileNo)
#
#    for j in fileNo:
#        print prefix+str(j+1)+".root"

#leptonFlavour  = ['ele', 'muo']
leptonFlavour   = ['muo']
#sampleSelection = 'TTJets_sorted'
sampleSelection = 'DYvsQCD_sorted'
ptSelection     = 'pt_15_to_inf' #'pt_10_to_inf'
ratioTrain      = 80
ratioTest       = 20

for flavour in leptonFlavour:

    filepath = os.path.join('/afs/hephy.at/data/gmoertl01/DeepLepton/trainfiles/v3/2016',flavour,ptSelection,sampleSelection)
    filelist = os.listdir(filepath)
    #print filepath
    #print filelist
    numpy.random.shuffle(filelist)

    trainfilelist = []
    testfilelist  = []

    for i in xrange(len(filelist)):
        if i <= len(filelist)*ratioTrain/(ratioTrain+ratioTest):
            trainfilelist.append(filelist[i])
        else:
            testfilelist.append(filelist[i])

    with open(filepath+'/train_'+flavour+'_std.txt', 'w') as f:
        for trainfile in trainfilelist:
            #print trainfile
            f.write("%s\n" % trainfile)

    with open(filepath+'/test_'+flavour+'_std.txt', 'w') as f:
        for testfile in testfilelist:
            #print trainfile
            f.write("%s\n" % testfile)


