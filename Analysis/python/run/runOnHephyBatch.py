#!/usr/bin/env python
import os
import time

from TopEFT.samples.gen_fwlite_benchmarks import *

#dim6_all        = [ x.name for x in allSamples_dim6top ]
dim6_dipoles    = [ x.name for x in dim6top_dipoles ]
dim6_currents   = [ x.name for x in dim6top_currents ]

#ewkDM_all       = [ x.name for x in ewkDM_all ]
ewkDM_dipoles   = [ ewkDM_central ] + ewkDM_dipoles
ewkDM_currents  = [ ewkDM_central ] + ewkDM_currents

dim6top_dipoles  = [ dim6top_central ] + dim6top_dipoles
dim6top_currents = [ dim6top_central ] + dim6top_currents

submitCMD = "submitBatch.py --title='CombineEra' "
#submitCMD = "echo "

signals = ewkDM_currents

'''
Currents
'''

#for i, x in enumerate(ewkDM_currents):
#    #print i, x.name
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal currents --useShape --useXSec --only=%s'"%str(i))
#    #if i>100: break
#    #if submitCMD.startswith("submit"):
#    #    time.sleep(2)

#'''
#Dipoles
#'''
#

#for i, x in enumerate(ewkDM_dipoles):
#    #print i, x.name
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles --useShape --useXSec --year 2016 --unblind --includeCR --only=%s'"%str(i))
#    if i > 437: break
#    #if submitCMD.startswith("submit"):
#    #    time.sleep(2)

#for i, x in enumerate(dim6top_dipoles):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model dim6top_LO --signal dipoles --useShape --useXSec  --year 2017 --unblind --includeCR --expected --only=%s'"%str(i))
#    time.sleep(1)
#
#for i, x in enumerate(dim6top_currents):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model dim6top_LO --signal currents --useShape --useXSec --year 2017 --unblind --includeCR --expected --only=%s'"%x.name)
#    time.sleep(1)

#for i, x in enumerate(dim6top_dipoles):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model dim6top_LO --signal dipoles --useShape --useXSec --year 2016 --unblind --includeCR --only=%s'"%str(i))
##    time.sleep(2)
#
#for i, x in enumerate(dim6top_currents):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model dim6top_LO --signal currents --useXSec --year 2016 --unblind --includeCR --expected --only=%s'"%x.name)
#    time.sleep(1)
#
#for i, x in enumerate(dim6top_dipoles):
#    os.system(submitCMD+"'python run_combination.py --model dim6top_LO --signal dipoles --useShape --useXSec --includeCR --expected --only=%s'"%str(i))
#    #time.sleep(1)
#
#for i, x in enumerate(dim6top_currents):
#    os.system(submitCMD+"'python run_combination.py --model dim6top_LO --signal currents --useShape --useXSec --includeCR --expected --only=%s'"%x.name)
#    #time.sleep(1)

#### ewkDM shape + xsec
#for i, x in enumerate(ewkDM_dipoles):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles  --useShape --useXSec --year 2017 --unblind --includeCR --expected --only=%s'"%str(i))
#    time.sleep(2)
#
#for i, x in enumerate(ewkDM_currents):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal currents --useShape --useXSec --year 2017 --unblind --includeCR --expected --only=%s'"%str(i))
#
#for i, x in enumerate(ewkDM_dipoles):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles  --useShape --useXSec --year 2016 --unblind --includeCR --expected --only=%s'"%str(i))
#
#for i, x in enumerate(ewkDM_currents):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal currents --useShape --useXSec --year 2016 --unblind --includeCR --expected --only=%s'"%str(i))
#
#### ewkDM xsec
#for i, x in enumerate(ewkDM_dipoles):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles  --useXSec --year 2017 --unblind --includeCR --expected --only=%s'"%str(i))
#
#for i, x in enumerate(ewkDM_currents):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal currents --useXSec --year 2017 --unblind --includeCR --expected --only=%s'"%str(i))
#
#for i, x in enumerate(ewkDM_dipoles):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles  --useXSec --year 2016 --unblind --includeCR --expected --only=%s'"%str(i))
#
#for i, x in enumerate(ewkDM_currents):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal currents --useXSec --year 2016 --unblind --includeCR --expected --only=%s'"%str(i))
#
#### ewkDM shape
#for i, x in enumerate(ewkDM_dipoles):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles  --useShape --year 2017 --unblind --includeCR --expected --only=%s'"%str(i))
#
#for i, x in enumerate(ewkDM_currents):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal currents --useShape --year 2017 --unblind --includeCR --expected --only=%s'"%str(i))
#
#for i, x in enumerate(ewkDM_dipoles):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles  --useShape --year 2016 --unblind --includeCR --expected --only=%s'"%str(i))
#
#for i, x in enumerate(ewkDM_currents):
#    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal currents --useShape --year 2016 --unblind --includeCR --expected --only=%s'"%str(i))


#for i, x in enumerate(ewkDM_dipoles):
#    os.system(submitCMD+"'python run_combination.py --model ewkDM --signal dipoles  --useShape --useXSec --includeCR --expected --only=%s'"%str(i))
#    #time.sleep(1)
#
#for i, x in enumerate(ewkDM_currents):
#    os.system(submitCMD+"'python run_combination.py --model ewkDM --signal currents --useShape --useXSec --includeCR --expected --only=%s'"%str(i))
#    #time.sleep(1)
#
#for i, x in enumerate(ewkDM_dipoles):
#    os.system(submitCMD+"'python run_combination.py --model ewkDM --signal dipoles  --useShape --includeCR --expected --only=%s'"%str(i))
#    #time.sleep(1)
#
#for i, x in enumerate(ewkDM_currents):
#    os.system(submitCMD+"'python run_combination.py --model ewkDM --signal currents --useShape --includeCR --expected --only=%s'"%str(i))
#    #time.sleep(1)
#
#for i, x in enumerate(ewkDM_dipoles):
#    os.system(submitCMD+"'python run_combination.py --model ewkDM --signal dipoles  --useXSec --includeCR --expected --only=%s'"%str(i))
#    #time.sleep(1)

for i, x in enumerate(ewkDM_currents):
    os.system(submitCMD+"'python run_combination.py --model ewkDM --signal currents --useXSec --includeCR --expected --only=%s'"%str(i))
    #time.sleep(1)
#

## for resubmission of failed jobs:
#from TopEFT.Analysis.run.getResults import getResult
#for i,s in enumerate(ewkDM_dipoles):
#    res = getResult(s)
#    if not type(res) == type({}):
#        os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles --useShape --only=%s'"%str(i))
##        print "Resubmitted signal point %s"%s.name


