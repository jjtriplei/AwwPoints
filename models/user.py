import datetime
from database import Manager
import sqlite3


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
                "INSERT INTO USER (USERNAME,EMAIL_ADDRESS,PASSWORD,LAST_LOGGED_IN,IS_PASS_SEQUENTIAL) VALUES (?,?,?,?,?)",
                (self.username, self.email_address, self.password, datetime.datetime.now(), self.is_pass_sequential))
        except sqlite3.IntegrityError as error:
            if "email_address" in str(error).lower():
                print("Sorry Chummmmmmmmmmm-p. That email address is being used")
            elif "username" in str(error).lower():
                print("Sorry Sucka! Username already exists")
        else:
            print("Looks like account was created")
        db_connection.commit()
        db_connection.close()
        print("Closed DB connection")

    @staticmethod
    def get_user_by_userid(userid):
        connection = Manager.get_db_connection()
        connection.cursor().execute("SELECT * FROM USER WHERE rowid = (?)", (userid,))
        connection.close()

    @staticmethod
    def get_user_by_email_address(email_address):
        connection = Manager.get_db_connection()
        connection.cursor().execute("SELECT * FROM USER WHERE email_address = (?)", (email_address,))
        connection.close()

    @staticmethod
    def get_all_users():
        connection = Manager.get_db_connection()
        connection.cursor().execute("SELECT * FROM USER")
        connection.close()

    @staticmethod
    def delete_user_by_username(username):
        connection = Manager.get_db_connection()
        connection.cursor().execute("DELETE FROM USER WHERE username = (?)", (username,))
        connection.commit()
        connection.close()

    @staticmethod
    def delete_user_by_userid(userid):
        connection = Manager.get_db_connection()
        connection.cursor().execute("DELETE FROM USER WHERE rowid = (?)", (userid,))
        connection.commit()
        connection.close()

    @staticmethod
    def update_email_address(userid, email_address):
        connection = Manager.get_db_connection()
        connection.cursor().execute("UPDATE USER SET email_address = (?) WHERE  rowid= (?);",
                                    (email_address, userid,))
        connection.commit()
        connection.close()


# def create_user(username, email_address, password, last_logged_in, is_pass_sequential, cursor):
#     Manager.insert_and_commit("INSERT INTO USER (USERNAME,EMAIL_ADDRESS,PASSWORD,LAST_LOGGED_IN,IS_PASS_SEQUENTIAL) VALUES (?,?,?,?,?)",/
#     (username, email_address, password, last_logged_in, is_pass_sequential,))
