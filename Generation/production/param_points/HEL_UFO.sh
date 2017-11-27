#!/bin/sh
run.py --model HEL_UFO --couplings cuW -0.3 --makeGridpack  --calcXSec --process ttZ_ll
run.py --model HEL_UFO --couplings cuW -0.2 --makeGridpack  --calcXSec --process ttZ_ll
run.py --model HEL_UFO --couplings cuW -0.1 --makeGridpack  --calcXSec --process ttZ_ll
run.py --model HEL_UFO --couplings cuW 0.0  --makeGridpack --calcXSec --process ttZ_ll
run.py --model HEL_UFO --couplings cuW 0.1  --makeGridpack --calcXSec --process ttZ_ll
run.py --model HEL_UFO --couplings cuW 0.2  --makeGridpack --calcXSec --process ttZ_ll
run.py --model HEL_UFO --couplings cuW 0.3  --makeGridpack --calcXSec --process ttZ_ll
