###############################################################################
# Python DB-API v2.0
###############################################################################
# the sqlite3 module is DB-API v2.0 compliant.
import sqlite3

# Complete the following function.
def add_user(dbconn: sqlite3.Connection, full_name: str, reference: str, postcount: int):
    ''' add_user adds a user record to the database.

        1.) Create a user record using the provided arguments and persist the changes. 

        Database Schema:
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                full_name TEXT, 
                reference TEXT,
                postcount INTEGER
            );
        >>> conn = sqlite3.connect(':memory:')
        >>> _ = conn.execute("CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT, reference TEXT, postcount INTEGER );")
        >>> add_user(conn, 'a', '@a', 2_000)

    '''
    

# Complete the following function.
def top_poster_reference(dbconn: sqlite3.Connection) -> str:
    ''' top_poster_reference returns the reference of the user with the highest postcount.

        1.) Select the reference for the user with the most posts.
        2.) Return the selected reference as a str. 

        Database Schema:
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                full_name TEXT, 
                reference TEXT,
                postcount INTEGER
            );

        Example Data:
            { "full_name": "a", "reference": "@a", "postcount": 2_000 },
            { "full_name": "b", "reference": "@b", "postcount": 1_000 }

        >>> conn = sqlite3.connect(':memory:')
        >>> _ = conn.execute("CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT, reference TEXT, postcount INTEGER );")
        >>> add_user(conn, "a", "@a", 2_000)
        >>> add_user(conn, "b", "@b", 1_000)
        >>> top_poster_reference(conn)
        '@a'
        
    '''
    


# Complete the following function.
def post_count_gt_n(dbconn: sqlite3.Connection, n: int) -> list[tuple[str, str]]:
    ''' post_count_gt_n returns a list of (reference, postcount) tuples for user's with a postcount greater than n.

        1.) Select reference and postcount for all users with a postcount greater than the provided n argument.
        2.) Return the selected as a list of tuples: (reference, postcount)

        Database Schema:
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                full_name TEXT, 
                reference TEXT,
                postcount INTEGER
            );

        Example Data:
            { "full_name": "a", "reference": "@a", "postcount": 2_000 },
            { "full_name": "b", "reference": "@b", "postcount": 1_000 },
            { "full_name": "c", "reference": "@c", "postcount": 100 },

        >>> conn = sqlite3.connect(':memory:')
        >>> _ = conn.execute("CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, full_name TEXT, reference TEXT, postcount INTEGER );")
        >>> add_user(conn, "a", "@a", 2_000)
        >>> add_user(conn, "b", "@b", 1_000)
        >>> add_user(conn, "c", "@c", 100)
        >>> post_count_gt_n(conn, 500)
        [('@a', 2000), ('@b', 1000)]
        
    '''
    
def connection():
    ''' Returns a SQLite database connection to a pre-created database file. 
        Use this connection to assist while developing, if needed.

        Example:

        >>> conn = connection()
        >>> add_user(conn, 'a', '@a', 500)

    '''
    return sqlite3.connect('debug_databases/non-orm.sqlite3')


if __name__ == '__main__':
    conn = connection()
    # Optional debug code here...
    # Example: 
    # print(post_count_gt_n(conn, 2000))
