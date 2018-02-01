#!/usr/bin/env python
import os
import time

from TopEFT.samples.gen_fwlite_benchmarks import *

dim6_all        = [ x.name for x in allSamples_dim6top ]
dim6_dipoles    = [ x.name for x in dim6top_dipoles ]
dim6_currents   = [ x.name for x in dim6top_currents ]

ewkDM_all       = [ x.name for x in ewkDM_all ]
ewkDM_dipoles   = [ ewkDM_central ] + [ x.name for x in ewkDM_dipoles ]
ewkDM_currents  = [ ewkDM_central ] + [ x.name for x in ewkDM_currents ]

submitCMD = "submitBatch.py --title='Limit2D' "
#submitCMD = "echo "

signals = ewkDM_dipoles

for i, x in enumerate(signals):
    print i, x
    os.system(submitCMD+"'python run_limit_reweighting.py --model ewkDM --signal dipoles --useXSec --useShape --only=%s'"%str(i))
    if submitCMD.startswith("submit"):
        time.sleep(2)

