import sqlite3
import os
import datetime


#  Connects to DB file
def get_db_connection():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__),'ap_db.sqlite'))
    return conn


def get_db_cursor():
    db_connection = get_db_connection()
    return db_connection.cursor()


def save_and_close_db_connection():
    get_db_connection().commit()
    get_db_connection().close()


## FIX FUNCTION. FUNCTION SHOULD ONLY RETURN SQL

def sql_to_create_user_table():
    cursor = get_db_cursor()
    cursor.execute("CREATE TABLE 'user_table' ('user_id' 'int' not null DEFAULT 1 PRIMARY KEY)")
    cursor.execute("ALTER TABLE 'user_table' ADD COLUMN 'username' 'varchar (255)' not null DEFAULT None")
    cursor.execute("ALTER TABLE 'user_table' ADD COLUMN 'email_address' 'varchar (255)' not null DEFAULT None")
    cursor.execute("ALTER TABLE 'user_table' ADD COLUMN 'password' 'tinyint' not null DEFAULT None")
    cursor.execute("ALTER TABLE 'user_table' ADD COLUMN 'last_logged_in' 'datetime' not null DEFAULT None")
    cursor.execute("ALTER TABLE 'user_table' ADD COLUMN 'is_pass_sequential' 'boolean' not null DEFAULT True")
    cursor.execute("ALTER TABLE 'user_table' ADD COLUMN 'violation_count' 'tinyint' not null DEFAULT 0")
    save_and_close_db_connection()



##Created table with initial column (WIP)
##table_name='user_table', new_field='user_id', field_type='tinyint'

## I want to create a list or dictionary with all of these values and iterate through it instead of \
## write a "curser.execute(ALTER TABLE ....) for each column"



cursor = get_db_cursor()

sql_to_create_user_table()


