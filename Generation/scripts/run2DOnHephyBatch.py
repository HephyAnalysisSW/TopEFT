#!/usr/bin/env python

# Standard imports
import os
import time
import itertools
import argparse

import TopEFT.Tools.logger as logger

argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',    action='store',         nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )

args = argParser.parse_args()

logger = logger.get_logger(args.logLevel, logFile = None)

def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in xrange(0, len(l), n)]

#model_name = "ewkDMGZ"

# for 4D scans
#nonZeroCouplings = ("DC1V","DC1A","DC2V","DC2A")
#dc1v = [ i*1.3/4 for i in range(-4,3) ]
#dc1a = [ i*1.3/4 for i in range(-2,5) ]
#dc2v = [ i*0.30/6 for i in range(-5,7) ]
#dc2a = [ i*0.30/6 for i in range(-5,7) ]
#couplingValues = [dc1v,dc1a,dc2v,dc2a]

#dc1v = [ i*1./2 for i in range(-2,3) ]
#couplingValues = [ dc1v, dc1v, dc1v, dc1v ]

# for 2D scans
#nonZeroCouplings = ("DC2V","DC2A")
#nonZeroCouplings = ("DVG","DAG")

## HEL
#model_name = "HEL_UFO"
#nonZeroCouplings = ("cuW", "cuB")
#dc2v = [ i*0.05/5 for i in range(-5,6) ]
#dc2a = [ i*0.15/5 for i in range(-5,6) ]
#couplingValues = [dc2v,dc2a]

## dim6top_LO
model_name = "dim6top_LO"
nonZeroCouplings = ("ctZ", "ctZI")
dc2v = [ i*2./5 for i in range(-5,6) ]
dc2a = [ i*2./5 for i in range(-5,6) ]
couplingValues = [dc2v,dc2a]


nDim = len(nonZeroCouplings)
# prepare the grid with all points
couplingGrid = [ a for a in itertools.product(*couplingValues) ]

# zip with coupling names
allCombinations =  [ zip(nonZeroCouplings, a) for a in couplingGrid ]
allCombinationsFlat = []
for comb in allCombinations:
    allCombinationsFlat.append([item for sublist in comb for item in sublist])


#processes = ['tZq_4f', 'ttZ','ttW','ttH']
#processes = ['ttgamma', 'ttZ']
processes = ['ttZ_ll']
submitCMD = "submitBatch.py"
#submitCMD = "echo"

nJobs = len(processes[:1])*len(allCombinationsFlat)

logger.info("Will need to run over %i combinations.",nJobs)

combinationChunks = chunks(allCombinationsFlat, 10)

for p in processes[:1]:
    for i,comb in enumerate(combinationChunks):
        with open("%s_%i.txt"%(p,i), 'w') as f:
            for c in comb:
                strBase = "{} {} "*nDim
                couplingStr = (strBase+'\n').format(*c)
                f.write(couplingStr)
        #if i == 2 or i == 8: continue
        os.system(submitCMD+" --title %s_%i 'python run.py --model "%(p,i)+model_name+" --process "+p+" --couplings %s_%i.txt --calcXSec --makeGridpack'"%(p,i))
        if "echo" not in submitCMD:
            time.sleep(30)
