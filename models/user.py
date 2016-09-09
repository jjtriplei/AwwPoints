import datetime
from database import Manager
import sqlite3
from models.exceptions import UsernameAlreadyExistsError, EmailAlreadyExistsError


#  USER CLASS SETTINGS

# (1, 'Joseph', 'Joseph@John.com', 12345, '2016-08-24 21:12:18.656620', 1, 0)

'''
CREATE TABLE IF NOT EXISTS USER (
username VARCHAR (255) NOT NULL UNIQUE,
email_address VARCHAR (255) NOT NULL UNIQUE,
password TINYINT NOT NULL,
last_logged_in DATETIME NOT NULL,
is_pass_sequential BOOLEAN NOT NULL DEFAULT 1,
violation_count TINYINT NOT NULL DEFAULT 0,
is_admin BOOLEAN NOT NULL DEFAULT 0,
is_active BOOLEAN NOT NULL DEFAULT 1 ,
profile_pic_URL VARCHAR (2083)
)
'''

class User:
    tuple_index = {
        "user_id": 0,
        "username": 1,
        "email_address": 2,
        "password": 3,
        "last_logged_in": 4,
        "is_pass_sequential": 5,
        "violation_count": 6,
        "is_admin": 7,
        "is_active": 8,
        "profile_pic_URL": 9
    }

    def __init__(self, user_name, email_address, password):


    def insert_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO USER (USERNAME,EMAIL_ADDRESS,PASSWORD,LAST_LOGGED_IN,IS_PASS_SEQUENTIAL) "
                "VALUES (?,?,?,?,?)", (self.username, self.email_address, self.password,
                                       datetime.datetime.now(), self.is_pass_sequential))
        except sqlite3.IntegrityError as error:
            if "email_address" in str(error).lower():
                raise EmailAlreadyExistsError
            elif "username" in str(error).lower():
                raise UsernameAlreadyExistsError
        else:
            print("Looks like account was created")
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def get_user_by_user_id(user_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT rowid, * FROM USER WHERE rowid = (?)", (user_id,))
        query_results = cursor.fetchall()
        db_connection.close()
        return query_results

    @staticmethod
    def get_user_by_email_address(email_address):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT rowid, * FROM USER WHERE email_address = (?)", (email_address,))
        query_results = cursor.fetchall()
        db_connection.close()
        return query_results

    @staticmethod
    def get_all_users():
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT rowid, * FROM USER")
        query_results = cursor.fetchall()
        db_connection.close()
        return query_results

    @staticmethod
    def delete_user_by_username(username):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM USER WHERE username = (?)", (username,))
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def delete_user_by_userid(user_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM USER WHERE rowid = (?)", (user_id,))
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def update_email_address(user_id, email_address):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE USER SET email_address = (?) WHERE  rowid= (?);",
                       (email_address, user_id,))
        db_connection.commit()
        db_connection.close()
