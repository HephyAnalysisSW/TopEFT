''' Benchmark samples for TopEFT (EDM)'''

# RootTools
from RootTools.core.standard import *

# FWLite TTZ benchmarks, first shot with approx same x-Sec of 0.5pb
#fwlite_ttZ_sm   = FWLiteSample.fromFiles( "SM", texName = "SM", files = ["/data/rschoefbeck/TopEFT/GEN/ewkDM_ttZ.root"] )
#fwlite_ttZ_bm1  = FWLiteSample.fromFiles( "C1Vm1p0_C1A0p5", texName = "C1V=-1.0 C1A=0.5", files = ["/data/rschoefbeck/TopEFT/GEN/ewkDM_ttZ_DC1A_0.500000_DC1V_-1.000000.root"] )
#fwlite_ttZ_bm2  = FWLiteSample.fromFiles( "C1V0p5_C1A0p5",  texName = "C1V=0.5 C1A=0.5", files = ["/data/rschoefbeck/TopEFT/GEN/ewkDM_ttZ_DC1A_0.500000_DC1V_0.500000.root"] )


# dipole moments = 0, approx SM LO x-sec
fwlite_ttZ_ll_LO_sm                   = FWLiteSample.fromDAS("ttZ_ll_LO_sm", "/ewkDM_ttZ_ll/schoef-ewkDM-e1a069162e896efecc10f859afdda0d0/USER", "phys03")
fwlite_ttZ_ll_LO_DC1V_0p5_DC1A_0p5    = FWLiteSample.fromDAS("ttZ_ll_LO_DC1V_0p5_DC1A_0p5", "/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000/schoef-ewkDM-863d441c1e97429a518397b2b60fd1be/USER", "phys03")
fwlite_ttZ_ll_LO_DC1V_m1_DC1A0p5      = FWLiteSample.fromDAS("ttZ_ll_LO_DC1V_m1_DC1A0p5", "/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000/schoef-ewkDM-ff3cbbd709193316b9c63feda6313fd2/USER", "phys03")

# benchmark from https://arxiv.org/pdf/1501.05939.pdf
fwlite_ttZ_ll_LO_C2VA_0p2 = FWLiteSample.fromDAS("ttZ_ll_LO_C2VA_0p2", "/ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000/schoef-ewkDM-d5ca1cdb139c8f92e34abf823fbeb652/USER", "phys03")

# DC1V/A = - C1V/A(SM), then 8 points on a circle in DC2V/A space such that x-sec(BSM)~x-sec(SM) at NLO
fwlite_ttZ_ll_LO_minXSecC1VA_0 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_0", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/schoef-ewkDM-83046cbf09b262686da67ff44f4901ef/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_1 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_1", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/schoef-ewkDM-bedd681b46b413b9e38bf1a1ea2e75b5/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_2 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_2", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/schoef-ewkDM-fc88fc2758a774e57c48fe86b5da4bcc/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_3 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_3", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/schoef-ewkDM-d670ddb18e88e55b6a43b4acd2505de3/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_4 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_4", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/schoef-ewkDM-f750c11322cf3df8d05711a6083e929b/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_5 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_5", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/schoef-ewkDM-10e11608d2c97bb8d3584319b95ebd12/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_6 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_6", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/schoef-ewkDM-3a75ae4139536634dab39690896bcd56/USER", "phys03")
fwlite_ttZ_ll_LO_minXSecC1VA_7 = FWLiteSample.fromDAS("ttZ_ll_LO_minXSecC1VA_7", "/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/schoef-ewkDM-28215b5f801d5ea3987bbdce381a4244/USER", "phys03")

# samples where C1A/V are set to SM values, 10k events
daniel_fwlite_ttZ_ll_LO_sm                     = FWLiteSample.fromFiles( "ttZ_ll_LO_SM", texName = "SM", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC2A_0p2_DC2V_0p2      = FWLiteSample.fromFiles( "ttZ_ll_LO_DC2A_0p2_DC2V_0p2", texName = "DC2A_0p2_DC2V_0p2", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC2A_0p2_DC2V_0p2/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC2A_0p4_DC2V_0p4      = FWLiteSample.fromFiles( "ttZ_ll_LO_DC2A_0p4_DC2V_0p4", texName = "DC2A_0p4_DC2V_0p4", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC2A_0p4_DC2V_0p4/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC2A_0p6_DC2V_0p6      = FWLiteSample.fromFiles( "ttZ_ll_LO_DC2A_0p6_DC2V_0p6", texName = "DC2A_0p6_DC2V_0p6", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC2A_0p6_DC2V_0p6/events.root"] )

# extensions
daniel_fwlite_ttZ_ll_LO_sm_ext1                     = FWLiteSample.fromFiles( "ttZ_ll_LO_SM_ext1", texName = "SM", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_SM_exp1/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC2A_0p2_DC2V_0p2_ext1      = FWLiteSample.fromFiles( "ttZ_ll_LO_DC2A_0p2_DC2V_0p2_ext1", texName = "DC2A_0p2_DC2V_0p2", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC2A_0p2_DC2V_0p2_exp1/events.root"] )


daniel_fwlite_ttZ_ll_LO_DC2A_0p216_DC2V_0p523   = FWLiteSample.fromFiles( "ttZ_ll_LO_DC2A_0p216_DC2V_0p523", texName = "DC2A_0p216_DC2V_0p523", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC2A_0p216_DC2V_0p523/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC2A_0p523_DC2V_0p216   = FWLiteSample.fromFiles( "ttZ_ll_LO_DC2A_0p523_DC2V_0p216", texName = "DC2A_0p523_DC2V_0p216", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC2A_0p523_DC2V_0p216/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC2A_0p57_DC2V_0p0      = FWLiteSample.fromFiles( "ttZ_ll_LO_DC2A_0p57_DC2V_0p0", texName = "DC2A_0p57_DC2V_0p0", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC2A_0p57_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC2A_0p0_DC2V_0p57      = FWLiteSample.fromFiles( "ttZ_ll_LO_DC2A_0p0_DC2V_0p57", texName = "DC2A_0p0_DC2V_0p57", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC2A_0p0_DC2V_0p57/events.root"] )

# samples on the C1A/V ellipse with SM x-sec
daniel_fwlite_ttZ_ll_LO_DC1A_1p19_DC1V_m0p31    = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1A_1p19_DC1V_-0p31", texName="",     files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_1p19_DC1V_-0p31_DC2A_0p0_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC1A_0p8_DC1V_0p8       = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1A_0p8_DC1V_0p8", texName="",        files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p8_DC1V_0p8_DC2A_0p0_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC1A_0p6_DC1V_0p59      = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1A_0p6_DC1V_0p59", texName="",       files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_0p59_DC2A_0p0_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC1A_0p6_DC1V_m1p05     = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1A_0p6_DC1V_-1p05", texName="",      files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_-1p05_DC2A_0p0_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC1A_0p6_DC1V_m0p24     = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1A_0p6_DC1V_-0p24", texName="",      files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_-0p24_DC2A_0p0_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC1A_0p4_DC1V_0p4       = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1A_0p4_DC1V_0p4", texName="",        files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p4_DC1V_0p4_DC2A_0p0_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC1A_1p0_DC1V_1p0       = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1A_1p0_DC1V_1p0", texName="",        files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_1p0_DC1V_1p0_DC2A_0p0_DC2V_0p0/events.root"] )


# samples where C1A/V are set to 0, so DC1A/V = -C1A/V(SM), 25k events
daniel_fwlite_ttZ_ll_LO_antiSM_DC2A_0p28_DC2V_0p0       = FWLiteSample.fromFiles( "ttZ_ll_LO_antiSM_DC2A_0p28_DC2V_0p0", texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_-0p24_DC2A_0p28_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_antiSM_DC2A_0p0_DC2V_0p3        = FWLiteSample.fromFiles( "ttZ_ll_LO_antiSM_DC2A_0p0_DC2V_0p3", texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_-0p24_DC2A_0p0_DC2V_0p3/events.root"] )
daniel_fwlite_ttZ_ll_LO_antiSM_DC2A_0p205_DC2V_0p205    = FWLiteSample.fromFiles( "ttZ_ll_LO_antiSM_DC2A_0p205_DC2V_0p205", texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_-0p24_DC2A_0p205_DC2V_0p205/events.root"] )
daniel_fwlite_ttZ_ll_LO_antiSM_DC2A_0p12_DC2V_0p27      = FWLiteSample.fromFiles( "ttZ_ll_LO_antiSM_DC2A_0p12_DC2V_0p27", texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_-0p24_DC2A_0p12_DC2V_0p27/events.root"] )
daniel_fwlite_ttZ_ll_LO_antiSM_DC2A_0p24_DC2V_0p155     = FWLiteSample.fromFiles( "ttZ_ll_LO_antiSM_DC2A_0p24_DC2V_0p155", texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_-0p24_DC2A_0p24_DC2V_0p155/events.root"] )

daniel_fwlite_ttZ_ll_LO_antiSM_DC2A_0p5 = FWLiteSample.fromFiles( "ttZ_ll_LO_antiSM_DC2A_0p5", texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_-0p24_DC2A_0p5_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_antiSM_DC2A_0p7 = FWLiteSample.fromFiles( "ttZ_ll_LO_antiSM_DC2A_0p7", texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_-0p24_DC2A_0p7_DC2V_0p0/events.root"] )


# same as above, but using ttZ instead of ttZ_ll process cards, 25k events
daniel_fwlite_ttZ_LO_antiSM_DC2A_0p28_DC2V_0p0       = FWLiteSample.fromFiles( "ttZ_LO_antiSM_DC2A_0p28_DC2V_0p0", texName = "",    files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_DC1A_0p6_DC1V_-0p24_DC2A_0p28_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_LO_antiSM_DC2A_0p0_DC2V_0p3        = FWLiteSample.fromFiles( "ttZ_LO_antiSM_DC2A_0p0_DC2V_0p3", texName = "",     files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_DC1A_0p6_DC1V_-0p24_DC2A_0p0_DC2V_0p3/events.root"] )
daniel_fwlite_ttZ_LO_antiSM_DC2A_0p205_DC2V_0p205    = FWLiteSample.fromFiles( "ttZ_LO_antiSM_DC2A_0p205_DC2V_0p205", texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_DC1A_0p6_DC1V_-0p24_DC2A_0p205_DC2V_0p205/events.root"] )
daniel_fwlite_ttZ_LO_antiSM_DC2A_0p12_DC2V_0p27      = FWLiteSample.fromFiles( "ttZ_LO_antiSM_DC2A_0p12_DC2V_0p27", texName = "",   files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_DC1A_0p6_DC1V_-0p24_DC2A_0p12_DC2V_0p27/events.root"] )
daniel_fwlite_ttZ_LO_antiSM_DC2A_0p24_DC2V_0p155     = FWLiteSample.fromFiles( "ttZ_LO_antiSM_DC2A_0p24_DC2V_0p155", texName = "",  files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_DC1A_0p6_DC1V_-0p24_DC2A_0p24_DC2V_0p155/events.root"] )

# settting one of C1V/A to 0, the other is kept at the SM value, 25k events
daniel_fwlite_ttZ_ll_LO_DC1V_m0p24_DC2V_0p3     = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1V_m0p24_DC2V_0p3",  texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p0_DC1V_-0p24_DC2A_0p0_DC2V_0p30/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC1V_m0p24_DC2A_0p28    = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1V_m0p24_DC2A_0p28", texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p0_DC1V_-0p24_DC2A_0p28_DC2V_0p0/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC1A_0p6_DC2V_0p3       = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1A_0p6_DC2V_0p3",    texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_0p0_DC2A_0p0_DC2V_0p30/events.root"] )
daniel_fwlite_ttZ_ll_LO_DC1A_0p6_DC2A_0p28      = FWLiteSample.fromFiles( "ttZ_ll_LO_DC1A_0p6_DC2A_0p28",   texName = "", files = ["/afs/hephy.at/data/dspitzbart01/TopEFT/samples/ttZ_ll_DC1A_0p6_DC1V_0p0_DC2A_0p28_DC2V_0p0/events.root"] )

