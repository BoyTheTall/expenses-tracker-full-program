import sqlite3
from PyQt5 import QtWidgets
#constants
ERROR_MSG = 0
LGN_SUCC = 1

#add encryption to this, I will try to make it a bundle with the login ui that can be used in any project without a care in the world.
def create_tables():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE tblPasswords(username, password)"
    cursor.execute(sql)
    cursor.close()
    conn.close()

def authenticate(username, password):
    code = 0 #this is for tracking if the atttempt is successful 0 is for an unsuccessful attempt, 1 is a successful attempt and 2 is for a duplicate resut
    conn, cursor = open_conn()
    sql_statement = f"SELECT * FROM tblPasswords WHERE username = '{username}' AND password = '{password}'"
    result_set  = cursor.execute(sql_statement)
    items = list(result_set.fetchall())

    if(len(items) == 0):
        display_message("Error invalid username or password", ERROR_MSG)
        
    elif(len(items) > 1):
        code = 2
        display_message("Error duplicate creditials found in database. Guess I did not code this abomination correctly", ERROR_MSG)
        
    elif(len(items) == 1):
        code = 1
        display_message("Welcome", LGN_SUCC)

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
    
def update_user(old_username, old_password, new_username, new_password):
    sql_statement = f"UPDATE tblPasswords SET username = '{new_username}' AND password = '{new_password}' WHERE username = '{old_username}' AND password = '{old_password}'"
    conn, cursor = open_conn()
    cursor.execute(sql_statement)
    conn.commit()
    cursor.close()
    conn.close()
    print("Login Credintials updated successfully")
    #untested

#create a json file that will check if we did the first time set up of this
def initialise():
    create_tables()

def auTest():
    conn, cursor = open_conn()
    sql_statement = f"SELECT * FROM tblPasswords"
    result_set  = cursor.execute(sql_statement)
    items = list(result_set.fetchall())
    print(items)
    cursor.close()
    conn.close()
        
def open_conn():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    return conn, cursor

def display_message(message, message_type):
    msg = QtWidgets.QMessageBox()
    if message_type == ERROR_MSG:
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Error :(")
    elif message_type == LGN_SUCC:
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Welcome :)")
    msg.setText(message)
    msg.exec_()