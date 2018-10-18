#!/bin/sh

# Fall 17 MC ###
### for uncertainties
#python cmgPostProcessing.py --forceProxy   --skim singlelepTiny --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample TTSemi_pow # SPLIT90

#### TTZ
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTZToLLNuNu_amc  #SPLIT30
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTZToLLNuNu_amc_psw  #SPLIT80
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTZToLLNuNu_m1to10 #SPLIT20
##
### WZ
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WZTo3LNu_fxfx  #SPLIT20
##
### TTW, TZQ and TTX backgrounds
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTWToLNu_fxfx  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTHnobb_pow  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TZQToLL   #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTGJets TTGJets_ext      #SPLIT20
#python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTTT  #SPLIT20
#python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTWW #SPLIT10
#python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTWZ #SPLIT10
#python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTZZ #SPLIT10
#python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample THQ #SPLIT10
#python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample THW #SPLIT10
#python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample tWll #SPLIT10
##
### Rare
###python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample ZZTo4L ZZTo4L_ext #SPLIT200
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample ZZTo4L #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample ZZZ  #SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WZZ  #SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WWZ_4F  #SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WWW_4F  #SPLIT10
###ZGTo2LG_ext
###WGToLNuG
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample GluGluToZZTo2e2mu #SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample GluGluToZZTo4e   #SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample GluGluToZZTo4mu  #SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample GluGluToZZTo2e2tau  #SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample GluGluToZZTo2mu2tau  #SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample QQHZZ4L QQHZZ4L_ext #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample GGHZZ4L # SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WpHZZ4L # SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WmHZZ4L WmHZZ4L_ext # SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample ZHZZ4LF ZHZZ4LF_ext # SPLIT10
#
#
#
## Nonprompt
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTLep_pow   #SPLIT60
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample T_sch_lep  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample T_tch  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TBar_tch  #SPLIT20
#
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M50_ext  #SPLIT30
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M50_LO DYJetsToLL_M50_LO_ext   #SPLIT30
#
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --LHEHTCut=100 --sample DYJetsToLL_M50_LO DYJetsToLL_M50_LO_ext   #SPLIT30
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M50_HT100to200 DYJetsToLL_M50_HT100to200_ext1    #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M50_HT200to400 DYJetsToLL_M50_HT200to400_ext1   #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M50_HT400to600 DYJetsToLL_M50_HT400to600_ext1   #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M50_HT600to800    #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M50_HT800to1200   #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M50_HT1200to2500  #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M50_HT2500toInf   #SPLIT20
##
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M10to50_LO #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M4to50_HT100to200 #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M4to50_HT200to400 #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M4to50_HT600toInf #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M4to50_HT70to100 #SPLIT20
##
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTWW  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WWTo2L2Nu #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WWToLNuQQ WWToLNuQQ_ext #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WZG #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WZTo1L1Nu2Q #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample ZZ #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample ZZTo2L2Nu #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample ZZTo4L ZZTo4L_ext #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTH_pow #SPLIT20
##python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTJets #SPLIT20
#
##
##### 2017 data 
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleMuon_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleMuon_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleMuon_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleMuon_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleMuon_Run2017F_17Nov2017 #SPLIT20

python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleEG_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleEG_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleEG_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleEG_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample DoubleEG_Run2017F_17Nov2017 #SPLIT20

python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample MuonEG_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample MuonEG_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample MuonEG_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample MuonEG_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample MuonEG_Run2017F_17Nov2017 #SPLIT20

python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleMuon_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleMuon_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleMuon_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleMuon_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleMuon_Run2017F_17Nov2017 #SPLIT20

python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleElectron_Run2017B_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleElectron_Run2017C_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleElectron_Run2017D_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleElectron_Run2017E_17Nov2017 #SPLIT20
python cmgPostProcessing.py  --triggerSelection --skim trilep --fileBasedSplitting  --year 2017 --processingEra TopEFT_PP_2017_mva_v21 --sample SingleElectron_Run2017F_17Nov2017 #SPLIT20

###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample MET_Run2017B_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample MET_Run2017C_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample MET_Run2017D_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample MET_Run2017E_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample MET_Run2017F_17Nov2017 --keepLHEWeights #SPLIT20
###
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample JetHT_Run2017B_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample JetHT_Run2017C_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample JetHT_Run2017D_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample JetHT_Run2017E_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample JetHT_Run2017F_17Nov2017 --keepLHEWeights #SPLIT20
###
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample HTMHT_Run2017B_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample HTMHT_Run2017C_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample HTMHT_Run2017D_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample HTMHT_Run2017E_17Nov2017 --keepLHEWeights #SPLIT20
###python cmgPostProcessing.py  --skim singlelep --year 2017 --keepLHEWeights --fileBasedSplitting --forceProxy --processingEra TopEFT_PP_2017_mva_v7 --sample HTMHT_Run2017F_17Nov2017 --keepLHEWeights #SPLIT20
###

## Others
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M10to50_LO  #SPLIT10
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DY1JetsToLL_M50_LO      #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DY1JetsToLL_M50_LO_ext  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DY2JetsToLL_M50_LO      #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DY2JetsToLL_M50_LO_ext  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DY3JetsToLL_M50_LO      #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DY4JetsToLL_M50_LO      #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M4to50_HT70to100   #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M4to50_HT100to200  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M4to50_HT200to400  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M4to50_HT400to600  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample DYJetsToLL_M4to50_HT600toInf  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTJets  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTLep_pow   #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTHad_pow   #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTSemi_pow  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTLep_pow_TuneDown   #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTLep_pow_TuneUp     #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTLep_pow_hdampDown  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTLep_pow_hdampUp    #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample T_tWch_noFullyHad     #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TBar_tWch_noFullyHad  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTW_LO  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTZToLLNuNu_m1to10   #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTH_pow   #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTHnobb_fxfx  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTHtautau_pow  #SPLIT20
##python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTWH  #SPLIT20
##python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTZH  #SPLIT20
##python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTWW  #SPLIT20
##python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTHH  #SPLIT20
##python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTTJ  #SPLIT20
##python cmgPostProcessing.py --forceProxy    --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample TTTW  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WWTo2L2Nu  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample WW_DPS  #SPLIT20
#python cmgPostProcessing.py --forceProxy   --skim trilep --fileBasedSplitting  --year 2017 --keepLHEWeights --processingEra TopEFT_PP_2017_mva_v21 --sample ZZTo2L2Nu  #SPLIT20
