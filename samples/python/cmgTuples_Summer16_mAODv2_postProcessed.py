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
  postProcessing_directory = "TopEFT_PP_v5/trilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))


dirs = {}
dirs['TTZtoLLNuNu']     = ["TTZToLLNuNu_ext"]
dirs["WZ"]              = ["WZTo3LNu_amcatnlo"]

dirs['TTW']             = ["TTWToLNu_ext_comb"]
dirs['TTX']             = ["TTGJets_comb", "TTHnobb_pow", "TTTT", "tWll"] # should be complete
dirs['TZQ']             = ["tZq_ll_ext"]

dirs['rare']            = ["WGToLNuG","WWZ","WZZ","ZGTo2LG_ext","ZZTo4L","ZZZ"] # should be complete

dirs['nonprompt']       = ['TTLep_pow'] #only ttjets for now
#dirs['nonprompt']       = ['DYJetsToLL_M50', 'TTJets'] # no v4 version atm

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TTZtoLLNuNu     = Sample.fromDirectory(name="TTZtoNuNu",        treeName="Events", isData=False, color=color.TTZtoLLNuNu,       texName="t#bar{t}Z (l#bar{l}/#nu#bar{#nu})",    directory=directories['TTZtoLLNuNu'])
WZ              = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,                texName="WZ",                                   directory=directories['WZ'])
TTX             = Sample.fromDirectory(name="TTX",              treeName="Events", isData=False, color=ROOT.kRed-10,               texName="t(t)X",                                directory=directories['TTX'])
TTW             = Sample.fromDirectory(name="TTW",              treeName="Events", isData=False, color=color.TTX,               texName="t#bar{t}W",                                directory=directories['TTW'])
TZQ             = Sample.fromDirectory(name="TZQ",              treeName="Events", isData=False, color=ROOT.kOrange+7,               texName="tZq",                                directory=directories['TZQ'])
rare            = Sample.fromDirectory(name="rare",             treeName="Events", isData=False, color=color.rare,              texName="rare",                                 directory=directories['rare'])
nonprompt       = Sample.fromDirectory(name="nonprompt",        treeName="Events", isData=False, color=color.nonprompt,         texName="nonprompt",                            directory=directories['nonprompt'])
