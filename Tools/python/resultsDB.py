'''
Implementation for CMS analyses

Concurrent writing is not supported in sqlite on network drives, hence there will be problems if multiple (batch) jobs from different worker nodes are writing to the same database file at the same time.
To circumvent this, we don't care about dataloss since a missing result will just be re-calculated in the next go.
This whole code is messy, however, it finally seems to work.

Establishing exclusive connections was also not successful, however, one might give it another shot at some point.
Use sth like
self.conn.isolation_level = 'EXCLUSIVE'
self.conn.execute('BEGIN EXCLUSIVE')

'''

# Standard imports
import os
import time
import sqlite3
import cPickle

from u_float import u_float

# Logger
import logging
logger = logging.getLogger(__name__)

class dbopen(object):
    """
    Simple CM for sqlite3 databases. Commits everything at exit.
    """
    def __init__(self, path, write=True):
        self.path = path
        self.conn = None
        self.cursor = None
        self.write = write

    def __enter__(self):
        logger.debug("Connecting to DB file %s", self.path)
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()



class resultsDB:
    def __init__(self, database, tableName, columns):
        '''
        Will create a table with name tableName, with the provided columns (as a list) and two additional columns: value and time_stamp
        '''
        self.database_file = database
        self.tableName      = tableName
        self.columns        = self.clean(columns)
        self.columns        = self.columns + ["value"]
        self.columnString   = ", ".join([ s+" text" for s in self.columns ])

        self.connect()
        try:
            with self.conn:
                '''
                Use context manager for connections. Closes the connection on exit.
                '''
                executeString = '''CREATE TABLE %s (%s, time_stamp real )'''%(self.tableName, self.columnString)
                try:
                    self.conn.execute(executeString)
                    # try to aviod database malform problems
                    self.conn.execute('''PRAGMA journal_mode = DELETE''') # WAL doesn't work on network filesystems
                    self.conn.execute('''PRAGMA synchronus = 2''')
                except sqlite3.OperationalError:
                    # Doesn't really matter if that doesn't work.
                    logger.debug("Table already exists.")
                except sqlite3.DatabaseError:
                    logger.debug("Concurrency problem. Table should already exist.")
        except:
            pass
        self.close()

    def clean(self, columns):
        return [ c for c in columns ]
    
    def dropTable(self):
        executeString = '''DROP TABLE %s'''%self.tableName
        self.connect()
        with self.conn:
            self.conn.execute(executeString)

    def connect(self):
        '''
        only establish the connection when needed, not when resultsDB object is created
        '''
        self.conn = sqlite3.connect(self.database_file)
    
    def cursor(self):
        self.cursor = self.database.cursor()

    def close(self):
        '''
        Not really needed anymore if all connections are handled with context manager
        '''
        self.conn.close()
        del self.conn
        
    def getObjects(self, key):
        '''
        Get all entries in the database matching the provided key.
        '''
        columns = self.clean(key.keys()+["value", "time_stamp"])
        selection = " AND ".join([ "%s = '%s'"%(k, key[k]) for k in key.keys() ])

        selectionString = "SELECT * FROM {} ".format(self.tableName) + " WHERE {} ".format(selection) + " ORDER BY time_stamp"

        logger.debug("Trying to read")
        for i in range(100):
            self.connect()
            try:
                with self.conn:
                    try:
                        obj = self.conn.execute(selectionString)
                        objs = [o for o in obj]
                        if len(objs) > 0:
                            logger.debug("Reading successfull.")
                        return objs
                    except sqlite3.OperationalError:
                        logger.debug("OE: Locked (reading).")
                    except sqlite3.DatabaseError:
                        logger.debug("DE: Locked (reading).")
                time.sleep(0.01)
            except:
                pass
            self.close()
        return False

    def getDicts(self, key):
        objs = self.getObjects(key)
        if objs:
            o = []
            for obj in objs:
                o.append({c:str(v) for c,v in zip( self.columns, obj ) })
            return o
        else:
            return False
    
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
        return len(objs) if type(objs) == type([]) else 1 # in case there's a locking problem act as if stuff existed

    def getObject(self, key):
        objs = self.getObjects(key)
        try:
            return objs[-1]
        except IndexError:
            return 0

    def get(self, key, plain=False):
        '''
        Careful! This method only returns the newest entry in the database that's matching the key. This is not necessarily a unique match!
        '''
        logger.debug("Getting only the newest entry in the database matching the key. You should know what you're doing here.")
        objs = self.getDicts(key)
        if not plain:
            if objs:
                if len(objs[-1]["value"]) > 50:
                    try:
                        return cPickle.loads(objs[-1]["value"])
                    except:
                        return False
                else:
                    try:
                        return u_float.fromString(objs[-1]["value"])
                    except IndexError:
                        return False
            else:
                return False
        else:
            try:
                return objs[-1]["value"]
            except:
                return False

    def addData(self, key, data, overwrite):
        '''
        add binary data to a databse as blob
        '''
        if overwrite and self.contains(key):
            self.removeObjects(key)

        columns = self.clean(key.keys()+["value"])
        if not sorted(columns) == sorted(self.columns):
            raise(ValueError("The columns don't match the table. Use the following: %s"%", ".join(self.columns)))
        
        columns += ["time_stamp"]
        pdata = cPickle.dumps(data, cPickle.HIGHEST_PROTOCOL)
        values  = key.values()
        
        # check if number of columns matches. By default, there is no error if not, but better be save than sorry.
        if len(key.keys())+1 < len(self.columns):
            raise(ValueError("The length of the given key doesn't match the number of columns in the table. The following columns (excluding value and time_stamp) are part of the table: %s"%", ".join(self.columns)))
        
        selectionString = "INSERT INTO {} ".format(self.tableName) + " ({}) ".format(", ".join( columns )) + " VALUES ({}".format(", ".join([ "'%s'"%i for i in values ])) + ", :data, '%s')"%time.time()
        
        for i in range(100):
            self.connect()
            try:
                with self.conn:
                    try:
                        self.conn.execute(selectionString, (sqlite3.Binary(pdata),))
                        logger.info("Added data to database.")
                        return data
                    except sqlite3.OperationalError:
                        logger.debug("OE: Locked (writing data).")
                    except sqlite3.DatabaseError:
                        logger.debug("DE: Locked (writing data).")
                time.sleep(0.01)
            except:
                pass
            self.close()

    def add(self, key, value, overwrite, overwriteOldest=False):
        '''
        new DB structure. key needs to be a python dictionary. Overwrite removes all previous entries found under the key.
        '''

        if overwrite and self.contains(key):
            logger.info("Overwriting old result.")
            self.removeObjects(key)

        logger.debug("Trying to write")
        columns = self.clean(key.keys()+["value"])
        if not sorted(columns) == sorted(self.columns):
            raise(ValueError("The columns don't match the table. Use the following: %s"%", ".join(self.columns)))
        
        columns += ["time_stamp"]
        values  = key.values()+[str(value), time.time()]
        
        # check if number of columns matches. By default, there is no error if not, but better be save than sorry.
        if len(key.keys())+1 < len(self.columns):
            raise(ValueError("The length of the given key doesn't match the number of columns in the table. The following columns (excluding value and time_stamp) are part of the table: %s"%", ".join(self.columns)))

        selectionString = "INSERT INTO {} ".format(self.tableName) + " ({}) ".format(", ".join( columns )) + " VALUES ({})".format(", ".join([ "'%s'"%i for i in values ]))

        for i in range(100):
            self.connect()
            try:
                with self.conn:
                    try:
                        self.conn.execute(selectionString)
                        logger.info("Added value %s to database",value)
                        return value
                    except sqlite3.OperationalError:
                        logger.debug("OE: Locked (writing).")
                    except sqlite3.DatabaseError:
                        logger.debug("DE: Locked (writing).")
                time.sleep(0.01)
            except:
                pass
            self.close()
                

    def removeObjects(self, key):
        '''
        Remove entries matching the key. Careful when not all columns are specified!
        '''
        selection = " AND ".join([ "%s = '%s'"%(k, key[k]) for k in key.keys() ])

        selectionString = "DELETE FROM {} ".format(self.tableName) + " WHERE {} ".format(selection)
        for i in range(100):
            self.connect()
            try:
                with self.conn:
                    try:
                        self.conn.execute(selectionString)
                        return
                    except sqlite3.OperationalError:
                        logger.debug("OE: Locked (removing).")
                    except sqlite3.DatabaseError:
                        logger.debug("DE: Locked (removing).")
                time.sleep(0.01)
            except:
                pass
            self.close()
        return False


    def resetDatabase(self):
        if os.path.isfile(self.database_file):
            os.remove(self.database_file)
        self.__init__(self.database_file)

