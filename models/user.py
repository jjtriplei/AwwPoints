import datetime
from database import Manager
import sqlite3
from models.exceptions import UsernameAlreadyExistsError, EmailAlreadyExistsError


#  USER CLASS SETTINGS


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

    def __init__(self, user_tuple):
        if user_tuple:
            self.user_id = user_tuple[User.tuple_index["user_id"]]
            self.username = user_tuple[User.tuple_index["username"]]
            self.email_address = user_tuple[User.tuple_index["email_address"]]
            self.password = user_tuple[User.tuple_index["password"]]
            self.last_logged_in = user_tuple[User.tuple_index["last_logged_in"]]
            self.is_pass_sequential = user_tuple[User.tuple_index["is_pass_sequential"]]
            self.violation_count = user_tuple[User.tuple_index["violation_count"]]
            self.is_admin = user_tuple[User.tuple_index["is_admin"]]
            self.is_active = user_tuple[User.tuple_index["is_active"]]
            self.profile_pic_url = user_tuple[User.tuple_index["profile_pic_URL"]]
        else:
            self.user_id = None
            self.username = None
            self.email_address = None
            self.password = None
            self.last_logged_in = None
            self.is_pass_sequential = None
            self.violation_count = None
            self.is_admin = None
            self.is_active = None
            self.url = None

    def insert_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO USER (USERNAME,EMAIL_ADDRESS,PASSWORD,LAST_LOGGED_IN,IS_PASS_SEQUENTIAL,is_admin,"
                "is_active, profile_pic_url) VALUES (?,?,?,?,?,?,?,?)", (self.username, self.email_address,
                                                                         self.password, datetime.datetime.now(),
                                                                         self.is_pass_sequential, self.is_admin, 1,
                                                                         self.profile_pic_url))
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
