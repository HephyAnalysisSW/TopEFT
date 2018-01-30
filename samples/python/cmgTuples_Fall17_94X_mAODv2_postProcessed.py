import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

from TopEFT.samples.color import color

# Data directory
try:
    data_directory = sys.modules['__main__'].data_directory
except:
    from TopEFT.Tools.user import data_directory as user_data_directory
    data_directory = user_data_directory 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory = sys.modules['__main__'].postProcessing_directory
except:
  postProcessing_directory = "TopEFT_PP_2017_v14/dilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))


dirs = {}
dirs['TTZtoLLNuNu']     = ["TTZToLLNuNu", "TTZToLLNuNu_m1to10"]

# all inclusive right now
dirs["WW"]              = ["WW"]
dirs["WZ"]              = ["WZ"]
dirs["ZZ"]              = ["ZZ"]

dirs['TTLep_pow']       = ['TTLep_pow']
dirs['DY']              = ['DYJetsToLL_M50'] #amc@NLO
#dirs['DY_LO']           = ['DYJetsToLL_M50_LO','DYJetsToLL_M10to50_LO']

dirs['nonprompt']       = ['TTLep_pow']

#dirs['pseudoData']      = dirs['TTZtoLLNuNu'] + dirs["WZ"] + dirs['TTW'] + dirs['TTX'] + dirs['TZQ'] + dirs['rare'] + dirs['nonprompt']

dirs['rare']            = ["WW","ZZ"] # almost everything missing


directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TTZtoLLNuNu_17      = Sample.fromDirectory(name="TTZtoLLNuNu_17",       treeName="Events", isData=False, color=color.TTZtoLLNuNu,       texName="t#bar{t}Z (l#bar{l}/#nu#bar{#nu})",    directory=directories['TTZtoLLNuNu'])
WW_17               = Sample.fromDirectory(name="WW_17",                treeName="Events", isData=False, color=color.WW,                texName="WW",                                   directory=directories['WW'])
WZ_17               = Sample.fromDirectory(name="WZ_17",                treeName="Events", isData=False, color=color.WZ,                texName="WZ",                                   directory=directories['WZ'])
ZZ_17               = Sample.fromDirectory(name="ZZ_17",                treeName="Events", isData=False, color=color.ZZ,                texName="ZZ",                                   directory=directories['ZZ'])
DY_17               = Sample.fromDirectory(name="DY_17",                treeName="Events", isData=False, color=color.DY,                texName="DY (LO)",                              directory=directories['DY'])
TTLep_pow_17        = Sample.fromDirectory(name="TTLep_pow_17",         treeName="Events", isData=False, color=color.TTJets,            texName="t#bar{t}",                             directory=directories['TTLep_pow'])
nonprompt_17        = Sample.fromDirectory(name="nonprompt",            treeName="Events", isData=False, color=color.nonprompt,         texName="nonprompt",                            directory=directories['nonprompt'])
rare_17             = Sample.fromDirectory(name="rare",                 treeName="Events", isData=False, color=color.rare,              texName="rare",                                 directory=directories['rare'])

