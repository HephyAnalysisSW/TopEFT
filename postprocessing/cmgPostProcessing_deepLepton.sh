#!/bin/sh

##########################
### DeepLepton Samples ###
##########################

### Summer 16 MC ###

##TTJets
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample TTJets_DiLepton TTJets_DiLepton_ext #SPLIT135
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample TTJets_SingleLeptonFromTbar TTJets_SingleLeptonFromTbar_ext #SPLIT200  
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample TTJets_SingleLeptonFromT TTJets_SingleLeptonFromT_ext #SPLIT200
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample TTLep_pow #SPLIT50
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample TTSemiLep_pow #SPLIT50
#
###DY
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample DYJetsToLL_M50_LO_ext #SPLIT100
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample DY1JetsToLL_M50_LO #SPLIT50
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample DY2JetsToLL_M50_LO #SPLIT50
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample DY3JetsToLL_M50_LO #SPLIT50
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample DY4JetsToLL_M50_LO #SPLIT50
#
###QCD
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt15to20_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt20to30_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt30to50_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt50to80_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt80to120_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt80to120_Mu5_ext #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt120to170_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt170to300_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt170to300_Mu5_ext #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt300to470_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt300to470_Mu5_ext #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt300to470_Mu5_ext2 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt470to600_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt470to600_Mu5_ext #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt470to600_Mu5_ext2 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt600to800_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt600to800_Mu5_ext #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt800to1000_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt800to1000_Mu5_ext #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt800to1000_Mu5_ext2 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt1000toInf_Mu5 #SPLIT10
##python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample QCD_Pt1000toInf_Mu5_ext #SPLIT10
#
#
#### Data 16 ###
#
##Double Muon
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  DoubleMuon_Run2016B_07Aug17_v2 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  DoubleMuon_Run2016C_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  DoubleMuon_Run2016D_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  DoubleMuon_Run2016E_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  DoubleMuon_Run2016F_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  DoubleMuon_Run2016G_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  DoubleMuon_Run2016H_07Aug17 #SPLIT200
#
##Single Muon
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  SingleMuon_Run2016B_07Aug17_v2 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  SingleMuon_Run2016C_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  SingleMuon_Run2016D_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  SingleMuon_Run2016E_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  SingleMuon_Run2016F_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  SingleMuon_Run2016G_07Aug17 #SPLIT200
python cmgPostProcessing_deepLepton.py --deepLepton --skim singlelep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --processingEra deepLepton_v5 --sample  SingleMuon_Run2016H_07Aug17 #SPLIT200


#####################
### Other Samples ###
#####################

### Summer 16 MC ###
###
##
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50_LO_ext DYJetsToLL_M50_LO_ext2 #SPLIT60
###python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --LHEHTCut=70 --sample  DYJetsToLL_M50_LO_ext DYJetsToLL_M50_LO_ext2 #SPLIT30
###python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50_HT70to100 #SPLIT10
###python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50_HT100to200 DYJetsToLL_M50_HT100to200_ext #SPLIT10
###python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50_HT200to400 DYJetsToLL_M50_HT200to400_ext #SPLIT10
###python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50_HT400to600 DYJetsToLL_M50_HT400to600_ext #SPLIT10
###python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50_HT600to800 #SPLIT10
###python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50_HT800to1200 #SPLIT10
###python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50_HT1200to2500 #SPLIT10
###python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50_HT2500toInf #SPLIT10
###
### Stops trilepton
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample TTZToLLNuNu_m1to10 #SPLIT10
##python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample TTZToQQ #SPLIT10
##python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample VVTo2L2Nu VVTo2L2Nu_ext #SPLIT10
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample WZ WZ_ext #SPLIT10
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample ZZ ZZ_ext #SPLIT10
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample WZTo2L2Q #SPLIT10
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample ZZTo2L2Q #SPLIT10
#
# Others (not used atm, no need to run)
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample VHToNonbb #SPLIT10
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample WWDoubleTo2L #SPLIT10
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample WpWpJJ #SPLIT10
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample WWTo2L2Nu #SPLIT10
#python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite  --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample ZZTo2L2Nu #SPLIT10

##python cmgPostProcessing_deepLepton.py --skim trilep --forceProxy --fileBasedSplitting --overwrite --remakeTTVLeptonMVA --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v21 --sample DYJetsToLL_M50 # SPLIT10
##python cmgPostProcessing_deepLepton.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M10to50_LO # SPLIT10
##python cmgPostProcessing_deepLepton.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M5to50_HT100to200 DYJetsToLL_M5to50_HT100to200_ext #SPLIT10
##python cmgPostProcessing_deepLepton.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M5to50_HT200to400 DYJetsToLL_M5to50_HT200to400_ext #SPLIT10
##python cmgPostProcessing_deepLepton.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M5to50_HT400to600 #SPLIT10
##python cmgPostProcessing_deepLepton.py --skim trilep --year 2016 --keepLHEWeights --processingEra TopEFT_PP_2016_mva_v10 --sample DYJetsToLL_M5to50_HT600toInf DYJetsToLL_M5to50_HT600toInf_ext #SPLIT10
#
##
##
##### 2016 data 
####
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleMuon_Run2016B_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleMuon_Run2016C_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleMuon_Run2016D_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleMuon_Run2016E_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleMuon_Run2016F_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleMuon_Run2016G_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleMuon_Run2016H_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleMuon_Run2016H_03Feb2017_v3 #SPLIT20
###
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016B_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016C_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016D_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016E_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016F_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016G_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016H_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016H_03Feb2017_v3 #SPLIT20
###
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016B_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016C_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016D_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016E_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016F_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016G_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016H_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016H_03Feb2017_v3 #SPLIT20
###
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleMuon_Run2016B_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleMuon_Run2016C_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleMuon_Run2016D_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleMuon_Run2016E_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleMuon_Run2016F_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleMuon_Run2016G_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleMuon_Run2016H_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleMuon_Run2016H_03Feb2017_v3 #SPLIT20
###
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016B_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016C_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016D_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016E_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016F_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016G_03Feb2017 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016H_03Feb2017_v2 #SPLIT20
###python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016H_03Feb2017_v3 #SPLIT20
##
## legacy rereco
#
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016B_07Aug17_v2 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016C_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016D_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016E_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016F_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016G_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  DoubleEG_Run2016H_07Aug17 #SPLIT20
#
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016B_07Aug17_v2 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016C_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016D_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016E_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016F_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016G_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  MuonEG_Run2016H_07Aug17 #SPLIT20
#
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016B_07Aug17_v2 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016C_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016D_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016E_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016F_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016G_07Aug17 #SPLIT20
#python cmgPostProcessing_deepLepton.py  --triggerSelection --forceProxy --remakeTTVLeptonMVA --skim trilep --fileBasedSplitting --overwrite --year 2016 --processingEra TopEFT_PP_2016_mva_v21 --sample  SingleElectron_Run2016H_07Aug17 #SPLIT20
