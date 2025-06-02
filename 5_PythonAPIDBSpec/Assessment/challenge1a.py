###############################################################################
# Python DB-API v2.0
###############################################################################
# the sqlite3 module is DB-API v2.0 compliant.
import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent.parent / 'debug_databases' / 'non-orm.sqlite3'

print(DATABASE_PATH)
# Complete the following function.
def connection():
    ''' Returns a SQLite database connection to a pre-created database file. 
       
        1.) Return a sqlite3 connection to the non-orm.sqlite3 database using the following code to form a connection string.

        str(DATABASE_PATH)

    '''
    return sqlite3.connect(str(DATABASE_PATH))
