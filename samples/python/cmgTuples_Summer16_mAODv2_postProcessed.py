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
  postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}
dirs['TTZtoLLNuNu']     = ["TTZToLLNuNu_ext_comb"]
#dirs['TTZ_LO']          = ["TTZ_LO"]
dirs["WZ_amcatnlo"]     = ["WZTo3LNu_amcatnlo"]#, "WZTo2L2Q"]
dirs["WZ_powheg"]       = ["WZTo3LNu_comb"]#, "WZTo2L2Q"]
#dirs["WZ_mllmin01"]     = ["WZTo3LNu_mllmin01", "WZTo2L2Q"]


dirs['TTG']             = ["TTGJets_comb"]
dirs['TTW']             = ["TTWToLNu_ext_comb"]
dirs['TTH']             = ["TTHnobb_pow"]
dirs['TTX']             = ["TTTT", "tWll", "tZq_ll_ext","TTHnobb_pow", "THW", "THQ", "TTWW", "TTWZ", "TTZZ","TTWToLNu_ext_comb","TTZToLLNuNu_m1to10"] # everything except ttZ and t(t)gamma
dirs['TTWW']            = ['TTWW']
dirs['TTWZ']            = ['TTWZ']
dirs['TTXX']            = ['TTTT', 'TTWW','TTWZ','TTZZ']
dirs['TWZ']             = ['tWll']
dirs['TTXrest']         = ['THW','THQ',"TTZToLLNuNu_m1to10"]
dirs['TZQ']             = ["tZq_ll_ext"]

dirs['TTX_all']         = ["TTGJets_comb", "TTHnobb_pow", "TTTT", "tWll", "TTWToLNu_ext_comb","tZq_ll_ext","TTZToLLNuNu_ext_comb"]
dirs['TTX_noTTG']       = ["TTHnobb_pow", "TTTT", "tWll", "TTWToLNu_ext_comb","tZq_ll_ext","TTZToLLNuNu_ext_comb"]

dirs['TTW']             = ['TTWToLNu_ext_comb']
dirs['TTWW']            = ['TTWW']
dirs['TTWZ']            = ['TTWZ']
dirs['TTX_rare']        = ["TTTT", "tZq_ll_ext","TTHnobb_pow", "THW", "THQ", "TTZZ","TTZToLLNuNu_m1to10"] # everything except ttZ and t(t)gamma
dirs['TTX_rare_TWZ']    = ["TTTT", "TTHnobb_pow", "THW", "THQ", "TTZZ", "TTZToLLNuNu_m1to10"] # same as TTX_rare but without tZq_ll_ext
dirs['TTX_rare_TWZ']    = ["TTTT", "TTHnobb_pow", "THW", "THQ", "TTZZ", "TTZToLLNuNu_m1to10"] # same as TTX_rare but without tZq_ll_ext

dirs['TTLep_pow']       = ['TTLep_pow']
dirs['singleTop']       = ['TToLeptons_sch_amcatnlo', 'T_tch_powheg', 'TBar_tch_powheg']

#dirs['DY_HT_LO']        = ['DYJetsToLL_M50_LO_ext_comb_lheHT70','DYJetsToLL_M50_HT70to100', 'DYJetsToLL_M50_HT100to200_comb', 'DYJetsToLL_M50_HT200to400_comb', 'DYJetsToLL_M50_HT400to600_comb', 'DYJetsToLL_M50_HT600to800', 'DYJetsToLL_M50_HT800to1200', 'DYJetsToLL_M50_HT1200to2500', 'DYJetsToLL_M50_HT2500toInf']
dirs['DY_LO']              = ['DYJetsToLL_M50_LO_ext_comb'] #,'DYJetsToLL_M10to50_LO']
#dirs['DY

dirs['nonprompt_TWZ_3l']    = ['TTLep_pow'] + dirs['DY_LO'] + dirs['singleTop']
dirs['nonprompt_TWZ_4l']    = ['TTLep_pow'] + dirs['DY_LO'] + dirs['singleTop'] + dirs['TZQ'] + dirs["WZ_powheg"] 

dirs['ZZ']              = ['ZZTo4L']#,'GluGluToZZTo2e2mu','GluGluToZZTo4e','GluGluToZZTo4mu','GluGluToZZTo2mu2tau','GluGluToZZTo2e2tau','GGHZZ4L','QQHZZ4L','WmHZZ4L','WpHZZ4L','ZHZZ4LF'] 
#dirs['rare']            = ['WGToLNuG','WZG','WWW', 'WWZ', 'WZZ', 'ZZZ','WWDoubleTo2L']
dirs['rare']            = ['WGToLNuG','WWW', 'WWZ', 'WZZ', 'ZZZ','WWDoubleTo2L'] # without WZG 
dirs['WWZ']             = ['WWZ']
dirs['WZZ']             = ['WZZ']
dirs['ZZZ']             = ['ZZZ']
dirs['WGToLNuG']        = ['WGToLNuG']
dirs['ZGTo2LG']         = ['ZGTo2LG_ext']
dirs['Xgamma']          = ['ZGTo2LG_ext', 'TTGJets_comb', 'TGJets']

dirs['ewkDM_ttZ_ll_noH']            = ["ewkDM_ttZ_ll_noH"]

dirs['TTTT']            = ['TTTT']

dirs['pseudoData']      = dirs['TTZtoLLNuNu'] + dirs["WZ_powheg"] + dirs['TTW'] + dirs['TTX'] + dirs['rare'] + dirs['nonprompt_TWZ_3l'] +dirs['ZZ']
#dirs['pseudoDataPriv']  = dirs['ewkDM_ttZ_ll_noH'] + dirs["WZ"] + dirs['TTW'] + dirs['TTX'] + dirs['TZQ'] + dirs['rare'] + dirs['nonprompt']

dirs['background']      = dirs["WZ_amcatnlo"] + dirs['TTW'] + dirs['TTX'] + dirs['TZQ'] + dirs['rare']

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

pseudoData      = Sample.fromDirectory(name="pseudoData",       treeName="Events", isData=False, color=ROOT.kBlack,             texName="pseudo-data",                          directory=directories['pseudoData'])
#pseudoDataPriv  = Sample.fromDirectory(name="pseudoDataPriv",   treeName="Events", isData=False, color=ROOT.kBlack,            texName="pseudo-data",                           directory=directories['pseudoDataPriv'])
TTZtoLLNuNu     = Sample.fromDirectory(name="TTZtoLLNuNu",      treeName="Events", isData=False, color=color.TTZtoLLNuNu,       texName="t#bar{t}Z (l#bar{l}/#nu#bar{#nu})",     directory=directories['TTZtoLLNuNu'])
#TTZ_LO          = Sample.fromDirectory(name="TTZ_LO",           treeName="Events", isData=False, color=color.TTZtoLLNuNu+1,     texName="t#bar{t}Z (LO)",                       directory=directories['TTZ_LO'])
TTG             = Sample.fromDirectory(name="TTG",              treeName="Events", isData=False, color=color.TTG_signal,        texName="t#bar{t}#gamma",                       directory=directories['TTG'])
WZ_amcatnlo     = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,                texName="WZ",                                   directory=directories['WZ_amcatnlo'])
WZ_powheg       = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,                texName="WZ (powheg)",                          directory=directories['WZ_powheg'])
#WZ_mllmin01     = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,                texName="WZ (powheg), M_{ll}>0.1 GeV",          directory=directories['WZ_mllmin01'])
#WJets_LO        = Sample.fromDirectory(name="WJets_LO",         treeName="Events", isData=False, color=color.WJetsToLNu,        texName="W+jets (LO)",                          directory=directories['WJets_LO'])
#WJets           = Sample.fromDirectory(name="WJets",            treeName="Events", isData=False, color=color.WJetsToLNu+2,      texName="W+jets (NLO)",                         directory=directories['WJets'])
TTH             = Sample.fromDirectory(name="TTH",              treeName="Events", isData=False, color=color.TTH,               texName="t#bar{t}H",                             directory=directories['TTH'])
TTX             = Sample.fromDirectory(name="TTX",              treeName="Events", isData=False, color=ROOT.kRed-10,            texName="t(t)X",                                directory=directories['TTX'])
TTX_all         = Sample.fromDirectory(name="TTX_all",          treeName="Events", isData=False, color=ROOT.kRed-10,            texName="t(t)X",                                directory=directories['TTX_all'])
TTX_noTTG       = Sample.fromDirectory(name="TTX_noTTG",        treeName="Events", isData=False, color=ROOT.kRed-10,            texName="t(t)X",                                directory=directories['TTX_noTTG'])
TTW             = Sample.fromDirectory(name="TTW",              treeName="Events", isData=False, color=color.TTW,               texName="t#bar{t}W",                             directory=directories['TTW'])
TZQ             = Sample.fromDirectory(name="TZQ",              treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="tZq",                                  directory=directories['TZQ'])
#TWZ             = Sample.fromDirectory(name="TWZ",              treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="tWZ",                                  directory=directories['TWZ'])
TWZ             = Sample.fromDirectory(name="TWZ",              treeName="Events", isData=False, color=ROOT.kRed,               texName="tWZ",                                  directory=directories['TWZ'])
TTXX            = Sample.fromDirectory(name="TTXX",             treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="ttXX",                                 directory=directories['TTXX'])
TTX_rest        = Sample.fromDirectory(name="TTX_rest",         treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="ttX rest",                             directory=directories['TTXrest'])

TTW             = Sample.fromDirectory(name="TTW",              treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="TTW",                                  directory=directories['TTW'])
#TTWW            = Sample.fromDirectory(name="TTWW",             treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="TTWW",                                 directory=directories['TTWW'])
TTWW            = Sample.fromDirectory(name="TTWW",             treeName="Events", isData=False, color=ROOT.kRed,               texName="TTWW",                                 directory=directories['TTWW'])
TTWZ            = Sample.fromDirectory(name="TTWZ",             treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="TTWZ",                                 directory=directories['TTWZ'])
TTX_rare        = Sample.fromDirectory(name="TTX_rare",         treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="TTX(rare)",                            directory=directories['TTX_rare'])
TTX_rare_TWZ    = Sample.fromDirectory(name="TTX_rare_TWZ",     treeName="Events", isData=False, color=ROOT.kRed-10,            texName="t#bar{t}+(H/t#bar{t}/VV)",                            directory=directories['TTX_rare_TWZ'])
TTTT            = Sample.fromDirectory(name="TTTT",             treeName="Events", isData=False, color=ROOT.kYellow,            texName="TTTT",                                 directory=directories['TTTT'])

ZZ              = Sample.fromDirectory(name="ZZ",               treeName="Events", isData=False, color=color.ZZ,                texName="ZZ",                                   directory=directories['ZZ'])
rare            = Sample.fromDirectory(name="rare",             treeName="Events", isData=False, color=color.rare,              texName="rare",                                 directory=directories['rare'])
WWZ             = Sample.fromDirectory(name="WWZ",              treeName="Events", isData=False, color=color.rare,              texName="WWZ",                                 directory=directories['WWZ'])
WZZ             = Sample.fromDirectory(name="WZZ",              treeName="Events", isData=False, color=color.rare,              texName="WZZ",                                 directory=directories['WZZ'])
ZZZ             = Sample.fromDirectory(name="ZZZ",              treeName="Events", isData=False, color=color.rare,              texName="ZZZ",                                 directory=directories['ZZZ'])
WGToLNuG        = Sample.fromDirectory(name="WGToLNuG",         treeName="Events", isData=False, color=color.rare,              texName="W#gamma",                               directory=directories['WGToLNuG'])
ZGTo2LG         = Sample.fromDirectory(name="ZGTo2LG",          treeName="Events", isData=False, color=color.ZG,                texName="Z#gamma",                               directory=directories['ZGTo2LG'])
Xgamma          = Sample.fromDirectory(name="Xgamma",           treeName="Events", isData=False, color=color.ZG,                texName="X#gamma",                               directory=directories['Xgamma'])
DY_LO           = Sample.fromDirectory(name="DY_LO",            treeName="Events", isData=False, color=color.DY,                texName="DY (LO)",                              directory=directories['DY_LO'])
#DY_HT_LO        = Sample.fromDirectory(name="DY_HT_LO",         treeName="Events", isData=False, color=ROOT.kBlue+1,            texName="DY HT (LO)",                           directory=directories['DY_HT_LO'])
nonprompt_TWZ_3l= Sample.fromDirectory(name="nonprompt_TWZ_3l", treeName="Events", isData=False, color=color.nonprompt,         texName="non prompt",                           directory=directories['nonprompt_TWZ_3l'])
nonprompt_TWZ_4l= Sample.fromDirectory(name="nonprompt_TWZ_4l", treeName="Events", isData=False, color=color.nonprompt,         texName="non prompt",                           directory=directories['nonprompt_TWZ_4l'])
TTLep_pow       = Sample.fromDirectory(name="TTLep_pow",        treeName="Events", isData=False, color=color.TTJets,            texName="t#bar{t}(2l)",                          directory=directories['TTLep_pow'])
singleTop       = Sample.fromDirectory(name="singleTop",        treeName="Events", isData=False, color=color.singleTop,         texName="t/#bar{t}",                             directory=directories['singleTop'])
background      = Sample.fromDirectory(name="background",       treeName="Events", isData=False, color=color.nonprompt,         texName="background",                           directory=directories['background'])


yt_TWZ_filter   = Sample.fromDirectory(name="yt_TWZ_filter",    treeName="Events", isData=False, color=ROOT.kRed,               texName="TWZ",                                  directory="/afs/hephy.at/data/rschoefbeck01/cmgTuples/TopEFT_PP_2016_mva_v21/dilepTiny/yt_tWZ_filter/")
yt_TWZ          = Sample.fromDirectory(name="yt_TWZ",           treeName="Events", isData=False, color=ROOT.kRed,               texName="TWZ",                                  directory="/afs/hephy.at/data/rschoefbeck01/cmgTuples/TopEFT_PP_2016_mva_v21/dilepTiny/yt_tWZ/")
yt_TZZ          = Sample.fromDirectory(name="yt_TZZ",           treeName="Events", isData=False, color=ROOT.kRed,               texName="TZZ",                                  directory="/afs/hephy.at/data/rschoefbeck01/cmgTuples/TopEFT_PP_2016_mva_v22/dilepTiny/yt_tZZ/")
#yt_TWW          = Sample.fromDirectory(name="yt_TWW",           treeName="Events", isData=False, color=ROOT.kRed,               texName="TWW",                                  directory="/afs/hephy.at/data/rschoefbeck01/cmgTuples/TopEFT_PP_2016_mva_v22/dilepTiny/yt_tWW_0/")
yt_TWW          = Sample.fromDirectory(name="yt_TWW",           treeName="Events", isData=False, color=ROOT.kRed,               texName="TWW",                                  directory="/afs/hephy.at/data/cms04/ttschida/cmgTuples/yt_tWW")
dim6top_TTW     = Sample.fromDirectory(name="dim6top_TTW",      treeName="Events", isData=False, color=ROOT.kYellow,            texName="TTW",                                  directory="/afs/hephy.at/data/rschoefbeck01/cmgTuples/TopEFT_PP_2016_mva_v21/dilepTiny/dim6top_ttW/")
yt_TWZ_filter.reweight_pkl = "/afs/hephy.at/data/cms04/ttschida/gridpacks/tWZ01j_new/tWZ01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.pkl"

## set sample selection strings for the nonprompt and Zgamma sample
#nonpromptMC.setSelectionString('nLeptons_FO_3l_genPrompt<=2')
#ZGTo2LG.setSelectionString('nLeptons_FO_3l_genPrompt>2')

