import sqlite3


#  Connects to DB file
def connect_to_db():
    conn = sqlite3.connect('/Development/Awwpoints/database/ap_db.sqlite')
    return conn


def db_cursor():
    c = conn.cursor()
    return c



# Save changes to DB with:
# conn.commit()

# Close DB connection
# conn.close()