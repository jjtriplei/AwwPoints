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
            is_pass_sequential BOOLEAN NOT NULL DEFAULT 1,
            violation_count TINYINT NOT NULL DEFAULT 0,
            is_admin BOOLEAN NOT NULL DEFAULT 0,
            is_active BOOLEAN NOT NULL DEFAULT 1 ,
            profile_pic_url VARCHAR (2083)
            )
            '''


SQL_TO_CREATE_POST_TABLE = '''
            CREATE TABLE IF NOT EXISTS POST (
            user_id INT NOT NULL,
            post_comment VARCHAR (255),
            image_location_url VARCHAR (255) NOT NULL UNIQUE,
            is_deleted BOOLEAN NOT NULL DEFAULT 0,
            last_edited DATETIME,
            posted_date DATETIME NOT NULL,
            FOREIGN KEY (user_id) REFERENCES USER(rowid)
            )
            '''


SQL_TO_CREATE_POINT_TABLE = '''
        CREATE TABLE IF NOT EXISTS POINT (
        user_id INT NOT NULL,
        post_id INT NOT NULL,
        date_created DATETIME NOT NULL,
        is_aww BOOLEAN NOT NULL DEFAULT 1,
        FOREIGN KEY (user_id) REFERENCES USER(rowid),
        FOREIGN KEY (post_id) REFERENCES POST(rowid)
        )
        '''


SQL_TO_CREATE_COMMENT_TABLE = '''
            CREATE TABLE IF NOT EXISTS COMMENT (
            user_id INT NOT NULL,
            post_id INT NOT NULL,
            comment VARCHAR (255) NOT NULL,
            is_deleted BOOLEAN NOT NULL DEFAULT 0,
            date_created DATETIME NOT NULL,
            FOREIGN KEY (user_id) REFERENCES USER(rowid),
            FOREIGN KEY (post_id) REFERENCES POST(rowid)
            )
            '''

# This table has not yet been defined. This code block is a placeholder.
SQL_TO_CREATE_ACTIVITY_TABLE = '''
            CREATE TABLE IF NOT EXISTS ACTIVITY (
            activity0 INT NOT NULL,
            activity1 INT NOT NULL,
            activity2 VARCHAR (255) NOT NULL,
            activity3 DATETIME NOT NULL
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


def check_tables_exist():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT tbl_name FROM sqlite_master")
    table_names = cursor.fetchall()
    ap_tables = {"USER": False, "POST": False, "POINT": False, "COMMENT": False, "ACTIVITY": False}

    for table in table_names:
        ap_tables[table[0]] = True

    for key, value in ap_tables.items():
        if value == False:
            create_single_table(key, cursor, db_connection)
    db_connection.close()


def create_single_table(table_name, cursor, db_connection):
    table_creation_sql_map = {"USER": SQL_TO_CREATE_USER_TABLE, "POST": SQL_TO_CREATE_POST_TABLE,
                              "POINT": SQL_TO_CREATE_POINT_TABLE, "COMMENT": SQL_TO_CREATE_COMMENT_TABLE,
                              "ACTIVITY": SQL_TO_CREATE_ACTIVITY_TABLE}
    cursor.execute(table_creation_sql_map[table_name])
    db_connection.commit()


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
