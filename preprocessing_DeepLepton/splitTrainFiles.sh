#####################
# trainings samples #
#####################

#before submitting get grid certificate:
#voms-proxy-init -voms cms -out ~/private/.proxy
#export X509_USER_PROXY=~/private/.proxy

#submit jobs to batch:
#submitBatch.py --dpm splitTrainFiles.sh

#job status:
#squeue|grep gmoertl

#single jobs
#python -i splitTrainFiles.py --version v3_small --year 2016 --flavour muo --ptSubSelection pt_15_to_inf --sampleSelection TTJets --nJobs 2 --job 0
#python -i splitTrainFiles.py --version v3_small --year 2016 --flavour muo --ptSubSelection pt_15_to_inf --sampleSelection DYvsQCD --nJobs 2 --job 0
#python -i splitTrainFiles.py --version v3_small --year 2016 --flavour muo --ptSubSelection pt_15_to_inf --sampleSelection DY --nJobs 2 --job 0
#python -i splitTrainFiles.py --version v3_small --year 2016 --flavour muo --ptSubSelection pt_15_to_inf --sampleSelection QCD --nJobs 2 --job 0

#full version
#python -i splitTrainFiles.py --version v3 --year 2016 --flavour muo --ptSubSelection pt_15_to_inf --sampleSelection TTJets #SPLIT200
python -i splitTrainFiles.py --version v3 --year 2016 --flavour muo --ptSubSelection pt_15_to_inf --sampleSelection DYvsQCD #SPLIT200

