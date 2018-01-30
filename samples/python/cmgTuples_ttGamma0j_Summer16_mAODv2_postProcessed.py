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
    data_directory = '/afs/hephy.at/data/rschoefbeck01/cmgTuples/' 

# Take post processing directory if defined in main module
try:
  import sys
  postProcessing_directory = sys.modules['__main__'].postProcessing_directory
except:
  postProcessing_directory = "TopEFT_PP_v14/dilep/"

logger.info("Loading MC samples from directory %s", os.path.join(data_directory, postProcessing_directory))

dirs = {}

dirs['ttGamma0j_ll_DAG_0p176700_DVG_0p176700']  = ['ttGamma0j_ll_DAG_0p176700_DVG_0p176700']
dirs['ttGamma0j_ll_DAG_0p176700_DVG_m0p176700'] = ['ttGamma0j_ll_DAG_0p176700_DVG_m0p176700']
dirs['ttGamma0j_ll_DAG_0p250000']               = ['ttGamma0j_ll_DAG_0p250000']
dirs['ttGamma0j_ll_DAG_0p500000']               = ['ttGamma0j_ll_DAG_0p500000']
dirs['ttGamma0j_ll_DAG_m0p176700_DVG_0p176700'] = ['ttGamma0j_ll_DAG_m0p176700_DVG_0p176700']
dirs['ttGamma0j_ll_DAG_m0p176700_DVG_m0p176700']= ['ttGamma0j_ll_DAG_m0p176700_DVG_m0p176700']
dirs['ttGamma0j_ll_DAG_m0p250000']              = ['ttGamma0j_ll_DAG_m0p250000']
dirs['ttGamma0j_ll_DAG_m0p500000']              = ['ttGamma0j_ll_DAG_m0p500000']
dirs['ttGamma0j_ll_DVG_0p250000']               = ['ttGamma0j_ll_DVG_0p250000']
dirs['ttGamma0j_ll_DVG_0p500000']               = ['ttGamma0j_ll_DVG_0p500000']
dirs['ttGamma0j_ll_DVG_m0p250000']              = ['ttGamma0j_ll_DVG_m0p250000']
dirs['ttGamma0j_ll_DVG_m0p500000']              = ['ttGamma0j_ll_DVG_m0p500000']

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

#ewkDMGZ

#ttGamma0j_ll                        = Sample.fromDirectory(name="ttGamma0j_ll", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll'])
ttGamma0j_ll_DAG_0p176700_DVG_0p176700 = Sample.fromDirectory(name="ttGamma0j_ll_DAG_0p176700_DVG_0p176700", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DAG_0p176700_DVG_0p176700'])
ttGamma0j_ll_DAG_0p176700_DVG_m0p176700 = Sample.fromDirectory(name="ttGamma0j_ll_DAG_0p176700_DVG_m0p176700", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DAG_0p176700_DVG_m0p176700'])
ttGamma0j_ll_DAG_0p250000 = Sample.fromDirectory(name="ttGamma0j_ll_DAG_0p250000", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DAG_0p250000'])
ttGamma0j_ll_DAG_0p500000 = Sample.fromDirectory(name="ttGamma0j_ll_DAG_0p500000", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DAG_0p500000'])
ttGamma0j_ll_DAG_m0p176700_DVG_0p176700 = Sample.fromDirectory(name="ttGamma0j_ll_DAG_m0p176700_DVG_0p176700", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DAG_m0p176700_DVG_0p176700'])
ttGamma0j_ll_DAG_m0p176700_DVG_m0p176700 = Sample.fromDirectory(name="ttGamma0j_ll_DAG_m0p176700_DVG_m0p176700", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DAG_m0p176700_DVG_m0p176700'])
ttGamma0j_ll_DAG_m0p250000 = Sample.fromDirectory(name="ttGamma0j_ll_DAG_m0p250000", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DAG_m0p250000'])
ttGamma0j_ll_DAG_m0p500000 = Sample.fromDirectory(name="ttGamma0j_ll_DAG_m0p500000", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DAG_m0p500000'])
ttGamma0j_ll_DVG_0p250000 = Sample.fromDirectory(name="ttGamma0j_ll_DVG_0p250000", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DVG_0p250000'])
ttGamma0j_ll_DVG_0p500000 = Sample.fromDirectory(name="ttGamma0j_ll_DVG_0p500000", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DVG_0p500000'])
ttGamma0j_ll_DVG_m0p250000 = Sample.fromDirectory(name="ttGamma0j_ll_DVG_m0p250000", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DVG_m0p250000'])
ttGamma0j_ll_DVG_m0p500000 = Sample.fromDirectory(name="ttGamma0j_ll_DVG_m0p500000", treeName="Events", isData=False, color=1, texName="SM", directory=directories['ttGamma0j_ll_DVG_m0p500000'])


allSignals = [\

    #ttGamma0j_ll,
    ttGamma0j_ll_DAG_0p176700_DVG_0p176700,
    ttGamma0j_ll_DAG_0p176700_DVG_m0p176700,
    ttGamma0j_ll_DAG_0p250000,
    ttGamma0j_ll_DAG_0p500000,
    ttGamma0j_ll_DAG_m0p176700_DVG_0p176700,
    ttGamma0j_ll_DAG_m0p176700_DVG_m0p176700,
    ttGamma0j_ll_DAG_m0p250000,
    ttGamma0j_ll_DAG_m0p500000,
    ttGamma0j_ll_DVG_0p250000,
    ttGamma0j_ll_DVG_0p500000,
    ttGamma0j_ll_DVG_m0p250000,
    ttGamma0j_ll_DVG_m0p500000,
    ]
