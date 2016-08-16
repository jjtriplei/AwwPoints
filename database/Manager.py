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
    cursor.execute("CREATE TABLE {table_name}({new_field} {field_type})".format(table_name='user_table', \
                                                            new_field='user_id', field_type='int' ' ' 'not null'))
    cursor.execute("ALTER TABLE {table_name} ADD COLUMN '{new_field}' {field_type} DEFAULT '{default_value}'" \
                   .format(table_name='user_table', new_field='username', field_type='varchar (255)' ' ' 'not null', default_value=None))
    cursor.execute("ALTER TABLE {table_name} ADD COLUMN '{new_field}' {field_type} DEFAULT '{default_value}'" \
                   .format(table_name='user_table', new_field='last_logged_in', field_type='datetime' ' ' 'not null', default_value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
    save_and_close_db_connection()



##Created table with initial column (WIP)
##table_name='user_table', new_field='user_id', field_type='tinyint'

## I want to create a list or dictionary with all of these values and iterate through it instead of \
## write a "curser.execute(ALTER TABLE ....) for each column"

# new_field='username', field_type='varchar (255)' ' ' 'not null', default_value=None
# new_field='email_address', field_type='varchar (255)' ' ' 'not null', default_value=None
# new_field='password', field_type='tinyint' ' ' 'not null'
# new_field='last_logged_in', field_type='datetime' ' ' 'not null' ' ' GETDATE()
# new_field='is_pass_sequential', field_type='boolean' ' ' 'not null', default_value=True
# new_field='violation_count', field_type='tinyint' ' ' 'not null', default_value=0



cursor = get_db_cursor()

sql_to_create_user_table()


