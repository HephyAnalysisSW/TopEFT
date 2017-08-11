#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530

cmsDriver.py step1 --fileout file:SUS-RunIISummer16MiniAODv2-00088.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --nThreads 4 --era Run2_2016 --python_filename SUS-RunIISummer16MiniAODv2-00088_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2880 || exit $? ;
