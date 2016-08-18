import datetime
from database import Manager

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


def create_user(username, email_address, password, last_logged_in, is_pass_sequential, cursor):
    Manager.insert_and_commit(
        "INSERT INTO USER (USERNAME,EMAIL_ADDRESS,PASSWORD,LAST_LOGGED_IN,IS_PASS_SEQUENTIAL) VALUES (?,?,?,?,?)",
        (username, email_address, password, last_logged_in, is_pass_sequential)
    )



#Testing script

# Manager.create_all_tables()

# db_connection = Manager.get_db_connection()
# cursor = db_connection.cursor()
# for x in range(0, 5000):
#     create_user("User" + str(x), "user" + str(x) + "@aol.com", "123", datetime.datetime.now(), True, cursor)
# db_connection.commit()
# db_connection.close()