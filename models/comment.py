from database import Manager
import datetime

class Comment:
    def __init__(self, commenter, related_post, comment):
        self.commenter = commenter
        self.related_post = related_post
        self.comment = comment
        self.created = datetime.datetime.now()

    def inset_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO COMMENT (commenter, post, comment, date_created) VALUES (?,?,?,?)",
                       (self.commenter, self.related_post, self.comment, self.created))
        print("Looks like comment was added")
        db_connection.commit()
        db_connection.close()
        print("Db connection closed")

