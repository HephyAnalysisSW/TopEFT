import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

from TopEFT.samples.color import color

# Data directory
try:
    data_directory = sys.modules['__main__'].data_directory
except:
    #from TopEFT.Tools.user import data_directory as user_data_directory
    data_directory = '/afs/hephy.at/data/rschoefbeck02/cmgTuples/' 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory = sys.modules['__main__'].postProcessing_directory
except:
  postProcessing_directory = "TopEFT_PP_v11/trilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}

dirs['ttZ0j_ll'] = ['ttZ0j_ll']
dirs['ttZ0j_ll_cuW_0p100000'] = ['ttZ0j_ll_cuW_0p100000']
dirs['ttZ0j_ll_cuW_0p200000'] = ['ttZ0j_ll_cuW_0p200000']
dirs['ttZ0j_ll_cuW_0p300000'] = ['ttZ0j_ll_cuW_0p300000']
dirs['ttZ0j_ll_cuW_m0p100000'] = ['ttZ0j_ll_cuW_m0p100000']
dirs['ttZ0j_ll_cuW_m0p200000'] = ['ttZ0j_ll_cuW_m0p200000']
dirs['ttZ0j_ll_cuW_m0p300000'] = ['ttZ0j_ll_cuW_m0p300000']
dirs['ttZ0j_ll_DC1A_0p500000_DC1V_0p500000'] = ['ttZ0j_ll_DC1A_0p500000_DC1V_0p500000']
dirs['ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000'] = ['ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000']
dirs['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700'] = ['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700']
dirs['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700'] = ['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700']
dirs['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000'] = ['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000']
dirs['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700'] = ['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700']
dirs['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700'] = ['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700']
dirs['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000'] = ['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000']
dirs['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000'] = ['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000']
dirs['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000'] = ['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000']
dirs['ttZ0j_ll_DC1A_1p000000'] = ['ttZ0j_ll_DC1A_1p000000']
dirs['ttZ0j_ll_DC2A_0p200000_DC2V_0p200000'] = ['ttZ0j_ll_DC2A_0p200000_DC2V_0p200000']

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

#ewkDM_TTZToLL_LO                    = Sample.fromDirectory(name="ewkDM_TTZToLL_LO",                 treeName="Events", isData=False, color=1, texName="#DeltaC_{1,2;V,A}=0",        directory=directories['ewkDM_TTZToLL_LO'])
#ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2    = Sample.fromDirectory(name="ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2", treeName="Events", isData=False, color=1, texName="C_{2A}=0.2, C_{2V}=0.2",     directory=directories['ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2'])


ttZ0j_ll                        = Sample.fromDirectory(name="ttZ0j_ll", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttZ0j_ll'])

#HEL_UFO
ttZ0j_ll_cuW_0p100000           = Sample.fromDirectory(name="ttZ0j_ll_cuW_0p100000", treeName="Events", isData=False, color=1, texName="c_{uW}=0.1", directory=directories['ttZ0j_ll_cuW_0p100000'])
ttZ0j_ll_cuW_0p200000           = Sample.fromDirectory(name="ttZ0j_ll_cuW_0p200000", treeName="Events", isData=False, color=1, texName="c_{uW}=0.2", directory=directories['ttZ0j_ll_cuW_0p200000'])
ttZ0j_ll_cuW_0p300000           = Sample.fromDirectory(name="ttZ0j_ll_cuW_0p300000", treeName="Events", isData=False, color=1, texName="c_{uW}=0.3", directory=directories['ttZ0j_ll_cuW_0p300000'])
ttZ0j_ll_cuW_m0p100000          = Sample.fromDirectory(name="ttZ0j_ll_cuW_m0p100000", treeName="Events", isData=False, color=1, texName="c_{uW}=0.1", directory=directories['ttZ0j_ll_cuW_m0p100000'])
ttZ0j_ll_cuW_m0p200000          = Sample.fromDirectory(name="ttZ0j_ll_cuW_m0p200000", treeName="Events", isData=False, color=1, texName="c_{uW}=-0.2", directory=directories['ttZ0j_ll_cuW_m0p200000'])
ttZ0j_ll_cuW_m0p300000          = Sample.fromDirectory(name="ttZ0j_ll_cuW_m0p300000", treeName="Events", isData=False, color=1, texName="c_{uW}=-0.3", directory=directories['ttZ0j_ll_cuW_m0p300000'])

# Markus' standard point
ttZ0j_ll_DC2A_0p200000_DC2V_0p200000                                = Sample.fromDirectory(name="ttZ0j_ll_DC2A_0p200000_DC2V_0p200000", treeName="Events", isData=False, color=1, texName="C_{2,V}=0.2, C_{2,A}=0.2", directory=directories['ttZ0j_ll_DC2A_0p200000_DC2V_0p200000'])

# current ellipsis
ttZ0j_ll_DC1A_0p500000_DC1V_0p500000                                = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p500000_DC1V_0p500000", treeName="Events", isData=False, color=1, texName="#DeltaC_{1,V}=0.5, #DeltaC_{1,A}=0.5", directory=directories['ttZ0j_ll_DC1A_0p500000_DC1V_0p500000'])
ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000                               = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000", treeName="Events", isData=False, color=1, texName="#DeltaC_{1,V}=-1, #DeltaC_{1,A}=0.5", directory=directories['ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000'])
ttZ0j_ll_DC1A_1p000000                                              = Sample.fromDirectory(name="ttZ0j_ll_DC1A_1p000000", treeName="Events", isData=False, color=1, texName="#DeltaC_{1,V}=0, #DeltaC_{1,A}=1", directory=directories['ttZ0j_ll_DC1A_1p000000'])

# dipole ellipsis
ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700   = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700", treeName="Events", isData=False, color=1, texName="C_{1,V,A}=0, C_{2,V}=0.176, C_{2,A}=0.176", directory=directories['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700'])
ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700  = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700", treeName="Events", isData=False, color=1, texName="C_{1,V,A}=0, C_{2,V}=-0.176, C_{2,A}=0.176", directory=directories['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700'])
ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000                 = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000", treeName="Events", isData=False, color=1, texName="C_{1,V,A}=0, C_{2,V}=0, C_{2,A}=0.25", directory=directories['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000'])
ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700  = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700", treeName="Events", isData=False, color=1, texName="C_{1,V,A}=0, C_{2,V}=0.176, C_{2,A}=-0.176", directory=directories['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700'])
ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700 = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700", treeName="Events", isData=False, color=1, texName="C_{1,V,A}=0, C_{2,V}=-0.176, C_{2,A}=-0.176", directory=directories['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700'])
ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000                = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000", treeName="Events", isData=False, color=1, texName="C_{1,V,A}=0, C_{2,V}=0, C_{2,A}=-0.25", directory=directories['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000'])
ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000                = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000", treeName="Events", isData=False, color=1, texName="C_{1,V,A}=0, C_{2,V}=-0.25, C_{2,A}=0", directory=directories['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000'])
ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000                = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000", treeName="Events", isData=False, color=1, texName="C_{1,V,A}=0, C_{2,V}=-0.25, C_{2,A}=0", directory=directories['ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000'])



allSignals = [\
    # default
    ttZ0j_ll,
    # Markus' point
    ttZ0j_ll_DC2A_0p200000_DC2V_0p200000,

    # HEL_UFO
    ttZ0j_ll_cuW_0p100000,
    ttZ0j_ll_cuW_0p200000,
    ttZ0j_ll_cuW_0p300000,
    ttZ0j_ll_cuW_m0p100000,
    ttZ0j_ll_cuW_m0p200000,
    ttZ0j_ll_cuW_m0p300000,

    # current ellipsis
    ttZ0j_ll_DC1A_1p000000,
    ttZ0j_ll_DC1A_0p500000_DC1V_0p500000,
    ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000,

    # dipole ellipsis
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700,
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700,
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000,
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700,
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700,
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000,
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000,
    ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000,
    ]
