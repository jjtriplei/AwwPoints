import datetime
from database import Manager


class Post:
    def __init__(self, user_id, post_comment, location_url):
        self.user_id = user_id
        self.post_comment = post_comment
        self.location_URL = location_url
        self.is_deleted = False
        self.last_edited = datetime.datetime.now()
        self.posted_date = datetime.datetime.now()

    def insert_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO POST (user_id, post_comment, image_location_url, is_deleted,"
                       "last_edited, posted_date) VALUES (?,?,?,?,?,?)",
                       (self.user_id, self.post_comment, self.location_URL, self.is_deleted,
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
        return cursor.fetchall()
        db_connection.close()

    @staticmethod
    def get_all_posts_from_user(user_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM POST WHERE user_id = (?)", (user_id))
        return cursor.fetchall()
        db_connection.close()

    @staticmethod
    def get_all_posts_by_last_edited():
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM POST ORDER BY last_edited ASC")
        return cursor.fetchall()
        db_connection.close()

    @staticmethod
    def update_post_comment(post_id, new_post_comment):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE POST SET post_comment = (?), last_edited = (?) WHERE rowid= (?);",
                       (new_post_comment, datetime.datetime.now(), post_id))
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def mark_comment_as_deleted(post_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE POST SET is_deleted = (?) WHERE rowid= (?);", (True, post_id))
        db_connection.commit()
        db_connection.close()
