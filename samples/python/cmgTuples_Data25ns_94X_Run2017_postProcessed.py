import copy, os, sys
from RootTools.core.Sample import Sample 
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

# Data directory
try:    data_directory = sys.modules['__main__'].data_directory
except: from TopEFT.Tools.user import data_directory

# Take post processing directory if defined in main module
try:    postProcessing_directory = sys.modules['__main__'].postProcessing_directory
except: postProcessing_directory = 'TopEFT_PP_2017_v19/dilep'

logger.info("Loading data samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}

for (run, version) in [('B',''),('C',''),('D',''),('E',''),('F','')]:
    runTag = 'Run2017' + run + '_17Nov2017' + version
    dirs["DoubleEG_Run2017"   + run + version ] = ["DoubleEG_"    + runTag ]
    dirs["DoubleMuon_Run2017"       + run + version ] = ["DoubleMuon_"        + runTag ]

def merge(pd, totalRunName, listOfRuns):
    dirs[pd + '_' + totalRunName] = []
    for run in listOfRuns: dirs[pd + '_' + totalRunName].extend(dirs[pd + '_' + run])

for pd in ['DoubleEG','DoubleMuon']:
    merge(pd, 'Run2017BC',   ['Run2017B', 'Run2017C'])
    merge(pd, 'Run2017EF',   ['Run2017E', 'Run2017F'])
    merge(pd, 'Run2017DEF',  ['Run2017D', 'Run2017E', 'Run2017F'])
    merge(pd, 'Run2017BCD',  ['Run2017B', 'Run2017C', 'Run2017D'])
    merge(pd, 'Run2017',     ['Run2017BCD', 'Run2017E', 'Run2017F'])

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]]


def getSample(pd, runName, lumi):
    sample      = Sample.fromDirectory(name=(pd + '_' + runName), treeName="Events", texName=(pd + ' (' + runName + ')'), directory=dirs[pd + '_' + runName])
    sample.lumi = lumi
    return sample

DoubleEG_Run2017BC    = getSample('DoubleEG',   'Run2017BC',       (1.)*1000)
DoubleMuon_Run2017BC  = getSample('DoubleMuon',       'Run2017BC',       (1.)*1000)

DoubleEG_Run2017D     = getSample('DoubleEG', 'Run2017D',       (1.)*1000)
DoubleMuon_Run2017D   = getSample('DoubleMuon',     'Run2017D',       (1.)*1000)

DoubleEG_Run2017DEF   = getSample('DoubleEG',   'Run2017DEF',       (1.)*1000)
DoubleMuon_Run2017DEF = getSample('DoubleMuon',       'Run2017DEF',       (1.)*1000)

DoubleEG_Run2017EF    = getSample('DoubleEG',   'Run2017EF',       (1.)*1000)
DoubleMuon_Run2017EF  = getSample('DoubleMuon',       'Run2017EF',       (1.)*1000)

DoubleEG_Run2017      = getSample('DoubleEG',   'Run2017',       (1.)*1000)
DoubleMuon_Run2017    = getSample('DoubleMuon',       'Run2017',       (1.)*1000)

allSamples_Data25ns_2017 = []
allSamples_Data25ns_2017+= [DoubleMuon_Run2017, DoubleEG_Run2017]#, MET_Run2017]

for s in allSamples_Data25ns_2017:
  s.color   = ROOT.kBlack
  s.isData  = True
