#!/bin/sh
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V -0.24 DC1A 0.60 DC2A  0.25
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V -0.24 DC1A 0.60 DC2V  0.25
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V -0.24 DC1A 0.60 DC2A -0.25 
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V -0.24 DC1A 0.60 DC2V -0.25
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V -0.24 DC1A 0.60 DC2A  0.1767 DC2V 0.1767
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V -0.24 DC1A 0.60 DC2A -0.1767 DC2V 0.1767
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V -0.24 DC1A 0.60 DC2A -0.1767 DC2V -0.1767
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V -0.24 DC1A 0.60 DC2A  0.1767 DC2V -0.1767
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC2A  0.2  DC2V 0.2
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V  0.5  DC1A 0.5
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1A  1.0
run.py --overwrite --model ewkDM --process ttZ_ll --makeGridpack --couplings DC1V -1    DC1A 0.5
