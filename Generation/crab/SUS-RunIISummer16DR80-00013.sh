#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530

cmsDriver.py step1 --filein "dbs:/topEFT_signal_LHEGEN/dspitzba-topEFT_signal_LHEGEN-ttZ_HEL_UFO_cuw_0p051-08082017_RAWSIMoutput-dfca6a65821676e7cd825fbf500930f3/USER" --fileout file:SUS-RunIISummer16DR80-00013_step1.root --pileup_input "dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer15GS-MCRUN2_71_V1_ext1-v1/GEN-SIM" --mc --eventcontent RAWSIM --pileup 2016_25ns_Moriond17MC_PoissonOOTPU --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGI,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --era Run2_2016 --python_filename SUS-RunIISummer16DR80-00013_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 || exit $? ;

cmsDriver.py step2 --filein file:SUS-RunIISummer16DR80-00013_step1.root --fileout file:SUS-RunIISummer16DR80-00013.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,L1Reco,RECO,EI --nThreads 4 --era Run2_2016 --python_filename SUS-RunIISummer16DR80-00013_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 || exit $? ;

