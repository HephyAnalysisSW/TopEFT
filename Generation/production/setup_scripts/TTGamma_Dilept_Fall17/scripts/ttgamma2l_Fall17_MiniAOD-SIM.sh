#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_9_4_4/src ] ; then 
 echo release CMSSW_9_4_4 already exists
else
scram p CMSSW CMSSW_9_4_4
fi
cd CMSSW_9_4_4/src
eval `scram runtime -sh`


scram b
cd ../../
cmsDriver.py step1 --fileout file:TOP-RunIIFall17MiniAOD-00189.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mc2017_realistic_v11 --step PAT --nThreads 8 --era Run2_2017 --python_filename TOP-RunIIFall17MiniAOD-00189_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 4800 || exit $? ; 


