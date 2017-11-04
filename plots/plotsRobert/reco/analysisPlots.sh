#!/bin/sh
python analysisPlots.py --plot_directory 80X_v4_dipoleEllipsis --noData --onlyTTZ --signal ewkDM_dipoleEllipsis --selection lepSelTTZ-njet3p-btag1p-onZ &
python analysisPlots.py --plot_directory 80X_v4_currentEllipsis --noData --onlyTTZ --signal ewkDM_currentEllipsis --selection lepSelTTZ-njet3p-btag1p-onZ &

#python analysisPlots.py --plot_directory 80X_v1_SM_ellipse --noData --onlyTTZ --signal ewkDM --selection lepSel-njet3p-btag1p-onZ-ZlldPhiTo1 &
#python analysisPlots.py --plot_directory 80X_v1_SM_ellipse --noData --onlyTTZ --signal ewkDM --selection lepSel-njet3p-btag1p-onZ-ZlldPhi1 &
