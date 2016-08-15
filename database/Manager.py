import sqlite3


#  Connects to DB file
def get_db_connection():
    conn = sqlite3.connect('ap_db.sqlite')
    return conn


def get_db_cursor():
    cursor = get_db_connection()
    return cursor.cursor()


cursor = get_db_cursor()

# Save changes to DB with:
# conn.commit()

# Close DB connection
# conn.close()