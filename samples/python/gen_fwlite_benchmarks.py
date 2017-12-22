''' Benchmark samples for TopEFT (EDM)'''

# standard imports
import os

# RootTools
from RootTools.core.standard import *

#Top EFT
from TopEFT.Tools.user import results_directory 

# Robert GENSIM 0j benchmarks 09Nov17 (used for analysis development)
gen_dir = "/afs/hephy.at/data/rschoefbeck02/TopEFT/skims/gen/v2/"
ewkDM_ttZ_ll_gen                                             = Sample.fromDirectory("ewkDM_ttZ_ll_gen",                                                                                directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS/")])
ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_0p500000                 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_0p500000",                                                    directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p500000_DC1V_0p500000/")])
ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_m1p000000                = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_m1p000000",                                                   directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p500000_DC1V_m1p000000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000",                                     directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000",                                    directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000",                                     directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000",                                    directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/")])
ewkDM_ttZ_ll_gen_DC2A_0p200000_DC2V_0p200000                 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC2A_0p200000_DC2V_0p200000",                                                    directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC2A_0p200000_DC2V_0p200000/")])
ewkDM_ttZ_ll_gen_DC1A_1p000000                               = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_1p000000",                                                                  directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_1p000000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700   = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700",        directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700",       directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700",       directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700",      directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/")])
HEL_UFO_ttZ_ll_gen_cuW_0p100000                              = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_0p100000",                                                                 directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_0p100000/")])
HEL_UFO_ttZ_ll_gen_cuW_0p200000                              = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_0p200000",                                                                 directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_0p200000/")])
HEL_UFO_ttZ_ll_gen_cuW_0p300000                              = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_0p300000",                                                                 directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_0p300000/")])
HEL_UFO_ttZ_ll_gen_cuW_m0p100000                             = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_m0p100000",                                                                directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_m0p100000/")])
HEL_UFO_ttZ_ll_gen_cuW_m0p200000                             = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_m0p200000",                                                                directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_m0p200000/")])
HEL_UFO_ttZ_ll_gen_cuW_m0p300000                             = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_m0p300000",                                                                directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_m0p300000/")])

