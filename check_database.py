import sqlite3
import json
from sqlite3 import Error

with open('config_db.json') as f:
    db_config = json.load(f)

def create_connection(db_file):
    #Checks if the given database already exists and ask if you want to replace it
    conn = None
    #Trys to connect to the database
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    #Print error if connection cannot be made
    except Error as e:
        print(e)
    #Return connection object?
    return conn

def select_all_tasks(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    db_file = db_config['database_name']
    conn = create_connection(db_file)

    select_all_tasks(conn)

main()