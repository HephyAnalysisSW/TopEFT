import copy, os, sys
from RootTools.core.Sample import Sample 
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

# Data directory
try:    data_directory = sys.modules['__main__'].data_directory
except:
    #from TopEFT.Tools.user import data_directory
    data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"

# Take post processing directory if defined in main module
try:    postProcessing_directory = sys.modules['__main__'].postProcessing_directory
except: postProcessing_directory = 'TopEFT_PP_v20/trilep'

logger.info("Loading data samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}
for (run, version) in [('B','_v2'),('C',''),('D',''),('E',''),('F',''),('G',''),('H','_v2'),('H','_v3')]:
    runTag = 'Run2016' + run + '_03Feb2017' + version + '_TriggerStrategy2018'
    dirs["DoubleEG_Run2016"         + run + version ] = ["DoubleEG_"          + runTag ]
    dirs["DoubleMuon_Run2016"       + run + version ] = ["DoubleMuon_"        + runTag ]
    dirs["SingleElectron_Run2016"   + run + version ] = ["SingleElectron_"    + runTag ]
    dirs["SingleMuon_Run2016"       + run + version ] = ["SingleMuon_"        + runTag ]
    dirs["MuonEG_Run2016"           + run + version ] = ["MuonEG_"            + runTag ]
    #dirs["SingleElectron_Run2016"   + run + version ] = ["SingleElectron_"    + runTag + "_Trig_e"]
    #dirs["SingleMuon_Run2016"       + run + version ] = ["SingleMuon_"        + runTag + "_Trig_mu"]
    #dirs["SingleEleMu_Run2016"      + run + version ] = ["SingleMuon_"        + runTag + "_Trig_mu", "SingleElectron_"        + runTag + "_Trig_e_for_mu"]

def merge(pd, totalRunName, listOfRuns):
    dirs[pd + '_' + totalRunName] = []
    for run in listOfRuns: dirs[pd + '_' + totalRunName].extend(dirs[pd + '_' + run])

for pd in ['SingleElectron','SingleMuon', 'MuonEG', 'DoubleMuon', 'DoubleEG']:
    merge(pd, 'Run2016BCD',    ['Run2016B_v2', 'Run2016C', 'Run2016D'])
    merge(pd, 'Run2016BCDEFG', ['Run2016BCD', 'Run2016E', 'Run2016F', 'Run2016G'])
    merge(pd, 'Run2016',       ['Run2016BCDEFG', 'Run2016H_v2', 'Run2016H_v3'])

for key in dirs:
    dirs[key] = [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]]


def getSample(pd, runName, lumi):
    sample      = Sample.fromDirectory(name=(pd + '_' + runName), treeName="Events", texName=(pd + ' (' + runName + ')'), directory=dirs[pd + '_' + runName])
    sample.lumi = lumi
    return sample

DoubleEG_Run2016                = getSample('DoubleEG',         'Run2016',       (5.744+2.573+4.248+4.009+3.101+7.540+8.329+0.210)*1000)
DoubleMuon_Run2016              = getSample('DoubleMuon',       'Run2016',       (5.744+2.573+4.248+4.009+3.101+7.540+8.329+0.210)*1000)
SingleElectron_Run2016          = getSample('SingleElectron',   'Run2016',       (5.744+2.573+4.248+4.009+3.101+7.540+8.329+0.210)*1000)
SingleMuon_Run2016              = getSample('SingleMuon',       'Run2016',       (5.744+2.573+4.248+4.009+3.101+7.540+8.329+0.210)*1000)
MuonEG_Run2016                  = getSample('MuonEG',           'Run2016',       (5.744+2.573+4.248+4.009+3.101+7.540+8.329+0.210)*1000)

allSamples_Data25ns = []
#allSamples_Data25ns += [SingleElectron_Run2016]
allSamples_Data25ns += [SingleMuon_Run2016, SingleElectron_Run2016, MuonEG_Run2016, DoubleEG_Run2016, DoubleMuon_Run2016]

Run2016 = Sample.combine("Run2016", [SingleMuon_Run2016, SingleElectron_Run2016, MuonEG_Run2016, DoubleEG_Run2016, DoubleMuon_Run2016], texName = "Data")
Run2016.lumi = (5.744+2.573+4.248+4.009+3.101+7.540+8.329+0.210)*1000

for s in allSamples_Data25ns:
  s.color   = ROOT.kBlack
  s.isData  = True
