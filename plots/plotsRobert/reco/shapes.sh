#!/bin/sh

#python shapes.py --normalizeBSM --onlyTTZ --signal=currentEllipsis &
python shapes.py --normalizeBSM --onlyTTZ --signal=dipoleEllipsis &
#python shapes.py --normalizeBSM --onlyTTZ --signal=C2VA0p2 &
#python shapes.py --normalizeBSM --onlyTTZ --signal=cuW &
#python shapes.py --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=currentEllipsis &
python shapes.py --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=dipoleEllipsis &
#python shapes.py --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=C2VA0p2 &
#python shapes.py --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=cuW &

#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM --onlyTTZ --signal=currentEllipsis &
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM --onlyTTZ --signal=dipoleEllipsis &
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM --onlyTTZ --signal=C2VA0p2 &
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM --onlyTTZ --signal=cuW &
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=currentEllipsis &
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=dipoleEllipsis &
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=C2VA0p2 &
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=cuW &
