#lepton2016 samples

python -i splittedLeptonFiles.py  --version v1 --year 2016 --sample TTJets_LO --small --logLevel DEBUG #SPLIT2

#before submitting get grid certificate:
#voms-proxy-init -voms cms -out ~/private/.proxy
#export X509_USER_PROXY=~/private/.proxy

#submit jobs to batch:
#submitBatch.py --dpm splittedLeptonFiles2016.sh

#job status:
#squeue|grep gmoertl

#job log if done/killed:
#vi /afs/hephy.at/work/g/gmoertl/batch_output/batch-test.123456789.out

#display samples names:
#ipython -i splittedLeptonFiles.py -- --year 2016 --sample TTJets --small --logLevel DEBUG
#lepton_heppy_mapper.heppy_sample_names
