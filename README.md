# TopEFT
Repository for work on top quark coupling measurements

## Installation

```
cmsrel CMSSW_8_0_28
cd CMSSW_8_0_28/src
cmsenv
git cms-init
git clone https://github.com/danbarto/TopEFT
./TopEFT/setup80X.sh
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

