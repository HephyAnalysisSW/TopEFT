#!/bin/sh
run.py --overwrite --model HEL_UFO --couplings cuW -0.3 --makeGridpack --process ttZ_ll
run.py --overwrite --model HEL_UFO --couplings cuW -0.2 --makeGridpack --process ttZ_ll
run.py --overwrite --model HEL_UFO --couplings cuW -0.1 --makeGridpack --process ttZ_ll
run.py --overwrite --model HEL_UFO --couplings cuW 0.0 --makeGridpack --process ttZ_ll
run.py --overwrite --model HEL_UFO --couplings cuW 0.1 --makeGridpack --process ttZ_ll
run.py --overwrite --model HEL_UFO --couplings cuW 0.2 --makeGridpack --process ttZ_ll
run.py --overwrite --model HEL_UFO --couplings cuW 0.3 --makeGridpack --process ttZ_ll
