# Standard imports
import os
import time, subprocess
import shutil
import re
import imp 
import copy 

# TopEFT
from TopEFT.tools.user import results_directory

# Logger
import logging
logger = logging.getLogger(__name__)

def makeUniquePath():
    ''' Create unique path in tmp directory
    '''

    from TopEFT.tools.user import tmp_directory
    import uuid

    while True:
        uniqueDir = uuid.uuid4().hex
        uniquePath = os.path.join(tmp_directory, uniqueDir)
        if not os.path.isdir(uniquePath): break
        logger.warning( "Path exists, waiting 0.1 sec." )
        time.sleep(0.1)

    return uniquePath

class Configuration:
    def __init__(self, model_name, modified_couplings):

        self.model_name = model_name

        # Load model
        model_file = os.path.expandvars( "$CMSSW_BASE/python/TopEFT/gencode/models.py" )
        logger.debug( "Loading model %s from file %s", model_name, model_file )
        try:
            tmp_module = imp.load_source( model_name, os.path.expandvars( model_file ) ) 
            self.model = getattr(tmp_module, model_name)
        except:
            logger.error( "Failed to import model %s from %s", model_name, model_file )
            raise  #raise w/o argument re-raises last exception

        # make work directory
        self.uniquePath = makeUniquePath()
        logger.info( "Using temporary directory %s", self.uniquePath )

        # MG file locations
        self.data_path = os.path.expandvars( '$CMSSW_BASE/src/TopEFT/gencode/data' )

        # MG5 directories
        self.MG5_tarball     = os.path.join(self.data_path, 'template', 'MG5_aMC_v2_3_3.tar.gz')
        self.MG5_tmpdir      = os.path.join(self.uniquePath, 'tmpdirMG5')

        # GridPack directories
        self.GP_tarball      = os.path.join(self.data_path, 'template', 'ttZ01j_5f_MLM_tarball.tar.xz') 
        self.GP_tmpdir       = os.path.join(self.uniquePath, 'centralGridpack')

        # restriction file
        self.restrictCardTemplate = os.path.join( self.data_path,  'template', 'template_restrict_no_b_mass_'+model_name+'.dat')
        self.restrictCard         = os.path.join( self.MG5_tmpdir, 'models', self.model_name, 'restrict_no_b_mass.dat' ) 

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

    def setup( self ):
        ''' Create temporary directories and unzip GP. 
        Time consuming. '''

        # Now begin with the work
        logger.info( "########### Configuration ###########" )
        os.makedirs(self.uniquePath)

        # create new directories
        os.makedirs(self.GP_tmpdir)
        os.makedirs(self.MG5_tmpdir)

        logger.info( "Preparing madgraph" )
        subprocess.call(['tar', 'xaf', self.MG5_tarball, '--directory', self.MG5_tmpdir])
        logger.info( "Preparing central gridpack" )
        subprocess.call(['tar', 'xaf', self.GP_tarball,  '--directory', self.GP_tmpdir])

        logger.debug( 'Creating restriction file based on template %s', self.restrictCardTemplate )
        # make block strings to be inserted into template file
        block_strings = {}
        for block in self.model.keys():
            
            # copy defaults
            couplings = copy.deepcopy(self.model[block])
            
            # make modifications & build string for the template file
            block_strings[block+'_template_string'] = ""
            for i_coupling, coupling in enumerate(couplings):       # coupling is a pair (name, value) 
                if self.modified_couplings.has_key( coupling[0] ):
                    coupling[1] = self.modified_couplings[coupling[0]]
                block_strings[block+'_template_string'] += "%6i %8.6f # %s\n"%( i_coupling + 1, coupling[1], coupling[0] )
        
        # read template file
        with open(self.restrictCardTemplate, 'r') as f:
            template_string = f.read()

        out = open(self.restrictCard, 'w')
        out.write(template_string.format( **block_strings ) )
        out.close()

        logger.debug( 'Written restriction file %s', self.restrictCard )
        logger.info( "########### Configuration finished ###########" )

    def cleanup(self):
        if os.path.isdir(self.uniquePath):
            logger.info( "Cleaning up, deleting %s"%self.uniquePath )
            #shutil.rmtree(self.uniquePath) #FIXME
