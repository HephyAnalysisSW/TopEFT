#!/bin/sh

#DeepLepton plots
#plotptSelection='pt_15_to_inf'
#plotsampleSelection='DYvsQCD_sorted'
#plottrainingDate=20181028
#plotflavour='muo'
#plotsampleSize='full'

#######
#muons#
#######

#roc curves
python -i roc_compared_DLvsMVAs.py --version v2 --year 2016 --flavour muo --trainingDate 20181028 --isTestData 99 --ptSelection pt_15_to_inf --sampleSelection DYvsQCD_sorted --trainingType std --sampleSize full --predictionPath /afs/hephy.at/data/gmoertl01/DeepLepton/trainings/muons/roc_testfiles/DYvsQCD/

