''' Benchmark samples for TopEFT (skimmed, flat ntuples)'''

#Standard import
import os
import ROOT

# RootTools
from RootTools.core.standard import *

# TopEFT
from TopEFT.tools.user import skim_directory

directory = 'v1'

# dipole moments = 0, approx SM LO x-sec
ttZ_ll_LO_sm                   = Sample.fromDirectory("ttZ_ll_LO_sm",                texName = "SM",                 directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_sm"                ) , color = ROOT.kBlack ) 
ttZ_ll_LO_DC1V_0p5_DC1A_0p5    = Sample.fromDirectory("ttZ_ll_LO_DC1V_0p5_DC1A_0p5", texName = "C1V=0.5 C1A=0.5",    directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC1V_0p5_DC1A_0p5" ) , color = ROOT.kRed )
ttZ_ll_LO_DC1V_m1_DC1A0p5      = Sample.fromDirectory("ttZ_ll_LO_DC1V_m1_DC1A0p5",   texName = "C1V=-1.0 C1A=0.5",   directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_DC1V_m1_DC1A0p5"   ) , color = ROOT.kBlue )

# benchmark from https://arxiv.org/pdf/1501.05939.pdf
ttZ_ll_LO_C2VA_0p2 = Sample.fromDirectory("ttZ_ll_LO_C2VA_0p2",                      texName = "C2V/A=0.2",   directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_C2VA_0p2") , color = ROOT.kMagenta )


# DC1V/A = - C1V/A(SM), then 8 points on a circle in DC2V/A space such that x-sec(BSM)~x-sec(SM) at NLO
ttZ_ll_LO_minXSecC1VA_0 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_0", texName = "C1VA=0 DC2V=0.25 DC2A=0",        directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_0") , color = ROOT.kBlack)
ttZ_ll_LO_minXSecC1VA_1 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_1", texName = "C1VA=0 DC2V=0.18 DC2A=18",      directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_1") , color = ROOT.kRed)
ttZ_ll_LO_minXSecC1VA_2 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_2", texName = "C1VA=0 DC2V=0 DC2A=0.25",         directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_2") , color = ROOT.kBlue)
ttZ_ll_LO_minXSecC1VA_3 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_3", texName = "C1VA=0 DC2V=-0.18 DC2A=0.18",   directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_3") , color = ROOT.kGreen)
ttZ_ll_LO_minXSecC1VA_4 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_4", texName = "C1VA=0 DC2V=-0.25 DC2A=0.0",      directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_4") , color = ROOT.kOrange)
ttZ_ll_LO_minXSecC1VA_5 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_5", texName = "C1VA=0 DC2V=-0.18 DC2A=-0.18",  directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_5") , color = ROOT.kOrange-5)
ttZ_ll_LO_minXSecC1VA_6 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_6", texName = "C1VA=0 DC2V=0.0 DC2A=-0.25",      directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_6") , color = ROOT.kOrange-7)
ttZ_ll_LO_minXSecC1VA_7 = Sample.fromDirectory("ttZ_ll_LO_minXSecC1VA_7", texName = "C1VA=0 DC2V=0.18 DC2A=-0.18",   directory = os.path.join( skim_directory, directory, "ttZ_ll_LO_minXSecC1VA_7") , color = ROOT.kCyan)

