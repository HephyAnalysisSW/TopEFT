# Standard imports
import pickle, os, time
import errno

# TopEFT 
from TopEFT.Tools.lock import waitForLock, removeLock

# Logger
import logging
logger = logging.getLogger(__name__)

class PickleCache:
    def __init__(self, filename=None, overwrite=False):
        self.initCache(filename)

    def initCache(self, filename):
        self.filename=filename
        if not os.path.isfile(filename) or os.stat(self.filename).st_size == 0:  # Check if there's already something in there
          logger.info( "File %s not found. Starting new cache.", filename )
          self._cache = {}
        else:
          try:
            waitForLock(filename)
            with open(filename, 'r') as f:
              self._cache = pickle.load(f)
            removeLock(filename)
            logger.info( "Loaded cache file %s", filename )
          except:# (IOError, ValueError, EOFError):
              logger.error( "File %s looks corrupted, please check before proceeding",  filename )
              exit(1)

    # Try to reload to cache file in order to get updates from other jobs/threads
    def reload(self, removeKey=None):
        if not os.path.isfile(self.filename) or os.stat(self.filename).st_size == 0:
          pass
        else:
          try:
            temp = self._cache
            waitForLock(self.filename)
            with open(self.filename, 'r') as f:
              self._cache = pickle.load(f)
              if removeKey and removeKey in self._cache:   # This is to avoid that an old value overwrites an updated value when using parallel jobs
                del self._cache[removeKey]
              self._cache.update(temp)
            removeLock(self.filename)
          except Exception as e:# (IOError, ValueError, EOFError):
              logger.warning( "PickleCache file %s could not be reloaded", self.filename )
              removeLock(self.filename)

    def contains (self, key):
        return key in self._cache

    def get(self, key):
        return self._cache[key]

    def add(self, key, val, save):
        self._cache[key] = val
        if save==True:
            logger.debug( "Storing new result %r to key %r", val, key )
            self.save(key)
        return self._cache[key]

    def save(self, removeKey = None):
        self.reload(removeKey)
        waitForLock(self.filename)
        with open(self.filename, 'w') as f:
          pickle.dump(self._cache, f)
        removeLock(self.filename)
        logger.debug( "Written cache file %s", self.filename )
