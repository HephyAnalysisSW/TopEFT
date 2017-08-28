# Standard imports
import os
import time
import itertools

# Logger
import logging
logger = logging.getLogger(__name__)

#nonZeroCouplings = ("RC3phiq", "RCtW")
#nonZeroCouplings = ("IC3phiq", "ICtW")

nonZeroCouplings = ("DC1V","DC1A","DC2V","DC2A")

nDim = len(nonZeroCouplings)

n = 2

# values
couplingValues = [ round(i*1.0/n,2) for i in range(-n,n+1) ]
diag = [couplingValues]*nDim

## this is how it should be done for 2D. However, becomes too expensive quite fast
#couplingPairs = []
#for a in itertools.permutations(cuW, len(cuB)):
#    tmp = zip(a,cuB)
#    for t in tmp:
#        if t not in couplingPairs: couplingPairs.append(t)#(round(t[0],2),round(t[1],2)))

# this is the workaround
couplingGrid = [a for a in itertools.permutations(couplingValues,nDim)] + zip(*diag)

allCombinations =  [ zip(nonZeroCouplings, a) for a in couplingGrid ]
allCombinationsFlat = []
for comb in allCombinations:
    allCombinationsFlat.append([item for sublist in comb for item in sublist])

#processes = ['ttZ','ttW','ttH']
processes = ['ttZ']
#submitCMD = "submitBatch.py --title='DMmultDim'"
submitCMD = "echo"

for p in processes:
    for comb in allCombinationsFlat:
        strBase = "{} {} "*nDim
        couplingStr = strBase.format(*comb)
        #couplingStr = "%s %s %s %s"%(nonZeroCouplings[0], c[0], nonZeroCouplings[1], c[1])
        os.system(submitCMD+" 'python calcXSec.py --model ewkDM --overwrite --process "+p+" --couplings "+couplingStr+"'")
        if not "echo" in submitCMD:
            time.sleep(60) # need to distribute load, shouldn't start with 40 jobs at a time

