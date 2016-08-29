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
        db_connection.commit()
        db_connection.close()
        print("Db connection closed")

    @staticmethod
    def get_post_by_id(post_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM POST WHERE rowid = (?)", (post_id,))
        db_connection.close()

    @staticmethod
    def get_all_posts_from_user(user_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM POST WHERE user_id = (?)", (user_id))
        db_connection.close()

    @staticmethod
    def update_post_comment(post_id,new_post_comment):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE POST SET post_comment = (?), last_edited = (?) WHERE rowid= (?);",
                       (new_post_comment,datetime.datetime.now(),post_id))
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def mark_comment_as_deleted(post_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE POST SET is_deleted = (?) WHERE rowid= (?);", (True,post_id))
        db_connection.commit()
        db_connection.close()




happy = post(5,"Here we go","www.github.com/3")
happy.insert_into_database()
happy.update_post_comment(10, "Update me baby!")

post.update_post_comment(8, "Check Last Edited SON!")

post.mark_comment_as_deleted(9)

# db_connection = Manager.get_db_connection()
# cursor = db_connection.cursor()

# cursor.execute()

# for x in range(0, 10):
#     cursor.execute(
#         "INSERT INTO POST (user_id, post_comment, image_location_URL, is_deleted, last_edited, posted_date) VALUES (?,?,?,?,?,?)",
#         (x, "YOUR COMMENT HERE", "http://www.google.com/" + str(x), False, datetime.datetime.now(), datetime.datetime.now()))


# db_connection.commit()
# db_connection.close()