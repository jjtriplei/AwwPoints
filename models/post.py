import datetime
from database import Manager


class Post:
    post_tuple_index = {
        "post_id": 0,
        "user_id": 1,
        "post_comment": 2,
        "image_location_url": 3,
        "is_deleted": 4,
        "last_edited": 5,
        "posted_date": 6
    }

    def __init__(self, post_tuple):
        if post_tuple:
            self.post_id = post_tuple[Post.post_tuple_index["post_id"]]
            self.user_id = post_tuple[Post.post_tuple_index["user_id"]]
            self.post_comment = post_tuple[Post.post_tuple_index["post_comment"]]
            self.location_url = post_tuple[Post.post_tuple_index["location_url"]]
            self.is_deleted = post_tuple[Post.post_tuple_index["is_deleted"]]
            self.last_edited = post_tuple[Post.post_tuple_index["last_edited"]]
            self.posted_date = post_tuple[Post.post_tuple_index["posted_date"]]
        else:
            self.post_id = None
            self.user_id = None
            self.post_comment = None
            self.location_url = None
            self.is_deleted = None
            self.last_edited = None
            self.posted_date = None

    def insert_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO POST (user_id, post_comment, image_location_url, is_deleted,"
                       "last_edited, posted_date) VALUES (?,?,?,?,?,?)",
                       (self.user_id, self.post_comment, self.location_url, self.is_deleted,
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
        query_results = cursor.fetchall()
        db_connection.close()
        return query_results

    @staticmethod
    def get_all_posts_from_user(user_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM POST WHERE user_id = (?)", (user_id))
        query_results = cursor.fetchall()
        db_connection.close()
        return query_results

    @staticmethod
    def get_all_posts_by_last_edited():
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM POST ORDER BY last_edited ASC")
        query_results = cursor.fetchall()
        db_connection.close()
        return query_results

    @staticmethod
    def update_post_comment(post_id, new_post_comment):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE POST SET post_comment = (?), last_edited = (?) WHERE rowid= (?);",
                       (new_post_comment, datetime.datetime.now(), post_id))
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def update_last_edited(post_id, db_object):
        db_connection = db_object
        cursor = db_connection.cursor()
        cursor.execute("UPDATE POST SET last_edited = (?) WHERE rowid= (?);",
                       (datetime.datetime.now(), post_id))
        db_connection.commit()

    @staticmethod
    def mark_post_as_deleted(post_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE POST SET is_deleted = (?) WHERE rowid= (?);", (True, post_id))
        db_connection.commit()
        db_connection.close()
