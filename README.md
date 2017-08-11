# TopEFT
Repository for work on top quark coupling measurements

Use a gridpack used for central MC production (ttZ01j_5f_MLM_tarball.tar.xz) and replace model relevant information to obtain cross-sections and MC samples for EFT models. The Madgraph tarball contains the customized Higgs Effective Lagrangian (HEL) UFO where first and second generation couplings are disabled.
All masses, couplings and widths are synchronized with the values used in central productions.

Prepare a gridpack with gencode/test.py

Cross sections are reported, gridpacks stored in gencode/data/gridpacks
Automatic launch of production on crab is work in progress.
A miniAOD sample with 10k events and new coupling (Higgs Effective Lagrangian model) of cuW = 0.051 (x-sec of 1.539 pb) has been produced:

RAWSIM:
```
/topEFT_signal_LHEGEN/dspitzba-topEFT_signal_LHEGEN-ttZ_HEL_UFO_cuw_0p051-08082017_RAWSIMoutput-dfca6a65821676e7cd825fbf500930f3/USER
```
DIGI:
```
/topEFT_signal_LHEGEN/dspitzba-topEFT_signal_LHEGEN-ttZ_HEL_UFO_cuw_0p051_DIGI-08082017-19898e58c9c00509372f15bcc801ecbe/USER
```
RECO:
```
/topEFT_signal_LHEGEN/dspitzba-topEFT_signal_LHEGEN-ttZ_HEL_UFO_cuw_0p051_RECO-08082017-0f111def6b9b94823916592fdafc5ec9/USER
```
miniAOD:
```
/topEFT_signal_LHEGEN/dspitzba-topEFT_signal_LHEGEN-ttZ_HEL_UFO_cuw_0p051_MAOD-08082017-28028af67189b3de7224b79195bd0e1d/USER
```
