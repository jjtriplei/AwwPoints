import datetime
from database import Manager
import sqlite3

class post:
    def __init__(self, user_id,post_comment,location_URL):
        self.user_id = user_id
        self.post_comment = post_comment
        self.location_URL = location_URL
        self.is_deleted = False
        self.last_edited = datetime.datetime.now()
        self.posted_date = datetime.datetime.now()

    def insert_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO POST (user_id, post_comment, image_location_URL, is_deleted, last_edited, posted_date) "
                       "VALUES (?,?,?,?,?,?)", (self.user_id, self.post_comment, self.location_URL, self.is_deleted,
                                                self.last_edited, self.posted_date))
        print("Looks like post was added")
        cursor.commit()
        cursor.close()
        print("Db connection closed")

    @staticmethod
    def get_post_by_id(post_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM POST WHERE rowid = (?)", (post_id,))
        cursor.close()

    @staticmethod
    def get_all_posts_from_user(user_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM POST WHERE user_id = (?)", (user_id))
        cursor.close()


# db_connection = Manager.get_db_connection()
# cursor = db_connection.cursor()
# for x in range(0, 10):
#     cursor.execute(
#         "INSERT INTO POST (user_id, post_comment, image_location_URL, is_deleted, last_edited, posted_date) VALUES (?,?,?,?,?,?)",
#         (x, "YOUR COMMENT HERE", "http://www.google.com/000" + str(x), False, datetime.datetime.now(), datetime.datetime.now()))
# db_connection.commit()
# db_connection.close()