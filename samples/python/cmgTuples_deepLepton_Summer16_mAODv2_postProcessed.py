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
  postProcessing_directory = "deepLepton_v1/inclusive"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}
#TTJets
dirs['TTJets_DiLepton']     = ["TTJets_DiLepton"]
dirs['TTJets_SingleLepton'] = ["TTJets_SingleLeptonFromT", "TTJets_SingleLeptonFromTbar"]
##DYvsQCD
#dirs['DY']                  = ["DY1JetsToLL_M50_LO", "DY2JetsToLL_M50_LO", "DY3JetsToLL_M50_LO", "DY4JetsToLL_M50_LO"]
#dirs['QCD']                 = ["QCD_Pt1000toInf_Mu5", "QCD_Pt1000toInf_Mu5_ext", "QCD_Pt120to170_Mu5", "QCD_Pt15to20_Mu5", 
#                               "QCD_Pt170to300_Mu5", "QCD_Pt170to300_Mu5_ext", "QCD_Pt20to30_Mu5", "QCD_Pt300to470_Mu5", 
#                               "QCD_Pt300to470_Mu5_ext", "QCD_Pt300to470_Mu5_ext2", "QCD_Pt30to50_Mu5", "QCD_Pt470to600_Mu5", 
#                               "QCD_Pt470to600_Mu5_ext", "QCD_Pt470to600_Mu5_ext2", "QCD_Pt50to80_Mu5", "QCD_Pt600to800_Mu5", 
#                               "QCD_Pt600to800_Mu5_ext", "QCD_Pt800to1000_Mu5", "QCD_Pt800to1000_Mu5_ext", "QCD_Pt800to1000_Mu5_ext2", 
#                               "QCD_Pt80to120_Mu5", "QCD_Pt80to120_Mu5_ext"]

#dirs["WZ_amcatnlo"]     = ["WZTo3LNu_amcatnlo"]#, "WZTo2L2Q"]
#dirs["WZ_powheg"]       = ["WZTo3LNu_comb"]#, "WZTo2L2Q"]
#dirs["WZ_mllmin01"]     = ["WZTo3LNu_mllmin01", "WZTo2L2Q"]
#dirs['TTG']             = ["TTGJets_comb"]
#dirs['TTW']             = ["TTWToLNu_ext_comb"]
#dirs['TTH']             = ["TTHnobb_pow"]
#dirs['TTX']             = ["TTTT", "tWll", "tZq_ll_ext","TTHnobb_pow", "THW", "THQ", "TTWW", "TTWZ", "TTZZ","TTWToLNu_ext_comb","TTZToLLNuNu_m1to10"] # everything except ttZ and t(t)gamma
#dirs['TZQ']             = ["tZq_ll_ext"]
#
#dirs['TTX_all']         = ["TTGJets_comb", "TTHnobb_pow", "TTTT", "tWll", "TTWToLNu_ext_comb","tZq_ll_ext","TTZToLLNuNu_ext_comb"]
#dirs['TTX_noTTG']       = ["TTHnobb_pow", "TTTT", "tWll", "TTWToLNu_ext_comb","tZq_ll_ext","TTZToLLNuNu_ext_comb"]
#
#
#dirs['TTLep_pow']       = ['TTLep_pow']
#dirs['singleTop']       = ['TToLeptons_sch_amcatnlo', 'T_tch_powheg', 'TBar_tch_powheg']

#dirs['DY_HT_LO']        = ['DYJetsToLL_M50_LO_ext_comb_lheHT70','DYJetsToLL_M50_HT70to100', 'DYJetsToLL_M50_HT100to200_comb', 'DYJetsToLL_M50_HT200to400_comb', 'DYJetsToLL_M50_HT400to600_comb', 'DYJetsToLL_M50_HT600to800', 'DYJetsToLL_M50_HT800to1200', 'DYJetsToLL_M50_HT1200to2500', 'DYJetsToLL_M50_HT2500toInf']
#dirs['DY_LO']              = ['DYJetsToLL_M50_LO_ext_comb'] #,'DYJetsToLL_M10to50_LO']

#dirs['nonprompt']       = ['TTLep_pow'] + dirs['DY_LO'] + dirs['singleTop']
#
#dirs['ZZ']              = ['ZZTo4L','GluGluToZZTo2e2mu','GluGluToZZTo4e','GluGluToZZTo4mu','GluGluToZZTo2mu2tau','GluGluToZZTo2e2tau','GGHZZ4L','QQHZZ4L','WmHZZ4L','WpHZZ4L','ZHZZ4LF'] 
#dirs['rare']            = ['WGToLNuG','WZG','WWW', 'WWZ', 'WZZ', 'ZZZ','WWDoubleTo2L']
#dirs['WGToLNuG']        = ['WGToLNuG']
#dirs['ZGTo2LG']         = ['ZGTo2LG_ext']
#dirs['Xgamma']          = ['ZGTo2LG_ext', 'TTGJets_comb', 'TGJets']
#
#dirs['ewkDM_ttZ_ll_noH']            = ["ewkDM_ttZ_ll_noH"]
#

#dirs['background']      = dirs["WZ_amcatnlo"] + dirs['TTW'] + dirs['TTX'] + dirs['TZQ'] + dirs['rare']

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

TTJets_DiLepton      = Sample.fromDirectory(name="TTJets_DiLepton",       treeName="Events", isData=False, color=color.TTJets,        texName="t#bar{t}(2l)",              directory=directories['TTJets_DiLepton'])
TTJets_SingleLepton  = Sample.fromDirectory(name="TTJets_SingleLepton",   treeName="Events", isData=False, color=color.TTJets,        texName="t#bar{t}(2l)",              directory=directories['TTJets_SingleLepton'])
#DY                   = Sample.fromDirectory(name="DY",                    treeName="Events", isData=False, color=color.DY,            texName="DY",                        directory=directories['DY'])
#QCD                  = Sample.fromDirectory(name="QCD",                   treeName="Events", isData=False, color=color.DY,            texName="QCD",                       directory=directories['QCD'])

#TTZtoLLNuNu     = Sample.fromDirectory(name="TTZtoLLNuNu",      treeName="Events", isData=False, color=color.TTZtoLLNuNu,       texName="t#bar{t}Z (l#bar{l}/#nu#bar{#nu})",     directory=directories['TTZtoLLNuNu'])
#TTZ_LO          = Sample.fromDirectory(name="TTZ_LO",           treeName="Events", isData=False, color=color.TTZtoLLNuNu+1,     texName="t#bar{t}Z (LO)",                       directory=directories['TTZ_LO'])
#TTG             = Sample.fromDirectory(name="TTG",              treeName="Events", isData=False, color=color.TTG_signal,        texName="t#bar{t}#gamma",                       directory=directories['TTG'])
#WZ_amcatnlo     = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,                texName="WZ",                                   directory=directories['WZ_amcatnlo'])
#WZ_powheg       = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,                texName="WZ (powheg)",                          directory=directories['WZ_powheg'])
#WZ_mllmin01     = Sample.fromDirectory(name="WZ",               treeName="Events", isData=False, color=color.WZ,                texName="WZ (powheg), M_{ll}>0.1 GeV",          directory=directories['WZ_mllmin01'])
#WJets_LO        = Sample.fromDirectory(name="WJets_LO",         treeName="Events", isData=False, color=color.WJetsToLNu,        texName="W+jets (LO)",                          directory=directories['WJets_LO'])
#WJets           = Sample.fromDirectory(name="WJets",            treeName="Events", isData=False, color=color.WJetsToLNu+2,      texName="W+jets (NLO)",                         directory=directories['WJets'])
#TTH             = Sample.fromDirectory(name="TTH",              treeName="Events", isData=False, color=color.TTH,               texName="t#bar{t}H",                             directory=directories['TTH'])
#TTX             = Sample.fromDirectory(name="TTX",              treeName="Events", isData=False, color=ROOT.kRed-10,            texName="t(t)X",                                directory=directories['TTX'])
#TTX_all         = Sample.fromDirectory(name="TTX_all",          treeName="Events", isData=False, color=ROOT.kRed-10,            texName="t(t)X",                                directory=directories['TTX_all'])
#TTX_noTTG       = Sample.fromDirectory(name="TTX_noTTG",        treeName="Events", isData=False, color=ROOT.kRed-10,            texName="t(t)X",                                directory=directories['TTX_noTTG'])
#TTW             = Sample.fromDirectory(name="TTW",              treeName="Events", isData=False, color=color.TTW,               texName="t#bar{t}W",                             directory=directories['TTW'])
#TZQ             = Sample.fromDirectory(name="TZQ",              treeName="Events", isData=False, color=ROOT.kOrange+7,          texName="tZq",                                  directory=directories['TZQ'])
#ZZ              = Sample.fromDirectory(name="ZZ",               treeName="Events", isData=False, color=color.ZZ,                texName="ZZ",                                   directory=directories['ZZ'])
#rare            = Sample.fromDirectory(name="rare",             treeName="Events", isData=False, color=color.rare,              texName="rare",                                 directory=directories['rare'])
#WGToLNuG        = Sample.fromDirectory(name="WGToLNuG",         treeName="Events", isData=False, color=color.rare,              texName="W#gamma",                               directory=directories['WGToLNuG'])
#ZGTo2LG         = Sample.fromDirectory(name="ZGTo2LG",          treeName="Events", isData=False, color=color.ZG,                texName="Z#gamma",                               directory=directories['ZGTo2LG'])
#Xgamma          = Sample.fromDirectory(name="Xgamma",           treeName="Events", isData=False, color=color.ZG,                texName="X#gamma",                               directory=directories['Xgamma'])
#DY_LO           = Sample.fromDirectory(name="DY_LO",            treeName="Events", isData=False, color=color.DY,                texName="DY (LO)",                              directory=directories['DY_LO'])
#DY_HT_LO        = Sample.fromDirectory(name="DY_HT_LO",         treeName="Events", isData=False, color=ROOT.kBlue+1,            texName="DY HT (LO)",                           directory=directories['DY_HT_LO'])
#nonpromptMC     = Sample.fromDirectory(name="nonprompt",        treeName="Events", isData=False, color=color.nonprompt,         texName="nonprompt (MC)",                       directory=directories['nonprompt'])
#TTLep_pow       = Sample.fromDirectory(name="TTLep_pow",        treeName="Events", isData=False, color=color.TTJets,            texName="t#bar{t}(2l)",                          directory=directories['TTLep_pow'])
#singleTop       = Sample.fromDirectory(name="singleTop",        treeName="Events", isData=False, color=color.singleTop,         texName="t/#bar{t}",                             directory=directories['singleTop'])
#background      = Sample.fromDirectory(name="background",        treeName="Events", isData=False, color=color.nonprompt,        texName="background",                           directory=directories['background'])

## set sample selection strings for the nonprompt and Zgamma sample
#nonpromptMC.setSelectionString('nLeptons_FO_3l_genPrompt<=2')
#ZGTo2LG.setSelectionString('nLeptons_FO_3l_genPrompt>2')

