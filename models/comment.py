from database import Manager
from models.post import Post
import datetime


class Comment:
    def __init__(self, user_id, post_id, comment):
        self.user_id = user_id
        self.post_id = post_id
        self.comment = comment
        self.created = datetime.datetime.now()

    def insert_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO COMMENT (user_id, post_id, comment, date_created) VALUES (?,?,?,?)",
                       (self.user_id, self.post_id, self.comment, self.created))
        Post.update_last_edited(self.post_id, db_connection)
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
    def meth():
        pass






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
def mark_comment_as_deleted(post_id):
    db_connection = Manager.get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("UPDATE POST SET is_deleted = (?) WHERE rowid= (?);", (True, post_id))
    db_connection.commit()
    db_connection.close()