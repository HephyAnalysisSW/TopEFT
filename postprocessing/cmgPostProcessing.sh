#!/bin/sh

# 2016 backgrounds
#
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTZToLLNuNu_ext # SPLIT20
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample WZTo3LNu_amcatnlo # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTWToLNu_ext TTWToLNu_ext2 # SPLIT20
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTHnobb_pow # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample tWll # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample tZq_ll_ext # SPLIT20
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample ZZTo4L # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample WZZ # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample WWZ # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample ZZZ # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample ZGTo2LG_ext # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample WGToLNuG # SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTGJets TTGJets_ext # SPLIT20
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTTT # SPLIT10
#
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTLep_pow #SPLIT40
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample GGHZZ4L #SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TGJets TGJets_ext #SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTZToLLNuNu_m1to10 #SPLIT2
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample VHToNonbb #SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample WWDoubleTo2L #SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample WpWpJJ #SPLIT10
#python cmgPostProcessing.py --skim dilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTZ_LO #SPLIT10
#
### optional
#python cmgPostProcessing.py --skim trilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTJets_DiLepton TTJets_DiLepton_ext #SPLIT30
#python cmgPostProcessing.py --skim trilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTJets_trileptonFromT TTJets_trileptonFromT_ext #SPLIT30
#python cmgPostProcessing.py --skim trilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTJets_trileptonFromTbar TTJets_trileptonFromTbar_ext #SPLIT30
#python cmgPostProcessing.py --skim trilep --keepAllJets --keepLHEWeights --processingEra TopEFT_PP_v14 --sample TTJets_LO #SPLIT10

# 2016 signals
#
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll

#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_noH
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_noH_DC2V_0p050000
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_noH_DC2V_0p100000
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_noH_DC2V_0p200000
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_noH_DC2V_0p300000
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_noH_DC2V_m0p150000  
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ewkDM_ttZ_ll_noH_DC2V_m0p250000

#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v11 --keepLHEWeights --sample ewkDM_TTZToLL_LO #SPLIT4
#python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v11 --keepLHEWeights --sample ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2 #SPLIT4


#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC2A_0p200000_DC2V_0p200000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p500000_DC1V_0p500000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_1p000000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000 # SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_cuW_0p100000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_cuW_0p200000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_cuW_0p300000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_cuW_m0p100000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_cuW_m0p200000 #SPLIT10
#python cmgPostProcessing.py --skim inclusive --processingEra TopEFT_PP_v14 --keepLHEWeights --sample ttZ0j_ll_cuW_m0p300000 #SPLIT10
#
# 2016 MC For fake rate studies?
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample DYJetsToLL_M50 # SPLIT20
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample DYJetsToLL_M10to50_LO # SPLIT20
#python cmgPostProcessing.py --skim dilep --processingEra TopEFT_PP_v14 --keepLHEWeights --sample DYJetsToLL_M50_LO_ext # SPLIT20
##python cmgPostProcessing.py --skim trilep --skipSystematicVariations --sample TTJets # SPLIT20
##python cmgPostProcessing.py --skim trilep --skipSystematicVariations --sample  # SPLIT10

# 2016 data
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection mu --sample  SingleMuon_Run2016B_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection mu --sample  SingleMuon_Run2016C_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection mu --sample  SingleMuon_Run2016D_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection mu --sample  SingleMuon_Run2016E_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection mu --sample  SingleMuon_Run2016F_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection mu --sample  SingleMuon_Run2016G_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection mu --sample  SingleMuon_Run2016H_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection mu --sample  SingleMuon_Run2016H_03Feb2017_v3 #SPLIT10
##
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e --sample  SingleElectron_Run2016B_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e --sample  SingleElectron_Run2016C_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e --sample  SingleElectron_Run2016D_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e --sample  SingleElectron_Run2016E_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e --sample  SingleElectron_Run2016F_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e --sample  SingleElectron_Run2016G_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e --sample  SingleElectron_Run2016H_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e --sample  SingleElectron_Run2016H_03Feb2017_v3 #SPLIT10
#
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e_for_mu --sample  SingleElectron_Run2016B_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e_for_mu --sample  SingleElectron_Run2016C_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e_for_mu --sample  SingleElectron_Run2016D_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e_for_mu --sample  SingleElectron_Run2016E_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e_for_mu --sample  SingleElectron_Run2016F_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e_for_mu --sample  SingleElectron_Run2016G_03Feb2017 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e_for_mu --sample  SingleElectron_Run2016H_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py --overwrite  --skim dilep --processingEra TopEFT_PP_v14 --triggerSelection e_for_mu --sample  SingleElectron_Run2016H_03Feb2017_v3 #SPLIT10

# 2017 dilepton data 

#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleMuon_Run2016B_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleMuon_Run2016C_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleMuon_Run2016D_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleMuon_Run2016E_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleMuon_Run2016F_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleMuon_Run2016G_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleMuon_Run2016H_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleMuon_Run2016H_03Feb2017_v3 #SPLIT10
#
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleEG_Run2016B_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleEG_Run2016C_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleEG_Run2016D_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleEG_Run2016E_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleEG_Run2016F_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleEG_Run2016G_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleEG_Run2016H_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  DoubleEG_Run2016H_03Feb2017_v3 #SPLIT10

#python cmgPostProcessing.py  --skim dilep --processingEra TopEFT_PP_v14 --sample  MuonEG_Run2016B_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py  --skim dilep --processingEra TopEFT_PP_v14 --sample  MuonEG_Run2016C_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim dilep --processingEra TopEFT_PP_v14 --sample  MuonEG_Run2016D_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim dilep --processingEra TopEFT_PP_v14 --sample  MuonEG_Run2016E_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim dilep --processingEra TopEFT_PP_v14 --sample  MuonEG_Run2016F_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim dilep --processingEra TopEFT_PP_v14 --sample  MuonEG_Run2016G_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim dilep --processingEra TopEFT_PP_v14 --sample  MuonEG_Run2016H_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py  --skim dilep --processingEra TopEFT_PP_v14 --sample  MuonEG_Run2016H_03Feb2017_v3 #SPLIT10

## 2017 single lepton data
#
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017B_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017C_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017Cv2 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017D #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017E #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017F #SPLIT10
#
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017B_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017C_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017Cv2 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017D #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017E #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017F #SPLIT10
#
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017B_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017C_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017Cv2 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017D #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017E #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017F #SPLIT10
#
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017B_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017C_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017Cv2 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017D #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017E #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection mu --sample SingleMuon_Run2017F #SPLIT10
#
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017B_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017C_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017Cv2 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017D #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017E #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e --sample SingleElectron_Run2017F #SPLIT10
#
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017B_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017C_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017Cv2 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017D #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017E #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --triggerSelection e_for_mu --sample SingleElectron_Run2017F #SPLIT10
#
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample MET_Run2017B_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample MET_Run2017C_12Sep2017 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample MET_Run2017Cv2 #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample MET_Run2017D #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample MET_Run2017E #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample MET_Run2017F #SPLIT10

python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleMuon_Run2017B_12Sep2017 #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleMuon_Run2017C_12Sep2017 #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleMuon_Run2017Cv2 #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleMuon_Run2017D #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleMuon_Run2017E #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleMuon_Run2017F #SPLIT10

python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleElectron_Run2017B_12Sep2017 #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleElectron_Run2017C_12Sep2017 #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleElectron_Run2017Cv2 #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleElectron_Run2017D #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleElectron_Run2017E #SPLIT10
python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample SingleElectron_Run2017F #SPLIT10


# 2017 MC
#
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample TT_pow #SPLIT30
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample DYJetsToLL_M10to50_LO #SPLIT20
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample DYJetsToLL_M50_LO_ext #SPLIT20
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample WW #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample WZ #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim trilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample ZZ #SPLIT10
#
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample TT_pow #SPLIT30
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample DYJetsToLL_M10to50_LO #SPLIT20
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample DYJetsToLL_M50_LO_ext #SPLIT20
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample WW #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample WZ #SPLIT10
#python cmgPostProcessing.py  --overwrite --skim dilep --year 2017 --processingEra TopEFT_PP_2017_v19 --sample ZZ #SPLIT10

#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  MET_Run2016B_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  MET_Run2016C_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  MET_Run2016D_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  MET_Run2016E_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  MET_Run2016F_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  MET_Run2016G_03Feb2017 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  MET_Run2016H_03Feb2017_v2 #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample  MET_Run2016H_03Feb2017_v3 #SPLIT10


#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample WJetsToLNu #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample WJetsToLNu_LO #SPLIT10
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample WJetsToLNu
#python cmgPostProcessing.py  --skim trilep --processingEra TopEFT_PP_v14 --sample WJetsToLNu_LO
