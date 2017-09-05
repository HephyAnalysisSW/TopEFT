''' Benchmark samples for TopEFT'''

# RootTools
from RootTools.core.standard import *

# FWLite TTZ benchmarks, first shot with approx same x-Sec of 0.5pb
#fwlite_ttZ_sm   = FWLiteSample.fromFiles( "SM", texName = "SM", files = ["/data/rschoefbeck/TopEFT/GEN/ewkDM_ttZ.root"] )
#fwlite_ttZ_bm1  = FWLiteSample.fromFiles( "C1Vm1p0_C1A0p5", texName = "C1V=-1.0 C1A=0.5", files = ["/data/rschoefbeck/TopEFT/GEN/ewkDM_ttZ_DC1A_0.500000_DC1V_-1.000000.root"] )
#fwlite_ttZ_bm2  = FWLiteSample.fromFiles( "C1V0p5_C1A0p5",  texName = "C1V=0.5 C1A=0.5", files = ["/data/rschoefbeck/TopEFT/GEN/ewkDM_ttZ_DC1A_0.500000_DC1V_0.500000.root"] )
#
#
# benchmark from https://arxiv.org/pdf/1501.05939.pdf
fwlite_ttZ_ll_LO_C2VA_0p2 = FWLiteSample.fromDAS("ttZ_ll_LO_C2VA_0p2", "/ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000/schoef-ewkDM-d5ca1cdb139c8f92e34abf823fbeb652/USER", "phys03")

# dipole moments = 0, approx SM LO x-sec
fwlite_ttZ_ll_LO_sm                   = FWLiteSample.fromDAS("ttZ_ll_LO_sm", "/ewkDM_ttZ_ll/schoef-ewkDM-e1a069162e896efecc10f859afdda0d0/USER", "phys03")
fwlite_ttZ_ll_LO_DC1V_0p5_DC1A_0p5    = FWLiteSample.fromDAS("ttZ_ll_LO_DC1V_0p5_DC1A_0p5", "/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000/schoef-ewkDM-863d441c1e97429a518397b2b60fd1be/USER", "phys03")
fwlite_ttZ_ll_LO_DC1V_m1_DC1A0p5      = FWLiteSample.fromDAS("ttZ_ll_LO_DC1V_m1_DC1A0p5", "/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000/schoef-ewkDM-ff3cbbd709193316b9c63feda6313fd2/USER", "phys03")

# DC1V/A = - C1V/A(SM), then 8 points on a circle in DC2V/A space such that x-sec(BSM)~x-sec(SM) at NLO
fwlite_ttZ_ll_LO_minXSecC1VA_0 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_0", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/schoef-ewkDM-83046cbf09b262686da67ff44f4901ef/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_1 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_1", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/schoef-ewkDM-bedd681b46b413b9e38bf1a1ea2e75b5/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_2 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_2", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/schoef-ewkDM-fc88fc2758a774e57c48fe86b5da4bcc/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_3 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_3", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/schoef-ewkDM-d670ddb18e88e55b6a43b4acd2505de3/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_4 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_4", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/schoef-ewkDM-f750c11322cf3df8d05711a6083e929b/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_5 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_5", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/schoef-ewkDM-10e11608d2c97bb8d3584319b95ebd12/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_6 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_6", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/schoef-ewkDM-3a75ae4139536634dab39690896bcd56/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_7 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_7", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/schoef-ewkDM-28215b5f801d5ea3987bbdce381a4244/USER", "phys03")

