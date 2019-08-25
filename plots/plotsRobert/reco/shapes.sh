#!/bin/sh

python shapes.py 
python shapes.py --normalizeBSM  
python shapes.py --reweightPtZToSM --normalizeBSM  
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --normalizeBSM  
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --reweightPtZToSM --normalizeBSM  
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --normalizeBSM  
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --reweightPtZToSM --normalizeBSM  
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --normalizeBSM  
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --reweightPtZToSM --normalizeBSM  
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM  
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM  

python shapes.py  --background=OnltTTZ --signal=currentEllipsis
python shapes.py  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py  --background=OnltTTZ --signal=C2VA0p2
python shapes.py  --background=OnltTTZ --signal=cuW

python shapes.py --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --normalizeBSM  --background=OnltTTZ --signal=cuW
python shapes.py --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=cuW

python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --normalizeBSM  --background=OnltTTZ --signal=cuW
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=cuW

python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --normalizeBSM  --background=OnltTTZ --signal=cuW
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=cuW

python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --normalizeBSM  --background=OnltTTZ --signal=cuW
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=cuW

python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM  --background=OnltTTZ --signal=cuW
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=currentEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=dipoleEllipsis
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=C2VA0p2
python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM  --background=OnltTTZ --signal=cuW
