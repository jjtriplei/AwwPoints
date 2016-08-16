import sqlite3
import os



#  Connects to DB file
def get_db_connection():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__),'ap_db.sqlite'))
    return conn


def get_db_cursor():
    db_connection = get_db_connection()
    return db_connection.cursor()


cursor = get_db_cursor()

# Save changes to DB with:
# conn.commit()

# Close DB connection
# conn.close()


