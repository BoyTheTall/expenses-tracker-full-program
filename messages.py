ERROR_MSG = 0
INFO_MSG = 1
from PyQt5 import QtWidgets

def display_message(message, message_type):
    msg = QtWidgets.QMessageBox()
    if message_type == ERROR_MSG:
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Error :(")
    elif message_type == INFO_MSG:
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Welcome :)")
    msg.setText(message)
    msg.exec_()