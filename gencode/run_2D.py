from TopEFT.gencode.EFT import *
import itertools
import os,time

nonZeroCouplings = ("RC3phiq", "RCtW")
nonZeroCouplings = ("IC3phiq", "ICtW")

n = 5

# cuW
cuW = [ i*0.1/n for i in range(-n,n+1) ]
cuB = [ i*10.0/n for i in range(-n,n+1) ]

## this is how it should be done. However, becomes too expensive quite fast
#couplingPairs = []
#for a in itertools.permutations(cuW, len(cuB)):
#    tmp = zip(a,cuB)
#    for t in tmp:
#        if t not in couplingPairs: couplingPairs.append(t)#(round(t[0],2),round(t[1],2)))

# this is the workaround
couplingPairs = [a for a in itertools.permutations(cuB,2)] + zip(cuB,cuB)
couplingPairs = [(round(a[0],2), round(a[1],2)) for a in couplingPairs]

print len(couplingPairs)

processes = ['ttZ','ttW','ttH']
#processes = ['ttZ']
submitCMD = "submitBatch.py --title='2D' "
#submitCMD = "echo "

for p in processes:
    for c in couplingPairs:
        couplingStr = "%s_%s_%s_%s"%(nonZeroCouplings[0], c[0], nonZeroCouplings[1], c[1])
        os.system(submitCMD+"'python makeTarball.py --model TopEffTh --process "+p+" --noGridpack --couplings="+couplingStr+"_Lambda_1000.'")
        time.sleep(60) # need to distribute load, shouldn't start with 40 jobs at a time

