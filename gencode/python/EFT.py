import os

HEL_couplings_newcoup =\
    ['cH','cT','c6','cu','cd','cl','cWW','cB','cHW','cHB',
    'cA','cG','cHQ','cpHQ','cHu','cHd','cHud','cHL','cpHL',
    'cHe','cuB','cuW','cuG','cdB','cdW','cdG','clB','clW',
    'c3W','c3G','c2W','c2B','c2G','tcHW','tcHB','tcG','tcA',
    'tc3W','tc3G']
TOP_EFT_couplings_dim6 = []
TOP_EFT_couplings_fourfermion = []

class configuration:
    def __init__(self):
        self.asdf = "bla"
        self.abspath = os.path.abspath('./')
        self.MG5tarball = '/'.join([self.abspath, 'MG5.tar.gz'])
        self.GPtarball = '/'.join([self.abspath, 'gridpack_template.tar.gz'])
        self.processCards = '/'.join([self.abspath, 'data', 'processCards'])
        self.restrictCardTemplate = '/'.join([self.abspath, 'data','template', 'restrict_no_b_mass_template.dat'])
        self.restrictCard = '/'.join([self.abspath, 'restrict_no_b_mass.dat'])

    def setup(self):
        return
        #untar

    def connectDB(self,DB):
        return
    # connect DB, load mg, gridpack, template files (proc_cards)

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
        self.nEvents = nEvents
        self.config = config
        self.couplings = []
        self.xsec = 0

    def addCoupling(self, coupling):
        self.couplings.append(coupling)

    def getParameterBlock(self):
        for c in self.couplings:
            print "Block %s"%c.blockname
            for i,v in enumerate(c.couplingNames):
                print "{:5}{:10}".format([])

    #def getParameterBlock(self)
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
                    #out.write("This should be the new block\n")
                    writeNewBlock = False
            #while not f.
            #tmp = f.readline()
            #print tmp

    def run(self):
        ###
        # tar the new gridpack
        self.gridpack = "pathToGridpack"
        self.xsec = xsec
    # write to DB
#def makeObjectFromString(s):

#### load the restrict card, read it, replace the new couplings
