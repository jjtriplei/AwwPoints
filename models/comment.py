from database import Manager
from models.post import Post
import datetime


class Comment:
    comment_tuple_index = {
        "comment_id": 0,
        "user_id": 1,
        "post_id": 2,
        "comment": 3,
        "is_deleted": 4,
        "date_created": 5
    }
    def __init__(self, user_tuple):
        if user_tuple:
            self.comment_id = user_tuple[Comment.comment_tuple_index["comment_id"]]
            self.user_id = user_tuple[Comment.comment_tuple_index["user_id"]]
            self.post_id = user_tuple[Comment.comment_tuple_index["post_id"]]
            self.comment = user_tuple[Comment.comment_tuple_index["comment"]]
            self.is_deleted = user_tuple[Comment.comment_tuple_index["is_deleted"]]
            self.created = user_tuple[Comment.comment_tuple_index["date_created"]]
        else:
            self.comment_id = None
            self.user_id = None
            self.post_id = None
            self.comment = None
            self.is_deleted = None
            self.date_created = None

    def insert_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO COMMENT (user_id, post_id, comment, is_deleted, date_created) VALUES (?,?,?,?,?)",
                       (self.user_id, self.post_id, self.comment, self.is_deleted, self.created))
        Post.update_last_edited(self.post_id, db_connection)
        db_connection.commit()
        db_connection.close()

    # NEED TO CHANGE CLASS OBJECT #
    def mark_comment_as_deleted(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE COMMENT SET is_deleted = (?) WHERE rowid = (?)", (True, comment_id))
        db_connection.commit()
        db_connection.close()

    @staticmethod
    def get_comments_by_post(post_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM COMMENT WHERE post_id = (?)", (post_id,))
        query_results = cursor.fetchall()
        db_connection.close()
        return query_results

    @staticmethod
    def get_all_comments_by_user(user_id):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM COMMENT WHERE user_id = (?)", (user_id))
        query_results = cursor.fetchall()
        db_connection.close()
        return query_results

    @staticmethod
    def edit_comment(comment_id, edited_comment):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("UPDATE COMMENT SET COMMENT = (?), date_created = (?) WHERE rowid = (?);",
                       (edited_comment, datetime.datetime.now(), comment_id))
        db_connection.commit()
        db_connection.close()
