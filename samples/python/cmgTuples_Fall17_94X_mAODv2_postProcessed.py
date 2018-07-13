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
  postProcessing_directory = "TopEFT_PP_2017_mva_v9/trilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))


dirs = {}
dirs['TTZtoLLNuNu']     = ["TTZToLLNuNu_amc", "TTZToLLNuNu_m1to10"]

# all inclusive right now
dirs["WZ_amcatnlo"]     = ["WZTo3LNu_fxfx"]

dirs['TTW']             = ["TTWToLNu_fxfx"]
dirs['TTX']             = ["TTGJets_comb","TTTT","TZQToLL"] # TTVV missing. should be minor
dirs['TZQ']             = ["TZQToLL"]
dirs['TTH']             = ["TTHnobb_pow"]


dirs['TTLep_pow']       = ['TTLep_pow']
#dirs['DY']              = ['DYJetsToLL_M50_comb'] #amc@NLO
#dirs['DY_HT_LO']        = ['DYJetsToLL_M50_LO_comb_lheHT100','DYJetsToLL_M50_HT100to200_comb', 'DYJetsToLL_M50_HT200to400_comb', 'DYJetsToLL_M50_HT400to600_ext1', 'DYJetsToLL_M50_HT600to800', 'DYJetsToLL_M50_HT800to1200', 'DYJetsToLL_M50_HT1200to2500', 'DYJetsToLL_M50_HT2500toInf']
dirs['DY_LO']           = ['DYJetsToLL_M50_LO_comb']


dirs['nonprompt']       = ['TTLep_pow', 'DYJetsToLL_M50_LO_comb']
dirs['rare']            = ["WWW_4F", "WWZ_4F", "WZZ","ZZZ", "WWTo2L2Nu"] # not complete yet
dirs['ZZ']              = ["ZZTo4L_comb","GluGluToZZTo2e2mu","GluGluToZZTo4e","GluGluToZZTo4mu","GluGluToZZTo2e2tau","GluGluToZZTo2mu2tau"]

dirs['Zgamma']          = ['DYJetsToLL_M50_ext']

dirs['pseudoData']      = dirs['TTZtoLLNuNu'] + dirs["WZ_amcatnlo"] + dirs['TTW'] + dirs['TTX'] + dirs['TZQ'] + dirs['rare'] + dirs['nonprompt'] + dirs['ZZ']



directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TTZtoLLNuNu_17      = Sample.fromDirectory(name="TTZtoLLNuNu_17",   treeName="Events", isData=False, color=color.TTZtoLLNuNu,       texName="t#bar{t}Z (l#bar{l}/#nu#bar{#nu})",    directory=directories['TTZtoLLNuNu'])
#DY_17               = Sample.fromDirectory(name="DY_17",            treeName="Events", isData=False, color=color.DY,                texName="DY (NLO)",                           directory=directories['DY'])
#DY_HT_LO_17         = Sample.fromDirectory(name="DY_HT_LO_17",      treeName="Events", isData=False, color=color.DY,                texName="DY HT (LO)",                           directory=directories['DY_HT_LO'])
TTX_17              = Sample.fromDirectory(name="TTX_17",           treeName="Events", isData=False, color=color.TTX,               texName="t(t)X",                                directory=directories['TTX'])
TTH_17              = Sample.fromDirectory(name="TTH_17",           treeName="Events", isData=False, color=color.TTH,               texName="t#bar{t}H",                            directory=directories['TTH'])
TTW_17              = Sample.fromDirectory(name="TTW_17",           treeName="Events", isData=False, color=color.TTW,               texName="t#bar{t}W",                            directory=directories['TTW'])
TZQ_17              = Sample.fromDirectory(name="TZQ_17",           treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="tZq",                                  directory=directories['TZQ'])
TTLep_pow_17        = Sample.fromDirectory(name="TTLep_pow_17",     treeName="Events", isData=False, color=color.TTJets,            texName="t#bar{t}",                             directory=directories['TTLep_pow'])
nonpromptMC_17      = Sample.fromDirectory(name="nonprompt_17",     treeName="Events", isData=False, color=color.nonprompt,         texName="nonprompt",                            directory=directories['nonprompt'])
rare_17             = Sample.fromDirectory(name="rare_17",          treeName="Events", isData=False, color=color.rare,              texName="rare",                                 directory=directories['rare'])
WZ_amcatnlo_17      = Sample.fromDirectory(name="WZ_17",            treeName="Events", isData=False, color=color.WZ,                texName="WZ",                                   directory=directories['WZ_amcatnlo'])
pseudoData_17       = Sample.fromDirectory(name="pseudoData_17",    treeName="Events", isData=False, color=ROOT.kBlack,             texName="pseudo-data",                          directory=directories['pseudoData'])
ZZ_17               = Sample.fromDirectory(name="ZZ_17",            treeName="Events", isData=False, color=color.ZZ,                texName="ZZ",                                   directory=directories['ZZ'])
Zgamma_17           = Sample.fromDirectory(name="Zgamma_17",        treeName="Events", isData=False, color=color.ZG,                texName="Z#gamma",                              directory=directories['Zgamma'])

## set sample selection strings for the nonprompt and Zgamma sample
nonpromptMC_17.setSelectionString('nLeptons_FO_3l_genPrompt<=2')
Zgamma_17.setSelectionString('nLeptons_FO_3l_genPrompt>2')
