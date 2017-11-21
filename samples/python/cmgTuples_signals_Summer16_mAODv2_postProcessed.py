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
  postProcessing_directory = "TopEFT_PP_v11/trilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))


dirs = {}
dirs['ttZ0j_ll']     = ["ttZ0j_ll"]
dirs['ttZ0j_ll_DC2A_0p20_DC2V_0p20']     = ["ttZ0j_ll_DC2A_0p200000_DC2V_0p200000"]
dirs['ttZ0j_ll_DC1A_0p50_DC1V_0p50']     = ["ttZ0j_ll_DC1A_0p500000_DC1V_0p500000"]
dirs['ttZ0j_ll_DC1A_0p50_DC1V_m1p00']    = ['ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000']

dirs['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767']     = ["ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700"]
dirs['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767']     = ["ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700"]
dirs['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767']    = ["ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700"]
dirs['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_0p1767']      = ["ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700"]

dirs['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25']      = ["ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000"]
dirs['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25']     = ["ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000"]
dirs['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25']      = ["ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000"]
dirs['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25']     = ["ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000"]

dirs['ttZ0j_ll_noH']            = ["ttZ0j_ll_noH"]
dirs['ttZ0j_ll_noH_DC2V_0p05']  = ["ttZ0j_ll_noH_DC2V_0p050000"]
dirs['ttZ0j_ll_noH_DC2V_0p10']  = ["ttZ0j_ll_noH_DC2V_0p100000"]
dirs['ttZ0j_ll_noH_DC2V_0p20']  = ["ttZ0j_ll_noH_DC2V_0p200000"]
dirs['ttZ0j_ll_noH_DC2V_0p30']  = ["ttZ0j_ll_noH_DC2V_0p300000"]
dirs['ttZ0j_ll_noH_DC2V_m0p15'] = ["ttZ0j_ll_noH_DC2V_m0p150000"]
dirs['ttZ0j_ll_noH_DC2V_m0p25'] = ["ttZ0j_ll_noH_DC2V_m0p250000"]

dirs['ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2']    = ['ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2']
dirs['ewkDM_TTZToLL_LO']                    = ['ewkDM_TTZToLL_LO']


directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

#ttZ0j_ll = Sample.fromDirectory(name="ttZ0j_ll",        treeName="Events", isData=False, color=ROOT.kMagenta+2,       texName="#DeltaC_{1,2;V,A}=0",    directory=directories['ttZ0j_ll'])
#
#ttZ0j_ll_DC2A_0p20_DC2V_0p20     = Sample.fromDirectory(name="ttZ0j_ll_DC2A_0p20_DC2V_0p20",        treeName="Events", isData=False, color=ROOT.kMagenta,       texName="C_{2A}=0.2, C_{2V}=0.2",    directory=directories['ttZ0j_ll_DC2A_0p20_DC2V_0p20'])
#ttZ0j_ll_DC1A_0p50_DC1V_0p50 = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p50_DC1V_0p50", treeName="Events", isData=False, color=ROOT.kMagenta+4, texName="#DeltaC_{1A}=0.5, #DeltaC_{1V}=0.5",    directory=directories['ttZ0j_ll_DC1A_0p50_DC1V_0p50'])
#ttZ0j_ll_DC1A_0p50_DC1V_m1p00 = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p50_DC1V_m1p00", treeName="Events", isData=False, color=1, texName="#DeltaC_{1A}=0.5, #DeltaC_{1V}=-1.0",    directory=directories['ttZ0j_ll_DC1A_0p50_DC1V_m1p00'])
#
#ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_0p1767   = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_0p1767", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=0.18, C_{2V}=0.18", directory=directories['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_0p1767'])
#ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767  = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=0.18, C_{2V}=-0.18",    directory=directories['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767'])
#ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767  = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=-0.18, C_{2V}=0.18",    directory=directories['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767'])
#ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767 = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=-0.18, C_{2V}=-0.18",    directory=directories['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767'])
#ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25  = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=0.25, C_{2V}=0",    directory=directories['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25'])
#ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25 = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=-0.25, C_{2V}=0",    directory=directories['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25'])
#ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25  = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=0, C_{2V}=0.25",    directory=directories['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25'])
#ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25 = Sample.fromDirectory(name="ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25", treeName="Events", isData=False, color=1, texName="C_{1A/V}=0, C_{2A}=-0.25, C_{2V}=0",    directory=directories['ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25'])
#
#ttZ0j_ll_noH            = Sample.fromDirectory(name="ttZ0j_ll_noH",                 treeName="Events", isData=False, color=1, texName="#DeltaC_{1,2;V,A}=0",                directory=directories['ttZ0j_ll_noH'])
#ttZ0j_ll_noH_DC2V_0p05  = Sample.fromDirectory(name="ttZ0j_ll_noH_DC2V_0p05",   treeName="Events", isData=False, color=1, texName="#DeltaC_{1;V,A}=0, C_{2V}=0.05",     directory=directories['ttZ0j_ll_noH_DC2V_0p05']) 
#ttZ0j_ll_noH_DC2V_0p10  = Sample.fromDirectory(name="ttZ0j_ll_noH_DC2V_0p10",   treeName="Events", isData=False, color=1, texName="#DeltaC_{1;V,A}=0, C_{2V}=0.10",     directory=directories['ttZ0j_ll_noH_DC2V_0p10'])
#ttZ0j_ll_noH_DC2V_0p20  = Sample.fromDirectory(name="ttZ0j_ll_noH_DC2V_0p20",   treeName="Events", isData=False, color=1, texName="#DeltaC_{1;V,A}=0, C_{2V}=0.20",     directory=directories['ttZ0j_ll_noH_DC2V_0p20'])
#ttZ0j_ll_noH_DC2V_0p30  = Sample.fromDirectory(name="ttZ0j_ll_noH_DC2V_0p30",   treeName="Events", isData=False, color=1, texName="#DeltaC_{1;V,A}=0, C_{2V}=0.30",     directory=directories['ttZ0j_ll_noH_DC2V_0p30'])
#ttZ0j_ll_noH_DC2V_m0p15 = Sample.fromDirectory(name="ttZ0j_ll_noH_DC2V_m0p15",  treeName="Events", isData=False, color=1, texName="#DeltaC_{1;V,A}=0, C_{2V}=-0.15",    directory=directories['ttZ0j_ll_noH_DC2V_m0p15'])
#ttZ0j_ll_noH_DC2V_m0p25 = Sample.fromDirectory(name="ttZ0j_ll_noH_DC2V_m0p25",  treeName="Events", isData=False, color=1, texName="#DeltaC_{1;V,A}=0, C_{2V}=-0.25",    directory=directories['ttZ0j_ll_noH_DC2V_m0p25'])

ewkDM_TTZToLL_LO                    = Sample.fromDirectory(name="ewkDM_TTZToLL_LO",                 treeName="Events", isData=False, color=1, texName="#DeltaC_{1,2;V,A}=0",        directory=directories['ewkDM_TTZToLL_LO'])
ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2    = Sample.fromDirectory(name="ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2", treeName="Events", isData=False, color=1, texName="C_{2A}=0.2, C_{2V}=0.2",     directory=directories['ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2'])

allSignals = [\
#    ttZ0j_ll,
#    ttZ0j_ll_DC2A_0p20_DC2V_0p20,
#    ttZ0j_ll_DC1A_0p50_DC1V_0p50,
#    ttZ0j_ll_DC1A_0p50_DC1V_m1p00,
#    ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_m0p1767,
#    ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p1767_DC2V_0p1767,
#    ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_0p1767,
#    ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p1767_DC2V_m0p1767,
#    ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_0p25,
#    ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2A_m0p25,
#    ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_0p25,
#    ttZ0j_ll_DC1A_0p60_DC1V_m0p24_DC2V_m0p25,
#    ttZ0j_ll_noH,
#    ttZ0j_ll_noH_DC2V_0p05,
#    ttZ0j_ll_noH_DC2V_0p10,
#    ttZ0j_ll_noH_DC2V_0p20,
#    ttZ0j_ll_noH_DC2V_0p30,
#    ttZ0j_ll_noH_DC2V_m0p15,
#    ttZ0j_ll_noH_DC2V_m0p25,
    ewkDM_TTZToLL_LO,
    ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2,
    ]
