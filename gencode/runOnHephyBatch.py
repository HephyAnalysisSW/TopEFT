# Standard imports
import os
import time
import itertools

# TopEFT
from TopEFT.gencode.EFT import *

# Logger
import logging
logger = logging.getLogger(__name__)

n = 15

coup = "cuW"
couplingValues = [ i*0.1/n for i in range(-n,n+1) ]


processes = ['ttZ','ttW','ttH']
#processes = ['ttZ']
submitCMD = "submitBatch.py --title='scan'"
#submitCMD = "echo"

for p in processes:
    for cv in couplingValues:
        couplingStr = "%s %s"%(coup, cv)
        os.system(submitCMD+" 'python calcXSec.py --model HEL_UFO --process "+p+" --couplings "+couplingStr+"'")
        if not "echo" in submitCMD:
            time.sleep(60) # need to distribute load, shouldn't start with 40 jobs at a time

