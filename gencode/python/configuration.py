# Standard imports
import os
import time, hashlib, subprocess, uuid
import shutil
import re
import copy
import imp 

# TopEFT
from TopEFT.tools.Cache import Cache
from TopEFT.tools.u_float import u_float
from TopEFT.tools.user import results_directory

# Logger
import logging
logger = logging.getLogger(__name__)

def makeUniquePath():
    ''' Create unique path in tmp directory
    '''

    from TopEFT.tools.user import tmp_directory

    while True:
        uniqueDir = uuid.uuid4().hex
        uniquePath = os.path.join(tmp_directory, uniqueDir)
        if not os.path.isdir(uniquePath): break
        logger.warning( "Path exists, waiting 0.1 sec." )
        time.sleep(0.1)

    return uniquePath

class configuration:
    def __init__(self, model, modified_couplings, cache="xsec_DB.pkl"):

        self.model_name = model
        # Load model
        model_file = os.path.expandvars( "$CMSSW_BASE/python/TopEFT/gencode/models.py" )
        logger.debug( "Loading model %s from file %s", model, model_file )
        try:
            tmp_module = imp.load_source( model, os.path.expandvars( model_file ) ) 
            self.model = getattr(tmp_module, model)
        except:
            logger.error( "Failed to import model %s from %s", model, model_file )
            raise  #raise w/o argument re-raises last exception

        # make work directory
        self.uniquePath = makeUniquePath()
        logger.info( "Using temporary directory %s", self.uniquePath )

        # MG file locations
        data_path = os.path.expandvars( '$CMSSW_BASE/src/TopEFT/gencode/data' )

        # MG5 directories
        self.MG5_tarball     = os.path.join(data_path, 'template', 'MG5_aMC_v2_3_3.tar.gz')
        self.MG5_tmpdir      = os.path.join(self.uniquePath, 'tmpdirMG5')

        # GridPack directories
        self.GP_tarball      = os.path.join(data_path, 'template', 'ttZ01j_5f_MLM_tarball.tar.xz') 
        self.GP_tmpdir       = os.path.join(self.uniquePath, 'centralGridpack')
        self.GP_outputDir    = os.path.join(data_path, 'gridpacks')

        self.processCardDir = os.path.join(data_path, 'processCards')

        # restriction file
        self.restrictCardTemplate = os.path.join(data_path,       'template', 'template_restrict_no_b_mass_'+model+'.dat')
        self.restrictCard         = os.path.join(self.uniquePath, 'restrict_no_b_mass.dat')

        # Cache location
        self.DBFile         = os.path.join(results_directory, cache)
        self.connectDB(self.DBFile)

        # Consistency check of the model: Check that couplings are unique
        all_couplings = [ c[0] for c in sum(self.model.values(),[]) ]
        seen = set()
        uniq = [x for x in all_couplings if x not in seen and not seen.add(x)] 
        if len(seen)!=len(all_couplings): 
            logger.error( "Apparently, list of couplings for model %s is not unique: %s. Check model file %s.", self.model_name, ",".join(all_couplings), model_file )
            raise RuntimeError

        # store couplings
        self.modified_couplings = modified_couplings

        # Check whether couplings are in the model
        for coup in self.modified_couplings.keys():
            if coup not in all_couplings:
                logger.error( "Coupling %s not found in model %s. All available couplings: %s", coup, self.model_name, ",".join(all_couplings) )
                raise RuntimeError

    def setup(self):

        # Now begin with the work
        logger.info( "### SETUP ###" )
        os.makedirs(self.uniquePath)

        # create new directories
        os.makedirs(self.GP_tmpdir)
        os.makedirs(self.MG5_tmpdir)

        logger.info( "Preparing madgraph" )
        subprocess.call(['tar', 'xaf', self.MG5_tarball, '--directory', self.MG5_tmpdir])
        logger.info( "Preparing central gridpack" )
        subprocess.call(['tar', 'xaf', self.GP_tarball,  '--directory', self.GP_tmpdir])

        logger.info( "### FINISHED ###" )

    def connectDB(self,DBFile):
        self.xsecDB = Cache(DBFile)

    def clean(self):
        if os.path.isdir(self.uniquePath):
            logger.info( "Cleaning up, deleting %s"%self.uniquePath )
            #shutil.rmtree(self.uniquePath) #FIXME
