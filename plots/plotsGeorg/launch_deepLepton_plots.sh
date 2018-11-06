#!/bin/sh

##Gird
#voms-proxy-init -voms cms -out ~/private/.proxy
#export X509_USER_PROXY=~/private/.proxy
#submitBatch.py --dpm launch_deepLepton_plots.sh

#######
#muons#
#######

#TESTDATA
#stacked classes
python -i stacked_classes_DL.py    --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full

#roc curves
python -i roc_compared_DLvsMVAs.py --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full

#binned pt plots
python -i roc_binned_DLvsMVAs.py   --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full --eBbins 50 --binned pt
python -i roc_binned_DLvsMVAs.py   --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full --eBbins 50 --binned eta
python -i roc_binned_DLvsMVAs.py   --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full --eBbins 50 --binned nTrueInt

#TRAINDATA
#stacked classes
python -i stacked_classes_DL.py    --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 0 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full

#roc curves
python -i roc_compared_DLvsMVAs.py --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 0 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full

#binned pt plots
python -i roc_binned_DLvsMVAs.py   --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 0 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full --eBbins 50 --binned pt
python -i roc_binned_DLvsMVAs.py   --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 0 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full --eBbins 50 --binned eta
python -i roc_binned_DLvsMVAs.py   --version v3 --year 2016 --flavour muo --trainingDate 20181105 --isTestData 0 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted_looseId --trainingType std --sampleSize full --eBbins 50 --binned nTrueInt

###########
#electrons#
###########

##stacked classes
#python -i stacked_classes_DL.py    --version v1 --year 2016 --flavour ele --trainingDate 20181022 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYVsQCD_PFandSVSorted --trainingType std --sampleSize full
#
##roc curves
#python -i roc_compared_DLvsMVAs.py --version v1 --year 2016 --flavour ele --trainingDate 20181022 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYVsQCD_PFandSVSorted --trainingType std --sampleSize full
#
##binned pt plots
#python -i roc_binned_DLvsMVAs.py   --version v1 --year 2016 --flavour ele --trainingDate 20181022 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYVsQCD_PFandSVSorted --trainingType std --sampleSize full --eBbins 50 --binned pt
#python -i roc_binned_DLvsMVAs.py   --version v1 --year 2016 --flavour ele --trainingDate 20181022 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYVsQCD_PFandSVSorted --trainingType std --sampleSize full --eBbins 50 --binned eta
#python -i roc_binned_DLvsMVAs.py   --version v1 --year 2016 --flavour ele --trainingDate 20181022 --isTestData 1 --ptSelection pt_15_to_inf --sampleSelection DYVsQCD_PFandSVSorted --trainingType std --sampleSize full --eBbins 50 --binned nTrueInt


