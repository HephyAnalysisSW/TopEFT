# Standard imports
import os
import subprocess
import shutil
import re
import copy
import imp 
import sys

# TopEFT
from TopEFT.Tools.resultsDB import resultsDB
from TopEFT.Tools.user import results_directory, tmp_directory
from TopEFT.Tools.u_float import u_float

# Logger
import logging
logger = logging.getLogger(__name__)

# Helper
def add_reweight_cmd( filename ):
    '''Helper to add the reweight cmd to the run_cmsgrid.sh
    '''
    c_str = \
"""#reweight if necessary
if [ -e process/madevent/Cards/reweight_card.dat ]; then
    echo "reweighting events"
    mv cmsgrid_final.lhe process/madevent/Events/GridRun_${rnum}/unweighted_events.lhe
    cd process/madevent
    echo "0" |./bin/madevent --debug reweight GridRun_${rnum}
    cd ../..
    mv process/madevent/Events/GridRun_${rnum}/unweighted_events.lhe.gz cmsgrid_final.lhe.gz
    gzip -d  cmsgrid_final.lhe.gz
fi"""
    with open(filename, "r") as in_file:
        buf = in_file.readlines()

    with open(filename, "w") as out_file:
        for line in buf:
            if line.startswith( "./run.sh "):
                line = line + "\n" + c_str + "\n"
            out_file.write(line) 

def make_reweight_card( filename, reweights ):
    import datetime
    with open(filename, "w") as out_file:
        out_file.write("# reweight card file created with https://github.com/danbarto/TopEFT on %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        out_file.write("change rwgt_dir rwgt\n\n")
        for reweight in reweights:
            name = "_".join( [ "%s_%8.6f"%( reweight[2*i], reweight[2*i+1] ) for i in range(len(reweight)/2) ] ) 
            name = name.replace('.','p').replace('-','m')
            out_file.write( "launch --rwgt_name=%s\n"%name )
            for i in range(len(reweight)/2):
                out_file.write("set %s %8.6f\n"%( reweight[2*i], reweight[2*i+1]))
            out_file.write('\n')
    
class Process:
    def __init__(self, process, nEvents, config, xsec_cache = 'xsec_DBv2.db', reweight=False):

        self.process            = process
        self.config             = config
        self.processCardDir     = os.path.join(self.config.data_path, 'processCards')
        self.processCardFile    = process+'.dat'
        self.reweight           = reweight

        # template process card file
        self.templateProcessCard = os.path.join(self.processCardDir, self.processCardFile)
        # temporary process card output
        self.tmpProcessCard = os.path.join(self.config.uniquePath, self.processCardFile)

        # temporary process output directory
        self.processTmpDir = os.path.join( self.config.uniquePath, 'processtmp' )
        self.nEvents = nEvents

        self.GP_outputDir    = os.path.join(results_directory, 'gridpacks')

        # xsec cache location
        columns = ["process", "nEvents"]+self.config.all_model_couplings
        self.xsecDB = resultsDB( os.path.join(results_directory, xsec_cache), self.config.model_name, columns )

    def __initialize( self, modified_couplings = None):

        # Initialize setup
        self.config.initialize( modified_couplings)

        # Write process card
        self.__writeProcessCard()
        
        logger.info( "Running MG executable: python %s -f %s", self.config.MG5_tmpdir+'/bin/mg5_aMC', self.tmpProcessCard )
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
        
        # copy reweight cards
        if self.reweight:
            source = os.path.join( self.config.data_path,  'template', 'template_reweight_card_'+self.config.model_name+'.dat')
            target = os.path.join( self.processTmpDir, 'Cards', 'reweight_card.dat' )
            print target
            shutil.copyfile( source, target )
            if os.path.isfile(target):
                logger.debug( "Done with %s -> %s", source, target )
            else:
                logger.info("File copy failed. WTF!")
        

        # Append to me5_configuration.txt 
        with open( os.path.join( self.processTmpDir, 'Cards/me5_configuration.txt'), 'a') as f:
            f.write("run_mode = 2\n")
            f.write("nb_core = 4\n")
            f.write("lhapdf = /cvmfs/cms.cern.ch/%s/external/lhapdf/6.1.6/share/LHAPDF/../../bin/lhapdf-config\n" % os.environ["SCRAM_ARCH"] )
            f.write("automatic_html_opening = False\n")

        # Append to run_card.dat
        with open( os.path.join( self.processTmpDir, 'Cards/run_card.dat'), 'a') as f:
            f.write("{}  =  nevents\n".format(self.nEvents))
 
    def __writeProcessCard(self):

        out = open(self.tmpProcessCard, 'w')
        with open(self.templateProcessCard, 'r') as f:  #FIXME (somewhat dirty)
            for line in f:
                if "import model" in line:
                    out.write("import model %s-no_b_mass\n\n"%self.config.model_name)
                elif "NP=1" in line and self.config.model_name == "TopEffTh":
                    out.write(line.replace("NP=1","NP=2"))
                elif "NP=1" in line and self.config.model_name == "dim6top_LO":
                    #out.write(line.replace("NP=1","DIM6=1"))
                    out.write(line.replace("NP=1","DIM6<=1"))
                else:
                    out.write(line)
            out.write("output %s -nojpeg" % self.processTmpDir)
        out.close()
        logger.info( "Written process card to %s", self.tmpProcessCard )

    def xsec(self, modified_couplings = None, overwrite=False, skip=False):

        key = self.getKey( modified_couplings )
        # Do we have the x-sec?
        if self.xsecDB.contains(key) and not overwrite:
            logger.debug( "Found x-sec %s for key %r. Do nothing.", self.xsecDB.get(key), key )
            return self.xsecDB.get(key)
        elif skip:
            return u_float(0)
        else:
            print "Trying to get xsec"
            self.__initialize( modified_couplings ) 
            logger.info( "Calculating x-sec" )
            # rerun MG to obtain the correct x-sec (with more events)
            with open( os.path.join( self.processTmpDir, 'Cards/run_card.dat'), 'a') as f:
                f.write(".false. =  gridpack\n")
            logger.info( "Calculate x-sec: Calling bin/generate_events" )
            output = subprocess.check_output([ os.path.join( self.processTmpDir, 'bin/generate_events') , '-f'])
            for i in range(10):
                try:
                    output = subprocess.check_output([ os.path.join( self.processTmpDir, 'bin/generate_events') , '-f'])
                    m = re.search("Cross-section :\s*(.*) \pb", output)
                    logger.info( "x-sec: {} pb".format(m.group(1)) )
                    break
                except ValueError:
                    logger.info("Encountered problem during the MG run. Restarting.")

            xsec_ = u_float.fromString(m.group(1)) 
            
            self.xsecDB.add(key, xsec_, overwrite=True)

            logger.info( "Done!" )

            return xsec_

    def makeGridpack(self, modified_couplings = None, overwrite=False, reweights = None):

        do_reweight = len(reweights)>0
        postfix = "_reweight" if do_reweight else ""

        # gridpack file name
        gridpack = '%s/%s%s.tar.xz'%(self.GP_outputDir, self.getGridpackFileName( modified_couplings ), postfix )
        # Do we have the gridpack?
        if os.path.exists( gridpack ) and not overwrite: 
            logger.info( "Found gridpack %s. Do nothing", gridpack )
            return
        else:
            logger.info( "Will create gridpack %s", gridpack )
            self.__initialize( modified_couplings ) 

            # Make gridpack directory
            if not os.path.exists( self.GP_outputDir ):
                os.makedirs( self.GP_outputDir )

            logger.info( "Preparing gridpack" )
            #print "Testing reweighting"
            if self.reweight:
                # not yet working
                output = subprocess.check_output([os.path.join( self.config.uniquePath, 'processtmp/bin/generate_events' ), 'reweight', '-f'])
            else:
                output = subprocess.check_output([os.path.join( self.config.uniquePath, 'processtmp/bin/generate_events' ), '-f'])

            logger.info( "Stitching together all the parts of the gridpack" )
            subprocess.call(['tar', 'xaf', os.path.join( self.config.uniquePath, 'processtmp/run_01_gridpack.tar.gz'), '--directory', self.config.uniquePath])

            # create fresh processpath
            process_path = os.path.join( self.config.uniquePath, 'process')
            if os.path.exists( process_path ): shutil.rmtree( process_path ) 
            os.mkdir( process_path )

            # madevent directory
            shutil.copytree(os.path.join( self.config.uniquePath,  'madevent'),   os.path.join( process_path , 'madevent') )

            # run.sh
            shutil.copy(os.path.join( self.config.uniquePath,  'run.sh'),         process_path )

            # mgbasedir 
            mgbasedir_gridpack = os.path.join(self.config.uniquePath, 'mgbasedir')
            if os.path.exists( mgbasedir_gridpack ): shutil.rmtree( mgbasedir_gridpack )
            shutil.copytree(os.path.join( self.config.GP_tmpdir,   'mgbasedir'),  mgbasedir_gridpack )

            # runcmsgrid.sh
            shutil.copy(os.path.join( self.config.GP_tmpdir,   'runcmsgrid.sh'),  self.config.uniquePath )

            if do_reweight:
                # copy models directory (for reweighting )
                source_models = os.path.join( self.config.MG5_tmpdir, 'models' )
                target_models = os.path.join( self.config.uniquePath, 'mgbasedir', 'models' )
                logger.info( "Copying models directory %s -> %s", source_models, target_models )
                if os.path.exists( target_models ): shutil.rmtree( target_models )
                shutil.copytree( source_models, target_models )
                # modify runcmsgrid.sh
                rungrid_sh_file = os.path.join( self.config.uniquePath, 'runcmsgrid.sh' )
                logger.info( "Modify runcmsgrid.sh for reweighting." )
                logger.debug( "runcmsgrid.sh at %s", rungrid_sh_file )
                add_reweight_cmd( rungrid_sh_file )
                logger.info( "Make reweight card file.")
                # reweight card file
                reweight_card_file = os.path.join( self.config.uniquePath, 'process/madevent/Cards/reweight_card.dat' )
                logger.debug( "Reweight card file is %s", reweight_card_file)
                make_reweight_card( reweight_card_file , reweights ) 

            logger.info( "Compressing the gridpack" )
            os.system('cd %s; tar cJpsf %s mgbasedir process runcmsgrid.sh'%(self.config.uniquePath,gridpack))

            logger.info( "Done!" )
            logger.info( "The gridpack is now ready to use: %r", gridpack )

            return gridpack

    def diagrams(self, plot_dir, modified_couplings):
        self.__initialize( modified_couplings )
        subprocessDir = os.path.join(self.processTmpDir,"SubProcesses")
        subProcessDirs = [ os.path.join(subprocessDir,d) for d in os.listdir(subprocessDir) if os.path.isdir(os.path.join(subprocessDir,d)) ]
        for i,sb in enumerate(subProcessDirs):
            postScriptFiles = [ os.path.join(sb,d) for d in os.listdir(sb) if ".ps" in d ]
            for j,ps in enumerate(postScriptFiles):
                mod_c = modified_couplings.keys()
                mod_c_str = "_".join( [ "%s_%8.6f"%( k, modified_couplings[k] ) for k in mod_c ] )
                plot_path = os.path.join(plot_dir, self.config.model_name, "diagrams", self.process, mod_c_str)
                if not os.path.isdir(plot_path):
                    os.makedirs(plot_path)
                subprocess.call(" ".join(["ps2pdf",ps,"%s/Diagrams_%i_%i.pdf"%(plot_path,i,j)]), shell=True)
        
    def getGridpackFileName(self, modified_couplings):

        mod_c = modified_couplings.keys()
        mod_c.sort()
        
        mod_c_str = "_".join( [ "%s_%8.6f"%( k, modified_couplings[k] ) for k in mod_c if modified_couplings[k]!=self.config.default_model_couplings[k] ] )
        return ( '_'.join( [self.config.model_name, self.process, mod_c_str.replace('.','p').replace('-','m') ])).rstrip('_')
    
    def getKey(self, modified_couplings):
        key = {"process":self.process, "nEvents":self.nEvents}
        for k in self.config.all_model_couplings:
            if k in modified_couplings.keys():
                key[k] = float(modified_couplings[k])
            else:
                key[k] = self.config.default_model_couplings[k]
        return key
    
    def hasXSec(self, modified_couplings):
        return self.xsecDB.contains(self.getKey(modified_couplings=modified_couplings))
