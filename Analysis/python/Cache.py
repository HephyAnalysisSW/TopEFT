import pickle, os, time
import errno

# Logging
import logging
logger = logging.getLogger(__name__)

from TopEFT.Tools.resultsDB import resultsDB

class Cache:
    def __init__(self, filename=None, verbosity=0, overwrite=False):
        self.verbosity=verbosity
        self.initCache(filename)

    def initCache(self, filename):
        self.filename=filename
        self.columns = ["region", "channel", "weights", "modification", "lumi"]
        self.DB = resultsDB(filename, "Cache", self.columns)

    def translateKey(self, key):
        '''
        This is unsafe. Should change the key structure in the estimators instead - will do so asap.
        '''
        newKey = {c:0 for c in self.columns}
        for i,c in enumerate(self.columns):
            newKey[c] = str(key[i])
        return newKey

    def contains (self, key):
        key = self.translateKey(key)
        return self.DB.contains(key)

    def get(self, key):
        key = self.translateKey(key)
        return self.DB.get(key)

    def add(self, key, val, overwrite=True):
        key = self.translateKey(key)
        return self.DB.add(key, val, overwrite)
