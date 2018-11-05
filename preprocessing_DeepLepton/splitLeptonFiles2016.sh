######################
# lepton2016 samples #
######################

#before submitting get grid certificate:
#voms-proxy-init -voms cms -out ~/private/.proxy
#export X509_USER_PROXY=~/private/.proxy

#submit jobs to batch:
#submitBatch.py --dpm splitLeptonFiles2016.sh

#job status:
#squeue|grep gmoertl

#job log if done/killed:
#vi /afs/hephy.at/work/g/gmoertl/batch_output/batch-test.123456789.out

#display samples names:
#ipython -i splitLeptonFiles.py -- --year 2016 --sample TTJets  --logLevel DEBUG
#lepton_heppy_mapper.heppy_sample_names

##small test
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample TTJets_DiLepton #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample TTJets_DiLepton_ext #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromTbar #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromTbar_ext #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromT #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromT_ext #SPLIT2
#
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample DY1JetsToLL_M50_LO #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample DY2JetsToLL_M50_LO #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample DY3JetsToLL_M50_LO #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample DY4JetsToLL_M50_LO #SPLIT2
#
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt15to20_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt20to30_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt30to50_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt50to80_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt80to120_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt80to120_Mu5_ext #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt120to170_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt170to300_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt170to300_Mu5_ext #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt300to470_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt300to470_Mu5_ext #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt300to470_Mu5_ext2 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt470to600_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt470to600_Mu5_ext #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt470to600_Mu5_ext2 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt600to800_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt600to800_Mu5_ext #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5_ext #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5_ext2 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt1000toInf_Mu5 #SPLIT2
#python -i splitLeptonFiles.py  --version v3 --small --year 2016  --logLevel DEBUG --sample QCD_Pt1000toInf_Mu5_ext #SPLIT2

#Lepton 2016 v3 (Oct18 crab jobs processed by Robert)

#DY
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample DY1JetsToLL_M50_LO #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample DY2JetsToLL_M50_LO #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample DY3JetsToLL_M50_LO #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample DY4JetsToLL_M50_LO #SPLIT20
##TTJets Dilepton
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample TTJets_DiLepton #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample TTJets_DiLepton_ext #SPLIT20
##TTJets SingleLepton
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromTbar #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromTbar_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromT #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromT_ext #SPLIT20
##TTTo2L2Nu
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample TTLep_pow #SPLIT20
##TTToSemilepton
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample TTSemiLep_pow #SPLIT20
##QCD
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt15to30 #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt30to50 #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt50to80 #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt80to120 #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt80to120_ext2 #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt120to170 #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt120to170_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt170to300 #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt170to300_ext #SPLIT20
#QCD MuEnriched
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt15to20_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt20to30_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt30to50_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt50to80_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt80to120_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt80to120_Mu5_ext #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt120to170_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt170to300_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt170to300_Mu5_ext #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt300to470_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt300to470_Mu5_ext #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt300to470_Mu5_ext2 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt470to600_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt470to600_Mu5_ext #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt470to600_Mu5_ext2 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt600to800_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt600to800_Mu5_ext #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5_ext #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5_ext2 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt1000toInf_Mu5 #SPLIT20
python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt1000toInf_Mu5_ext #SPLIT20
##QCD EMEnriched
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt20to30_EMEnriched #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt30to50_EMEnriched #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt30to50_EMEnriched_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt50to80_EMEnriched_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt80to120_EMEnriched_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt120to170_EMEnriched #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt170to300_EMEnriched #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt300toInf_EMEnriched #SPLIT20
##QCD bcToE
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt_20to30_bcToE #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt_30to80_bcToE #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt_80to170_bcToE #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt_170to250_bcToE #SPLIT20
#python -i splitLeptonFiles.py  --version v3 --year 2016  --logLevel DEBUG --sample QCD_Pt_250toInf_bcTo #SPLIT20





#old version (Aug18)
#QCD
#EMEnriched
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt20to30_EMEnriched #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt30to50_EMEnriched #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt30to50_EMEnriched_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt50to80_EMEnriched_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt80to120_EMEnriched_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt120to170_EMEnriched #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt170to300_EMEnriched #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt300toInf_EMEnriched #SPLIT20
##bcToE
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt_20to30_bcToE #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt_30to80_bcToE #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt_80to170_bcToE #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt_170to250_bcToE #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt_250toInf_bcToE #SPLIT20
##MuEnriched
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt15to20_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt20to30_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt30to50_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt50to80_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt80to120_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt80to120_Mu5_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt120to170_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt170to300_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt170to300_Mu5_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt300to470_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt300to470_Mu5_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt300to470_Mu5_ext2 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt470to600_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt470to600_Mu5_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt470to600_Mu5_ext2 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt600to800_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt600to800_Mu5_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5_ext #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5_ext2 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt1000toInf_Mu5 #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample QCD_Pt1000toInf_Mu5_ext #SPLIT20
###TT_Jets
###SingleLepton
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromTbar #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromTbar_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromT #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_SingleLeptonFromT_ext #SPLIT20
###Dilepton
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_DiLepton #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_DiLepton_ext #SPLIT20
###other
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_LO #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TT_pow_ext3 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TT_pow #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTLep_pow #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTSemiLep_pow #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_LO_HT600to800_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_LO_HT800to1200_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_LO_HT1200to2500_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample TTJets_LO_HT2500toInf_ext #SPLIT20
##Drell-Yan
###VJets
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M10to50 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M10to50_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M10to50_LO #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_LO_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_LO_ext2 #SPLIT20
##DYNJets
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DY1JetsToLL_M50_LO #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DY2JetsToLL_M50_LO #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DY3JetsToLL_M50_LO #SPLIT20
#python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DY4JetsToLL_M50_LO #SPLIT20
###DYJetsM50HT
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT70to100 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT100to200 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT100to200_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT200to400 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT200to400_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT400to600 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT400to600_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT600toInf #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT600toInf_ext #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT600to800 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT800to1200 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT1200to2500 #SPLIT20
##python -i splitLeptonFiles.py  --version v2 --year 2016  --logLevel DEBUG --sample DYJetsToLL_M50_HT2500toInf #SPLIT20
#

