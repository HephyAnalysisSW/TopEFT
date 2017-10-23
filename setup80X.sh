# 
# Recipe to continue the setup of our 80X analysis after the checkout of TopEFT package
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
git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git -f -t heppy_80X
cp $CMSSW_BASE/src/TopEFT/.sparse-checkout $CMSSW_BASE/src/.git/info/sparse-checkout
git checkout -b heppy_80X cmg-central/heppy_80X

# add your mirror, and push the 80X branch to it
git remote add origin git@github.com:GhentAnalysis/cmg-cmssw.git
git push -u origin heppy_80X

# now get the CMGTools subsystem from the cmgtools-lite repository
git clone -o cmg-central https://github.com/CERN-PH-CMG/cmgtools-lite.git -b 80X CMGTools
cd CMGTools 

# add your fork, and push the 80X branch to it
git remote add origin git@github.com:GhentAnalysis/cmgtools-lite.git 
git fetch origin
git push -u origin 80X_StopsDilepton

cd $CMSSW_BASE/src
#add the repository with the updated Egamma package
git cms-merge-topic cms-egamma:EGM_gain_v1
cd EgammaAnalysis/ElectronTools/data
# download the txt files with the corrections
git clone https://github.com/ECALELFS/ScalesSmearings.git
git checkout Moriond17_23Jan_v2

cd $CMSSW_BASE/src
git fetch origin
git checkout -b 80X_StopsDilepton origin/80X_StopsDilepton

#compile
cd $CMSSW_BASE/src && scram b -j 8 
