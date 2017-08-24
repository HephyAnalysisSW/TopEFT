import os, time, hashlib, subprocess, uuid
import shutil
import re
from TopEFT.gencode.Cache import Cache
from TopEFT.gencode.u_float import u_float
from TopEFT.gencode.user import results_directory

HEL_couplings_newcoup =\
    ['cH','cT','c6','cu','cd','cl','cWW','cB','cHW','cHB',
    'cA','cG','cHQ','cpHQ','cHu','cHd','cHud','cHL','cpHL',
    'cHe','cuB','cuW','cuG','cdB','cdW','cdG','clB','clW',
    'c3W','c3G','c2W','c2B','c2G','tcHW','tcHB','tcG','tcA',
    'tc3W','tc3G']

TOP_EFT_couplings_dim6 =\
    ['Lambda', 'RC3phiq', 'IC3phiq', 'RCtW', 'ICtW', 'RCtG', 'ICtG', 'CG', 'CphiG']

TOP_EFT_couplings_fourfermion =\
    ['C13qq', 'C81qq', 'C83qq', 'C8ut', 'C8dt', 'C1qu', 'C1qd', 'C1qt']

class configuration:
    def __init__(self, model, cache="xsec_DB.pkl"):
        if model not in ["HEL_UFO", "TopEffTh"]:
            raise NotImplementedError( "The model %s is not yet implemented." %model )
        else:
            self.model = model
        self.abspath = os.path.abspath('./')
        self.makeUniquePath()
        self.MG5tarball = '/'.join([self.abspath, 'data','template', 'MG5_aMC_v2_3_3.tar.gz'])
        self.GPtarball = '/'.join([self.abspath, 'data','template', 'ttZ01j_5f_MLM_tarball.tar.xz'])
        self.processCards = '/'.join([self.abspath, 'data', 'processCards'])
        self.gridpacksDir = '/'.join([self.abspath, 'data', 'gridpacks'])
        self.restrictCardTemplate = '/'.join([self.abspath, 'data','template', 'restrict_no_b_mass_'+model+'.dat'])
        self.restrictCard = '/'.join([self.uniquePath, 'restrict_no_b_mass.dat'])
        self.DBFile = '/'.join([results_directory,cache])
        self.connectDB(self.DBFile)


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

    def makeUniquePath(self):
        while True:
            self.uniqueDir = uuid.uuid4().hex
            self.uniquePath = '/'.join([self.abspath, self.uniqueDir])
            if not os.path.isdir(self.uniquePath): break
            print "Path exists, waiting"
            time.sleep(0.1)

    def connectDB(self,DBFile):
        self.xsecDB = Cache(DBFile, verbosity=2)
        print "Loaded DB from %s"%self.DBFile

    def clean(self):
        if os.path.isdir(self.uniquePath):
            print "Cleaning up, deleting %s"%self.uniquePath
            shutil.rmtree(self.uniquePath)

class coupling:
    def __init__(self, blockname, couplingName, couplingValue):
        self.blockname  = blockname
        self.name       = couplingName
        self.value      = couplingValue
    
    def getTuple(self):
        return (self.name, self.value)
    
    def getStringTuple(self):
        return (self.name, "{:.3}".format(self.value))

class couplings:
    def __init__(self):
        self.l = []
        self.blocks = []

    def add(self, coupling):
        if coupling.blockname not in self.blocks:
            self.blocks.append(coupling.blockname)
        if not coupling.name in [ a.name for a in self.l ]:
            self.l.append(coupling)

    def addBlock(self, blockname, names):
        for n in names:
            self.add(coupling(blockname, n, 0))

    def setCoupling(self, couplingName, couplingValue):
        for c in self.l:
            if c.name == couplingName:
                c.value = couplingValue
                return True
        return False

class process(configuration):
    def __init__(self, process, nEvents, config):
        self.process = process
        self.processCard = process+'.dat'
        self.nEvents = nEvents
        self.config = config
        self.couplings = couplings()
        self.xsec = 0
        self.gridpack = "None"
        
    def addCoupling(self, couplings):
        self.couplings = couplings

    def updateRestrictCard(self):
        out = open(self.config.restrictCard, 'w')
        with open(self.config.restrictCardTemplate, 'r') as f:
            rewrite = False
            for line in f:
                for block in self.couplings.blocks:
                    if block in line:
                        rewrite = True
                        writeNewBlock = True
                if rewrite and "##############" in line:
                    rewrite = False
                if not rewrite:
                    out.write(line)
                elif writeNewBlock:
                    for block in self.couplings.blocks:
                        if block in line:
                            out.write("Block %s\n"%block)
                            j = 1
                            for i,coup in enumerate(self.couplings.l):
                                if coup.blockname == block:
                                    out.write("{:5} {:15.6} # {}\n".format(j, float(coup.value), coup.name))
                                    j += 1
                    writeNewBlock = False

    def writeProcessCard(self):
        templateProcessCard = '/'.join([self.config.processCards,self.processCard])
        self.tmpProcessCard = '/'.join([self.config.uniquePath,self.processCard])
        out = open(self.tmpProcessCard, 'w')
        with open(templateProcessCard, 'r') as f:
            for line in f:
                if "import model" in line:
                    out.write("import model %s-no_b_mass\n\n"%self.config.model)
                elif "NP=1" in line and self.config.model == "TopEffTh":
                    out.write(line.replace("NP=1","NP=2"))
                else:
                    out.write(line)
            out.write("output {} -nojpeg".format(self.config.uniqueDir+'/processtmp'))
        out.close()

    def run(self, keepGridpack=True, overwrite=False):
        if not self.config.xsecDB.contains(self.getKey()) or overwrite:

            self.updateRestrictCard()

            shutil.copyfile(self.config.restrictCard, self.config.MG5+'/models/'+self.config.model+'/restrict_no_b_mass.dat')
            #self.tmpProcessCard = '/'.join([self.config.uniquePath,self.processCard])
            #shutil.copyfile('/'.join([self.config.processCards,self.processCard]), self.tmpProcessCard)
            
            self.writeProcessCard()
            
            print "Calculating diagrams"
            output = subprocess.check_output(["python",self.config.MG5+'/bin/mg5_aMC', '-f', self.tmpProcessCard])
            
            print "Preparing files"
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
                print "Preparing first part of gridpack"
                output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])

            print "Calculating x-sec"
            # rerun MG to obtain the correct x-sec (with more events)
            with open(self.config.uniquePath+'/processtmp/Cards/run_card.dat', 'a') as f:
                f.write(".false. =  gridpack\n")
            #subprocess.call(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])
            output = subprocess.check_output(['%s/processtmp/bin/generate_events'%self.config.uniquePath, '-f'])
            m = re.search("Cross-section :\s*(.*) \pb", output)
            print "x-sec: {} pb".format(m.group(1))
            self.xsec = u_float.fromString(m.group(1))
            
            if not self.config.xsecDB.contains(self.getKey()) or overwrite:
                self.config.xsecDB.add(self.getKey(), self.xsec, save=True)
            ###
            # tar the new gridpack
            if keepGridpack:
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
            else:
                print "Done!"
        else:
            print "Found x-sec in DB. Use option overwrite to force recalculation."
            print "Skipping."

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
    
    def makeStati(self):
        stati = ["GS_status", "GS_dataset", "GS_crabdir", "DIGI_status", "DIGI_dataset", "DIGI_crabdir", "RECO_status", "RECO_dataset", "RECO_crabdir", "MA_status", "MA_dataset", "MA_crabdir"]
        for s in stati:
            setattr(self,s,"None")
    
    def getColumns(self):
        self.columns = ["model", "process"]
        for couplings in self.couplings.l:
            self.columns += [c.name for c in couplings]
        self.columns += ["nEvents", "xsec", "gridpack"]
        self.columns += stati

    def getEntries(self):
        self.columns = [self.config.model, self.process]
        for couplings in self.couplings.l:
            self.columns += [c.value for c in couplings]
        self.columns += [self.nEvents, self.xsec, self.gridpack]
        self.columns += [self.GS_status, self.GS_dataset, self.GS_crabdir, self.DIGI_status, self.DIGI_dataset, self.DIGI_crabdir, self.RECO_status, selfRECO_dataset, self.RECO_crabdir, self.MA_status, self.MA_dataset, self.MA_crabdir]
    
    def getKey(self):
        cn = []
        cv = []
        for c in self.couplings.l:
            cn += [c.name]
            cv += [c.value]
        key = self.config.model, self.process, str(cn), str(cv)
        return key
    
    def getXSec(self):
        print
        print "{:10}{:10}{:100}".format(self.config.model, self.process, self.getNonZeroCoupling())
        if self.config.xsecDB.contains(self.getKey()):
            xsec = self.config.xsecDB.get(self.getKey())
            print "{:10}{:10} pb".format("x-sec",xsec)
            return xsec
        else:
            print "Couldn't find x-sec"
            return u_float(0)
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