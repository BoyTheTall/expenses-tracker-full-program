ERROR_MSG = 0
INFO_MSG = 1
YES_NO_BOX = 4
from PyQt5 import QtWidgets

def display_message(message, title, message_type):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    if message_type == ERROR_MSG:
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        
    elif message_type == INFO_MSG:
        msg.setIcon(QtWidgets.QMessageBox.Information)

    msg.exec_()

def display_option_message(message, title, type_of_dialog):
    msg = QtWidgets.QMessageBox()
    msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    msg.setWindowTitle(title)
    msg.setText(message)
    result = msg.exec()
    if result == QtWidgets.QMessageBox.Yes:
        return True
    else:
        return False
    
