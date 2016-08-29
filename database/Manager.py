import sqlite3
import os
import datetime

# =============================================================

# Database.manager is in charge of handling lower-level functions that deal
# Directly with the database.  (ex: Opening a connection, inserting some SQL, deleting all tables... etc

# =============================================================


#  Connects to DB file


SQL_TO_CREATE_USER_TABLE = '''
            CREATE TABLE IF NOT EXISTS USER (
            username VARCHAR (255) NOT NULL UNIQUE,
            email_address VARCHAR (255) NOT NULL UNIQUE,
            password TINYINT NOT NULL,
            last_logged_in DATETIME NOT NULL,
            is_pass_sequential BOOLEAN NOT NULL DEFAULT True,
            violation_count TINYINT NOT NULL DEFAULT 0
            )
            '''


SQL_TO_CREATE_POST_TABLE = '''
            CREATE TABLE IF NOT EXISTS POST (
            user_id INT NOT NULL,
            post_comment VARCHAR (255),
            image_location_URL VARCHAR (255) NOT NULL UNIQUE,
            is_deleted BOOLEAN NOT NULL DEFAULT FALSE,
            last_edited DATETIME,
            posted_date DATETIME,
            FOREIGN KEY (user_id) REFERENCES USER(rowid)
            )
            '''


def get_db_connection():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'ap_db.sqlite'))
    return conn


def insert_and_commit(sql_command, *args, **kwargs):
    connection = get_db_connection()
    connection.cursor().execute(sql_command, *args, **kwargs)
    connection.commit()
    connection.close()


def create_all_tables():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(SQL_TO_CREATE_USER_TABLE)
    cursor.execute(SQL_TO_CREATE_POST_TABLE)
    # cursor.execute(SQL_TO_CREATE_POINTS_TABLE)
    # cursor.execute(SQL_TO_CREATE_COMMENTS_TABLE)
    # cursor.execute(SQL_TO_CREATE_ACTIVITY_TABLE)
    db_connection.commit()
    db_connection.close()


def drop_user_table():
    connection = get_db_connection()
    connection.cursor().execute("DROP TABLE USER;")
    connection.commit()
    connection.close()


def drop_post_table():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("DROP TABLE POST;")
    db_connection.close()


def drop_all_tables():
    connection = get_db_connection()
    connection.cursor().execute("DROP TABLE USER;")
    connection.cursor().execute("DROP TABLE POST;")
    connection.cursor().execute("DROP TABLE POINTS;")
    connection.cursor().execute("DROP TABLE COMMENTS;")
    connection.cursor().execute("DROP TABLE ACTIVITY;")
    connection.commit()
    connection.close()


create_all_tables()