''' Benchmark samples for TopEFT'''

# RootTools
from RootTools.core.standard import *

# FWLite TTZ benchmarks, first shot with approx same x-Sec of 0.5pb
fwlite_ttZ_sm   = FWLiteSample.fromFiles( "SM", texName = "SM", files = ["/data/rschoefbeck/TopEFT/GEN/ewkDM_ttZ.root"] )
fwlite_ttZ_bm1  = FWLiteSample.fromFiles( "C1Vm1p0_C1A0p5", texName = "C1V=-1.0 C1A=0.5", files = ["/data/rschoefbeck/TopEFT/GEN/ewkDM_ttZ_DC1A_0.500000_DC1V_-1.000000.root"] )
fwlite_ttZ_bm2  = FWLiteSample.fromFiles( "C1V0p5_C1A0p5",  texName = "C1V=0.5 C1A=0.5", files = ["/data/rschoefbeck/TopEFT/GEN/ewkDM_ttZ_DC1A_0.500000_DC1V_0.500000.root"] )
