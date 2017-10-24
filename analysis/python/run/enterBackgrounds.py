# Standard imports
import os
import subprocess
import shutil
import re
import copy
import imp 

# TopEFT
from TopEFT.tools.resultsDB import resultsDB
from TopEFT.tools.user import results_directory, tmp_directory
from TopEFT.tools.u_float import u_float as u

from TopEFT.analysis.regions import regionsA

# Logging
import TopEFT.tools.logger as logger

logger = logger.get_logger("INFO", logFile = None)

processes = [ "ttZ", "fake", "WZ", "WZ", "ttH", "ttW", "ttX", "ZZ", "rare" ]

lumi            = 35.9
columns         = ["process", "region", "channel", "presel", "lumi", "weightString"]
presel          = "lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10&&nGoodLeptons==3&&njet>2&&nBTag>0&&abs(Z_mass-91.2)<10"
weightString    = "weight*%s"%lumi

#for process in processes:
#    resultsCache = resultsDB( os.path.join(results_directory, "resultsCache.db"), process, columns )

key = {"channel":"all", "lumi":lumi, "presel":presel, "weightString":weightString}

r0 = regionsA[0].cutString()
r1 = regionsA[1].cutString()
r2 = regionsA[2].cutString()

#ttZ     = Sample("ttZ", "Events", ["dummy.root"])

def fillResults(process, values, key):
    tmp = copy.deepcopy(key)
    for i in range(3):
        r = regionsA[i].cutString()
        k = {"channel":"all", "lumi":lumi, "presel":presel, "weightString":weightString, "process":process, "region":r}
        resultsCache.add(k, values[i], overwrite=True)

resultsCache = resultsDB( os.path.join(results_directory, "resultsCache.db"), "TopEFT", columns )

values = [u(102.2091, 102.2091*0.0075), u(31.6185, 31.6185*0.0143), u(5.3084, 5.3084*0.0352)]
fillResults("ttZ", values, key)

values = [u(30.8514, 30.8514*0.1178), u(2.4059, 2.4059*0.4277), u(0.1, 0.1*0.7393)]
fillResults("fake", values, key)

values = [u(23.1666, 23.1666*0.0438), u(7.4121, 7.4121*0.0758), u(1.8730, 1.8730*0.1537)]
fillResults("WZ", values, key)

values = [u(2.4804, 2.4804*0.0511), u(0.1074, 0.1074*0.2437), u(0.0020,0.0020*2.0613)]
fillResults("ttH", values, key)

values = [u(3.9295, 3.9295*0.0228), u(0.2330, 0.2330*0.0935), u(0.0105, 0.0105*0.4897)]
fillResults("ttW", values, key)

values = [u(34.7993, 34.7993*0.0154), u(6.1159, 6.1159*0.0314), u(0.8531, 0.8531*0.0762)]
fillResults("ttX", values, key)

values = [u(3.4418, 3.4418*0.0456), u(0.6577, 0.6577*0.1078), u(0.1104, 0.1104*0.2527)]
fillResults("ZZ", values, key)

values = [u(5.6334, 5.6334*0.2422), u(1.5365, 1.5365*0.3349), u(0.2436, 0.2436*0.2868)]
fillResults("rare", values, key)

values = [u(210), u(55), u(6)]
fillResults("Data", values, key)
