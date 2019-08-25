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
except: postProcessing_directory = 'TopEFT_PP_2017_v18/dilep'

logger.info("Loading data samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}
#for (run, version) in [('B','_v2'),('C',''),('D',''),('E',''),('F',''),('G',''),('H','_v2'),('H','_v3')]:
#    runTag = 'Run2016' + run + '_03Feb2017' + version
#    dirs["SingleElectron_Run2016"   + run + version ] = ["SingleElectron_"    + runTag + "_Trig_e"]
#    dirs["SingleMuon_Run2016"       + run + version ] = ["SingleMuon_"        + runTag + "_Trig_mu"]
#    dirs["SingleEleMu_Run2016"      + run + version ] = ["SingleMuon_"        + runTag + "_Trig_mu", "SingleElectron_"        + runTag + "_Trig_e_for_mu"]

for (run, version) in [('B',''),('C','')]:
    runTag = 'Run2017' + run + '_12Sep2017' + version
    dirs["SingleElectron_Run2017"   + run + version ] = ["SingleElectron_"    + runTag + "_Trig_e"]
    dirs["SingleMuon_Run2017"       + run + version ] = ["SingleMuon_"        + runTag + "_Trig_mu"]
    dirs["SingleEleMu_Run2017"      + run + version ] = ["SingleMuon_"        + runTag + "_Trig_mu", "SingleElectron_"        + runTag + "_Trig_e_for_mu"]
    dirs["MET_Run2017"              + run + version ] = ["MET_"               + runTag]

for (run, version) in [('C','v2'), ('D',''),('E',''),('F','')]:
    runTag = 'Run2017' + run + version
    dirs["SingleElectron_Run2017"   + run + version ] = ["SingleElectron_"    + runTag + "_Trig_e"]
    dirs["SingleMuon_Run2017"       + run + version ] = ["SingleMuon_"        + runTag + "_Trig_mu"]
    dirs["SingleEleMu_Run2017"      + run + version ] = ["SingleMuon_"        + runTag + "_Trig_mu", "SingleElectron_"        + runTag + "_Trig_e_for_mu"]
    dirs["MET_Run2017"              + run + version ] = ["MET_"               + runTag]


def merge(pd, totalRunName, listOfRuns):
    dirs[pd + '_' + totalRunName] = []
    for run in listOfRuns: dirs[pd + '_' + totalRunName].extend(dirs[pd + '_' + run])

for pd in ['SingleElectron','SingleMuon','SingleEleMu','MET']:
    merge(pd, 'Run2017BC',      ['Run2017B', 'Run2017C'])
    merge(pd, 'Run2017EF',      ['Run2017E', 'Run2017F'])
    merge(pd, 'Run2017Cv2DEF',  ['Run2017Cv2','Run2017D', 'Run2017E', 'Run2017F'])
    merge(pd, 'Run2017Cv2D',    ['Run2017Cv2','Run2017D'])
    merge(pd, 'Run2017BCCv2D',  ['Run2017B', 'Run2017C', 'Run2017Cv2', 'Run2017D'])
    merge(pd, 'Run2017',        ['Run2017BCCv2D', 'Run2017E', 'Run2017F'])

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]]


def getSample(pd, runName, lumi):
    sample      = Sample.fromDirectory(name=(pd + '_' + runName), treeName="Events", texName=(pd + ' (' + runName + ')'), directory=dirs[pd + '_' + runName])
    sample.lumi = lumi
    return sample

lumi = 39*1000

SingleElectron_Run2017BC       = getSample('SingleElectron',   'Run2017BC',       (1.)*1000)
SingleMuon_Run2017BC           = getSample('SingleMuon',       'Run2017BC',       (1.)*1000)
SingleEleMu_Run2017BC          = getSample('SingleEleMu',      'Run2017BC',       (1.)*1000)

SingleElectron_Run2017Cv2D     = getSample('SingleElectron', 'Run2017Cv2D',       (1.)*1000)
SingleMuon_Run2017Cv2D         = getSample('SingleMuon',     'Run2017Cv2D',       (1.)*1000)
SingleEleMu_Run2017Cv2D        = getSample('SingleEleMu',    'Run2017Cv2D',       (1.)*1000)

SingleElectron_Run2017Cv2DEF   = getSample('SingleElectron',   'Run2017Cv2DEF',       (1.)*1000)
SingleMuon_Run2017Cv2DEF       = getSample('SingleMuon',       'Run2017Cv2DEF',       (1.)*1000)
SingleEleMu_Run2017Cv2DEF      = getSample('SingleEleMu',      'Run2017Cv2DEF',       (1.)*1000)

SingleElectron_Run2017EF       = getSample('SingleElectron',   'Run2017EF',       (1.)*1000)
SingleMuon_Run2017EF           = getSample('SingleMuon',       'Run2017EF',       (1.)*1000)
SingleEleMu_Run2017EF          = getSample('SingleEleMu',      'Run2017EF',       (1.)*1000)

SingleElectron_Run2017         = getSample('SingleElectron',   'Run2017',       lumi)
SingleMuon_Run2017             = getSample('SingleMuon',       'Run2017',       lumi)
SingleEleMu_Run2017            = getSample('SingleEleMu',      'Run2017',       lumi)

MET_Run2017                     = getSample('MET',       'Run2017',       lumi)

allSamples_Data25ns_2017= []
allSamples_Data25ns_2017+= [SingleMuon_Run2017, SingleElectron_Run2017, SingleEleMu_Run2017, MET_Run2017]

for s in allSamples_Data25ns_2017:
  s.color   = ROOT.kBlack
  s.isData  = True
