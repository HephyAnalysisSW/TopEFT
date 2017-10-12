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
    from TopEFT.tools.user import data_directory as user_data_directory
    data_directory = user_data_directory 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory = sys.modules['__main__'].postProcessing_directory
except:
  postProcessing_directory = "TopEFT_PP_v4/dilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))


dirs = {}
dirs['TTZtoLLNuNu']     = ["TTZToLLNuNu_ext"]
dirs["WZ"]              = ["WZTo3LNu_amcatnlo"]

#dirs['TTX']             = ["TTHnobb_pow", "TTWToLNu_ext", "tWll", "tZq_ll_ext"] # just a subset, not complete
dirs['TTX']             = ["TTGJets_comb", "TTHnobb_pow", "TTTT", "TTWToLNu_ext_comb", "tWll", "tZq_ll_ext"] # should be complete

#dirs['rare']            = ["ZZ","WZZ","WWZ","ZZZ"] # just a subset, not complete
dirs['rare']            = ["WGToLNuG","WWZ","WZZ","ZGTo2LG_ext","ZZTo4L","ZZZ"] # should be complete

#dirs['nonprompt']       = ['DYJetsToLL_M50', 'TTJets'] # no v4 version atm

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TTZtoLLNuNu     = Sample.fromDirectory(name="TTZtoNuNu",        treeName="Events", isData=False, color=color.TTZtoLLNuNu,       texName="t#bar{t}Z (l#bar{l}/#nu#bar{#nu})",    directory=directories['TTZtoLLNuNu'])
WZ              = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,                texName="WZ",                                   directory=directories['WZ'])
TTX             = Sample.fromDirectory(name="TTX",              treeName="Events", isData=False, color=color.TTX,               texName="t(t)X",                                directory=directories['TTX'])
rare            = Sample.fromDirectory(name="rare",             treeName="Events", isData=False, color=color.rare,              texName="rare",                                 directory=directories['rare'])
#nonprompt       = Sample.fromDirectory(name="nonprompt",        treeName="Events", isData=False, color=color.nonprompt,         texName="nonprompt",                            directory=directories['nonprompt'])
