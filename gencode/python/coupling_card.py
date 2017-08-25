'''
Create directories containing all the cards necessary for gridpack creation from a template.
'''

# Standard imports
import os, shutil

class coupling_card:
    def __init__(self, process, coupling, value, templateSubDir="template"):
        self.process        = process
        self.coupling       = coupling
        self.value          = value
        self.templateSubDir = templateSubDir
        self.nCouplings     = 6
        self.firstCoupling  = 2
        self.blockName      = "dim6"

        ## Get the templates
        self.dataDir         = "/".join([os.path.abspath("").split("TopEFT")[0],"TopEFT","gencode","data"])
        self.runTemplate     = "/".join([self.dataDir,"template", "template_run_card.dat"])
        self.paramTemplate   = "/".join([self.dataDir,"template", "template_customizecards.dat"])
        self.procTemplate    = "/".join([self.dataDir,"template", "template_proc_card.dat"])

        ## Output files
        self.identifier      = "_".join([self.process,"C",str(self.coupling),str(self.value)]).replace('.','p')
        self.outDir          = "/".join([self.dataDir, self.identifier])
        self.paramCardFile   = "/".join([self.outDir,"%s_customizecards.dat"%(self.identifier)])
        self.procCardFile    = "/".join([self.outDir,"%s_proc_card.dat"%(self.identifier)])
        self.runCardFile     = "/".join([self.outDir,"%s_run_card.dat"%(self.identifier)])

    def setNCouplings(self, nCouplings):
        self.nCouplings = nCouplings

    def writeCards(self,v=1):

        if not os.path.isdir(self.outDir):
            os.makedirs(self.outDir)

        ## write the file for param_card customizations
        with open(self.paramCardFile, "w") as f:
            f.write("#put card customizations here (change top and higgs mass for example)\n\n")
            f.write("set param_card mass 6 172.5\n")
            f.write("set param_card yukawa 6 172.5\n\n")
            for i in range(self.firstCoupling, self.nCouplings+1):
                if i == int(self.coupling):
                    f.write("set param_card %s %i %f\n"%(self.blockName, i,float(self.value)))
                else:
                    f.write("set param_card %s %i 0\n"%(self.blockName, i))

        ## write the process card
        lines = []
        with open(self.procTemplate, "r") as f:
            while True:
                l = f.readline()
                if l == '': break
                else: lines.append(l)

        with open(self.procCardFile, "w") as f:
            for l in lines:
                f.write(l)
            f.write("\noutput %s -nojpeg"%self.identifier)

        ## copy the run card
        shutil.copyfile(self.runTemplate,self.runCardFile)
        if os.path.isdir(self.outDir) and v>0:
            print "Written cards to %s"%self.outDir
