import datetime
from database import Manager
import sqlite3

class post:
    def __init__(self, user_id, location_URL):
        self.user_id = user_id
        self.location_URL = location_URL
        self.is_deleted = False
        self.last_edited = datetime.datetime.now()
        self.posted_date = datetime.datetime.now()

    def insert_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO POST (user_id, image_location_URL, is_deleted, last_edited, posted_date) "
                       "VALUES (?,?,?,?,?)", (self.user_id, self.location_URL, self.is_deleted, self.last_edited,
                                              self.posted_date))
        print("Looks like post was added")
        cursor.commit()
        cursor.close()
        print("Db connection closed")

