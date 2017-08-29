# Standard imports
import os
import time
import itertools
import argparse

import TopEFT.tools.logger as logger

argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',    action='store',         nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )

args = argParser.parse_args()

logger = logger.get_logger(args.logLevel, logFile = None)

#nonZeroCouplings = ("RC3phiq", "RCtW")
#nonZeroCouplings = ("IC3phiq", "ICtW")

nonZeroCouplings = ("DC1V","DC1A","DC2V","DC2A")
model_name = "ewkDM"
nDim = len(nonZeroCouplings)

n = 2

def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in xrange(0, len(l), n)]

## this is how it should be done for 2D. However, becomes too expensive quite fast
#couplingPairs = []
#for a in itertools.permutations(cuW, len(cuB)):
#    tmp = zip(a,cuB)
#    for t in tmp:
#        if t not in couplingPairs: couplingPairs.append(t)#(round(t[0],2),round(t[1],2)))


# define lists of coupling values
couplingValues = [ [round(i*1.0/n,2)]*nDim for i in range(-n,n+1) ]
couplingValues = [ item for sublist in couplingValues for item in sublist ]

# walk through all permutations, check for uniqueness 
couplingGrid = []
for cV in itertools.permutations(couplingValues,nDim):
    if cV not in couplingGrid:
        couplingGrid.append(cV)

# zip with coupling names
allCombinations =  [ zip(nonZeroCouplings, a) for a in couplingGrid ]
allCombinationsFlat = []
for comb in allCombinations:
    allCombinationsFlat.append([item for sublist in comb for item in sublist])


#processes = ['ttZ','ttW','ttH']
processes = ['ttZ']
#submitCMD = "submitBatch.py"
submitCMD = "echo"

nJobs = len(processes)*len(allCombinationsFlat)

logger.info("Will need to run over %i combinations.",nJobs)

combinationChunks = chunks(allCombinationsFlat, 650)

for p in processes:
    for i,comb in enumerate(combinationChunks):
        with open("%s_%i.txt"%(p,i), 'w') as f:
            for c in comb:
                strBase = "{} {} "*nDim
                couplingStr = (strBase+'\n').format(*c)
                f.write(couplingStr)
                
        os.system(submitCMD+" --title DM_%s_%i 'python calcXSecModified.py --model "%(p,i)+model_name+" --process "+p+" --couplings %s_%i.txt'"%(p,i))
        #allCombinationsFlat[150:300]:
        #strBase = "{} {} "*nDim
        #couplingStr = strBase.format(*comb)
        ##couplingStr = "%s %s %s %s"%(nonZeroCouplings[0], c[0], nonZeroCouplings[1], c[1])
        #logger.info("Going to calculate x-sec for process %s in model %s with the following couplings:",p,model_name)
        #logger.info(couplingStr)
        #os.system(submitCMD+" 'python calcXSec.py --model "+model_name+" --process "+p+" --couplings "+couplingStr+"'")
        #if not "echo" in submitCMD:
        #    time.sleep(30) # need to distribute load, shouldn't start with 40 jobs at a time

