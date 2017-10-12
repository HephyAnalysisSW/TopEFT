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
    from TopEFT.tools.user import data_directory as user_data_directory
    data_directory = user_data_directory 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory = sys.modules['__main__'].postProcessing_directory
except:
  postProcessing_directory = "TopEFT_PP_v4/dilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))


dirs = {}
dirs['ewkDM_ttZ_ll']     = ["ewkDM_ttZ_ll"]
dirs['ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20']     = ["ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000"]
dirs['ewkDM_ttZ_ll_DC1A_0p50_DC1V_0p50']     = ["ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000"]
dirs['ewkDM_ttZ_ll_DC1A_0p50_DC1V_m1p00']    = ['ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000']

dirs['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767']     = ["ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700"]
dirs['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767']     = ["ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700"]
dirs['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767']    = ["ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700"]

dirs['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25']      = ["ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000"]
dirs['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25']     = ["ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000"]
dirs['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25']      = ["ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000"]
dirs['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25']     = ["ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000"]



directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

ewkDM_ttZ_ll = Sample.fromDirectory(name="ewkDM_ttZ_ll",        treeName="Events", isData=False, color=ROOT.kMagenta+2,       texName="#DeltaC_{1,2;V,A}=0",    directory=directories['ewkDM_ttZ_ll'])

ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20     = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20",        treeName="Events", isData=False, color=ROOT.kMagenta,       texName="C_{2A}=0.2, C_{2V}=0.2",    directory=directories['ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20'])

ewkDM_ttZ_ll_DC1A_0p50_DC1V_0p50 = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC1A_0p50_DC1V_0p50", treeName="Events", isData=False, color=ROOT.kMagenta+4, texName="#DeltaC_{1A}=0.5, #DeltaC_{1V}=0.5",    directory=directories['ewkDM_ttZ_ll_DC1A_0p50_DC1V_0p50'])

ewkDM_ttZ_ll_DC1A_0p50_DC1V_m1p00 = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC1A_0p50_DC1V_m1p00", treeName="Events", isData=False, color=1, texName="#DeltaC_{1A}=0.5, #DeltaC_{1V}=-1.0",    directory=directories['ewkDM_ttZ_ll_DC1A_0p50_DC1V_m1p00'])
#ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700

ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767  = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=0.18, C_{2V}=-0.18",    directory=directories['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767'])

ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767  = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=-0.18, C_{2V}=0.18",    directory=directories['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767'])

ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767 = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=-0.18, C_{2V}=-0.18",    directory=directories['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767'])

ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25  = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=0.25, C_{2V}=0",    directory=directories['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25'])

ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25 = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=-0.25, C_{2V}=0",    directory=directories['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25'])

ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25  = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=0, C_{2V}=0.25",    directory=directories['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25'])

ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25 = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=-0.25, C_{2V}=0",    directory=directories['ewkDM_ttZ_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25'])

