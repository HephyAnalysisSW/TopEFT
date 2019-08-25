import copy, os, sys
from RootTools.core.Sample import Sample 
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

# Data directory
try:    data_directory = sys.modules['__main__'].data_directory
except: from TopEFT.Tools.user import data_directory

data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'

# Take post processing directory if defined in main module
try:    postProcessing_directory = sys.modules['__main__'].postProcessing_directory
except: postProcessing_directory = 'TopEFT_PP_2017_mva_v7/singlelep'

logger.info("Loading data samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}
for (run, version) in [('B',''),('C',''), ('D',''),('E','')]:
    runTag = 'Run2017' + run + '_17Nov2017' +  version
    dirs["MET_Run2017"   + run + version ] = ["MET_"    + runTag ]
    dirs["HTMHT_Run2017" + run + version ] = ["HTMHT_"  + runTag ]
    dirs["JetHT_Run2017" + run + version ] = ["JetHT_"  + runTag ]

#for (run, version) in [('D',''),('E','')]:
#    runTag = 'Run2017' + run + version
#    dirs["MET_Run2017"   + run + version ] = ["MET_"    + runTag ]
#

def merge(pd, totalRunName, listOfRuns):
    dirs[pd + '_' + totalRunName] = []
    for run in listOfRuns: dirs[pd + '_' + totalRunName].extend(dirs[pd + '_' + run])

for pd in ['MET', 'HTMHT', 'JetHT']:
    merge(pd, 'Run2017BC',      ['Run2017B', 'Run2017C'])
    merge(pd, 'Run2017DE',      ['Run2017D', 'Run2017E'])
    merge(pd, 'Run2017',        ['Run2017BC', 'Run2017DE'])

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]]


def getSample(pd, runName, lumi):
    sample      = Sample.fromDirectory(name=(pd + '_' + runName), treeName="Events", texName=(pd + ' (' + runName + ')'), directory=dirs[pd + '_' + runName])
    sample.lumi = lumi
    return sample

MET_Run2017          = getSample('MET',   'Run2017',       (1)*1000)
HTMHT_Run2017        = getSample('HTMHT', 'Run2017',       (1)*1000)
JetHT_Run2017        = getSample('JetHT', 'Run2017',       (1)*1000)


allSamples_Data25ns = [ MET_Run2017, HTMHT_Run2017, JetHT_Run2017 ]

for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True
