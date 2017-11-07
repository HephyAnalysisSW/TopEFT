#!/bin/sh
## backgrounds

#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTZToLLNuNu_ext  --overwrite # SPLIT20
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample WZTo3LNu_amcatnlo  --overwrite # SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTWToLNu_ext TTWToLNu_ext2  --overwrite # SPLIT20
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTHnobb_pow  --overwrite # SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample tWll  --overwrite # SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample tZq_ll_ext  --overwrite # SPLIT20
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample ZZTo4L  --overwrite # SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample WZZ  --overwrite # SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample WWZ  --overwrite # SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample ZZZ  --overwrite # SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample ZGTo2LG_ext  --overwrite # SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample WGToLNuG  --overwrite # SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTGJets TTGJets_ext  --overwrite # SPLIT20
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTTT  --overwrite # SPLIT10
#
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTLep_pow --overwrite #SPLIT30
##python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTJets_DiLepton TTJets_DiLepton_ext #SPLIT30
##python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTJets_SingleLeptonFromT TTJets_SingleLeptonFromT_ext #SPLIT30
##python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTJets_SingleLeptonFromTbar TTJets_SingleLeptonFromTbar_ext #SPLIT30
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample GGHZZ4L #SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TGJets TGJets_ext #SPLIT10
##python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTJets_LO #SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample TTZToLLNuNu_m1to10 #SPLIT2
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample VHToNonbb #SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample WWDoubleTo2L #SPLIT10
#python cmgPostProcessing.py --skim trilep --keepLHEWeights --processingEra TopEFT_PP_v10 --sample WpWpJJ #SPLIT10


## signals

python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000  --overwrite
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --sample ewkDM_ttZ_ll  --overwrite

python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_0p050000
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_0p100000
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_0p200000
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_0p300000
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_m0p150000  
python cmgPostProcessing.py --skim trilep --processingEra TopEFT_PP_v10 --keepLHEWeights --overwrite --sample ewkDM_ttZ_ll_noH_DC2V_m0p250000

#
### For fake rate studies?
##python cmgPostProcessing.py --skim trilep --skipSystematicVariations --sample DYJetsToLL_M50  --overwrite # SPLIT20
##python cmgPostProcessing.py --skim trilep --skipSystematicVariations --sample TTJets  --overwrite # SPLIT20
##python cmgPostProcessing.py --skim trilep --skipSystematicVariations --sample   --overwrite # SPLIT10

