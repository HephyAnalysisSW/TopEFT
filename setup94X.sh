# 
# Recipe to continue the setup of our 92X analysis after the checkout of TopEFT package
#
eval `scram runtime -sh`
cd $CMSSW_BASE/src

# 
# X-PAG code for limit
#
#git clone git@github.com:GhentAnalysis/PlotsSMS StopsDilepton/PlotsSMS
git clone git@github.com:GhentAnalysis/RootTools
git clone git@github.com:TTXPheno/TTXPheno
scram b -j9

#
# Setting up CMG
#
git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git -f -t heppy_94X_dev
git remote add origin https://github.com/GhentAnalysis/cmg-cmssw.git -f -t heppy_94X_dev
cp $CMSSW_BASE/src/TopEFT/.sparse-checkout_94X $CMSSW_BASE/src/.git/info/sparse-checkout
git checkout -b heppy_94X_dev origin/heppy_94X_dev

# add your mirror, and push the 92X branch to it
#git remote add origin git@github.com:GhentAnalysis/cmg-cmssw.git
#git checkout -b 92X_dev_StopsDilepton cmg-central/92X_dev_StopsDilepton
#git push -u origin 92X_dev_StopsDilepton

# now get the CMGTools subsystem from the cmgtools-lite repository
git clone -o cmg-central https://github.com/CERN-PH-CMG/cmgtools-lite.git -b 94X_dev CMGTools
cd CMGTools 

# add your fork, and push the 92X branch to it
git remote add origin git@github.com:GhentAnalysis/cmgtools-lite.git -f -t 94X_dev_StopsDilepton 
git checkout -b 94X_dev_StopsDilepton origin/94X_dev_StopsDilepton

# Fall17 EGM MVA -> meanwhile included in 946p1
# https://github.com/CERN-PH-CMG/cmgtools-lite/pull/218
# git remote add cmssw-guitargeek https://github.com/guitargeek/cmssw.git -t ElectronID_MVA2017_940pre3 -f
# git format-patch --stdout 2efa972169e..64030f65aa2 | git apply -
# Comment below because I added the training files under /src for running with crab
#cd $CMSSW_BASE/external/slc6_amd64_gcc630
#git clone https://github.com/lsoffi/RecoEgamma-ElectronIdentification.git data/RecoEgamma/ElectronIdentification/data
#cd data/RecoEgamma/ElectronIdentification/data
#git checkout CMSSW_9_4_0_pre3_TnP

cd $CMSSW_BASE/src
#compile
scram b -j 8 
