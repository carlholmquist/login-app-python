import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    #Checks if the given database already exists and ask if you want to replace it
    conn = None
    #Trys to connect to the database
    try:
        conn = sqlite3.connect(db_file)
        #print(sqlite3.version)
    #Print error if connection cannot be made
    except Error as e:
        print(e)
    #Return connection object?
    return conn
 