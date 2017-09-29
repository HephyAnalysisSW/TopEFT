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
  postProcessing_directory = "TopEFT_PP_v1/dilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))


dirs = {}
dirs['ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20']     = ["ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000"]

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20     = Sample.fromDirectory(name="ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20",        treeName="Events", isData=False, color=ROOT.kMagenta,       texName="C_{2A}=0.2, C_{2V}=0.2",    directory=directories['ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20'])
