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
scram b -j9

#
# Setting up CMG
#
git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git -f -t heppy_92X_dev
cp $CMSSW_BASE/src/TopEFT/.sparse-checkout $CMSSW_BASE/src/.git/info/sparse-checkout
git checkout -b heppy_92X_dev cmg-central/heppy_92X_dev

# add your mirror, and push the 92X branch to it
git remote add origin git@github.com:GhentAnalysis/cmg-cmssw.git
git push -u ghent-cmg-cmssw 92X_dev_StopsDileptonn

# now get the CMGTools subsystem from the cmgtools-lite repository
git clone -o cmg-central https://github.com/CERN-PH-CMG/cmgtools-lite.git -b 92X_dev CMGTools
cd CMGTools 

# add your fork, and push the 92X branch to it
git remote add origin git@github.com:GhentAnalysis/cmgtools-lite.git 
git fetch origin
git checkout -b 92X_dev_StopsDilepton origin/92X_dev_StopsDilepton

#cd $CMSSW_BASE/src
#add the repository with the updated Egamma package
#git cms-merge-topic cms-egamma:EGM_gain_v1
#cd EgammaAnalysis/ElectronTools/data
# download the txt files with the corrections
#git clone https://github.com/ECALELFS/ScalesSmearings.git
#git checkout Moriond17_23Jan_v2

#cd $CMSSW_BASE/src
#git fetch origin
#git checkout -b 80X_StopsDilepton origin/80X_StopsDilepton

## DeepCSV
#cd $CMSSW_BASE/src
#git cms-merge-topic -u mverzett:DeepFlavourCMVA-from-CMSSW_8_0_21
#mkdir RecoBTag/DeepFlavour/data/
#cd RecoBTag/DeepFlavour/data/
#wget http://home.fnal.gov/~verzetti//DeepFlavour/training/DeepFlavourNoSL.json
#wget http://mon.iihe.ac.be/~smoortga/DeepFlavour/CMSSW_implementation_DeepCMVA/Model_DeepCMVA.json

cd $CMSSW_BASE/src
#compile
scram b -j 8 
