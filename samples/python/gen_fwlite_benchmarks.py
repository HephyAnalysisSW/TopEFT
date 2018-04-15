''' Benchmark samples for TopEFT (EDM)'''

# standard imports
import os

# RootTools
from RootTools.core.standard import *

#Top EFT
from TopEFT.Tools.user import results_directory 

# Logging
import logging
logger = logging.getLogger(__name__)

import glob

gen_dir = "/afs/hephy.at/data/rschoefbeck02/TopEFT/skims/gen/v2/"
# Robert first ttZ_ll dim6top scan
#dim6top_ttZ_ll_LO_scan = Sample.fromDirectory("dim6top_ttZ_ll_LO_scan", texName = "ttZ (scan)", directory = [os.path.join( gen_dir, "fwlite_ttZ_ll_LO_scan")])
dim6top_ttZ_ll_LO_scan = Sample.fromDirectory("dim6top_ttZ_ll_LO_scan", texName = "ttZ (scan)", directory = [os.path.join( gen_dir, "fwlite_ttZ_ll_LO_highStat_scan")])

# Robert GENSIM 0j benchmarks 09Nov17 (used for analysis development)
gen_dir = "/afs/hephy.at/data/rschoefbeck02/TopEFT/skims/gen/v2/"
ewkDM_ttZ_ll_gen                                             = Sample.fromDirectory("ewkDM_ttZ_ll_gen",                                                                           texName ="SM",                                                       directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS/")])
ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_0p500000                 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_0p500000",                                               texName ="C_{1,V}^{Z} = 0.5, C_{1,A}^{Z} = 0.5",    directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p500000_DC1V_0p500000/")])
ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_m1p000000                = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_m1p000000",                                              texName ="C_{1,V}^{Z} = -1, C_{1,A}^{Z} = 0.5",      directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p500000_DC1V_m1p000000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000",                                texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,A}^{Z} = 0.25",     directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000",                               texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,A}^{Z} = -0.25",     directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000",                                texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = 0.25",                                 directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000",                               texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = -0.25",                                  directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/")])
ewkDM_ttZ_ll_gen_DC2A_0p200000_DC2V_0p200000                 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC2A_0p200000_DC2V_0p200000",                                               texName ="C_{2,V}^{Z}=C_{2,A}^{Z}=0.2",                                 directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC2A_0p200000_DC2V_0p200000/")])
ewkDM_ttZ_ll_gen_DC1A_1p000000                               = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_1p000000",                                                             texName ="C_{1,A}^{Z} = 1",                                   directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_1p000000/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700   = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700",   texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = 0.1767, C_{2,A}^{Z} = 0.1767",                                  directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700",  texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = -0.1767, C_{2,A}^{Z} = 0.1767",                                   directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700  = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700",  texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = 0.1767, C_{2,A}^{Z} = -0.1767",                                 directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/")])
ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700 = Sample.fromDirectory("ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700", texName ="C_{1,V}^{Z} = -0.24, C_{1,A}^{Z} = 0.60, C_{2,V}^{Z} = -0.1767, C_{2,A}^{Z} = -0.1767",                                 directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll_GS_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/")])

HEL_UFO_ttZ_ll_gen_cuW_0p100000                              = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_0p100000",                                                                 directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_0p100000/")])
HEL_UFO_ttZ_ll_gen_cuW_0p200000                              = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_0p200000",                                                                 directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_0p200000/")])
HEL_UFO_ttZ_ll_gen_cuW_0p300000                              = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_0p300000",                                                                 directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_0p300000/")])
HEL_UFO_ttZ_ll_gen_cuW_m0p100000                             = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_m0p100000",                                                                directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_m0p100000/")])
HEL_UFO_ttZ_ll_gen_cuW_m0p200000                             = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_m0p200000",                                                                directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_m0p200000/")])
HEL_UFO_ttZ_ll_gen_cuW_m0p300000                             = Sample.fromDirectory("HEL_UFO_ttZ_ll_gen_cuW_m0p300000",                                                                directory = [os.path.join( gen_dir, "HEL_UFO_ttZ_ll_GS_cuW_m0p300000/")])

# ttgamma but all W decays
ewkDMGZ_ttgamma_gen                             = Sample.fromDirectory("ewkDMGZ_ttgamma_gen",                               texName ="SM",                                                  directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS") ) 
ewkDMGZ_ttgamma_gen_DAG_m0p176700_DVG_m0p176700 = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_m0p176700_DVG_m0p176700",   texName ="C_{2,V}^{#gamma} = -0.1767, C_{2,A}^{#gamma} = -0.1767",directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_m0p176700_DVG_m0p176700") ) 
ewkDMGZ_ttgamma_gen_DAG_0p176700_DVG_0p176700   = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_0p176700_DVG_0p176700",     texName ="C_{2,V}^{#gamma} = 0.1767, C_{2,A}^{#gamma} = 0.1767", directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_0p176700_DVG_0p176700") ) 
ewkDMGZ_ttgamma_gen_DAG_0p176700_DVG_m0p176700  = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_0p176700_DVG_m0p176700",    texName ="C_{2,V}^{#gamma} = -0.1767, C_{2,A}^{#gamma} = 0.1767",directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_0p176700_DVG_m0p176700") )
ewkDMGZ_ttgamma_gen_DAG_m0p176700_DVG_0p176700  = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_m0p176700_DVG_0p176700",    texName ="C_{2,V}^{#gamma} = 0.1767, C_{2,A}^{#gamma} = -0.1767",directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_m0p176700_DVG_0p176700") )
ewkDMGZ_ttgamma_gen_DAG_m0p250000               = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_m0p250000",                 texName ="C_{2,A}^{#gamma} = -0.25",                            directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_m0p250000") )
ewkDMGZ_ttgamma_gen_DAG_m0p500000               = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_m0p500000",                 texName ="C_{2,A}^{#gamma} = -0.5",                             directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_m0p500000") )
ewkDMGZ_ttgamma_gen_DAG_0p250000                = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_0p250000",                  texName ="C_{2,A}^{#gamma} = 0.25",                            directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_0p250000") )
ewkDMGZ_ttgamma_gen_DAG_0p500000                = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DAG_0p500000",                  texName ="C_{2,A}^{#gamma} = 0.5",                              directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DAG_0p500000") )
ewkDMGZ_ttgamma_gen_DVG_0p250000                = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DVG_0p250000",                  texName ="C_{2,V}^{#gamma} = 0.25",                             directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DVG_0p250000") )
ewkDMGZ_ttgamma_gen_DVG_0p500000                = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DVG_0p500000",                  texName ="C_{2,V}^{#gamma} = 0.5",                              directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DVG_0p500000") )
ewkDMGZ_ttgamma_gen_DVG_m0p250000               = Sample.fromDirectory("ewkDMGZ_ttgamma_gen_DVG_m0p250000",                 texName ="C_{2,V}^{#gamma} = -0.25",                            directory = os.path.join( gen_dir,"ewkDMGZ_ttgamma_GS_DVG_m0p250000") )

### Daniel GENSIM 0j benchmarks Jan18 local production (for propaganda plots and reweighting studies)
gen_dir = "/afs/hephy.at/data/dspitzbart01/TopEFT/skims/gen/v2/"

allSampleNames  = glob.glob(gen_dir+"dim6top_LO_ttZ_ll_c*")
allSampleNames  = [ x.replace(gen_dir, '') for x in allSampleNames if glob.glob(x+"/*.root")]

dim6top_currents_daniel  = []
dim6top_dipoles_daniel   = []

logger.info("Loading ewkDM signals from %s", gen_dir)
for s in allSampleNames:
    if len(s) > 50:
        logger.info("Skipping sample %s because I don't know how to categorize it (current or dipole plane).",s)
        continue
    if s.startswith('dim6top_LO_ttZ_ll_cp'):
        # changed naming convention, need to do some stupid gymnastics to be consistent
        dim6top_currents_daniel.append(Sample.fromDirectory(s.replace('p00', 'p000000').replace('p50','p500000'), directory = [os.path.join( gen_dir, "%s/"%s)]))
    elif s.startswith('dim6top_LO_ttZ_ll_ct'):
        # changed naming convention, need to do some stupid gymnastics to be consistent
        dim6top_dipoles_daniel.append(Sample.fromDirectory(s.replace('p00', 'p000000').replace('p20','p200000').replace('p40','p400000').replace('p60','p600000').replace('p80','p800000'), directory = [os.path.join( gen_dir, "%s/"%s)]))
    else:
        logger.info("Don't know what to do with sample %s, can't categorize into current or dipole.", s)


## Robert GEN 0j benchmarks Jan30 local production (for propaganda plots and reweighting studies)
gen_dir = "/afs/hephy.at/data/rschoefbeck02/TopEFT/skims/gen/v2/"

allSampleNames  = glob.glob(gen_dir+"ewkDM_ttZ_ll_D*")
allSampleNames  = [ x.replace(gen_dir, '') for x in allSampleNames if glob.glob(x+"/*.root")] 
ewkDM_central   = Sample.fromDirectory('ewkDM_ttZ_ll', directory = [os.path.join( gen_dir, "ewkDM_ttZ_ll/")])

ewkDM_currents  = []
ewkDM_dipoles   = []

logger.info("Loading ewkDM signals")
for s in allSampleNames:
    if len(s) > 50:
        logger.info("Skipping sample %s because I don't know how to categorize it (current or dipole plane).",s)
        continue
    if s.startswith('ewkDM_ttZ_ll_DC1'):
        ewkDM_currents.append(Sample.fromDirectory(s, directory = [os.path.join( gen_dir, "%s/"%s)]))
    elif s.startswith('ewkDM_ttZ_ll_DC2'):
        ewkDM_dipoles.append(Sample.fromDirectory(s, directory = [os.path.join( gen_dir, "%s/"%s)]))
    else:
        logger.info("Don't know what to do with sample %s, can't categorize into current or dipole.", s)

ewkDM_all = [ewkDM_central] + ewkDM_currents + ewkDM_dipoles
logger.info("Loaded %s samples from directory %s", len(ewkDM_all), gen_dir)


## Fine scan of dim6top
gen_dir = "/afs/hephy.at/data/rschoefbeck02/TopEFT/skims/gen/v2/"

allSampleNames  = glob.glob(gen_dir+"dim6top_LO_ttZ_ll_c*")
allSampleNames  = [ x.replace(gen_dir, '') for x in allSampleNames if glob.glob(x+"/*.root")]
dim6top_central   = Sample.fromDirectory('dim6top_LO_ttZ_ll', directory = [os.path.join( gen_dir, "dim6top_LO_ttZ_ll/")])

dim6top_currents  = []
dim6top_dipoles   = []

logger.info("Loading ewkDM signals")
for s in allSampleNames:
    if len(s) > 50:
        logger.info("Skipping sample %s because I don't know how to categorize it (current or dipole plane).",s)
        continue
    if s.startswith('dim6top_LO_ttZ_ll_cp'):
        dim6top_currents.append(Sample.fromDirectory(s, directory = [os.path.join( gen_dir, "%s/"%s)]))
    elif s.startswith('dim6top_LO_ttZ_ll_ct'):
        dim6top_dipoles.append(Sample.fromDirectory(s, directory = [os.path.join( gen_dir, "%s/"%s)]))
    else:
        logger.info("Don't know what to do with sample %s, can't categorize into current or dipole.", s)

dim6top_currents_names = [ x.name for x in dim6top_currents]
dim6top_dipoles_names = [ x.name for x in dim6top_dipoles]

# Add the coarse scan to the fine scan
for cur in dim6top_currents_daniel:
    if not cur.name in dim6top_currents_names:
        dim6top_currents += [cur]
    
for cur in dim6top_dipoles_daniel:
    if not cur.name in dim6top_dipoles_names:
        dim6top_dipoles += [cur]

dim6top_all = [dim6top_central] + dim6top_currents + dim6top_dipoles
logger.info("Loaded %s samples from directory %s", len(dim6top_all), gen_dir)

