#!/bin/sh
run.py --model HEL_UFO --couplings cuW -0.3 --calcXSec --makeGridpack --process ttZ_ll &
run.py --model HEL_UFO --couplings cuW -0.2 --calcXSec --makeGridpack --process ttZ_ll &
run.py --model HEL_UFO --couplings cuW -0.1 --calcXSec --makeGridpack --process ttZ_ll &
run.py --model HEL_UFO --couplings cuW 0.0 --calcXSec --makeGridpack --process ttZ_ll &
run.py --model HEL_UFO --couplings cuW 0.1 --calcXSec --makeGridpack --process ttZ_ll &
run.py --model HEL_UFO --couplings cuW 0.2 --calcXSec --makeGridpack --process ttZ_ll &
run.py --model HEL_UFO --couplings cuW 0.3 --calcXSec --makeGridpack --process ttZ_ll &
