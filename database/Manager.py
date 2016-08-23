import sqlite3
import os
import datetime

# =============================================================

# Database.manager is in charge of handling lower-level functions that deal
# Directly with the database.  (ex: Opening a connection, inserting some SQL, deleting all tables... etc

# =============================================================


#  Connects to DB file
def get_db_connection():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'ap_db.sqlite'))
    return conn


def insert_and_commit(sql_command, *args, **kwargs):
    connection = get_db_connection()
    connection.cursor().execute(sql_command, *args, **kwargs)
    connection.commit()
    connection.close()


def create_all_tables():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(SQL_TO_CREATE_USER_TABLE)
    # cursor.execute(SQL_TO_CREATE_POST_TABLE)
    # cursor.execute(SQL_TO_CREATE_POINTS_TABLE)
    # cursor.execute(SQL_TO_CREATE_COMMENTS_TABLE)
    # cursor.execute(SQL_TO_CREATE_ACTIVITY_TABLE)
    db_connection.commit()
    db_connection.close()

#I DON'T THINK I NEED THIS!!
# def select_contact_columns(columns_to_select):
# # Enter columns_to_select as list or tuple
#     final_SQL_query = "SELECT "
#
#     if columns_to_select:
#         for column_name in columns_to_select:
#             final_SQL_query += column_name + ", "
#         final_SQL_query.rstrip(',')
#         final_SQL_query += 'FROM USER'
#         return final_SQL_query
#
#     else:
#         "SELECT * FROM USER"


def select_user_by_userid(userid):
    connection = get_db_connection()
    connection.cursor().execute("SELECT * FROM USER WHERE rowid = (?)", (userid,))
    connection.commit()
    connection.close()


def select_user_by_email_address(email_address):
    connection = get_db_connection()
    connection.cursor().execute("SELECT * FROM USER WHERE email_address = (?)", (email_address,))
    connection.commit()
    connection.close()


def delete_user_by_username(username):
    connection = get_db_connection()
    connection.cursor().execute("DELETE FROM USER WHERE username = (?)", (username,))
    connection.commit()
    connection.close()


