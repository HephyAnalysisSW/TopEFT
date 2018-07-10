# Logging
import logging
import os
import json
logger = logging.getLogger(__name__)

from TopEFT.Analysis.Region import Region
from TopEFT.Tools.u_float import u_float
from TopEFT.Analysis.Cache import Cache
from TopEFT.Analysis.SetupHelpers import trilepChannels, quadlepChannels

class DataObservation():
    def __init__(self, name, sample, cacheDir=None):
        self.name = name
        self.sample=sample
        self.initCache(cacheDir)

    def initCache(self, cacheDir):
        if cacheDir:
            self.cacheDir=cacheDir
            cacheFileName = os.path.join(cacheDir, self.name+'.sq')
            if not os.path.exists(os.path.dirname(cacheFileName)):
                os.makedirs(os.path.dirname(cacheFileName))
            self.cache = Cache(cacheFileName, verbosity=1)
        else:
            self.cache=None

    def uniqueKey(self, region, channel, setup):
        if hasattr(setup, 'blinding'): return region, channel.name, json.dumps(setup.sys, sort_keys=True), json.dumps(setup.parameters, sort_keys=True), json.dumps(setup.lumi, sort_keys=True), setup.blinding
        else:                          return region, channel.name, json.dumps(setup.sys, sort_keys=True), json.dumps(setup.parameters, sort_keys=True), json.dumps(setup.lumi, sort_keys=True)

    # alias for cachedObservation to make it easier to call the same function as for the mc's
    def cachedEstimate(self, region, channel, setup, save=True, overwrite=False):
        return self.cachedObservation(region, channel, setup, save, overwrite)

    def cachedObservation(self, region, channel, setup, save=True, overwrite=False):
        key =  self.uniqueKey(region, channel, setup)
        if self.cache and self.cache.contains(key):
            res = self.cache.get(key)
            logger.debug( "Loading cached %s result for %r : %r"%(self.name, key, res) )
            return res
        elif self.cache:
            logger.info( "Adding cached %s result for %r"%(self.name, key) )
            return self.cache.add( key, self.observation( region, channel, setup), overwrite=overwrite )
        else:
            return self.observation( region, channel, setup)

    def observation(self, region, channel, setup):
        if channel.name=='all':
            if setup.nLeptons == 3: channels = trilepChannels
            elif setup.nLeptons == 4: channels = quadlepChannels
            else: raise NotImplementedError
            preSelection = setup.preselection('Data')
            cut = "&&".join([region.cutString(setup.sys['selectionModifier']), preSelection['cut']])

            logger.info( "Getting Data observation for channel %s and region %s"%(channel.name, region.cutString()))
            logger.info( "Using cut %s"% cut )

            if hasattr(setup, 'blinding') and setup.blinding: weight = 'weight*' + setup.blinding
            else:                                             weight = 'weight'
            return u_float(**self.sample.getYieldFromDraw(selectionString = cut, weightString = weight) )
            #return sum([self.cachedEstimate(region, channel, setup) for c in channels])

        #if channel=='SF':
        #    return sum([self.cachedObservation(region, c, setup) for c in ['MuMu', 'EE']])

        #else:
        #    preSelection = setup.preselection('Data', nElectrons=channel.nE, nMuons=channel.nMu)
        #    cut = "&&".join([region.cutString(setup.sys['selectionModifier']), preSelection['cut']])

        #    logger.debug( "Using cut %s"% cut )

        #    if hasattr(setup, 'blinding') and setup.blinding: weight = 'weight*' + setup.blinding
        #    else:                                             weight = 'weight'
        #    return u_float(**self.sample.getYieldFromDraw(selectionString = cut, weightString = weight) )
