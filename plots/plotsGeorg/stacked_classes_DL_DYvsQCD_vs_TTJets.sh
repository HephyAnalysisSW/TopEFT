#!/bin/sh

##Gird
#voms-proxy-init -voms cms -out ~/private/.proxy
#export X509_USER_PROXY=~/private/.proxy
#submitBatch.py --dpm launch_deepLepton_plots.sh

#######
#muons#
#######

#TRAINDATA
#stacked classes
python -i stacked_classes_DL_DYvsQCD_vs_TTJets.py --version v4 --year 2016 --flavour muo --trainingDate 2018110801 --isTestData 0 --ptSelection pt_15_-1 --sampleSelection DYvsQCD_balanced --trainingType std --sampleSize full
python -i stacked_classes_DL_DYvsQCD_vs_TTJets.py --version v4 --year 2016 --flavour muo --trainingDate 2018110803 --isTestData 0 --ptSelection pt_15_-1 --sampleSelection TTJets_balanced --trainingType std --sampleSize full


