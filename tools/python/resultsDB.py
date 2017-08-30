'''
Implementation for CMS analyses
'''

import os, time
import sqlite3
from u_float import u_float

class resultsDB:
    def __init__(self, database):
        self.database_file = database
        self.database = sqlite3.connect(database)
        self.cursor = self.database.cursor()
        try:
            self.cursor.execute('''CREATE TABLE cache (id text, value text, time_stamp real )''')
        except sqlite3.OperationalError:
            print "Initializing existing database"

    def getKey(self, key):
        if ( type(key) == type(()) ) or ( type(key) == type([]) ):
            return '_'.join(list(key))
        else:
            return key

    def getObjects(self, key):
        key = self.getKey(key)
        selectionString = "SELECT * FROM cache WHERE id = '%s' ORDER BY time_stamp"%key
        obj = self.cursor.execute(selectionString)
        objs = [o for o in obj]
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
        print selectionString
        try:
            self.cursor.execute(selectionString)
            self.database.commit()
        except sqlite3.OperationalError:
            print "Database locked, waiting."
            time.sleep(0.1)
            self.add(key, value, save, overwriteOldest)
        return

    def resetDatabase(self):
        if os.path.isfile(self.database_file):
            os.remove(self.database_file)
        self.__init__(self.database_file)

#    def __del__(self):
#        self.cursor.close()

