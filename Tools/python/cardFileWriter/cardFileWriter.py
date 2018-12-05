import shutil

# Logging
import logging
logger = logging.getLogger(__name__)

class cardFileWriter:
    def __init__(self):
        self.reset()
        self.releaseLocation = "." #by default, use this releasee

    def reset(self):
        self.bins = []
        self.muted = {}
        self.uncertainties = []
        self.uncertaintyVal = {}
        self.uncertaintyString = {}
        self.processes = {}
        self.expectation = {}
        self.observation = {}
        self.contamination = {}
        self.niceNames = {}
        self.defWidth = 12
        self.precision = 7
        self.maxUncNameWidth = 30
        self.maxUncStrWidth = 30
        self.hasContamination=False
        self.rateParameters = []
        self.precision = 10

    
    def setPrecision(self, prec):
        self.precision = prec


    def addBin(self, name, processes, niceName=""):
        if len(name)>30:
            logger.info("Name for bin",name,"too long. Max. length is 30.")
            return
        if self.niceNames.has_key(name):
            logger.info("Bin already there! (",name,")")
            return
        for p in processes:
            if len(p)>30:
                logger.info("Name for process", p, "in bin", name, "is too long. Max. length is 30.")
                return
        self.niceNames[name]=niceName
        self.bins.append(name)
        self.muted[name]=False
        #self.processes[name] = ["signal", "signal_ALT"]+processes
        self.processes[name] = ["signal"]+processes

    def addUncertainty(self, name, t, n=0):
        assert len(name)<self.maxUncNameWidth,  "That's too long: %s. Max. length is %i"%(name, self.maxUncNameWidth)
        if self.uncertainties.count(name):
            print "Uncertainty already there! (",name,")"
            return
        self.uncertainties.append(name)
        self.uncertaintyString[name] = t
        if t=="gmN":
            if n==0:
                print "gmN Uncertainty with n=0! Specify n as third argument: addUncertainty(..., 'gmN', n)"
                return
            self.uncertaintyString[name] = t+' '+str(n)
        if len(self.uncertaintyString[name])>self.maxUncStrWidth:
            print "That's too long:",self.uncertaintyString[name],"Max. length is", self.maxUncStrWidth
            del self.uncertaintyString[name]
            return

    def addRateParameter(self, p, value, r):
        if [ a[0] for a in self.rateParameters ].count(p):
            logger.info("Rate parameter for process %s already added!"%p)
            return
        self.rateParameters.append((p, value, r))

    def specifyExpectation(self, b, p, exp):
        self.expectation[(b,p)] = round(exp, self.precision)

    def specifyObservation(self, b, obs):
        if not isinstance(obs, int):
            print "Observation not an integer! (",obs,")"
            return
        self.observation[b] = obs

    def specifyContamination(self, b, cont):
        self.contamination[b] = cont
        self.hasContamination = True

    def specifyFlatUncertainty(self, u,  val):
        if u not in self.uncertainties:
            print "This uncertainty has not been added yet!",u,"Available:",self.uncertainties
            return
        print "Adding ",u,"=",val,"for all bins and processes!"
        for b in self.bins:
            for p in self.processes[b]:
                self.uncertaintyVal[(u,b,p)] = round(val,self.precision)

    def specifyUncertainty(self, u, b, p, val):
        if u not in self.uncertainties:
            print "This uncertainty has not been added yet!",u,"Available:",self.uncertainties
            return
        if b not in self.bins:
            print "This bin has not been added yet!",b,"Available:",self.bins
            return
        if p not in self.processes[b]:
            print "Process ", p," is not in bin",b,". Available for ", b,":",self.processes[b]
            return
        if val<0:
#      assert self.expectation[(b, p)]<0.1, "Found negative uncertainty %f for yield %f in %r."%(val, self.expectation[(b, p)], (u,b,p))
            print "Warning! Found negative uncertainty %f for yield %f in %r. Reversing sign under the assumption that the correlation pattern is irrelevant (check!)."%(val, self.expectation[(b, p)], (u,b,p))
            _val=1.0
        else:
            _val = val
        self.uncertaintyVal[(u,b,p)] = round(_val,self.precision)

    def getUncertaintyString(self, k):
        u, b, p = k
        if self.uncertaintyString[u].count('gmN'):
            if self.uncertaintyVal.has_key((u,b,p)) and self.uncertaintyVal[(u,b,p)]>0.:
                n = float(self.uncertaintyString[u].split(" ")[1])
                return self.mfs(self.expectation[(b, p)]/float(n))
            else: return '-'
        if self.uncertaintyVal.has_key((u,b,p)):
            return self.mfs(self.uncertaintyVal[(u,b,p)])
        return '-'

    def checkCompleteness(self):
        for b in self.bins:
            if not self.observation.has_key(b) or not self.observation[b]<float('inf'):
                print "No valid observation for bin",b
                return False
            if self.hasContamination and (not self.contamination.has_key(b) or not self.contamination[b] < float('inf')):
                print "No valid contamination for bin",b
                return False
            if len(self.processes[b])==0:
                print "Warning, bin",b,"has no processes"
            for p in self.processes[b]:
                if not self.expectation.has_key((b,p)) or not self.expectation[(b,p)]<float('inf'):
                    print "No valid expectation for bin/process ",(b,p)
                    return False
            for k in self.uncertaintyVal.keys():
                if not self.uncertaintyVal[k]<float('inf'):
                    print "Uncertainty invalid for",k,':',self.uncertaintyVal[k]
                    return False
        return True

    def mfs(self, f):
        return str(round(float(f),self.precision))

    def writeToFile(self, fname):
        import datetime, os
        if not self.checkCompleteness():
            print "Incomplete specification."
            return
        allProcesses=[]
        numberID = {}
        i=1
        for b in self.bins:
            if not self.muted[b]:
                for p in self.processes[b]:
                    #if not p in allProcesses and not p=='signal':
                    if not p in allProcesses and (not 'signal' in p):
                        allProcesses.append(p)
                        numberID[p] = i
                        i+=1
        unmutedBins = [b for b in self.bins if not self.muted[b]]
        nBins = len(unmutedBins)
        numberID['signal'] = 0
        #numberID['signal'] = -1
        #numberID['signal_ALT'] = 0

        lspace = (self.maxUncStrWidth + self.maxUncNameWidth + 2)
        if not os.path.exists(os.path.dirname(fname)):
            os.makedirs(os.path.dirname(fname))
        outfile = file(fname, 'w')
        outfile.write('#cardFileWriter, %s'%datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")+'\n')
        outfile.write('imax %i'%nBins+'\n')
        outfile.write('jmax *\n')
        outfile.write('kmax *\n')
        outfile.write('\n')

        for b in self.bins:
            if not self.muted[b]:
                outfile.write( '# '+b+': '+self.niceNames[b]+'\n')
            else:
                outfile.write( '#Muted: '+b+': '+self.niceNames[b]+'\n')
        outfile.write( '\n')

        outfile.write( 'bin'.ljust(lspace)              +(' '.join([b.rjust(self.defWidth) for b in unmutedBins] ) ) +'\n')
        outfile.write( 'observation'.ljust(lspace)      +(' '.join([str(self.observation[b]).rjust(self.defWidth) for b in unmutedBins]) )+'\n')
        if self.hasContamination:
            outfile.write( 'contamination'.ljust(lspace)  +(' '.join([str(self.contamination[b]).rjust(self.defWidth) for b in unmutedBins]) )+'\n')
        outfile.write('\n')
        outfile.write( 'bin'.ljust(lspace)              +(' '.join( [' '.join([b.rjust(self.defWidth) for p in self.processes[b]] ) for b in unmutedBins]) ) +'\n')
        outfile.write( 'process'.ljust(lspace)          +(' '.join( [' '.join([p.rjust(self.defWidth) for p in self.processes[b]] ) for b in unmutedBins]) ) +'\n')
        outfile.write( 'process'.ljust(lspace)          +(' '.join( [' '.join([str(numberID[p]).rjust(self.defWidth) for p in self.processes[b]] ) for b in unmutedBins]) ) +'\n')
        outfile.write( 'rate'.ljust(lspace)             +(' '.join( [' '.join([self.mfs(self.expectation[(b,p)]).rjust(self.defWidth) for p in self.processes[b]] ) for b in unmutedBins]) )+'\n')
        outfile.write('\n')

        for u in self.uncertainties:
            outfile.write( u.ljust(self.maxUncNameWidth)+' '+self.uncertaintyString[u].ljust(self.maxUncStrWidth)+' '+
                                          ' '.join( [' '.join([self.getUncertaintyString((u,b,p)).rjust(self.defWidth) for p in self.processes[b]] ) for b in unmutedBins]) +'\n')

        for p in self.rateParameters:
            outfile.write('\n')
            for b in self.bins:
                outfile.write('%s_norm_%s rateParam %s %s (@0*1) %s_norm\n'%(p[0], b, b, p[0], p[0]))
            outfile.write('%s_norm extArg %s %s\n'%(p[0], str(p[1]), str(p[2])))


        outfile.close()
        print "[cardFileWrite] Written card file %s"%fname
        return fname

    def readResFile(self, fname):
        import ROOT
        f = ROOT.TFile.Open(fname)
        t = f.Get("limit")
        l = t.GetLeaf("limit")
        qE = t.GetLeaf("quantileExpected")
        limit = {}
        preFac = 1.
        for i in range(t.GetEntries()):
                t.GetEntry(i)
#        limit["{0:.3f}".format(round(qE.GetValue(),3))] = preFac*l.GetValue()
                limit["{0:.3f}".format(round(qE.GetValue(),3))] = preFac*l.GetValue()
        f.Close()
        return limit

    def readNLLFile(self, fname):
        import ROOT
        f = ROOT.TFile.Open(fname)
        t = f.Get("limit")
        nll = {}
        t.GetEntry(0) # changed from 1!
        # prefit NLL
        nll["nll0"] = t.nll0
        # delta NLL to prefit (should always be negative since stuff is fitted)
        nll["nll"] = t.nll
        # absolute NLL postfit
        nll["nll_abs"] = t.nll0 + t.nll
        f.Close()
        return nll

    def calcLimit(self, fname=None, options=""):
        import uuid, os
        ustr          = str(uuid.uuid4())
        uniqueDirname = os.path.join(self.releaseLocation, ustr)
        print "Creating %s"%uniqueDirname
        os.makedirs(uniqueDirname)

        if fname is not None:  # Assume card is already written when fname is not none
          filename = os.path.abspath(fname)
        else:
          filename = fname if fname else os.path.join(uniqueDirname, ustr+".txt")
          self.writeToFile(filename)
        resultFilename = filename.replace('.txt','')+'.root'

        assert os.path.exists(filename), "File not found: %s"%filename

        combineCommand = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combine --saveWorkspace -M AsymptoticLimits "+filename
        print combineCommand
        os.system(combineCommand)

        tempResFile = uniqueDirname+"/higgsCombineTest.AsymptoticLimits.mH120.root"
        try:
            res= self.readResFile(tempResFile)
        except:
            res=None
            print "[cardFileWrite] Did not succeed reeding result."
        if res:
            shutil.copyfile(tempResFile, resultFilename)

        shutil.rmtree(uniqueDirname)
        return res

    def calcNuisances(self, fname=None, options="", masks=''):
        import uuid, os
        ustr          = str(uuid.uuid4())
        uniqueDirname = os.path.join(self.releaseLocation, ustr)
        print "Creating %s"%uniqueDirname
        os.makedirs(uniqueDirname)
        shutil.copyfile(os.path.join(os.environ['CMSSW_BASE'], 'src', 'TopEFT', 'Tools', 'python', 'cardFileWriter', 'diffNuisances.py'), os.path.join(uniqueDirname, 'diffNuisances.py'))

        if fname is not None:  # Assume card is already written when fname is not none
          filename = os.path.abspath(fname)
        else:
          filename = fname if fname else os.path.join(uniqueDirname, ustr+".txt")
          self.writeToFile(filename)
        filePostfixes  = [ 'nuisances_r1.txt', 'nuisances_r1_full.txt', 'nuisances_r1.tex', 'nuisances_r1_full.tex' ]
        #filePostfixes += [ 'nuisances_bestfit.txt', 'nuisances_bestfit_full.txt', 'nuisances_bestfit.tex', 'nuisances_bestfit_full.tex' ]

        assert os.path.exists(filename), "File not found: %s"%filename

        # create the workspace
        #combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combineCards.py %s -S > shapeCard.txt; text2workspace.py shapeCard.txt -o myWorkspace.root --channel-masks --X-allow-no-signal -P HiggsAnalysis.CombinedLimit.PhysicsModel:defaultModel"%(filename)
        combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combineCards.py %s -S > shapeCard.txt; text2workspace.py shapeCard.txt -o myWorkspace.root -P HiggsAnalysis.CombinedLimit.PhysicsModel:defaultModel"%(filename)
        # get the nuisances for r = 1
        #combineCommand += ";combine -M FitDiagnostics myWorkspace.root --setParameterRanges r=0.95,1.05 --saveShapes --saveNormalizations --saveOverall --saveWithUncertainties --setParameters %s"%masks
        combineCommand += ";combine -M FitDiagnostics myWorkspace.root --saveShapes --saveNormalizations --saveOverall --freezeParameters r --setParameterRanges r=0.99,1.01 --saveWithUncertainties"
        combineCommand +=";python diffNuisances.py  fitDiagnostics.root &> nuisances_r1.txt"
        combineCommand +=";python diffNuisances.py -a fitDiagnostics.root &> nuisances_r1_full.txt"
        combineCommand +=";python diffNuisances.py -f latex fitDiagnostics.root &> nuisances_r1.tex"
        combineCommand +=";python diffNuisances.py -af latex fitDiagnostics.root &> nuisances_r1_full.tex"
        
        os.system(combineCommand)
        
        shutil.copyfile(uniqueDirname+'/fitDiagnostics.root', fname.replace('.txt','_FD_r1.root'))
        
        ##get the nuisances for bestfit
        #combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combineCards.py %s -S > shapeCard.txt; text2workspace.py shapeCard.txt -o myWorkspace.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:defaultModel"%filename
        #combineCommand += ";combine -M FitDiagnostics myWorkspace.root --setParameterRanges r=0.,5. --saveShapes --saveNormalizations --saveOverall --saveWithUncertainties "
        #combineCommand +=";python diffNuisances.py  fitDiagnostics.root &> nuisances_bestfit.txt"
        #combineCommand +=";python diffNuisances.py -a fitDiagnostics.root &> nuisances_bestfit_full.txt"
        #combineCommand +=";python diffNuisances.py -f latex fitDiagnostics.root &> nuisances_bestfit.tex"
        #combineCommand +=";python diffNuisances.py -af latex fitDiagnostics.root &> nuisances_bestfit_full.tex"

        #os.system(combineCommand)

        #shutil.copyfile(uniqueDirname+'/fitDiagnostics.root', fname.replace('.txt','_FD_bestfit.root'))

        for files in filePostfixes:
            tempResFile = "%s/%s"%(uniqueDirname, files)
            resFile = filename.replace('.txt','')+'_%s'%files
            shutil.copyfile(tempResFile, resFile)

        shutil.rmtree(uniqueDirname)
        return

    def combineCards(self, cards):

        import uuid, os
        ustr          = str(uuid.uuid4())
        uniqueDirname = os.path.join(self.releaseLocation, ustr)
        logger.info("Creating %s", uniqueDirname)
        os.makedirs(uniqueDirname)

        years = cards.keys()
        cmd = ''
        for year in years:
            cmd += " dc_%s=%s"%(year, cards[year])

        combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combineCards.py %s > combinedCard.txt"%cmd
        os.system(combineCommand)
        resFile = cards[years[0]].replace(str(years[0]), 'COMBINED')
        f = resFile.split('/')[-1]
        resPath = resFile.replace(f, '')
        if not os.path.isdir(resPath):
            os.makedirs(resPath)
        logger.info("Putting combined card into dir %s", resPath)
        shutil.copyfile(uniqueDirname+"/combinedCard.txt", resFile)

        return resFile

    def calcNLL(self, fname=None, options=""):
        '''
        Does max likelihood fits, both with r=1 and a best-fit value
        '''
        import uuid, os
        ustr          = str(uuid.uuid4())
        uniqueDirname = os.path.join(self.releaseLocation, ustr)
        print "Creating %s"%uniqueDirname
        os.makedirs(uniqueDirname)
        if fname is not None:  # Assume card is already written when fname is not none
          filename = os.path.abspath(fname)
        else:
          filename = fname if fname else os.path.join(uniqueDirname, ustr+".txt")
          self.writeToFile(filename)

        # too tight constraints lead to failing fits
        combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combine -M MultiDimFit -n Nominal --saveNLL --forceRecreateNLL --freezeParameters r "+filename
        #combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;text2workspace.py -o myWorkspace.root --channel-masks --X-allow-no-signal %s"%filename
        os.system(combineCommand)
        #combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combine -M MultiDimFit myWorkspace.root -v 3 --algo grid --points 1 --rMin 0.99 --rMax 1.01 -n Nominal --saveNLL --saveSpecifiedNuis=all %s --setParameters %s"%(normOption,masks)
        #os.system(combineCommand)
        #combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combine -M MultiDimFit --algo grid --points 1 --rMin 0.99 --rMax 1.01 -n Nominal --saveNLL --forceRecreateNLL "+filename
        #print combineCommand
        #os.system(combineCommand)
        nll = self.readNLLFile(uniqueDirname+"/higgsCombineNominal.MultiDimFit.mH120.root")
        #combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combine -M MultiDimFit --algo grid --points 100 --rMin 0. --rMax 2.0 -n Nominal %s --saveNLL --forceRecreateNLL %s > log.txt"%(options, filename)
        #os.system(combineCommand)
        #nll2 = self.readNLLFile(uniqueDirname+"/higgsCombineNominal.MultiDimFit.mH120.root")

        nll["bestfit"] = nll["nll"]
        #print "Comparing the two fits"
        #print nll["nll0"], nll2["nll0"]

        #print nll
        
        shutil.rmtree(uniqueDirname)
        
        return nll

    def consitencyCheck(self, a, b):
        return a - 0.01 <= b <= a + 0.01

    def physicsModel(self, fname=None, options="", normList=[], masks=''):
        '''
        Alternative version to get NLL. Results are similar, but should be more flexible for future changes, and also faster.
        '''
        import uuid, os
        ustr          = str(uuid.uuid4())
        uniqueDirname = os.path.join(self.releaseLocation, ustr)
        print "Creating %s"%uniqueDirname
        os.makedirs(uniqueDirname)
        if fname is not None:  # Assume card is already written when fname is not none
          filename = os.path.abspath(fname)
        else:
          filename = fname if fname else os.path.join(uniqueDirname, ustr+".txt")
          self.writeToFile(filename)
        
        normOption = ''
        if normList:
            from TopEFT.Tools.cardFileWriter.getNorms import getNorms
            normOption += " > output.txt"
        
        # create combine workspace
        combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;text2workspace.py -o myWorkspace.root --channel-masks --X-allow-no-signal -P HiggsAnalysis.CombinedLimit.PhysicsModel:defaultModel %s"%filename
        os.system(combineCommand)
        # use multiDimFit to first obtain fit and NLL value for r=1, then let r float
        combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combine -M MultiDimFit myWorkspace.root -v 3 --setParameterRanges r=0.99,1.01 --saveNLL --fastScan --floatOtherPOIs=0 --saveSpecifiedNuis=all %s --setParameters %s"%(normOption,masks)
        os.system(combineCommand)

        nll_r_one   = self.readNLLFile(uniqueDirname+"/higgsCombineTest.MultiDimFit.mH120.root")

        combineCommand  = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combine -M MultiDimFit myWorkspace.root -v 3 --setParameterRanges r=0.,5. --saveNLL --fastScan --floatOtherPOIs=0 --saveSpecifiedNuis=all %s"%normOption
        os.system(combineCommand)
        
        nll_r_float = self.readNLLFile(uniqueDirname+"/higgsCombineTest.MultiDimFit.mH120.root")
        
        # check consistency of results
        if not self.consitencyCheck(nll_r_one['nll0'], nll_r_float['nll0']):
            raise ValueError('NLL calculations are not consistent. This should not happen.')
        
        nll_r_one["bestfit"] = nll_r_float["nll"]
        
        #print os.listdir(uniqueDirname)
        
        print nll_r_one
        print nll_r_float
        
        if normList:
            getNorms(dirName=uniqueDirname, normsToExtract=normList)
            shutil.copyfile(uniqueDirname + '/SF.txt', fname.replace('.txt','_SF.txt'))
        
        #os.listdir
        shutil.copyfile(uniqueDirname+"/higgsCombineTest.MultiDimFit.mH120.root", fname.replace(".txt",".root"))
        
        shutil.rmtree(uniqueDirname)
        return nll_r_one


    def calcSignif(self, fname="", options=""):
        import uuid, os
        ustr          = str(uuid.uuid4())
        uniqueDirname = os.path.join(self.releaseLocation, ustr)
        print "Creating %s"%uniqueDirname
        os.makedirs(uniqueDirname)
        print fname
        #if fname=="":
        #    fname = str(ustr+".txt")
        #    self.writeToFile(uniqueDirname+"/"+fname)
        #else:
        #    self.writeToFile(fname)
        combineCommand = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combine --saveWorkspace -M Significance --uncapped 1 --significance --rMin -5 "+fname
        os.system(combineCommand)
        #os.system("pushd "+self.releaseLocation+";eval `scramv1 runtime -sh`;popd;cd "+uniqueDirname+";"+self.combineStr+" --saveWorkspace  -M ProfileLikelihood --significance "+fname+" -t -1 --expectSignal=1 ")
        try:
            res= self.readResFile(uniqueDirname+"/higgsCombineTest.Significance.mH120.root")
            os.system("rm -rf "+uniqueDirname+"/higgsCombineTest.Significance.mH120.root")
        except:
            res=None
            print "Did not succeed."
        #if res:
        #    os.system("cp "+uniqueDirname+"/higgsCombineTest.ProfileLikelihood.mH120.root "+fname.replace('.txt','')+'.root')
        shutil.rmtree(uniqueDirname)

        return res
