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

#python shapes.py --onlyTTZ --signal=currentEllipsis
#python shapes.py --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --onlyTTZ --signal=C2VA0p2
#python shapes.py --onlyTTZ --signal=cuW
#
#python shapes.py --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --normalizeBSM --onlyTTZ --signal=cuW
#python shapes.py --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=cuW
#
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --normalizeBSM --onlyTTZ --signal=cuW
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt0To100 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=cuW
#
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --normalizeBSM --onlyTTZ --signal=cuW
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=cuW
#
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --normalizeBSM --onlyTTZ --signal=cuW
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt100To200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=cuW
#
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --normalizeBSM --onlyTTZ --signal=cuW
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=currentEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=dipoleEllipsis
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=C2VA0p2
#python shapes.py --selection=lepSelTTZ-njet3p-btag1p-onZ-Zpt200 --reweightPtZToSM --normalizeBSM --onlyTTZ --signal=cuW
