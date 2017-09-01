# Standard imports
import os
import subprocess
import shutil
import re
import copy
import imp 

# TopEFT
from TopEFT.tools.Cache import Cache
from TopEFT.tools.resultsDB import resultsDB
from TopEFT.tools.user import results_directory, tmp_directory
from TopEFT.tools.u_float import u_float

# Logger
import logging
logger = logging.getLogger(__name__)

class Process:
    def __init__(self, process, nEvents, config, xsec_cache = 'xsec_DB.db'):

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

        self.GP_outputDir    = os.path.join(results_directory, 'gridpacks')

        # xsec cache location
        self.xsecDB = resultsDB( os.path.join(results_directory, xsec_cache) )

    def __initialize( self, modified_couplings = None):

        # Initialize setup
        self.config.initialize( modified_couplings )

        # Write process card
        self.__writeProcessCard()
        
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
            f.write("lhapdf = /cvmfs/cms.cern.ch/%s/external/lhapdf/6.1.6/share/LHAPDF/../../bin/lhapdf-config\n" % os.environ["SCRAM_ARCH"] )
            f.write("automatic_html_opening = False\n")

        # Append to run_card.dat
        with open(self.config.uniquePath+'/processtmp/Cards/run_card.dat', 'a') as f:
            f.write("{}  =  nevents\n".format(self.nEvents))
 
    def __writeProcessCard(self):

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

    def xsec(self, modified_couplings = None, overwrite=False):

        key = self.getKey( modified_couplings )
        # Do we have the x-sec?
        if self.xsecDB.contains(key) and not overwrite:
            logger.debug( "Found x-sec %s for key %r. Do nothing.", self.xsecDB.get(key), key )
            return self.xsecDB.get(key)
        else:
            self.__initialize( modified_couplings ) 
            logger.info( "Calculating x-sec" )
            # rerun MG to obtain the correct x-sec (with more events)
            with open(self.config.uniquePath+'/processtmp/Cards/run_card.dat', 'a') as f:
                f.write(".false. =  gridpack\n")
            #subprocess.call(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])
            output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])
            m = re.search("Cross-section :\s*(.*) \pb", output)
            logger.info( "x-sec: {} pb".format(m.group(1)) )

            xsec_ = u_float.fromString(m.group(1)) 
            
            self.xsecDB.add(key, xsec_, save=True)

            logger.info( "Done!" )

            return xsec_

    def makeGridpack(self, modified_couplings = None, overwrite=False):

        # gridpack file name
        key = self.getKey( modified_couplings )
        gridpack = '%s/%s.tar.xz'%(self.GP_outputDir, '_'.join( key ) )
        # Do we have the gridpack?
        if os.path.exists( gridpack ) and not  overwrite: 
            logger.debug( "Found gridpack %s. Do nothing", gridpack )
            return
        else:
            self.__initialize( modified_couplings ) 

            # Make gridpack directory
            if not os.path.exists( self.GP_outputDir ):
                os.makedirs( self.GP_outputDir )

            logger.info( "Preparing gridpack" )
            output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])

            logger.info( "Stitching together all the parts of the gridpack" )
            subprocess.call(['tar', 'xaf', '%s/processtmp/run_01_gridpack.tar.gz'%self.config.uniquePath, '--directory', self.config.uniquePath])
            os.mkdir('%s/process'%self.config.uniquePath)
            shutil.move('%s/madevent'%self.config.uniquePath, '%s/process'%self.config.uniquePath)
            shutil.move('%s/run.sh'%self.config.uniquePath, '%s/process'%self.config.uniquePath)
            shutil.move('%s/mgbasedir'%self.config.GP_tmpdir, self.config.uniquePath)
            shutil.move('%s/runcmsgrid.sh'%self.config.GP_tmpdir, self.config.uniquePath)
            logger.info( "Compressing the gridpack" )
            os.system('cd %s; tar cJpsf %s mgbasedir process runcmsgrid.sh'%(self.config.uniquePath,gridpack))
            #subprocess.call(['cd','%s;'%self.config.uniquePath, 'tar', 'cJpsf', gridpack, 'mgbasedir', 'process', 'runcmsgrid.sh'])
            logger.info( "Done!" )
            logger.info( "The gridpack is now ready to use: %r", gridpack )

            return gridpack

    def diagrams(self, plot_dir):
        self.setup()
        subprocessDir = os.path.join(self.processTmpDir,"SubProcesses")
        subProcessDirs = [ os.path.join(subprocessDir,d) for d in os.listdir(subprocessDir) if os.path.isdir(os.path.join(subprocessDir,d)) ]
        for i,sb in enumerate(subProcessDirs):
            postScriptFiles = [ os.path.join(sb,d) for d in os.listdir(sb) if ".ps" in d ]
            for j,ps in enumerate(postScriptFiles):
                mod_c = self.config.modified_couplings.keys()
                mod_c_str = "_".join( [ "%s_%8.6f"%( k, self.config.modified_couplings[k] ) for k in mod_c ] )
                plot_path = os.path.join(plot_dir, self.config.model_name, "diagrams", self.process, mod_c_str)
                if not os.path.isdir(plot_path):
                    os.makedirs(plot_path)
                subprocess.call(" ".join(["ps2pdf",ps,"%s/Diagrams_%i_%i.pdf"%(plot_path,i,j)]), shell=True)
        
    def getKey(self, modified_couplings):

        mod_c = modified_couplings.keys()
        mod_c.sort()
        
        mod_c_str = "_".join( [ "%s_%8.6f"%( k, modified_couplings[k] ) for k in mod_c ] )
        key = self.config.model_name, self.process, mod_c_str
        return key
