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
except: postProcessing_directory = 'TopEFT_PP_v14/dilep'

logger.info("Loading data samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}
for (run, version) in [('B','_v2'),('C',''),('D',''),('E',''),('F',''),('G',''),('H','_v2'),('H','_v3')]:
    runTag = 'Run2016' + run + '_03Feb2017' + version
    dirs["SingleElectron_Run2016"   + run + version ] = ["SingleElectron_"    + runTag]
    dirs["SingleMuon_Run2016"       + run + version ] = ["SingleMuon_"        + runTag]
    dirs["SingleEleMu_Run2016"      + run + version ] = ["SingleMuon_"        + runTag, "SingleElectron_"        + runTag]

def merge(pd, totalRunName, listOfRuns):
    dirs[pd + '_' + totalRunName] = []
    for run in listOfRuns: dirs[pd + '_' + totalRunName].extend(dirs[pd + '_' + run])

for pd in ['SingleElectron','SingleMuon', 'SingleEleMu']:
    merge(pd, 'Run2016BCD',    ['Run2016B_v2', 'Run2016C', 'Run2016D'])
    merge(pd, 'Run2016BCDEFG', ['Run2016BCD', 'Run2016E', 'Run2016F', 'Run2016G'])
    merge(pd, 'Run2016',       ['Run2016BCDEFG', 'Run2016H_v2', 'Run2016H_v3'])

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]]


def getSample(pd, runName, lumi):
    sample      = Sample.fromDirectory(name=(pd + '_' + runName), treeName="Events", texName=(pd + ' (' + runName + ')'), directory=dirs[pd + '_' + runName])
    sample.lumi = lumi
    return sample

SingleElectron_Run2016          = getSample('SingleElectron',   'Run2016',       (5.744+2.573+4.248+4.009+3.101+7.540+8.329+0.210)*1000)
SingleMuon_Run2016              = getSample('SingleMuon',       'Run2016',       (5.744+2.573+4.248+4.009+3.101+7.540+8.329+0.210)*1000)
SingleEleMu_Run2016             = getSample('SingleEleMu',      'Run2016',       (5.744+2.573+4.248+4.009+3.101+7.540+8.329+0.210)*1000)

allSamples_Data25ns = []
#allSamples_Data25ns += [SingleElectron_Run2016]
allSamples_Data25ns += [SingleMuon_Run2016, SingleElectron_Run2016, SingleEleMu_Run2016]

for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True
