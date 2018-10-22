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
#python -i splitTrainFiles.py --version v1_small --year 2016 --flavour ele --ptSubSelection pt_25_to_inf --nJobs 60 --job 10

#python -i splitTrainFiles.py --version v1_small --year 2016 --flavour ele --ptSubSelection pt_15_to_inf  --nJobs 60 --job 0

#full version
#python -i splitTrainFiles.py --version v1 --year 2016 --flavour muo --ptSubSelection pt_15_to_inf #SPLIT60
python -i splitTrainFiles.py --version v1 --year 2016 --flavour ele --ptSubSelection pt_15_to_inf #SPLIT60


