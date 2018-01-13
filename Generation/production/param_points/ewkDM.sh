#!/bin/sh

#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V -0.24 DC1A 0.60 DC2A  0.25
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V -0.24 DC1A 0.60 DC2V  0.25
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V -0.24 DC1A 0.60 DC2A -0.25 
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V -0.24 DC1A 0.60 DC2V -0.25
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V -0.24 DC1A 0.60 DC2A  0.1767 DC2V 0.1767
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V -0.24 DC1A 0.60 DC2A -0.1767 DC2V 0.1767
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V -0.24 DC1A 0.60 DC2A -0.1767 DC2V -0.1767
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V -0.24 DC1A 0.60 DC2A  0.1767 DC2V -0.1767
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC2A  0.2  DC2V 0.2
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V  0.5  DC1A 0.5
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1A  1.0
#run.py  --model ewkDM --process ttZ_ll --makeGridpack --calcXSec --couplings DC1V -1    DC1A 0.5

run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DAG  0.25 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DVG  0.25 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DAG -0.25  
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DVG -0.25 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DAG  0.5 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DVG  0.5 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DAG -0.5  
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DVG -0.5 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DAG  0.1767 DVG 0.1767 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DAG -0.1767 DVG 0.1767 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DAG -0.1767 DVG -0.1767 
run.py  --model ewkDMGZ --process ttgamma_ll --makeGridpack --couplings  DAG  0.1767 DVG -0.1767 
