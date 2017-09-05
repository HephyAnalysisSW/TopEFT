'''
Implementation for CMS analyses
'''

# Standard imports
import os
import time
import sqlite3

from u_float import u_float

# Logger
import logging
logger = logging.getLogger(__name__)

class resultsDB:
    def __init__(self, database):
        self.database_file = database
        self.connect()
        try:
            self.cursor.execute('''CREATE TABLE cache (id text, value text, time_stamp real )''')
        except sqlite3.OperationalError:
            pass
        # try to aviod database malform problems
        self.cursor.execute('''PRAGMA journal_mode = DELETE''') # WAL doesn't work on network filesystems
        self.cursor.execute('''PRAGMA synchronus = 2''')
        self.close()

    def connect(self):
        self.database = sqlite3.connect(self.database_file)
        self.cursor = self.database.cursor()

    def close(self):
        self.cursor.close()
        self.database.close()
        del self.cursor
        del self.database
        
    def getKey(self, key):
        if ( type(key) == type(()) ) or ( type(key) == type([]) ):
            return '_'.join(list(key))
        else:
            return key

    def getObjects(self, key):
        key = self.getKey(key)
        selectionString = "SELECT * FROM cache WHERE id = '%s' ORDER BY time_stamp"%key
        self.connect()
        try:
            obj = self.cursor.execute(selectionString)
        except sqlite3.DatabaseError as e:
            logger.info( "There seems to be an issue with the database, trying to read again." )
            for i in range(5):
                try:
                    obj = self.cursor.execute(selectionString)
                    objs = [o for o in obj]
                    self.close()
                    return objs
                except:
                    logger.info( "Attempt no %i", i )
                    self.close()
                    self.connect()
                    time.sleep(1.0)
            raise e
        objs = [o for o in obj]
        self.close()
        return objs

    def contains(self, key):
        objs = self.getObjects(key)
        return len(objs)

    def getObject(self, key):
        objs = self.getObjects(key)
        try:
            return objs[-1]
        except IndexError:
            return 0

    def get(self, key):
        objs = self.getObjects(key)
        try:
            return u_float.fromString(objs[-1][1])
        except IndexError:
            return False

    def add(self, key, value, save, overwriteOldest=False):
        '''
        Add new object with timestamp
        '''
        key = self.getKey(key)
        selectionString = "INSERT INTO cache VALUES ('%s', '%s', '%f')"%(key,str(value),time.time())
        self.connect()
        try:
            self.cursor.execute(selectionString)
            self.database.commit()

        except sqlite3.OperationalError:
            logger.info( "Database locked, waiting." )
            time.sleep(1.0)
            self.add(key, value, save, overwriteOldest)

        except sqlite3.DatabaseError as e:
            logger.info( "There seems to be an issue with the database, trying to write again." )
            for i in range(60):  
                try:
                    self.cursor.execute(selectionString)
                    self.database.commit()
                    self.close()
                    return
                except:
                    logger.info( "Attempt no %i", i )
                    self.close()
                    self.connect()
                    time.sleep(1.0)
            raise e
        
        self.close()
        return

    def resetDatabase(self):
        if os.path.isfile(self.database_file):
            os.remove(self.database_file)
        self.__init__(self.database_file)

#    def __del__(self):
#        self.cursor.close()

