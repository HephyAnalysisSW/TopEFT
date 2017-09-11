''' Benchmark samples for TopEFT (skimmed, flat ntuples)'''

#Standard import
import os
import ROOT

# RootTools
from RootTools.core.standard import *

# TopEFT
from TopEFT.tools.user import skim_directory

directory = 'v1'

## dipole moments = 0, approx SM LO x-sec
#ttZ_ll_LO_sm                   = Sample.fromDirectory("ttZ_ll_LO_sm",                texName = "SM",                 directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_sm"                ) , color = ROOT.kBlack ) 
#ttZ_ll_LO_DC1V_0p5_DC1A_0p5    = Sample.fromDirectory("ttZ_ll_LO_DC1V_0p5_DC1A_0p5", texName = "C1V=0.5 C1A=0.5",    directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC1V_0p5_DC1A_0p5" ) , color = ROOT.kRed )
#ttZ_ll_LO_DC1V_m1_DC1A0p5      = Sample.fromDirectory("ttZ_ll_LO_DC1V_m1_DC1A0p5",   texName = "C1V=-1.0 C1A=0.5",   directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC1V_m1_DC1A0p5"   ) , color = ROOT.kBlue )
#
## benchmark from https://arxiv.org/pdf/1501.05939.pdf
#ttZ_ll_LO_C2VA_0p2 = Sample.fromDirectory("ttZ_ll_LO_C2VA_0p2",                      texName = "C2V/A=0.2",   directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_C2VA_0p2") , color = ROOT.kMagenta )
#
#
## DC1V/A = - C1V/A(SM), then 8 points on a circle in DC2V/A space such that x-sec(BSM)~x-sec(SM) at NLO
#ttZ_ll_LO_minXSecC1VA_0 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_0", texName = "C1VA=0 DC2V=0.25 DC2A=0",        directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_0") , color = ROOT.kBlack)
#ttZ_ll_LO_minXSecC1VA_1 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_1", texName = "C1VA=0 DC2V=0.18 DC2A=18",      directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_1") , color = ROOT.kRed)
#ttZ_ll_LO_minXSecC1VA_2 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_2", texName = "C1VA=0 DC2V=0 DC2A=0.25",         directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_2") , color = ROOT.kBlue)
#ttZ_ll_LO_minXSecC1VA_3 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_3", texName = "C1VA=0 DC2V=-0.18 DC2A=0.18",   directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_3") , color = ROOT.kGreen)
#ttZ_ll_LO_minXSecC1VA_4 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_4", texName = "C1VA=0 DC2V=-0.25 DC2A=0.0",      directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_4") , color = ROOT.kOrange)
#ttZ_ll_LO_minXSecC1VA_5 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_5", texName = "C1VA=0 DC2V=-0.18 DC2A=-0.18",  directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_5") , color = ROOT.kOrange-5)
#ttZ_ll_LO_minXSecC1VA_6 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_6", texName = "C1VA=0 DC2V=0.0 DC2A=-0.25",      directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_6") , color = ROOT.kOrange-7)
#ttZ_ll_LO_minXSecC1VA_7 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_7", texName = "C1VA=0 DC2V=0.18 DC2A=-0.18",   directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_7") , color = ROOT.kCyan)


# samples where C1A/V are set to SM values
ttZ_ll_LO_DC2A_0p0_DC2V_0p0 = Sample.fromDirectory("ttZ_ll_LO_DC2A_0p0_DC2V_0p0", texName = "DC1V=0 DC1A=0 C2V=0.0 C2A=0.0",         directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_SM"), color = ROOT.kBlack)
ttZ_ll_LO_DC2A_0p2_DC2V_0p2 = Sample.fromDirectory("ttZ_ll_LO_DC2A_0p2_DC2V_0p2", texName = "DC1V=0 DC1A=0 C2V=0.2 C2A=0.2",         directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC2A_0p2_DC2V_0p2"), color = ROOT.kRed)
ttZ_ll_LO_DC2A_0p4_DC2V_0p4 = Sample.fromDirectory("ttZ_ll_LO_DC2A_0p4_DC2V_0p4", texName = "DC1V=0 DC1A=0 C2V=0.4 C2A=0.4",         directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC2A_0p4_DC2V_0p4"), color = ROOT.kBlue)
ttZ_ll_LO_DC2A_0p6_DC2V_0p6 = Sample.fromDirectory("ttZ_ll_LO_DC2A_0p6_DC2V_0p6", texName = "DC1V=0 DC1A=0 C2V=0.6 C2A=0.6",         directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC2A_0p6_DC2V_0p6"), color = ROOT.kGreen)

ttZ_ll_LO_DC2A_0p0_DC2V_0p57    = Sample.fromDirectory("ttZ_ll_LO_DC2A_0p0_DC2V_0p57",      texName = "DC1V=0 DC1A=0 C2V=0.57 C2A=0.0",      directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC2A_0p0_DC2V_0p57"), color = ROOT.kOrange)
ttZ_ll_LO_DC2A_0p57_DC2V_0p0    = Sample.fromDirectory("ttZ_ll_LO_DC2A_0p57_DC2V_0p0",      texName = "DC1V=0 DC1A=0 C2V=0.0  C2A=0.57",     directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC2A_0p57_DC2V_0p0"), color = ROOT.kCyan)
ttZ_ll_LO_DC2A_0p216_DC2V_0p523 = Sample.fromDirectory("ttZ_ll_LO_DC2A_0p216_DC2V_0p523",   texName = "DC1V=0 DC1A=0 C2V=0.52 C2A=0.22",     directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC2A_0p216_DC2V_0p523"), color = ROOT.kMagenta)
ttZ_ll_LO_DC2A_0p523_DC2V_0p216 = Sample.fromDirectory("ttZ_ll_LO_DC2A_0p523_DC2V_0p216",   texName = "DC1V=0 DC1A=0 C2V=0.22 C2A=0.52",     directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC2A_0p523_DC2V_0p216"), color = ROOT.kGreen)

# samples where C1A/V are set to 0, so DC1A/V = -C1A/V(SM)
ttZ_ll_LO_antiSM_DC2A_0p0_DC2V_0p3      = Sample.fromDirectory("ttZ_ll_LO_antiSM_DC2A_0p0_DC2V_0p3",      texName = "SM=0 C2V=0.30 DC2A=0.00",     directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_antiSM_DC2A_0p0_DC2V_0p3"), color = ROOT.kOrange)
ttZ_ll_LO_antiSM_DC2A_0p12_DC2V_0p27    = Sample.fromDirectory("ttZ_ll_LO_antiSM_DC2A_0p12_DC2V_0p27",    texName = "SM=0 C2V=0.27 DC2A=0.12",     directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_antiSM_DC2A_0p12_DC2V_0p27"), color = ROOT.kCyan)
ttZ_ll_LO_antiSM_DC2A_0p205_DC2V_0p205  = Sample.fromDirectory("ttZ_ll_LO_antiSM_DC2A_0p205_DC2V_0p205",  texName = "SM=0 C2V=0.21 DC2A=0.21",     directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_antiSM_DC2A_0p205_DC2V_0p205"), color =  ROOT.kMagenta)
ttZ_ll_LO_antiSM_DC2A_0p28_DC2V_0p0     = Sample.fromDirectory("ttZ_ll_LO_antiSM_DC2A_0p28_DC2V_0p0",     texName = "SM=0 C2V=0.00 DC2A=0.28",     directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_antiSM_DC2A_0p28_DC2V_0p0"), color = ROOT.kGreen)
ttZ_ll_LO_antiSM_DC2A_0p24_DC2V_0p155   = Sample.fromDirectory("ttZ_ll_LO_antiSM_DC2A_0p24_DC2V_0p155",   texName = "SM=0 C2V=0.16 DC2A=0.24",     directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_antiSM_DC2A_0p24_DC2V_0p155"), color = ROOT.kBlue)

# same as above, but using ttZ instead of ttZ_ll process cards
ttZ_LO_antiSM_DC2A_0p0_DC2V_0p3      = Sample.fromDirectory("ttZ_LO_antiSM_DC2A_0p0_DC2V_0p3",      texName = "SM=0 C2V=0.30 DC2A=0.00",     directory = os.path.join( skim_directory, directory, "ttZ_LO_antiSM_DC2A_0p0_DC2V_0p3"), color = ROOT.kOrange)
ttZ_LO_antiSM_DC2A_0p12_DC2V_0p27    = Sample.fromDirectory("ttZ_LO_antiSM_DC2A_0p12_DC2V_0p27",    texName = "SM=0 C2V=0.27 DC2A=0.12",     directory = os.path.join( skim_directory, directory, "ttZ_LO_antiSM_DC2A_0p12_DC2V_0p27"), color = ROOT.kCyan)
ttZ_LO_antiSM_DC2A_0p205_DC2V_0p205  = Sample.fromDirectory("ttZ_LO_antiSM_DC2A_0p205_DC2V_0p205",  texName = "SM=0 C2V=0.21 DC2A=0.21",     directory = os.path.join( skim_directory, directory, "ttZ_LO_antiSM_DC2A_0p205_DC2V_0p205"), color =  ROOT.kMagenta)
ttZ_LO_antiSM_DC2A_0p28_DC2V_0p0     = Sample.fromDirectory("ttZ_LO_antiSM_DC2A_0p28_DC2V_0p0",     texName = "SM=0 C2V=0.00 DC2A=0.28",     directory = os.path.join( skim_directory, directory, "ttZ_LO_antiSM_DC2A_0p28_DC2V_0p0"), color = ROOT.kGreen)
ttZ_LO_antiSM_DC2A_0p24_DC2V_0p155   = Sample.fromDirectory("ttZ_LO_antiSM_DC2A_0p24_DC2V_0p155",   texName = "SM=0 C2V=0.16 DC2A=0.24",     directory = os.path.join( skim_directory, directory, "ttZ_LO_antiSM_DC2A_0p24_DC2V_0p155"), color = ROOT.kBlue)

