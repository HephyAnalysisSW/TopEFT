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
cmsDriver.py step1 --fileout file:TOP-RunIIFall17DRPremix-00189_step1.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename TOP-RunIIFall17DRPremix-00189_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 || exit $? ; 

cmsDriver.py step2 --filein file:TOP-RunIIFall17DRPremix-00189_step1.root --fileout file:TOP-RunIIFall17DRPremix-00189.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 8 --era Run2_2017 --python_filename TOP-RunIIFall17DRPremix-00189_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 || exit $? ; 


