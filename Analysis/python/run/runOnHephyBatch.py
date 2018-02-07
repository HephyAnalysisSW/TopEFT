#!/usr/bin/env python
import os
import time

from TopEFT.samples.gen_fwlite_benchmarks import *

dim6_all        = [ x.name for x in allSamples_dim6top ]
dim6_dipoles    = [ x.name for x in dim6top_dipoles ]
dim6_currents   = [ x.name for x in dim6top_currents ]

#ewkDM_all       = [ x.name for x in ewkDM_all ]
ewkDM_dipoles   = [ ewkDM_central ] + ewkDM_dipoles
ewkDM_currents  = [ ewkDM_central ] + ewkDM_currents

#submitCMD = "submitBatch.py --title='Limit2D' "
submitCMD = "echo "

signals = ewkDM_currents

'''
Currents
'''

for i, x in enumerate(ewkDM_currents):
    #print i, x.name
    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal currents --useShape --useXSec --only=%s'"%str(i))
    if submitCMD.startswith("submit"):
        time.sleep(2)

#'''
#Dipoles
#'''
#
#for i, x in enumerate(ewkDM_dipoles):
#    #print i, x.name
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles --useShape --useXSec --only=%s'"%str(i))
#    if submitCMD.startswith("submit"):
#        time.sleep(2)
#

### for resubmission of failed jobs:
#from TopEFT.Analysis.run.getResults import getResult
#for i,s in enumerate(signals):
#    res = getResult(s)
#    if not type(res) == type({}):
#        os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal currents --useShape --only=%s'"%str(i))
#        print "Resubmitted signal point %s"%s.name


