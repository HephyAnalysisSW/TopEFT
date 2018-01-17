jmeVariations = ["JER", "JERUp", "JERDown", "JECUp", "JECDown"]
metVariations = ['UnclusteredEnUp', 'UnclusteredEnDown']

# Standard imports
import os
import abc
from math import sqrt
import json

# TopEFT
from TopEFT.Analysis.Cache import Cache
from TopEFT.Tools.u_float import u_float
from TopEFT.Analysis.SetupHelpers import channels

# Logging
import logging
logger = logging.getLogger(__name__)

class SystematicEstimator:
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, cacheDir=None):
        self.name = name
        self.initCache(cacheDir)
        self.isSignal = False

    def initCache(self, cacheDir):
        if cacheDir:
            self.cacheDir       = cacheDir
            try:    os.makedirs(cacheDir)
            except: pass

            cacheFileName       = os.path.join(cacheDir, self.name+'.sq')
            helperCacheFileName = os.path.join(cacheDir, self.name+'_helper.sq')

            self.cache       = Cache(cacheFileName,       verbosity=1)
            self.helperCache = Cache(helperCacheFileName, verbosity=1) if self.name.count('DD') else None
        else:
            self.cache=None
            self.helperCache=None

    # For the datadriven subclasses which often need the same getYieldFromDraw we write those yields to a cache
    def yieldFromCache(self, setup, sample, c, selectionString, weightString):
        s = (sample, c, selectionString, weightString)
        if self.helperCache and self.helperCache.contains(s):
          return self.helperCache.get(s)
        else:
          yieldFromDraw = u_float(**setup.samples[sample][c].getYieldFromDraw(selectionString, weightString))
          if self.helperCache: self.helperCache.add(s, yieldFromDraw )
          return yieldFromDraw

    def uniqueKey(self, region, channel, setup):
        sysForKey = setup.sys.copy()
        sysForKey['reweight'] = 'TEMP'
        reweightKey ='["' + '", "'.join(sorted([i for i in setup.sys['reweight']])) + '"]' # little hack to preserve order of list when being dumped into json
        return region, channel, json.dumps(sysForKey, sort_keys=True).replace('"TEMP"',reweightKey), json.dumps(setup.parameters, sort_keys=True), json.dumps(setup.lumi, sort_keys=True)

    def replace(self, i, r):
        try:
          if i.count('reweight'): return i.replace(r[0], r[1])
          else:                   return i
        except:                   return i

    def cachedEstimate(self, region, channel, setup, save=True, overwrite=False):
        key =  self.uniqueKey(region, channel, setup)
        if (self.cache and self.cache.contains(key)) and not overwrite:
            res = self.cache.get(key)
            logger.debug( "Loading cached %s result for %r : %r"%(self.name, key, res) )
        elif self.cache:
            logger.info( "Calculating %s result for %r"%(self.name, key) )
            estimate = self._estimate( region, channel, setup)
            res = self.cache.add( key, estimate )
            logger.debug( "Adding cached %s result for %r : %r" %(self.name, key, estimate) )
        else:
            res = self._estimate( region, channel, setup)
        return res# if res > 0 else u_float(0,0)

    @abc.abstractmethod
    def _estimate(self, region, channel, setup):
        '''Estimate yield in 'region' using setup'''
        return

    def PUSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightPU36fbUp']}))
        down = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightPU36fbDown']}))
        return abs(0.5*(up-down)/ref) if ref > 0 else max(up,down)

    def topPtSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'remove':['reweightTopPt']}))
        return abs(0.5*(up-ref)/ref) if ref > 0 else up

    def JERSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'JERUp'}))
        down = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'JERDown'}))
        return abs(0.5*(up-down)/ref) if ref > 0 else max(up, down)

    def JECSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'JECUp'}))
        down = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'JECDown'}))
        return abs(0.5*(up-down)/ref) if ref > 0 else max(up, down)

    def unclusteredSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'UnclusteredEnUp'}))
        down = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'UnclusteredEnDown'}))
        return abs(0.5*(up-down)/ref) if ref > 0 else max(up, down)

    #def leptonFSSystematic(self, region, channel, setup):
    #    ref  = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightLeptonFastSimSF']}))
    #    up   = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightLeptonFastSimSFUp']}))
    #    down = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightLeptonFastSimSFDown']}))
    #    return abs(0.5*(up-down)/ref) if ref > 0 else max(up, down)

    def btaggingSFbSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_b_Up']}))
        down = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_b_Down']}))
        return abs(0.5*(up-down)/ref) if ref > 0 else max(up, down)

    def btaggingSFlSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_l_Up']}))
        down = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_l_Down']}))
        return abs(0.5*(up-down)/ref) if ref > 0 else max(up, down)

    def btaggingSFFSSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_FS_Up']}))
        down = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_FS_Down']}))
        return abs(0.5*(up-down)/ref) if ref > 0 else max(up, down)

    def leptonSFSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightLeptonSFUp']}))
        down = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightLeptonSFDown']}))
        return abs(0.5*(up-down)/ref) if ref > 0 else max(up, down)

    def triggerSystematic(self, region, channel, setup):
        ref  = self.cachedEstimate(region, channel, setup)
        up   = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightDilepTriggerBackupUp']}))
        down = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['reweightDilepTriggerBackupDown']}))
        return abs(0.5*(up-down)/ref) if ref > 0 else max(up, down)

    def reweight2D(self, region, channel, setup, f):
        ref = 0
        for r in setup.reweightRegions:
            if r.vals['Z_pt'][0] >= region.vals['Z_pt'][0] and (r.vals['Z_pt'][1] <= region.vals['Z_pt'][1] or region.vals['Z_pt'][1] == -1) and r.vals['cosThetaStar'][0] >= region.vals['cosThetaStar'][0] and r.vals['cosThetaStar'][1] <= region.vals['cosThetaStar'][1]:
                # This only works if the reweightRegions are aligned!!
                #print "in", r
                val     = self.cachedEstimate(r, channel, setup)
                weight  = f(r.vals['Z_pt'][0], r.vals['cosThetaStar'][0])
                ref += val*weight
            #else:
            #    print "out", r
        return ref

    #def fastSimMETSystematic(self, region, channel, setup):
    #    ref  = self.cachedEstimate(region, channel, setup)
    #    gen  = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'genMet'}))
    #    assert ref+gen > 0, "denominator > 0 not fulfilled, this is odd and should not happen!"
    #    return abs(ref-gen)/(ref+gen)

    #def fastSimPUSystematic(self, region, channel, setup):
    #    ''' implemented based on the official SUSY recommendation https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSRecommendationsMoriond17#Pileup_lumi
    #    '''
    #    incl        = self.cachedEstimate(region, channel, setup.systematicClone())
    #    incl_nvert  = self.cachedEstimate(region, channel, setup.systematicClone({'reweight':['nVert']}))
    #    if incl.val > 0:
    #        exp_nvert = int(incl_nvert.val/incl.val)
    #        incl_nvert = incl_nvert/incl
    #    else:
    #        return u_float(1) # Use 100% uncertainty until we have a better idea
    #    hiPU        = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'nVert>='+str(exp_nvert)}))
    #    hiPU_nvert  = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'nVert>='+str(exp_nvert), 'reweight':['nVert']}))
    #    loPU        = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'nVert<'+str(exp_nvert)}))
    #    loPU_nvert  = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'nVert<'+str(exp_nvert), 'reweight':['nVert']}))
    #    if loPU.val > 0 and hiPU.val > 0:
    #        loPU_nvert = loPU_nvert/loPU
    #        hiPU_nvert = hiPU_nvert/hiPU
    #    else:
    #        return u_float(1) # Use 100% uncertainty until we have a better idea

    #    k_central   = (loPU.val - hiPU.val)/(loPU_nvert.val - hiPU_nvert.val)
    #    k_loUp      = ((loPU.val + loPU.sigma) - (hiPU.val - hiPU.sigma))/(loPU_nvert.val - hiPU_nvert.val)
    #    k_loDown    = ((loPU.val - loPU.sigma) - (hiPU.val + hiPU.sigma))/(loPU_nvert.val - hiPU_nvert.val)
    #    
    #    d_central   = loPU.val - k_central*(loPU_nvert.val - incl_nvert.val)
    #    d_loUp      = loPU.val + loPU.sigma - k_loUp*(loPU_nvert.val - incl_nvert.val)
    #    d_loDown    = loPU.val - loPU.sigma - k_loDown*(loPU_nvert.val - incl_nvert.val)
    #    
    #    data_PU = setup.dataPUHistForSignal
    #    fold_loUp   = 0.
    #    fold_loDown = 0.
    #    for i in range(1,data_PU.GetNbinsX()+1):
    #        fold = (k_loUp*(i - incl_nvert.val) + d_loUp) * data_PU.GetBinContent(i)
    #        if fold > 0:
    #            fold_loUp += fold
    #        fold = (k_loDown*(i - incl_nvert.val) + d_loDown) * data_PU.GetBinContent(i)
    #        if fold > 0:
    #            fold_loDown += fold
    #    ref  = self.cachedEstimate(region, channel, setup)
    #    gen  = self.cachedEstimate(region, channel, setup.systematicClone({'selectionModifier':'genMet'}))
    #    unc = min([abs(fold_loDown - fold_loUp)/(0.5*(ref.val+gen.val)), 1.])
    #    return u_float(unc)

    def getBkgSysJobs(self, region, channel, setup):
        l = [
            (region, channel, setup.systematicClone({'reweight':['reweightPU36fbUp']})),
            (region, channel, setup.systematicClone({'reweight':['reweightPU36fbDown']})),

            (region, channel, setup.systematicClone({'remove':['reweightTopPt']})),

            (region, channel, setup.systematicClone({'selectionModifier':'JERUp'})),
            (region, channel, setup.systematicClone({'selectionModifier':'JERDown'})),

            (region, channel, setup.systematicClone({'selectionModifier':'JECUp'})),
            (region, channel, setup.systematicClone({'selectionModifier':'JECDown'})),

            (region, channel, setup.systematicClone({'selectionModifier':'UnclusteredEnUp'})),
            (region, channel, setup.systematicClone({'selectionModifier':'UnclusteredEnDown'})),

            (region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_b_Up']})),
            (region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_b_Down']})),
            (region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_l_Up']})),
            (region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_l_Down']})),

            (region, channel, setup.systematicClone({'reweight':['reweightLeptonSFDown']})),
            (region, channel, setup.systematicClone({'reweight':['reweightLeptonSFUp']})),

            (region, channel, setup.systematicClone({'reweight':['reweightDilepTriggerBackupDown']})),
            (region, channel, setup.systematicClone({'reweight':['reweightDilepTriggerBackupUp']})),
        ]
        return l

    def getSigSysJobs(self, region, channel, setup):
        l = self.getBkgSysJobs(region = region, channel = channel, setup = setup)

        # no extra signal uncertainties
        #if isFastSim:
        #    l.extend( [\
        #        (region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_FS_Up']})),
        #        (region, channel, setup.systematicClone({'reweight':['reweightBTag_SF_FS_Down']})),
        #        (region, channel, setup.systematicClone({'reweight':['reweightLeptonFastSimSFUp']})),
        #        (region, channel, setup.systematicClone({'reweight':['reweightLeptonFastSimSFDown']})),
        #        (region, channel, setup.systematicClone({'selectionModifier':'genMet'})),
        #        (region, channel, setup.systematicClone({'selectionModifier':'highPU'})),
        #        (region, channel, setup.systematicClone({'selectionModifier':'lowPU'})),

        #    ] )

        return l

    def getTexName(self, channel, rootTex=True):
        try:
          name = self.texName
        except:
          try:
            name = self.sample[channel].texName
          except:
            try:
              texNames = [self.sample[c].texName for c in channels]                # If all, only take texName if it is the same for all channels
              if texNames.count(texNames[0]) == len(texNames):
                name = texNames[0]
              else:
                name = self.name
            except:
              name = self.name
        if not rootTex: name = "$" + name.replace('#','\\') + "$" # Make it tex format
        return name
