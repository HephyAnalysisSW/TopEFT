#!/bin/sh

### Fall 17 MC ###
# TTZ
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTZToLLNuNu_amc  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTZToLLNuNu_amc_psw  #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTZ_LO  #SPLIT20

# WZ
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample WZTo3LNu_fxfx  #SPLIT20

# TTW, TZQ and TTX backgrounds
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTWToLNu_fxfx  #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTHnobb_pow  #SPLIT20
# twll
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TZQToLL   #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTGJets      #SPLIT20
#python cmgPostProcessing.py --overwrite  --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTTT  #SPLIT20

# Rare
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample ZZTo4L ZZTo4L_ext #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample ZZZ  #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample WZZ  #SPLIT20
#python cmgPostProcessing.py --overwrite  --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample WWZ  #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample WWW  #SPLIT20
#ZGTo2LG_ext
#WGToLNuG


# Nonprompt
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTLep_pow   #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample T_sch_lep  #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample T_tch  #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TBar_tch  #SPLIT20

python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M50 DYJetsToLL_M50_ext  #SPLIT10
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M50_LO DYJetsToLL_M50_LO_ext   #SPLIT10

python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --LHEHTCut=100 --sample DYJetsToLL_M50_LO DYJetsToLL_M50_LO_ext   #SPLIT10
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M50_HT100to200    #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M50_HT200to400    #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M50_HT400to600    #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M50_HT600to800    #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M50_HT800to1200   #SPLIT20
#python cmgPostProcessing.py --overwrite  --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M50_HT1200to2500  #SPLIT20
python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M50_HT2500toInf   #SPLIT20

## 2017 data 
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleMuon_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleMuon_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleMuon_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleMuon_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleMuon_Run2017F_17Nov2017 #SPLIT20

python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleEG_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleEG_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleEG_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleEG_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DoubleEG_Run2017F_17Nov2017 #SPLIT20

python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MuonEG_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MuonEG_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MuonEG_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MuonEG_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MuonEG_Run2017F_17Nov2017 #SPLIT20

python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleMuon_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleMuon_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleMuon_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleMuon_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleMuon_Run2017F_17Nov2017 #SPLIT20

python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleElectron_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleElectron_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleElectron_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleElectron_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample SingleElectron_Run2017F_17Nov2017 #SPLIT20

#python cmgPostProcessing.py  --skim singlelep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MET_Run2017B_17Nov2017 #SPLIT20
#python cmgPostProcessing.py  --skim singlelep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MET_Run2017C_17Nov2017 #SPLIT20
#python cmgPostProcessing.py  --skim singlelep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MET_Run2017D_17Nov2017 #SPLIT20
#python cmgPostProcessing.py  --skim singlelep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MET_Run2017E_17Nov2017 #SPLIT20
#python cmgPostProcessing.py  --skim singlelep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample MET_Run2017F_17Nov2017 #SPLIT20


## Others
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M10to50_LO  #SPLIT10
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DY1JetsToLL_M50_LO      #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DY1JetsToLL_M50_LO_ext  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DY2JetsToLL_M50_LO      #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DY2JetsToLL_M50_LO_ext  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DY3JetsToLL_M50_LO      #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DY4JetsToLL_M50_LO      #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M4to50_HT70to100   #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M4to50_HT100to200  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M4to50_HT200to400  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M4to50_HT400to600  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample DYJetsToLL_M4to50_HT600toInf  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTJets  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTLep_pow   #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTHad_pow   #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTSemi_pow  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTLep_pow_TuneDown   #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTLep_pow_TuneUp     #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTLep_pow_hdampDown  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTLep_pow_hdampUp    #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample T_tWch_noFullyHad     #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TBar_tWch_noFullyHad  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTW_LO  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTZToLLNuNu_m1to10   #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTH_pow   #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTHnobb_fxfx  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTHtautau_pow  #SPLIT20
##python cmgPostProcessing.py --overwrite  --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTWH  #SPLIT20
##python cmgPostProcessing.py --overwrite  --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTZH  #SPLIT20
##python cmgPostProcessing.py --overwrite  --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTWW  #SPLIT20
##python cmgPostProcessing.py --overwrite  --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTHH  #SPLIT20
##python cmgPostProcessing.py --overwrite  --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTTJ  #SPLIT20
##python cmgPostProcessing.py --overwrite  --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample TTTW  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample WWTo2L2Nu  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample WW_DPS  #SPLIT20
#python cmgPostProcessing.py --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_mva_v2 --sample ZZTo2L2Nu  #SPLIT20
