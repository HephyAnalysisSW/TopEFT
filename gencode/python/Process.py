# Standard imports
import os
import subprocess
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

class Process:
    def __init__(self, process, nEvents, config):
        self.process = process
        self.processCard = process+'.dat'
        self.nEvents = nEvents
        self.config = config
        self.xsec = 0
        self.gridpack = "None"
        
    def updateRestrictCard(self):
        # make block strings to be inserted into template file
        block_strings = {}
        for block in self.config.model.keys():

            # copy defaults
            couplings = copy.deepcopy(self.config.model[block])

            # make modifications & build string for the template file
            block_strings[block+'_template_string'] = ""
            for i_coupling, coupling in enumerate(couplings):       # coupling is a pair (name, value) 
                if self.config.modified_couplings.has_key( coupling[0] ):
                    coupling[1] = self.config.modified_couplings[coupling[0]]
                block_strings[block+'_template_string'] += "%6i %8.6f # %s\n"%( i_coupling + 1, coupling[1], coupling[0] )

        # read template file
        with open(self.config.restrictCardTemplate, 'r') as f:
            template_string = f.read()            
                 
        # output file
        out = open(self.config.restrictCard, 'w')
        out.write(template_string.format( **block_strings ) ) 
        out.close()

    def writeProcessCard(self):
        templateProcessCard = os.path.join(self.config.processCardDir,self.processCard)
        self.tmpProcessCard = os.path.join(self.config.uniquePath,self.processCard)
        out = open(self.tmpProcessCard, 'w')
        with open(templateProcessCard, 'r') as f:
            for line in f:
                if "import model" in line:
                    out.write("import model %s-no_b_mass\n\n"%self.config.model_name)
                elif "NP=1" in line and self.config.model_name == "TopEffTh":
                    out.write(line.replace("NP=1","NP=2"))
                else:
                    out.write(line)
            out.write("output {} -nojpeg".format(self.config.uniquePath+'/processtmp'))
        out.close()

    def run(self, keepGridpack=True, overwrite=False):
        if not self.config.xsecDB.contains(self.getKey()) or overwrite:

            self.updateRestrictCard()

            shutil.copyfile(self.config.restrictCard, self.config.MG5_tmpdir+'/models/'+self.config.model_name+'/restrict_no_b_mass.dat')
            
            self.writeProcessCard()
            
            logger.info( "Calculating diagrams" )
            output = subprocess.check_output(["python",self.config.MG5_tmpdir+'/bin/mg5_aMC', '-f', self.tmpProcessCard])
            
            logger.info( "Preparing files" )
            shutil.copyfile(self.config.centralGridpack+'/process/madevent/Cards/run_card.dat', self.config.uniquePath+'/processtmp/Cards/run_card.dat')
            shutil.copyfile(self.config.centralGridpack+'/process/madevent/Cards/grid_card.dat', self.config.uniquePath+'/processtmp/Cards/grid_card.dat')
            shutil.copyfile(self.config.centralGridpack+'/process/madevent/Cards/me5_configuration.txt', self.config.uniquePath+'/processtmp/Cards/me5_configuration.txt')
            
            with open(self.config.uniquePath+'/processtmp/Cards/me5_configuration.txt', 'a') as f:
                f.write("run_mode = 2\n")
                f.write("nb_core = 4\n")
                f.write("lhapdf = /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/lhapdf/6.1.6/share/LHAPDF/../../bin/lhapdf-config\n")
                f.write("automatic_html_opening = False\n")

            with open(self.config.uniquePath+'/processtmp/Cards/run_card.dat', 'a') as f:
                f.write("{}  =  nevents\n".format(self.nEvents))
            
            if keepGridpack:
                logger.info( "Preparing first part of gridpack" )
                output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])

            logger.info( "Calculating x-sec" )
            # rerun MG to obtain the correct x-sec (with more events)
            with open(self.config.uniquePath+'/processtmp/Cards/run_card.dat', 'a') as f:
                f.write(".false. =  gridpack\n")
            #subprocess.call(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])
            output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])
            m = re.search("Cross-section :\s*(.*) \pb", output)
            logger.info( "x-sec: {} pb".format(m.group(1)) )
            self.xsec = u_float.fromString(m.group(1))
            
            if not self.config.xsecDB.contains(self.getKey()) or overwrite:
                self.config.xsecDB.add(self.getKey(), self.xsec, save=True)
            ###
            # tar the new gridpack
            if keepGridpack:
                logger.info( "Stitching together all the parts of the gridpack" )
                subprocess.call(['tar', 'xaf', '%s/processtmp/run_01_gridpack.tar.gz'%self.config.uniquePath, '--directory', self.config.uniquePath])
                os.mkdir('%s/process'%self.config.uniquePath)
                shutil.move('%s/madevent'%self.config.uniquePath, '%s/process'%self.config.uniquePath)
                shutil.move('%s/run.sh'%self.config.uniquePath, '%s/process'%self.config.uniquePath)
                shutil.move('%s/mgbasedir'%self.config.centralGridpack, self.config.uniquePath)
                shutil.move('%s/runcmsgrid.sh'%self.config.centralGridpack, self.config.uniquePath)
                self.makeNameString()
                self.gridpack = '%s/%s.tar.xz'%(self.config.gridpacksDir, self.nameString)
                logger.info( "Compressing the gridpack" )
                os.system('cd %s; tar cJpsf %s mgbasedir process runcmsgrid.sh'%(self.config.uniquePath,self.gridpack))
                #subprocess.call(['cd','%s;'%self.config.uniquePath, 'tar', 'cJpsf', self.gridpack, 'mgbasedir', 'process', 'runcmsgrid.sh'])
                logger.info( "Done!" )
                logger.info( "The gridpack is now ready to use: %r", self.gridpack )
            else:
                logger.info( "Done!" )
        else:
            logger.info( "Found x-sec in DB. Use option overwrite to force recalculation. Skipping." )

    def getNonZeroCoupling(self):
        nonZeroCouplings = []
        for coup in self.couplings.l:
            if coup.value != 0 and coup.value != 0.:
                nonZeroCouplings += [coup.getStringTuple()]
            #for i,c in enumerate(couplings.couplingValues):
            #    if c != 0:
            #        nonZeroCouplings += [(couplings.couplingNames[i],"{:.3}".format(c))]
        return nonZeroCouplings

    def makeNameString(self):
        nonZeroCouplingStr = ''
        nonZeroCouplings = self.getNonZeroCoupling()
        for nZ in nonZeroCouplings:
            nonZeroCouplingStr += '_'.join([nZ[0], str("{:.3}".format(nZ[1])).replace('-','m').replace('.','p')])
                
        self.nameString = '_'.join([self.config.model, self.process, nonZeroCouplingStr])
    
    #def makeStati(self):
    #    stati = ["GS_status", "GS_dataset", "GS_crabdir", "DIGI_status", "DIGI_dataset", "DIGI_crabdir", "RECO_status", "RECO_dataset", "RECO_crabdir", "MA_status", "MA_dataset", "MA_crabdir"]
    #    for s in stati:
    #        setattr(self,s,"None")
    #
    #def getColumns(self):
    #    self.columns = ["model", "process"]
    #    for couplings in self.couplings.l:
    #        self.columns += [c.name for c in couplings]
    #    self.columns += ["nEvents", "xsec", "gridpack"]
    #    self.columns += stati

    #def getEntries(self):
    #    self.columns = [self.config.model, self.process]
    #    for couplings in self.couplings.l:
    #        self.columns += [c.value for c in couplings]
    #    self.columns += [self.nEvents, self.xsec, self.gridpack]
    #    self.columns += [self.GS_status, self.GS_dataset, self.GS_crabdir, self.DIGI_status, self.DIGI_dataset, self.DIGI_crabdir, self.RECO_status, selfRECO_dataset, self.RECO_crabdir, self.MA_status, self.MA_dataset, self.MA_crabdir]
    
    def getKey(self):
        cn = []
        cv = []
        for c in self.config.modified_couplings:
            cn += [c[0]]
            cv += [c[1]]
        key = self.config.model_name, self.process, str(cn), str(cv)
        return key
    
    def getXSec(self):
        print
        logger.info( "{:10}{:10}{:100}".format(self.config.model, self.process, self.getNonZeroCoupling()) )
        if self.config.xsecDB.contains(self.getKey()):
            xsec = self.config.xsecDB.get(self.getKey())
            logger.info( "{:10}{:10} pb".format("x-sec",xsec) )
            return xsec
        else:
            logger.info( "Couldn't find x-sec" )
            return u_float(0)

    def output(self):
        logger.info( "### Status and Results ###" )
        logger.info( "{:15}{:15}".format("Model","Process") )
        logger.info( "{:15}{:15}".format(self.config.model,self.process) )
