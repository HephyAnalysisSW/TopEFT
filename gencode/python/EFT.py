import os, time, hashlib, subprocess
import shutil
import re

HEL_couplings_newcoup =\
    ['cH','cT','c6','cu','cd','cl','cWW','cB','cHW','cHB',
    'cA','cG','cHQ','cpHQ','cHu','cHd','cHud','cHL','cpHL',
    'cHe','cuB','cuW','cuG','cdB','cdW','cdG','clB','clW',
    'c3W','c3G','c2W','c2B','c2G','tcHW','tcHB','tcG','tcA',
    'tc3W','tc3G']
TOP_EFT_couplings_dim6 = []
TOP_EFT_couplings_fourfermion = []

class configuration:
    def __init__(self, model):
        if model not in ["HEL_UFO", "TopEffTh"]:
            raise NotImplementedError( "The model %s is not yet implemented." %model )
        else:
            self.model = model
        self.abspath = os.path.abspath('./')
        self.uniqueDir = hashlib.md5(str(time.time())).hexdigest()
        self.uniquePath = '/'.join([self.abspath, self.uniqueDir])
        self.MG5tarball = '/'.join([self.abspath, 'data','template', 'MG5_aMC_v2_3_3.tar.gz'])
        self.GPtarball = '/'.join([self.abspath, 'data','template', 'ttZ01j_5f_MLM_tarball.tar.xz'])
        self.processCards = '/'.join([self.abspath, 'data', 'processCards'])
        self.gridpacksDir = '/'.join([self.abspath, 'data', 'gridpacks'])
        self.restrictCardTemplate = '/'.join([self.abspath, 'data','template', 'restrict_no_b_mass_'+model+'.dat'])
        self.restrictCard = '/'.join([self.uniquePath, 'restrict_no_b_mass.dat'])

    def setup(self):
        print "### SETUP ###"
        os.makedirs(self.uniquePath)
        self.centralGridpack = '/'.join([self.uniquePath, 'centralGridpack'])
        self.newGridpack = '/'.join([self.uniquePath, 'newGridpack'])
        self.MG5 = '/'.join([self.uniquePath, 'MG5'])
        os.makedirs(self.centralGridpack)
        os.makedirs(self.newGridpack)
        os.makedirs(self.MG5)
        print "Preparing central gridpack"
        subprocess.call(['tar', 'xaf', self.GPtarball, '--directory', self.centralGridpack])
        print "Preparing madgraph"
        subprocess.call(['tar', 'xaf', self.MG5tarball, '--directory', self.MG5])

        print "### FINISHED ###"

    def connectDB(self,DB):
        return
    # connect DB, load mg, gridpack, template files (proc_cards)

    def __del__(self):
        shutil.rmtree(self.uniqueDir)

class coupling:
    def __init__(self, blockname, couplingNames):
        self.blockname = blockname
        self.couplingNames = couplingNames
        self.couplingValues = [0]*len(couplingNames)
        for c in couplingNames:
            setattr(self, c, 0)

    def setAllCouplings(self, couplingValues):
        self.couplingValues = couplingValues
        for i,c in enumerate(self.couplingNames):
            setattr(self, c, couplingValues[i])

    def setCoupling(self, couplingName, couplingValue):
        if hasattr(self,couplingName):
            setattr(self,couplingName,couplingValue)
            self.couplingValues[self.couplingNames.index(couplingName)] = couplingValue
        else:
            print "Don't know coupling %s"%couplingName

    def resetCouplings(self):
        for c in self.couplingNames:
            setattr(self, c, 0)

class process(configuration):
    def __init__(self, process, nEvents, config):
        self.process = process
        self.processCard = process+'.dat'
        self.nEvents = nEvents
        self.config = config
        self.couplings = []
        self.xsec = 0
        self.gridpack = "None"
        
    def addCoupling(self, coupling):
        self.couplings.append(coupling)

    def updateRestrictCard(self):
        out = open(self.config.restrictCard, 'w')
        with open(self.config.restrictCardTemplate, 'r') as f:
            rewrite = False
            for line in f:
                for c in self.couplings:
                    if c.blockname in line:
                        rewrite = True
                        writeNewBlock = True
                if rewrite and "##############" in line:
                    rewrite = False
                if not rewrite:
                    out.write(line)
                elif writeNewBlock:
                    for c in self.couplings:
                        if c.blockname in line:
                            out.write("Block %s\n"%c.blockname)
                            for i,v in enumerate(c.couplingNames):
                                out.write("{:5}{:10.6} # {}\n".format(i+1, float(c.couplingValues[i]), v))
                    writeNewBlock = False

    def run(self):
        self.updateRestrictCard()
        shutil.copyfile(self.config.restrictCard, self.config.MG5+'/models/'+self.config.model+'/restrict_no_b_mass.dat')
        tmpProcessCard = '/'.join([self.config.uniquePath,self.processCard])
        shutil.copyfile('/'.join([self.config.processCards,self.processCard]), tmpProcessCard)

        with open(tmpProcessCard, 'a') as f:
            f.write("output {} -nojpeg".format(self.config.uniqueDir+'/processtmp'))
        print "Calculating diagrams"
        output = subprocess.check_output(["python",self.config.MG5+'/bin/mg5_aMC', '-f', tmpProcessCard])
        
        print "Preparing files"
        shutil.copyfile(self.config.centralGridpack+'/process/madevent/Cards/run_card.dat', self.config.uniquePath+'/processtmp/Cards/run_card.dat')
        shutil.copyfile(self.config.centralGridpack+'/process/madevent/Cards/grid_card.dat', self.config.uniquePath+'/processtmp/Cards/grid_card.dat')
        shutil.copyfile(self.config.centralGridpack+'/process/madevent/Cards/me5_configuration.txt', self.config.uniquePath+'/processtmp/Cards/me5_configuration.txt')
        
        with open(self.config.uniquePath+'/processtmp/Cards/me5_configuration.txt', 'a') as f:
            f.write("run_mode = 2\n")
            f.write("nb_core = 4\n")
            f.write("lhapdf = /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/lhapdf/6.1.6/share/LHAPDF/../../bin/lhapdf-config\n")
            f.write("automatic_html_opening = False\n")

        print "Preparing first part of gridpack"
        with open(self.config.uniquePath+'/processtmp/Cards/run_card.dat', 'a') as f:
            f.write("{}  =  nevents\n".format(self.nEvents))
        output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])

        print "Calculating x-sec"
        # rerun MG to obtain the correct x-sec (with more events)
        with open(self.config.uniquePath+'/processtmp/Cards/run_card.dat', 'a') as f:
            f.write(".false. =  gridpack\n")
        output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])
        m = re.search("Cross-section :\s*(.*) \+", output)
        print "x-sec: {} pb".format(m.group(1))
        self.xsec = float(m.group(1))

        ###
        # tar the new gridpack
        print "Stitching together all the parts of the gridpack"
        subprocess.call(['tar', 'xaf', '%s/processtmp/run_01_gridpack.tar.gz'%self.config.uniquePath, '--directory', self.config.uniquePath])
        os.mkdir('%s/process'%self.config.uniquePath)
        shutil.move('%s/madevent'%self.config.uniquePath, '%s/process'%self.config.uniquePath)
        shutil.move('%s/run.sh'%self.config.uniquePath, '%s/process'%self.config.uniquePath)
        shutil.move('%s/mgbasedir'%self.config.centralGridpack, self.config.uniquePath)
        shutil.move('%s/runcmsgrid.sh'%self.config.centralGridpack, self.config.uniquePath)
        self.makeNameString()
        self.gridpack = '%s/%s.tar.xz'%(self.config.gridpacksDir, self.nameString)
        print "Compressing the gridpack"
        os.system('cd %s; tar cJpsf %s mgbasedir process runcmsgrid.sh'%(self.config.uniquePath,self.gridpack))
        #subprocess.call(['cd','%s;'%self.config.uniquePath, 'tar', 'cJpsf', self.gridpack, 'mgbasedir', 'process', 'runcmsgrid.sh'])
        print "Done!"
        print "The gridpack is now ready to use:"
        print self.gridpack    

    def makeNameString(self):
        nonZeroCouplings = ''
        for couplings in self.couplings:
            for i,c in enumerate(couplings.couplingValues):
                if c != 0:
                    nonZeroCouplings += '_'.join([couplings.couplingNames[i], str(c).replace('-','m').replace('.','p')])
                
        self.nameString = '_'.join([self.config.model, self.process, nonZeroCouplings])
    
    def makeStati(self):
        stati = ["GS_status", "GS_dataset", "GS_crabdir", "DIGI_status", "DIGI_dataset", "DIGI_crabdir", "RECO_status", "RECO_dataset", "RECO_crabdir", "MA_status", "MA_dataset", "MA_crabdir"]
        for s in stati:
            setattr(self,s,"None")
    
    def getColumns(self):
        self.columns = ["model", "process"]
        for couplings in self.couplings:
            self.columns += [c for c in couplings]
        self.columns += ["nEvents", "xsec", "gridpack"]
        self.columns += stati

    def getEntries(self):
        self.columns = [self.config.model, self.process]
        for couplings in self.couplings:
            self.columns += [c for c in couplings]
        self.columns += [self.nEvents, self.xsec, self.gridpack]
        self.columns += [self.GS_status, self.GS_dataset, self.GS_crabdir, self.DIGI_status, self.DIGI_dataset, self.DIGI_crabdir, self.RECO_status, selfRECO_dataset, self.RECO_crabdir, self.MA_status, self.MA_dataset, self.MA_crabdir]
    
    #def connectDB():
    #def writeToDB():
    #def readFromDB():
    
    def output(self):
        print "### Status and Results ###"
        print "{:15}{:15}".format("Model","Process")
        print "{:15}{:15}".format(self.config.model,self.process)
    #    for couplings in self.couplings:
        


def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in xrange(0, len(l), n)]
