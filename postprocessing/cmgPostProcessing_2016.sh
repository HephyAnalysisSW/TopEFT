#!/bin/sh

### Summer 16 MC ###
### TTZ 
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTZToLLNuNu_ext # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTZ_LO #SPLIT10
#
# WZ
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WZTo3LNu_amcatnlo # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WZTo3LNu WZTo3LNu_ext # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WZTo3LNu_mllmin01 #SPLIT10

# TTW, TZQ and TTX backgrounds
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTWToLNu_ext TTWToLNu_ext2 # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTHnobb_pow # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample tWll # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample tZq_ll_ext # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTGJets TTGJets_ext # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTTT # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTZZ # SPLIT2
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTWZ # SPLIT6
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTWW # SPLIT4


# Rare
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample ZZTo4L # SPLIT32
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample ZZZ # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WZZ # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WWZ # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WWW # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample ZGTo2LG_ext # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WGToLNuG # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample GluGluToZZTo2e2mu # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample GluGluToZZTo4e # SPLIT6
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample GluGluToZZTo4mu # SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample GluGluToZZTo2e2tau # SPLIT6
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample GluGluToZZTo2mu2tau # SPLIT10


# Nonprompt
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTLep_pow #SPLIT40
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TToLeptons_sch_amcatnlo #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample T_tch_powheg #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TBar_tch_powheg #SPLIT10
#
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50_LO_ext DYJetsToLL_M50_LO_ext2 #SPLIT60
###python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --LHEHTCut=70 --sample  DYJetsToLL_M50_LO_ext DYJetsToLL_M50_LO_ext2 #SPLIT30
###python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50_HT70to100 #SPLIT10
###python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50_HT100to200 DYJetsToLL_M50_HT100to200_ext #SPLIT10
###python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50_HT200to400 DYJetsToLL_M50_HT200to400_ext #SPLIT10
###python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50_HT400to600 DYJetsToLL_M50_HT400to600_ext #SPLIT10
###python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50_HT600to800 #SPLIT10
###python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50_HT800to1200 #SPLIT10
###python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50_HT1200to2500 #SPLIT10
###python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50_HT2500toInf #SPLIT10
###
## Stops trilepton
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTZToLLNuNu_m1to10 #SPLIT10
#python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TTZToQQ #SPLIT10
#python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample VVTo2L2Nu VVTo2L2Nu_ext #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WZ WZ_ext #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample ZZ ZZ_ext #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WZTo2L2Q #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample ZZTo2L2Q #SPLIT10

# Others (not used atm, no need to run)
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample GGHZZ4L #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample TGJets #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample VHToNonbb #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WWDoubleTo2L #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WpWpJJ #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample WWTo2L2Nu #SPLIT10
python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample ZZTo2L2Nu #SPLIT10

#python cmgPostProcessing.py --skim trilep --forceProxy --fileBasedSplitting --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v18 --sample DYJetsToLL_M50 # SPLIT10
#python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M10to50_LO # SPLIT10
#python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M5to50_HT100to200 DYJetsToLL_M5to50_HT100to200_ext #SPLIT10
#python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M5to50_HT200to400 DYJetsToLL_M5to50_HT200to400_ext #SPLIT10
#python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M5to50_HT400to600 #SPLIT10
#python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M5to50_HT600toInf DYJetsToLL_M5to50_HT600toInf_ext #SPLIT10

##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample TTJets_trilepton TTJets_trilepton_ext #SPLIT30
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample TTJets_SingleLeptonFromT TTJets_SingleLeptonFromT_ext #SPLIT30
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample TTJets_SingleLeptonFromTbar TTJets_SingleLeptonFromTbar_ext #SPLIT30
#
### 2016 0j signals
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC2A_0p200000_DC2V_0p200000 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p500000_DC1V_0p500000 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_1p000000 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000 # SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000 #SPLIT10
##python cmgPostProcessing.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000 #SPLIT10
#
### 2016 MET/JetHT/HTMHT data 
##
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  MET_Run2016B_07Aug17_v2 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  MET_Run2016C_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  MET_Run2016D_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  MET_Run2016E_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  MET_Run2016F_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  MET_Run2016G_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  MET_Run2016H_07Aug17 #SPLIT10
##
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  JetHT_Run2016B_07Aug17_v2 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  JetHT_Run2016C_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  JetHT_Run2016D_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  JetHT_Run2016E_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  JetHT_Run2016F_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  JetHT_Run2016G_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  JetHT_Run2016H_07Aug17 #SPLIT10
##
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  HTMHT_Run2016B_07Aug17_v2 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  HTMHT_Run2016C_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  HTMHT_Run2016D_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  HTMHT_Run2016E_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  HTMHT_Run2016F_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  HTMHT_Run2016G_07Aug17 #SPLIT10
##python cmgPostProcessing.py  --skim singlelep --year 2016 --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2016_mva_v10 --sample  HTMHT_Run2016H_07Aug17 #SPLIT10
#
#
#### 2016 data 
###
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016B_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016C_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016D_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016E_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016F_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016G_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016H_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016H_03Feb2017_v3 #SPLIT20
##
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016B_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016C_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016D_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016E_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016F_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016G_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016H_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016H_03Feb2017_v3 #SPLIT20
##
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016B_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016C_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016D_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016E_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016F_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016G_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016H_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016H_03Feb2017_v3 #SPLIT20
##
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016B_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016C_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016D_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016E_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016F_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016G_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016H_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016H_03Feb2017_v3 #SPLIT20
##
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016B_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016C_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016D_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016E_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016F_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016G_03Feb2017 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016H_03Feb2017_v2 #SPLIT20
##python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016H_03Feb2017_v3 #SPLIT20
#
### legacy rereco
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016B_07Aug17_v2 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016C_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016D_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016E_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016F_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016G_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleMuon_Run2016H_07Aug17 #SPLIT20
#
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016B_07Aug17_v2 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016C_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016D_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016E_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016F_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016G_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  DoubleEG_Run2016H_07Aug17 #SPLIT20
#
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016B_07Aug17_v2 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016C_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016D_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016E_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016F_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016G_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  MuonEG_Run2016H_07Aug17 #SPLIT20
#
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016B_07Aug17_v2 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016C_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016D_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016E_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016F_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016G_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleMuon_Run2016H_07Aug17 #SPLIT20
#
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016B_07Aug17_v2 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016C_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016D_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016E_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016F_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016G_07Aug17 #SPLIT20
#python cmgPostProcessing.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --year 2016 --processingEra TopEFT_PP_2016_mva_v18 --sample  SingleElectron_Run2016H_07Aug17 #SPLIT20


