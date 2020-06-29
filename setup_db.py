import os
import sqlite3
import json
from sqlite3 import Error
import create_connection as cc

'''Script that sets up new databases and checks if they already exists'''

with open('config_db.json') as f:
    db_config = json.load(f)

#Check if database is already existing
def check_existing_db (db_file):
    #Check if db exists
    if os.path.isfile(db_file):
        #Connect to db to let user see what tables it contains before taking action on it
        conn = cc.create_connection(db_file)
        if conn is not None:
            try:
                #query what table the db contains and take input if user want to delete or keep existing db
                c = conn.cursor()
                c.execute("SELECT * FROM sqlite_master;")
                print('This database already exists and currently contains: ', c.fetchall())
                print('--------------------------------------')
                answer = input('Do you want to delete and recreate it (y/n)?: ')
                if answer == 'y':
                    #Remove old db
                    os.remove(db_file)
                    #Return new connection which creates a new db if one doesnt exists
                    return cc.create_connection(db_file)
            except Error as e:
                print(e)
    return cc.create_connection(db_file)

#Function for creating table within database
def create_table(conn,sql_instructions):
    #Not exactly sure how this works
    try:
        c = conn.cursor()
        c.execute(sql_instructions)
        c.close()
    except Error as e:
        print(e)

def main(db_config):
    db_file = db_config['database_name']
    table_name = db_config['table_name']
    column1 = db_config['column_name'][0]
    column2 = db_config['column_name'][1]

    #The SQL commands getting executed
    sql_create_table_instructions = f'CREATE TABLE {table_name} ({column1} VARCHAR, {column2} VARCHAR);'

    #Calling to create connection
    conn = check_existing_db(db_file)

    #If connection is made ie not None, call the create table function
    if conn is not None:
        create_table(conn,sql_create_table_instructions)
    else:
        print('Cannot crate connection to database')

'''Basically makes sure main only is called if this is 
   script is run first hand and not when its imported'''
if __name__ == '__main__':
    main(db_config)


