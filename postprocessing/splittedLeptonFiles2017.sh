######################
# lepton2017 samples #
######################

#before submitting get grid certificate:
#voms-proxy-init -voms cms -out ~/private/.proxy
#export X509_USER_PROXY=~/private/.proxy

#submit jobs to batch:
#submitBatch.py --dpm splittedLeptonFiles2017.sh

#job status:
#squeue|grep gmoertl

#job log if done/killed:
#vi /afs/hephy.at/work/g/gmoertl/batch_output/batch-test.123456789.out

#display samples names:
#ipython -i splittedLeptonFiles.py -- --year 2017 --sample TTJets  --logLevel DEBUG
#lepton_heppy_mapper.heppy_sample_names


#QCD
#EMEnriched
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt15to20_EMEnriched #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt20to30_EMEnriched #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt30to50_EMEnriched #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt50to80_EMEnriched #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt80to120_EMEnriched #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt120to170_EMEnriched #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt170to300_EMEnriched #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt300toInf_EMEnriched #SPLIT20
#bcToE
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt15to20_bcToE #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt20to30_bcToE #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt30to80_bcToE #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt80to170_bcToE #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt170to250_bcToE #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt250toInf_bcToE #SPLIT20
#MuEnriched
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt15to20_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt20to30_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt30to50_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt50to80_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt80to120_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt120to170_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt170to300_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt300to470_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt470to600_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt600to800_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt800to1000_Mu5 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample QCD_Pt1000toInf_Mu5 #SPLIT20
#TT_Jets
#TTs
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample TTJets #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample TTLep_pow #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample TTHad_pow #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample TTSemi_pow #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample TTJets_SingleLeptonFromT #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample TTLep_pow_TuneDown #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample TTLep_pow_TuneUp #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample TTLep_pow_hdampDown #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample TTLep_pow_hdampUp #SPLIT20
#Drell-Yan
#DYJets
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_ext #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_LO #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_LO_ext #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M10to50_LO #SPLIT20
#DYNJetsToLL
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DY1JetsToLL_M50_LO #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DY1JetsToLL_M50_LO_ext #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DY2JetsToLL_M50_LO #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DY2JetsToLL_M50_LO_ext #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DY3JetsToLL_M50_LO #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DY3JetsToLL_M50_LO_ext #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DY4JetsToLL_M50_LO #SPLIT20
#DYJetsToLLM50HT
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT100to200 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT100to200_ext1 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT200to400 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT200to400_ext1 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT400to600 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT400to600_ext1 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT600to800 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT800to1200 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT1200to2500 #SPLIT20
python -i splittedLeptonFiles.py  --version v1 --year 2017  --logLevel DEBUG --sample DYJetsToLL_M50_HT2500toInf #SPLIT20

