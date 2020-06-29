import hashlib
import sqlite3
import json
import create_connection as cc
import check_name as cn
from getpass import getpass
from sqlite3 import Error

with open('config_db.json') as f:
    db_config = json.load(f)

def input_user():
    username = input('Username: ')
    while cn.main(username) is True:
        username = input('Username is already taken, please select another one: ')

    password_hash = hashlib.sha256(getpass('Please enter your password:').encode()).hexdigest()

    sql_instructions = f"INSERT INTO {db_config['table_name']} ({db_config['column_name'][0]}, {db_config['column_name'][1]}) VALUES ('{username}','{password_hash}')"
    add_user_data_to_db(sql_instructions)

def add_user_data_to_db(sql_instructions):
    conn = cc.create_connection(db_config['database_name'])

    try:
        c = conn.cursor()
        c.execute(sql_instructions)
        conn.commit()
        #print(sql_instructions)
    except Error as e:
        print('Error!: ',e)

input_user()