import datetime
from database import Manager
import sqlite3
from models.exceptions import UsernameAlreadyExistsError, EmailAlreadyExistsError

class User:
    # (1, 'Joseph0', 'Email0@aol.com', 123, '2016-09-07 18:57:00.026029', 1, 0, 'False', 'True', None)
    tuple_positions = {
        "row_id": 0,
        "username": 1,
        "email_address": 2,
        "password": 3,
        "last_logged_in": 4,
        "is_pass_sequential": 5,
        "violation_count": 6,
        "is_admin": 7,
        "is_active": 8,
        "profile_pic_url": 9
    }

    def __init__(self, user_tuple=None):
        if user_tuple:
            self.user_id = user_tuple[User.tuple_positions["row_id"]]
            self.username = user_tuple[User.tuple_positions["username"]]
            self.email_address = user_tuple[User.tuple_positions["email_address"]]
            self.password = user_tuple[User.tuple_positions["password"]]
            self.last_logged_in = user_tuple[User.tuple_positions["last_logged_in"] or datetime.datetime.now()]
            self.is_pass_sequential = user_tuple[User.tuple_positions["is_pass_sequential"] or 1]
            self.is_admin = user_tuple[User.tuple_positions["is_admin"] or 0]
            self.is_active = user_tuple[User.tuple_positions["is_active"] or 1]
            self.violation_count = user_tuple[User.tuple_positions["violation_count"]]
            self.profile_pic_url = user_tuple[User.tuple_positions["profile_pic_url"]]
        else:
            # These are default values - if no data is passed in from the DB as a tuple, these will be set as the values
            # On the class object.
            self.user_id = None
            self.username = None
            self.email_address = None
            self.password = None
            self.is_admin = None
            self.is_active = None
            self.violation_count = None
            self.profile_pic_url = None
            self.last_logged_in = datetime.datetime.now()
            self.is_pass_sequential = True

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

    def delete_user(self):
        self.is_active = 0
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE USER SET is_active = (?) WHERE  rowid= (?);",
                       (self.is_active, self.user_id,))
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
        raw_user_data = User.get_all_users_as_tuples()
        users_to_return = []
        for user in raw_user_data:
            users_to_return.append(User(user))
        return users_to_return

    @staticmethod
    def get_all_users_as_tuples():
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

    def __str__(self):
        return "AwwPoints User(id: {id}, email: {email})".format(id=self.user_id or "No ID", email=self.email_address or "No E-Mail")