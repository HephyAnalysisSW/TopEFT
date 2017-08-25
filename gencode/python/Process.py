# Standard imports
import os
import subprocess
import shutil
import re
import copy
import imp 

# TopEFT
from TopEFT.tools.Cache import Cache
from TopEFT.tools.user import results_directory, tmp_directory

# Logger
import logging
logger = logging.getLogger(__name__)

class Process:
    def __init__(self, process, nEvents, config, xsec_cache = 'xsec_DB.pkl'):

        self.process            = process
        self.config             = config
        self.processCardDir     = os.path.join(self.config.data_path, 'processCards')
        self.processCardFile    = process+'.dat'

        # template process card file
        self.templateProcessCard = os.path.join(self.processCardDir, self.processCardFile)
        # temporary process card output
        self.tmpProcessCard = os.path.join(self.config.uniquePath, self.processCardFile)

        # temporary process output directory
        self.processTmpDir = os.path.join( self.config.uniquePath, 'processtmp' )
        self.nEvents = nEvents

        self.GP_outputDir    = os.path.join(tmp_directory, 'gridpacks')

        # xsec cache location
        self.xsecDB = Cache( os.path.join(results_directory, xsec_cache) )
 
    def writeProcessCard(self):

        out = open(self.tmpProcessCard, 'w')
        with open(self.templateProcessCard, 'r') as f:  #FIXME (somewhat dirty)
            for line in f:
                if "import model" in line:
                    out.write("import model %s-no_b_mass\n\n"%self.config.model_name)
                elif "NP=1" in line and self.config.model_name == "TopEffTh":
                    out.write(line.replace("NP=1","NP=2"))
                else:
                    out.write(line)
            out.write("output %s -nojpeg" % self.processTmpDir)
        out.close()
        logger.info( "Written process card to %s", self.tmpProcessCard )

    def setup( self ):

            # Initialize setup
            self.config.setup()

            # Write process card
            self.writeProcessCard()
            
            logger.info( "Running MG executable on %s", self.tmpProcessCard )
            subprocess.check_output(["python", self.config.MG5_tmpdir+'/bin/mg5_aMC', '-f', self.tmpProcessCard])
            logger.info( "Done with MG executable" ) 

            # copy files from central gridpack
            for filename in [ 
                'run_card.dat', 
                'grid_card.dat',
                'me5_configuration.txt',
                ] :
                logger.info(  "Copying files from GP directory to temporary process directory: %s", filename )
                source = os.path.join( self.config.GP_tmpdir, 'process/madevent/Cards', filename )
                target = os.path.join( self.processTmpDir, 'Cards', filename )
                shutil.copyfile( source, target )
                logger.debug( "Done with %s -> %s", source, target )

            # Append to me5_configuration.txt 
            with open(self.config.uniquePath+'/processtmp/Cards/me5_configuration.txt', 'a') as f:
                f.write("run_mode = 2\n")
                f.write("nb_core = 4\n")
                f.write("lhapdf = /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/lhapdf/6.1.6/share/LHAPDF/../../bin/lhapdf-config\n")
                f.write("automatic_html_opening = False\n")

            # Append to run_card.dat
            with open(self.config.uniquePath+'/processtmp/Cards/run_card.dat', 'a') as f:
                f.write("{}  =  nevents\n".format(self.nEvents))

    def xsec(self, overwrite=False):

        if self.xsecDB.contains(self.getKey()) and not  overwrite:
            return self.xsecDB.get(self.getKey())
        else:
           
            # call process setup 
            self.setup()           
 
            logger.info( "Calculating x-sec" )
            # rerun MG to obtain the correct x-sec (with more events)
            with open(self.config.uniquePath+'/processtmp/Cards/run_card.dat', 'a') as f:
                f.write(".false. =  gridpack\n")
            #subprocess.call(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])
            output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])
            m = re.search("Cross-section :\s*(.*) \pb", output)
            logger.info( "x-sec: {} pb".format(m.group(1)) )

            xsec_ = m.group(1)
            
            self.xsecDB.add(self.getKey(), xsec_, save=True)

            logger.info( "Done!" )

            return xsec_

    def gridpack(self, overwrite=False):

        # gridpack file name
        self.gridpack = '%s/%s.tar.xz'%(self.GP_outputDir, '_'.join( self.getKey() ) )

        if not os.path.exists( self.gridpack ) or overwrite: 

            # call process setup 
            self.setup()           
 
            logger.info( "Preparing first part of gridpack" )
            output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])

            logger.info( "Stitching together all the parts of the gridpack" )
            subprocess.call(['tar', 'xaf', '%s/processtmp/run_01_gridpack.tar.gz'%self.config.uniquePath, '--directory', self.config.uniquePath])
            os.mkdir('%s/process'%self.config.uniquePath)
            shutil.move('%s/madevent'%self.config.uniquePath, '%s/process'%self.config.uniquePath)
            shutil.move('%s/run.sh'%self.config.uniquePath, '%s/process'%self.config.uniquePath)
            shutil.move('%s/mgbasedir'%self.config.GP_tmpdir, self.config.uniquePath)
            shutil.move('%s/runcmsgrid.sh'%self.config.GP_tmpdir, self.config.uniquePath)
            logger.info( "Compressing the gridpack" )
            os.system('cd %s; tar cJpsf %s mgbasedir process runcmsgrid.sh'%(self.config.uniquePath,self.gridpack))
            #subprocess.call(['cd','%s;'%self.config.uniquePath, 'tar', 'cJpsf', self.gridpack, 'mgbasedir', 'process', 'runcmsgrid.sh'])
            logger.info( "Done!" )
            logger.info( "The gridpack is now ready to use: %r", self.gridpack )

    def getKey(self):

        mod_c = self.config.modified_couplings.keys()
        mod_c.sort()
        
        mod_c_str = "_".join( [ "%s_%8.6f"%( k, self.config.modified_couplings[k] ) for k in mod_c ] )
        key = self.config.model_name, self.process, mod_c_str
        return key
