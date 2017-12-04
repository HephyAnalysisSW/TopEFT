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
    def __init__(self, database, tableName, columns):
        '''
        Will create a table with name tableName, with the provided columns (as a list) and two additional columns: value and time_stamp
        '''
        self.database_file = database
        self.connect()
        self.tableName      = tableName
        self.columns        = self.clean(columns)
        self.columns        = self.columns + ["value"]
        self.columnString   = ", ".join([ s+" text" for s in self.columns ])
        executeString = '''CREATE TABLE %s (%s, time_stamp real )'''%(self.tableName, self.columnString)
        try:
            self.cursor.execute(executeString)
        except sqlite3.OperationalError:
            pass
        # try to aviod database malform problems
        self.cursor.execute('''PRAGMA journal_mode = DELETE''') # WAL doesn't work on network filesystems
        self.cursor.execute('''PRAGMA synchronus = 2''')
        self.close()

    def clean(self, columns):
        #return [ c.replace("-","m").replace(".","p") for c in columns ]
        return [ c for c in columns ]

    def connect(self):
        self.database = sqlite3.connect(self.database_file)
        self.cursor = self.database.cursor()

    def close(self):
        self.cursor.close()
        self.database.close()
        del self.cursor
        del self.database
        
    def getObjects(self, key):
        '''
        Get all entries in the database matching the provided key.
        '''
        columns = self.clean(key.keys()+["value", "time_stamp"])
        selection = " AND ".join([ "%s = '%s'"%(k, key[k]) for k in key.keys() ])

        selectionString = "SELECT * FROM {} ".format(self.tableName) + " WHERE {} ".format(selection) + " ORDER BY time_stamp"
        self.connect()
        
        for i in range(60):

            try:
                obj = self.cursor.execute(selectionString)
                objs = [o for o in obj]
                self.close()
                return objs

            except sqlite3.DatabaseError as e:
                logger.info( "There seems to be an issue with the database %s, trying to read again.", self.database_file)
                logger.info( "Attempt no %i", i )
                self.close()
                self.connect()
                time.sleep(1.0)

        self.close()
        raise e

    def getDicts(self, key):
        objs = self.getObjects(key)
        o = []
        for obj in objs:
            o.append({c:str(v) for c,v in zip( self.columns, obj ) })
        return o
    
    def getTable(self, key):
        '''
        Get a nice table printed on the screen of all entries in the database matching the provided key
        '''
        d = self.getDicts(key)
        tableColumns = ["Row#"] + self.columns
        header = "{:6}" + "| {:7} "*(len(self.columns)-1) + "| {:15} "
        print "="*(6+18+10*(len(self.columns)-1))
        print header.format(*tableColumns)
        print "="*(6+18+10*(len(self.columns)-1))
        row = "{:6}" + "  {:7} "*(len(self.columns)-1) + "| {:15} "
        lineCount = 0
        for entry in d:
            r = [lineCount]
            for col in self.columns:
                r.append(entry[col])
            print row.format(*r)
            lineCount += 1
            if lineCount%50==0 and lineCount>0:
                a = raw_input("continue scanning? 'q' to quit: ")
                if a == 'q': break
            

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
        '''
        Careful! This method only returns the newest entry in the database that's matching the key. This is not necessarily a unique match!
        '''
        logger.debug("Getting only the newest entry in the database matching the key. You should know what you're doing here.")
        objs = self.getDicts(key)
        try:
            return u_float.fromString(objs[-1]["value"])
        except IndexError:
            return False

    def add(self, key, value, overwrite, overwriteOldest=False):
        '''
        new DB structure. key needs to be a python dictionary. Overwrite removes all previous entries found under the key.
        '''

        if overwrite and self.contains(key):
            self.removeObjects(key)

        columns = self.clean(key.keys()+["value"])
        if not sorted(columns) == sorted(self.columns):
            raise(ValueError("The columns don't match the table. Use the following: %s"%", ".join(self.columns)))
        
        columns += ["time_stamp"]
        values  = key.values()+[str(value), time.time()]
        
        # check if number of columns matches. By default, there is no error if not, but better be save than sorry.
        if len(key.keys())+1 < len(self.columns):
            raise(ValueError("The length of the given key doesn't match the number of columns in the table. The following columns (excluding value and time_stamp) are part of the table: %s"%", ".join(self.columns)))

        selectionString = "INSERT INTO {} ".format(self.tableName) + " ({}) ".format(", ".join( columns )) + " VALUES ({})".format(", ".join([ "'%s'"%i for i in values ]))
        self.connect()

        for i in range(60):
            try:
                self.cursor.execute(selectionString)
                self.database.commit()
                logger.info("Added value %s to database",value)
                self.close()
                return value

            except sqlite3.OperationalError as e:
                logger.info( "Database locked, waiting." )
                time.sleep(1.0)

            except sqlite3.DatabaseError as e:
                logger.info( "There seems to be an issue with the database, trying to write again." )
                logger.info( "Attempt no %i", i )
                self.close()
                self.connect()
                time.sleep(1.0)
        
        self.close()
        raise e

    def removeObjects(self, key):
        '''
        Remove entries matching the key. Careful when not all columns are specified!
        '''
        selection = " AND ".join([ "%s = '%s'"%(k, key[k]) for k in key.keys() ])

        selectionString = "DELETE FROM {} ".format(self.tableName) + " WHERE {} ".format(selection)
        self.connect()
        
        for i in range(60):

            try:
                self.cursor.execute(selectionString)
                self.database.commit()
                self.close()
                return

            except sqlite3.DatabaseError as e:
                logger.info( "There seems to be an issue with the database, trying again." )
                logger.info( "Attempt no %i", i )
                self.close()
                self.connect()
                time.sleep(1.0)

        self.close()
        raise e


    def resetDatabase(self):
        if os.path.isfile(self.database_file):
            os.remove(self.database_file)
        self.__init__(self.database_file)

