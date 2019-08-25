# TopEFT
Repository for work on top quark coupling measurements

## Gridpacks:  
  
Code taken from the TTXPheno/gridpacks repository. Cards available there!  
Available gridpacks, pkl files, customize cards and STDOUTs stored at:  
```  
/afs/hephy.at/data/llechner01/TopEFT/gridpacks/<date>/<process>/order<poly order>/  
```  
### 25/09/2018  
2nd order WC gridpacks  
Reference Point: ctZ = 4., ctZI = 4., ctW = 4., ctWI = 4.  
Run cards and proc cards taken from TTGamma_Dilept CMS Analysis
changed to DIM6 model with DIM6 <= 1 for the gamma vertex

| process               | poly order | # coeff | Wilson coefficients  | Link to GEN-SIM events | Link to MiniAOD events |  
|:---------------------:|:----------:|:-------:|:--------------------:|:----------------------:|:----------------------:|  
| ttgamma dilept        | 2          | 4       | ctZ, ctZI, ctW, ctWI |                        |                        |  
| ttgamma semilept t    | 2          | 4       | ctZ, ctZI, ctW, ctWI |                        |                        |  
| ttgamma semilept tbar | 2          | 4       | ctZ, ctZI, ctW, ctWI |                        |                        |  
| ttgamma had           | 2          | 4       | ctZ, ctZI, ctW, ctWI |                        |                        |  


## Installation CMSSW_9_4_X

```
cmsrel CMSSW_9_4_6_patch1
cd CMSSW_9_4_6_patch1/src
cmsenv
git cms-init
git clone https://github.com/danbarto/TopEFT
cd $CMSSW_BASE/src
./TopEFT/setup94X.sh
```

## run.py

Use a gridpack used for central MC production (ttZ01j_5f_MLM_tarball.tar.xz) and replace model relevant information to obtain cross-sections and MC samples for EFT models. The Madgraph tarball contains the customized Higgs Effective Lagrangian (HEL) UFO where first and second generation couplings are disabled.
All masses, couplings and widths are synchronized with the values used in central productions during the creation of the tarball.

Usage
```
run.py --model ewkDM --process ttZ --couplings DC1V 0.5 DC1A 0.5 --makeGridpack --calcXSec
```
The argument to `--couplings` can be a file name with a list of model points.

## TOPAZ
For ifort on lxplus, add these two lines to `.profile`:
```
source /afs/cern.ch/sw/IntelSoftware/linux/x86_64/xe2016/compilers_and_libraries_2016.1.150/linux/bin/ifortvars.sh intel64
source /afs/cern.ch/sw/IntelSoftware/linux/setup.sh
```
Compile on lxplus
```
cd $CMSSW_BASE/src
git clone -b master git@github.com:schoef/TOPAZ
cd $CMSSW_BASE/src/TOPAZ/QCDLoop-1.9/ql
make
cd $CMSSW_BASE/src/TOPAZ/QCDLoop-1.9/ff
make
cd $CMSSW_BASE/src/TOPAZ
make
```
### TOPAZ usage
```
./TOPAZ Collider=13 Correction=0 NLOParam=1 TopDK=4 ZDK=1 ObsSet=53 Process=71 VegasNc0=50000 VegasNc1=500000
./TOPAZ Collider=13 Correction=0 NLOParam=1 TopDK=4 ZDK=1 ObsSet=53 Process=72 VegasNc0=50000 VegasNc1=500000
```

#### command line parameters

  * NLOparam=1 alphaS 1-loop running, LO PDF
  * NLOparam=2 alphaS 2-loop running, NLO PDF

##### TopDK - specify top decay
  * TopDK=0 no top decay
  * TopDK=1 2l decay
  * TopDK=2 fully hadronic
  * TopDK=3 semi leptonic
  * TopDK=4 semi leptonic (3 and 4 give the same answer, i.e. multiply by 2)

##### ZDK - specify Z decays
  * ZDK=0   stable
  * ZDK=1   2l (one lepton generation), i.e. multiply by three

##### ObsSet - Specify cuts & histograms in `mod_Kinematics.f90`
  * ObsSet=52 2l stop decays
  * ObsSet=53 1l stop decays
 
##### Process - Specify the process
  * Process=71 gg-->ttb+Z
  * Process=72 qqb-->ttb+Z

##### BSM parameters
  * RelDelF1V=0.00  C1VZ =   C1VZSM * (1 + RelDelF1V) with C1VZSM =  0.24364
  * RelDelF1A=0.00  C1AZ = - C1AZSM * (1 + RelDelF1A) with C1AZSM =  0.60069
  * RelDelF2V=0.00  C2VZ =   RelDelF2V
  * RelDelF2A=0.00  C2AZ = - RelDelF2A

##### Interface
  * HistoFile=filename
