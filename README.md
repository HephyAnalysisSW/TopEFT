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
