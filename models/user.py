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

    def insert_into_database(self):
        db_connection = Manager.get_db_connection()
        cursor = db_connection.cursor()
        cursor.execute(
            "INSERT INTO USER (USERNAME,EMAIL_ADDRESS,PASSWORD,LAST_LOGGED_IN,IS_PASS_SEQUENTIAL) VALUES (?,?,?,?,?)",
            (self.username, self.email_address, self.password, datetime.datetime.now(), self.is_pass_sequential))
        db_connection.commit()
        db_connection.close()



# def create_user(username, email_address, password, last_logged_in, is_pass_sequential, cursor):
#     Manager.insert_and_commit("INSERT INTO USER (USERNAME,EMAIL_ADDRESS,PASSWORD,LAST_LOGGED_IN,IS_PASS_SEQUENTIAL) VALUES (?,?,?,?,?)",/
#     (username, email_address, password, last_logged_in, is_pass_sequential,))





Joseph = User("Joseph", "Joseph@John.com", "12345")
Joseph.insert_into_database()

print(Joseph.email_address)





#Testing script

# Manager.create_all_tables()

# db_connection = Manager.get_db_connection()
# cursor = db_connection.cursor()
# for x in range(0, 500):
#     cursor.execute("User" + str(x), "user" + str(x) + "@aol.com", "123", datetime.datetime.now(), True)
# db_connection.commit()
# db_connection.close()