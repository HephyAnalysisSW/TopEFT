import pickle, os, time
import errno

from TopEFT.tools.resultsDB import resultsDB

class Cache:
    def __init__(self, filename=None, verbosity=0, overwrite=False):
        self.verbosity=verbosity
        self.initCache(filename)

    def initCache(self, filename):
        self.filename=filename
        self.DB = resultsDB(filename, "Cache", ["key"])

    def contains (self, key):
        return self.DB.contains(key)

    def get(self, key):
        return self.DB.get(key)

    def add(self, key, val, overwrite=True):
        return self.DB.add(key, val, overwrite)
