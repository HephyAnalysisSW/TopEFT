''' Helper functions for TopEFT
'''
#Standard imports
import ROOT
from math import pi, sqrt, cos, sin, sinh, log, cosh
from array import array
import itertools

# Logging
import logging
logger = logging.getLogger(__name__)

#scripts
ROOT.gROOT.LoadMacro("$CMSSW_BASE/src/TopEFT/tools/scripts/tdrstyle.C")
ROOT.setTDRStyle()
#mZ=91.1876
mZ = 91.2

def natural_sort(list, key=lambda s:s):
    """
    Sort the list into natural alphanumeric order.
    http://stackoverflow.com/questions/4836710/does-python-have-a-built-in-function-for-string-natural-sort
    """

    import re

    def get_alphanum_key_func(key):
        convert = lambda text: int(text) if text.isdigit() else text
        return lambda s: [convert(c) for c in re.split('([0-9]+)', key(s))]

    sort_key = get_alphanum_key_func(key)

    lc = sorted(list, key=sort_key)

    return lc

def cosThetaStar( Z_mass, Z_pt, Z_eta, Z_phi, l_pt, l_eta, l_phi ):

    Z   = ROOT.TVector3()
    l   = ROOT.TVector3()
    Z.SetPtEtaPhi( Z_pt, Z_eta, Z_phi )
    l.SetPtEtaPhi( l_pt, l_eta, l_phi )
    
    # get cos(theta) and the lorentz factor, calculate cos(theta*)
    cosTheta = Z*l / (sqrt(Z*Z) * sqrt(l*l))
    gamma   = sqrt( 1 + Z_pt**2/Z_mass**2 * cosh(Z_eta)**2 )
    beta    = sqrt( 1 - 1/gamma**2 )
    return (-beta + cosTheta) / (1 - beta*cosTheta)

def deltaPhi(phi1, phi2):
    dphi = phi2-phi1
    if  dphi > pi:
        dphi -= 2.0*pi
    if dphi <= -pi:
        dphi += 2.0*pi
    return abs(dphi)

def deltaR2(l1, l2):
    return deltaPhi(l1['phi'], l2['phi'])**2 + (l1['eta'] - l2['eta'])**2

def deltaR(l1, l2):
    return sqrt(deltaR2(l1,l2))

def bestDRMatchInCollection(l, coll, deltaR = 0.2, deltaRelPt = 0.5 ):
    lst = []
    for l2 in coll:
        dr2 = deltaR2(l, l2)
        if  ( dr2 < deltaR**2 ) and (abs( -1 + l2['pt']/l['pt']) < deltaRelPt or deltaRelPt < 0 ):
            lst.append((dr2, l2))
    lst.sort()
    if len(lst)>0:
        return lst[0][1]
    else:
        return None

def getFileList(dir, histname='histo', maxN=-1):
    import os
    filelist = os.listdir(os.path.expanduser(dir))
    filelist = [dir+'/'+f for f in filelist if histname in f and f.endswith(".root")]
    if maxN>=0:
        filelist = filelist[:maxN]
    return filelist

# Returns (closest mass, index1, index2)
def closestOSDLMassToMZ(leptons):
    inds = range(len(leptons))
    vecs = [ ROOT.TLorentzVector() for i in inds ]
    for i, v in enumerate(vecs):
        v.SetPtEtaPhiM(leptons[i]['pt'], leptons[i]['eta'], leptons[i]['phi'], 0.)
    dlMasses = [((vecs[comb[0]] + vecs[comb[1]]).M(), comb[0], comb[1])  for comb in itertools.combinations(inds, 2) if leptons[comb[0]]['pdgId']*leptons[comb[1]]['pdgId'] < 0 and abs(leptons[comb[0]]['pdgId']) == abs(leptons[comb[1]]['pdgId']) ]
    return min(dlMasses, key=lambda (m,i1,i2):abs(m-mZ)) if len(dlMasses)>0 else (float('nan'), -1, -1)

def m3( jets ):
    if not len(jets)>=3: return float('nan'), -1, -1, -1
    vecs = [(i, ROOT.TLorentzVector()) for i in range(len(jets))]
    for i, v in enumerate(vecs):
        v[1].SetPtEtaPhiM(jets[i]['pt'], jets[i]['eta'], jets[i]['phi'], 0.)
    maxSumPt = 0
    m3 = float('nan')
    i1, i2, i3 = -1, -1, -1
    for j3_comb in itertools.combinations(vecs, 3):
        vecSum = sum( [v[1] for v in j3_comb], ROOT.TLorentzVector())
        if vecSum.Pt()>maxSumPt:
            maxSumPt = vecSum.Pt()
            m3 = vecSum.M()
            i1, i2, i3 =  [v[0] for v in j3_comb]
    return m3, i1, i2, i3

def getChain(sampleList, histname='', maxN=-1, treeName="Events"):
    if not type(sampleList)==type([]):
        sampleList_ = [sampleList]
    else:
        sampleList_= sampleList
    c = ROOT.TChain(treeName)
    i=0
    for s in sampleList_:
        if type(s)==type(""):
            for f in getFileList(s, histname, maxN):
                if checkRootFile(f, checkForObjects=[treeName]):
                    i+=1
                    c.Add(f)
                else:
                    print "File %s looks broken."%f
            print "Added ",i,'files from samples %s' %(", ".join([s['name'] for s in sampleList_]))
        elif type(s)==type({}):
            if s.has_key('file'):
                c.Add(s['file'])
#        print "Added file %s"%s['file']
                i+=1
            if s.has_key('bins'):
                for b in s['bins']:
                    dir = s['dirname'] if s.has_key('dirname') else s['dir']
                    for f in getFileList(dir+'/'+b, histname, maxN):
                        if checkRootFile(f, checkForObjects=[treeName]):
                            i+=1
                            c.Add(f)
                        else:
                            print "File %s looks broken."%f
#      print 'Added %i files from %i elements' %(i, len(sampleList))
        else:
#      print sampleList
            print "Could not load chain from sampleList %s"%repr(sampleList)
    return c

def checkRootFile(f, checkForObjects=[]):
    rf = ROOT.TFile.Open(f)
    if not rf: return False
    try:
        good = (not rf.IsZombie()) and (not rf.TestBit(ROOT.TFile.kRecovered))
    except:
        if rf: rf.Close()
        return False
    for o in checkForObjects:
        if not rf.GetListOfKeys().Contains(o):
            print "[checkRootFile] Failed to find object %s in file %s"%(o, f)
            rf.Close()
            return False
#    print "Keys recoveredd %i zombie %i tb %i"%(rf.Recover(), rf.IsZombie(), rf.TestBit(ROOT.TFile.kRecovered))
    rf.Close()
    return good

def getChunks(sample,  maxN=-1):
    import os, subprocess
    chunks = [{'name':x} for x in os.listdir(sample.path) if x.startswith(sample.chunkString+'_Chunk') or x==sample.chunkString]
    chunks=chunks[:maxN] if maxN>0 else chunks
    sumWeights=0
    failedChunks=[]
    goodChunks  =[]
    const = 'All Events' if sample.isData else 'Sum Weights'
    for i, s in enumerate(chunks):
            logfile = "/".join([sample.path, s['name'], sample.skimAnalyzerDir,'SkimReport.txt'])
#      print logfile
            if os.path.isfile(logfile):
                line = [x for x in subprocess.check_output(["cat", logfile]).split('\n') if x.count(const)]
                assert len(line)==1,"Didn't find normalization constant '%s' in  number in file %s"%(const, logfile)
                n = int(float(line[0].split()[2]))
                sumW = float(line[0].split()[2])
                inputFilename = '/'.join([sample.path, s['name'], sample.rootFileLocation])
#        print sumW, inputFilename
                if os.path.isfile(inputFilename) and checkRootFile(inputFilename):
                    sumWeights+=sumW
                    s['file']=inputFilename
                    goodChunks.append(s)
                else:
                    failedChunks.append(chunks[i])
            else:
                print "log file not found:  ", logfile
                failedChunks.append(chunks[i])
#    except: print "Chunk",s,"could not be added"
    eff = round(100*len(failedChunks)/float(len(chunks)),3)
    print "Chunks: %i total, %i good (normalization constant %f), %i bad. Inefficiency: %f"%(len(chunks),len(goodChunks),sumWeights,len(failedChunks), eff)
    for s in failedChunks:
        print "Failed:",s
    return goodChunks, sumWeights

def getObjFromFile(fname, hname):
    f = ROOT.TFile(fname)
    assert not f.IsZombie()
    f.cd()
    htmp = f.Get(hname)
    if not htmp:  return htmp
    ROOT.gDirectory.cd('PyROOT:/')
    res = htmp.Clone()
    f.Close()
    return res

def writeObjToFile(fname, obj):
    gDir = ROOT.gDirectory.GetName()
    f = ROOT.TFile(fname, 'recreate')
    objw = obj.Clone()
    objw.Write()
    f.Close()
    ROOT.gDirectory.cd(gDir+':/')
    return

def getVarValue(c, var, n=-1):
    try:
        att = getattr(c, var)
    except AttributeError:
        return float('nan')
    if n>=0:
#    print "getVarValue %s %i"%(var,n)
        if n<att.__len__():
            return att[n]
        else:
            return float('nan')
    return att

def getEList(chain, cut, newname='eListTMP'):
    chain.Draw('>>eListTMP_t', cut)
    #elistTMP_t = ROOT.gROOT.Get('eListTMP_t')
    elistTMP_t = ROOT.gDirectory.Get('eListTMP_t')
    elistTMP = elistTMP_t.Clone(newname)
    del elistTMP_t
    return elistTMP

def getObjDict(c, prefix, variables, i):
    res={var: getVarValue(c, prefix+var, i) for var in variables}
    res['index']=i
    return res

def getCollection(c, prefix, variables, counter_variable):
    return [getObjDict(c, prefix+'_', variables, i) for i in range(int(getVarValue(c, counter_variable)))]

def getCutYieldFromChain(c, cutString = "(1)", cutFunc = None, weight = "weight", weightFunc = None, returnVar=False):
    c.Draw(">>eList", cutString)
    elist = ROOT.gDirectory.Get("eList")
    number_events = elist.GetN()
    res = 0.
    resVar=0.
    for i in range(number_events):
        c.GetEntry(elist.GetEntry(i))
        if (not cutFunc) or cutFunc(c):
            if weight:
                w = c.GetLeaf(weight).GetValue()
            else:
                w=1.
            if weightFunc:
                w*=weightFunc(c)
            res += w
            resVar += w**2
    del elist
    if returnVar:
        return res, resVar
    return res

def getYieldFromChain(c, cutString = "(1)", weight = "weight", returnError=False):
    h = ROOT.TH1D('h_tmp', 'h_tmp', 1,0,2)
    h.Sumw2()
    c.Draw("1>>h_tmp", "("+weight+")*("+cutString+")", 'goff')
    res = h.GetBinContent(1)
    resErr = h.GetBinError(1)
#  print "1>>h_tmp", weight+"*("+cutString+")",res,resErr
    del h
    if returnError:
        return res, resErr
    return res

def getPlotFromChain(c, var, binning, cutString = "(1)", weight = "weight", binningIsExplicit=False, addOverFlowBin=''):
    if binningIsExplicit:
        h = ROOT.TH1D('h_tmp', 'h_tmp', len(binning)-1, array('d', binning))
#    h.SetBins(len(binning), array('d', binning))
    else:
        if len(binning)==6:
            h = ROOT.TH2D('h_tmp', 'h_tmp', *binning)
        else:
            h = ROOT.TH1D('h_tmp', 'h_tmp', *binning)
    c.Draw(var+">>h_tmp", weight+"*("+cutString+")", 'goff')
    res = h.Clone()
    h.Delete()
    del h
    if addOverFlowBin.lower() == "upper" or addOverFlowBin.lower() == "both":
        nbins = res.GetNbinsX()
#    print "Adding", res.GetBinContent(nbins + 1), res.GetBinError(nbins + 1)
        res.SetBinContent(nbins , res.GetBinContent(nbins) + res.GetBinContent(nbins + 1))
        res.SetBinError(nbins , sqrt(res.GetBinError(nbins)**2 + res.GetBinError(nbins + 1)**2))
    if addOverFlowBin.lower() == "lower" or addOverFlowBin.lower() == "both":
        res.SetBinContent(1 , res.GetBinContent(0) + res.GetBinContent(1))
        res.SetBinError(1 , sqrt(res.GetBinError(0)**2 + res.GetBinError(1)**2))
    return res

