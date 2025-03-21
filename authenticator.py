
import sqlite3

Login_failed  = 0
Login_success = 1
duplicate_credentials = 2
db_path = "backend/passwords.db"
# add encryption to this, I will try to make it a bundle with the login ui that can be used in any project without a
# care in the world.
def create_tables():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = "CREATE TABLE tblPasswords(username, password)"
    cursor.execute(sql)
    cursor.close()
    conn.close()


def authenticate(username, password):
    code = 0  # this is for tracking if the attempt is successful 0 is for an unsuccessful attempt, 1 is a successful
    # attempt and 2 is for a duplicate result
    conn, cursor = open_conn()
    sql_statement = f"SELECT * FROM tblPasswords WHERE username = '{username}' AND password = '{password}'"
    result_set = cursor.execute(sql_statement)
    items = list(result_set.fetchall())
    print(items)
    if len(items) == 0:
        code = Login_failed
        

    elif len(items) > 1:
        code = duplicate_credentials
       

    elif len(items) == 1:
        code = Login_success
        

    cursor.close()
    conn.close()
    return code


def add_user(username, password):
    conn, cursor = open_conn()
    sql = f"INSERT into tblPasswords VALUES('{username}', '{password}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def update_user(old_username, new_username, new_password):
    sql_statement = f"UPDATE tblPasswords SET username = '{new_username}', password = '{new_password}' WHERE username = '{old_username}'"
    conn, cursor = open_conn()
    cursor.execute(sql_statement)
    conn.commit()
    cursor.close()
    conn.close()
    # needs more testing


# create a json file that will check if we did the first time set up of this
def initialise():
    create_tables()


def auTest():
    conn, cursor = open_conn()
    sql_statement = f"SELECT * FROM tblPasswords"
    result_set = cursor.execute(sql_statement)
    items = list(result_set.fetchall())
    print(items)
    cursor.close()
    conn.close()


def open_conn():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn, cursor

def getUserDetails(username):
    conn, cursor = open_conn()
    sql_statement = f"SELECT * FROM tblPasswords WHERE username = '{username}'"
    result_set = cursor.execute(sql_statement)
    items = list(result_set.fetchall())
    username = items[0][0]
    password = items[0][1]
    cursor.close()
    conn.close()
    return username, password


