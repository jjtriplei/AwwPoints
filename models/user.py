import datetime
from database import Manager
import sqlite3
from models.exceptions import UsernameAlreadyExistsError, EmailAlreadyExistsError


#  USER CLASS SETTINGS


class User:
    def __init__(self, user_name, email_address, password):
        self.user_id = ""
        self.username = user_name
        self.email_address = email_address
        self.password = password
        self.last_logged_in = datetime.datetime.now()
        self.is_pass_sequential = True
        self.violation_count = 0
        self.profile_pic_url = ""

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
        print("Closed DB connection")

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
