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
  postProcessing_directory = "TopEFT_PP_2017_mva_v2/trilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))


dirs = {}
dirs['TTZtoLLNuNu']     = ["TTZToLLNuNu_amc"]

# all inclusive right now
dirs["WZ_amcatnlo"]     = ["WZTo3LNu_fxfx"]

dirs['TTW']             = ["TTWToLNu_fxfx"]
dirs['TTX']             = ["TTGJets", "TTHnobb_pow"] # should be complete
dirs['TZQ']             = ["TZQToLL"]

dirs['TTLep_pow']       = ['TTLep_pow']
dirs['DY']              = ['DYJetsToLL_M50'] #amc@NLO
dirs['DY_HT_LO']        = ['DYJetsToLL_M50_LO_comb_lheHT100','DYJetsToLL_M50_HT100to200', 'DYJetsToLL_M50_HT200to400', 'DYJetsToLL_M50_HT400to600', 'DYJetsToLL_M50_HT600to800', 'DYJetsToLL_M50_HT800to1200', 'DYJetsToLL_M50_HT2500toInf']
dirs['DY_LO']           = ['DYJetsToLL_M50_LO_comb']


dirs['nonprompt']       = ['TTLep_pow', 'DYJetsToLL_M50_LO_comb']
dirs['rare']            = ["WWW","WZZ","ZZTo4L_comb"] # not complete yet

dirs['pseudoData']      = dirs['TTZtoLLNuNu'] + dirs["WZ_amcatnlo"] + dirs['TTW'] + dirs['TTX'] + dirs['TZQ'] + dirs['rare'] + dirs['nonprompt']



directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TTZtoLLNuNu_17      = Sample.fromDirectory(name="TTZtoLLNuNu_17",   treeName="Events", isData=False, color=color.TTZtoLLNuNu,       texName="t#bar{t}Z (l#bar{l}/#nu#bar{#nu})",    directory=directories['TTZtoLLNuNu'])
DY_HT_LO_17         = Sample.fromDirectory(name="DY_HT_LO_17",      treeName="Events", isData=False, color=color.DY,                texName="DY HT (LO)",                           directory=directories['DY_HT_LO'])
TTX_17              = Sample.fromDirectory(name="TTX_17",           treeName="Events", isData=False, color=ROOT.kRed-10,            texName="t(t)X",                                directory=directories['TTX'])
TTW_17              = Sample.fromDirectory(name="TTW_17",           treeName="Events", isData=False, color=color.TTW,               texName="t#bar{t}W",                            directory=directories['TTW'])
TZQ_17              = Sample.fromDirectory(name="TZQ_17",           treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="tZq",                                  directory=directories['TZQ'])
TTLep_pow_17        = Sample.fromDirectory(name="TTLep_pow_17",     treeName="Events", isData=False, color=color.TTJets,            texName="t#bar{t}",                             directory=directories['TTLep_pow'])
nonprompt_17        = Sample.fromDirectory(name="nonprompt_17",     treeName="Events", isData=False, color=color.nonprompt,         texName="nonprompt",                            directory=directories['nonprompt'])
rare_17             = Sample.fromDirectory(name="rare_17",          treeName="Events", isData=False, color=color.rare,              texName="rare",                                 directory=directories['rare'])
WZ_amcatnlo_17      = Sample.fromDirectory(name="WZ_17",            treeName="Events", isData=False, color=color.WZ,                texName="WZ",                                   directory=directories['WZ_amcatnlo'])
pseudoData_17       = Sample.fromDirectory(name="pseudoData_17",    treeName="Events", isData=False, color=ROOT.kBlack,             texName="pseudo-data",                          directory=directories['pseudoData'])
