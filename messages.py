ERROR_MSG = 0
INFO_MSG = 1
FAILED_OPERATION = 2
SUCCESSFUL_OPERATION = 3#do not use, breaks the whole application for some reason. i'll investigate this probably
from PyQt5 import QtWidgets

def display_message(message, message_type):
    msg = QtWidgets.QMessageBox()
    if message_type == ERROR_MSG:
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Error :(")
    elif message_type == INFO_MSG:
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Welcome :)")
    
    elif message_type == FAILED_OPERATION:
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle("Task Failed :(")
        
    elif message_type == SUCCESSFUL_OPERATION:
        msg.setIcon(QtWidgets.QMessageBox.information)
        msg.setWindowTitle("Operation Successful :)")
    msg.setText(message)
    msg.exec_()
    
#still working on this one so use display message for now
def display_operation_status(message, message_type):
    if message_type == FAILED_OPERATION:
        msg = QtWidgets.QMessageBox()
        msg.setWhatsThis(message)
        msg.exec_()
        msg.show()