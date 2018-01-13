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
  postProcessing_directory = "TopEFT_PP_v14/trilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))


dirs = {}
dirs['TTZtoLLNuNu']     = ["TTZToLLNuNu_ext"]
dirs['TTZ_LO']          = ["TTZ_LO"]
dirs["WZ"]              = ["WZTo3LNu_amcatnlo"]

dirs['TTW']             = ["TTWToLNu_ext_comb"]
dirs['TTX']             = ["TTGJets_comb", "TTHnobb_pow", "TTTT", "tWll"] # should be complete
dirs['TZQ']             = ["tZq_ll_ext"]

dirs['TTX_all']         = ["TTGJets_comb", "TTHnobb_pow", "TTTT", "tWll", "TTWToLNu_ext_comb","tZq_ll_ext","TTZToLLNuNu_ext"]

dirs['rare']            = ["WGToLNuG","WWZ","WZZ","ZGTo2LG_ext","ZZTo4L","ZZZ"] # should be complete

dirs['TTLep_pow']       = ['TTLep_pow']

#dirs['DY_LO']              = ['DYJetsToLL_M50_LO_ext','DYJetsToLL_M10to50_LO']

dirs['nonprompt']       = ['TTLep_pow'] #only ttjets for now

dirs['ewkDM_ttZ_ll_noH']            = ["ewkDM_ttZ_ll_noH"]

#dirs['WJets_LO']        = ['WJetsToLNu_LO']
#dirs['WJets']           = ['WJetsToLNu']

dirs['pseudoData']      = dirs['TTZtoLLNuNu'] + dirs["WZ"] + dirs['TTW'] + dirs['TTX'] + dirs['TZQ'] + dirs['rare'] + dirs['nonprompt']
#dirs['pseudoDataPriv']  = dirs['ewkDM_ttZ_ll_noH'] + dirs["WZ"] + dirs['TTW'] + dirs['TTX'] + dirs['TZQ'] + dirs['rare'] + dirs['nonprompt']

dirs['background']      = dirs["WZ"] + dirs['TTW'] + dirs['TTX'] + dirs['TZQ'] + dirs['rare']

#dirs['nonprompt']       = ['DYJetsToLL_M50', 'TTJets'] # no v4 version atm

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

pseudoData      = Sample.fromDirectory(name="pseudoData",       treeName="Events", isData=False, color=ROOT.kBlack,            texName="pseudo-data",                          directory=directories['pseudoData'])
#pseudoDataPriv  = Sample.fromDirectory(name="pseudoDataPriv",   treeName="Events", isData=False, color=ROOT.kBlack,            texName="pseudo-data",                          directory=directories['pseudoDataPriv'])
TTZtoLLNuNu     = Sample.fromDirectory(name="TTZtoLLNuNu",      treeName="Events", isData=False, color=color.TTZtoLLNuNu,       texName="t#bar{t}Z (l#bar{l}/#nu#bar{#nu})",    directory=directories['TTZtoLLNuNu'])
TTZ_LO          = Sample.fromDirectory(name="TTZ_LO",           treeName="Events", isData=False, color=color.TTZtoLLNuNu+1,            texName="t#bar{t}Z (LO)",                       directory=directories['TTZ_LO'])
WZ              = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,                texName="WZ",                                   directory=directories['WZ'])
#WJets_LO        = Sample.fromDirectory(name="WJets_LO",         treeName="Events", isData=False, color=color.WJetsToLNu,                texName="W+jets (LO)",            directory=directories['WJets_LO'])
#WJets           = Sample.fromDirectory(name="WJets",            treeName="Events", isData=False, color=color.WJetsToLNu+2,               texName="W+jets (NLO)",            directory=directories['WJets'])
TTX             = Sample.fromDirectory(name="TTX",              treeName="Events", isData=False, color=ROOT.kRed-10,               texName="t(t)X",                                directory=directories['TTX'])
TTX_all         = Sample.fromDirectory(name="TTX_all",          treeName="Events", isData=False, color=ROOT.kRed-10,               texName="t(t)X",                                directory=directories['TTX_all'])
TTW             = Sample.fromDirectory(name="TTW",              treeName="Events", isData=False, color=color.TTX,               texName="t#bar{t}W",                                directory=directories['TTW'])
TZQ             = Sample.fromDirectory(name="TZQ",              treeName="Events", isData=False, color=ROOT.kOrange+7,               texName="tZq",                                directory=directories['TZQ'])
rare            = Sample.fromDirectory(name="rare",             treeName="Events", isData=False, color=color.rare,              texName="rare",                                 directory=directories['rare'])
#DY_LO           = Sample.fromDirectory(name="DY_LO",            treeName="Events", isData=False, color=color.DY,                texName="DY (LO)",                              directory=directories['DY_LO'])
nonprompt       = Sample.fromDirectory(name="nonprompt",        treeName="Events", isData=False, color=color.nonprompt,         texName="nonprompt",                            directory=directories['nonprompt'])
TTLep_pow       = Sample.fromDirectory(name="TTLep_pow",        treeName="Events", isData=False, color=color.TTJets,         texName="t#bar{t}(2l)",                            directory=directories['TTLep_pow'])
background      = Sample.fromDirectory(name="background",        treeName="Events", isData=False, color=color.nonprompt,         texName="background",                            directory=directories['background'])
