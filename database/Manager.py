import sqlite3


#  Connects to DB file
def get_db_connection():
    conn = sqlite3.connect('/Development/Awwpoints/database/ap_db.sqlite')
    return conn


def get_db_cursor():
    c = get_db_connection()
    return c.cursor()


c = get_db_cursor()

# Save changes to DB with:
# conn.commit()

# Close DB connection
# conn.close()