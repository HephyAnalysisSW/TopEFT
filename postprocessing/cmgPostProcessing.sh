#!/bin/sh
## backgrounds

#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample TTZToLLNuNu_ext # SPLIT20
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample WZTo3LNu_amcatnlo # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample TTWToLNu_ext TTWToLNu_ext2 # SPLIT20
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample TTHnobb_pow # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample tWll # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample tZq_ll_ext # SPLIT20
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample ZZTo4L # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample WZZ # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample WWZ # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample ZZZ # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample ZGTo2LG_ext # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample WGToLNuG # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample TTGJets TTGJets_ext # SPLIT20
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample TTTT # SPLIT10
#
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample TTLep_pow #SPLIT30
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample GGHZZ4L #SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample TGJets TGJets_ext #SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample TTZToLLNuNu_m1to10 #SPLIT2
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample VHToNonbb #SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample WWDoubleTo2L #SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample WpWpJJ #SPLIT10
#
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v12 --sample TTZ_LO #SPLIT10

## optional
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTJets_DiLepton TTJets_DiLepton_ext #SPLIT30
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTJets_SingleLeptonFromT TTJets_SingleLeptonFromT_ext #SPLIT30
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTJets_SingleLeptonFromTbar TTJets_SingleLeptonFromTbar_ext #SPLIT30
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTJets_LO #SPLIT10


## signals

#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000  --overwrite
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll  --overwrite
#
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_0p050000
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_0p100000
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_0p200000
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_0p300000
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_m0p150000  
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_m0p250000

#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v11 --keepLHEWeights --overwrite --sample ewkDM_TTZToLL_LO #SPLIT4
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v11 --keepLHEWeights --overwrite --sample ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2 #SPLIT4


python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC2A_0p200000_DC2V_0p200000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p500000_DC1V_0p500000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_1p000000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000 # SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_cuW_0p100000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_cuW_0p200000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_cuW_0p300000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_cuW_m0p100000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_cuW_m0p200000 #SPLIT10
python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v12 --keepLHEWeights --overwrite --sample ttZ0j_ll_cuW_m0p300000 #SPLIT10
#
### For fake rate studies?
##python cmgPostProcessing.py --skim trilep --skipSystematicVariations --sample DYJetsToLL_M50  --overwrite # SPLIT20
##python cmgPostProcessing.py --skim trilep --skipSystematicVariations --sample TTJets  --overwrite # SPLIT20
##python cmgPostProcessing.py --skim trilep --skipSystematicVariations --sample   --overwrite # SPLIT10

## Data
#python cmgPostProcessing.py  --overwrite --skim singlelep --processingEra TopEFT_PP_v10 --sample MET_Run2016B_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim singlelep --processingEra TopEFT_PP_v10 --sample MET_Run2016C_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim singlelep --processingEra TopEFT_PP_v10 --sample MET_Run2016D_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim singlelep --processingEra TopEFT_PP_v10 --sample MET_Run2016E_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim singlelep --processingEra TopEFT_PP_v10 --sample MET_Run2016F_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim singlelep --processingEra TopEFT_PP_v10 --sample MET_Run2016G_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim singlelep --processingEra TopEFT_PP_v10 --sample MET_Run2016H_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim singlelep --processingEra TopEFT_PP_v10 --sample MET_Run2016H_03Feb2017_v3 #SPLIT10

#python cmgPostProcessing.py --overwrite  --skim singlelep --processingEra TopEFT_PP_v10 --sample WJetsToLNu #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim singlelep --processingEra TopEFT_PP_v10 --sample WJetsToLNu_LO #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim trilep --processingEra TopEFT_PP_v10 --sample WJetsToLNu
#python cmgPostProcessing.py --overwrite  --skim trilep --processingEra TopEFT_PP_v10 --sample WJetsToLNu_LO
