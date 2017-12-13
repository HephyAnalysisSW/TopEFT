#!/bin/sh

python dataToData.py --selection dilepOS-njet3p-btag1p --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag1p --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag1p --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p-btag0 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag0 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag0 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet0-btag0 --logLevel DEBUG
python dataToData.py --selection dilepOS --logLevel DEBUG

python dataToData.py --selection dilepOS-njet3p-btag1p-onZ --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag1p-onZ --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag1p-onZ --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p-btag0-onZ --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p-onZ --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag0-onZ --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag0-onZ --logLevel DEBUG
python dataToData.py --selection dilepOS-njet0-btag0-onZ --logLevel DEBUG
python dataToData.py --selection dilepOS-onZ --logLevel DEBUG

python dataToData.py --selection dilepOS-njet3p-btag1p-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag1p-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag1p-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p-btag0-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag0-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag0-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet0-btag0-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-mll20 --logLevel DEBUG

python dataToData.py --selection dilepOS-njet3p-btag1p-mllTo20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag1p-mllTo20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag1p-mllTo20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p-btag0-mllTo20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p-mllTo20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag0-mllTo20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag0-mllTo20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet0-btag0-mllTo20 --logLevel DEBUG
python dataToData.py --selection dilepOS-mllTo20 --logLevel DEBUG

python dataToData.py --selection dilepOS-njet3p-btag1p-offZ-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag1p-offZ-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag1p-offZ-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p-btag0-offZ-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet3p-offZ-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet2-btag0-offZ-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet1-btag0-offZ-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-njet0-btag0-offZ-mll20 --logLevel DEBUG
python dataToData.py --selection dilepOS-offZ-mll20 --logLevel DEBUG
