# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath("Backend"))

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt6.QtGui import QIcon

import backend.authenticator as authenticator
import ui_files.messages as messages

class Login_DetailsUI(QMainWindow):
    g_username = None

    def __init__(self):
        super(Login_DetailsUI, self).__init__()
        uic.loadUi('ui_files/login_detailsUI.ui', self)
        self.setWindowIcon(QIcon("icon.png"))
        self.show()

        # Custom setup
        self.getDetails()
        self.pwfPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.btnUpdate.clicked.connect(self.updateUserDetails)

    def updateUserDetails(self):
        username = self.pwfUsername.text()
        username_confirmation = self.pwfConfirmUsername.text()
        password = self.pwfPassword.text()
        password_confirmation = self.pwfConfirmPassword.text()

        if (
            username == username_confirmation and
            password == password_confirmation and
            username and password
        ):
            authenticator.update_user(
                old_username=self.g_username,
                new_password=password,
                new_username=username
            )
            with open("current session.txt", 'w') as f:
                f.write(username)

            self.g_username = username
            messages.display_message(
                "The login details were updated successfully.\nMake sure to remember them.",
                "Update Successful",
                messages.INFO_MSG
            )
        else:
            messages.display_message(
                "Check if all the fields have been filled with the correct information.",
                "Update Failed",
                messages.ERROR_MSG
            )

    def getDetails(self):
        try:
            with open("current session.txt", 'r') as f:
                self.g_username = f.read().strip()
            username, password = authenticator.getUserDetails(self.g_username)
            self.pwfUsername.setText(username)
            self.pwfPassword.setText(password)
        except Exception as e:
            messages.display_message(
                f"Failed to load user details: {str(e)}",
                "Error",
                messages.ERROR_MSG
            )

def launch():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Login_DetailsUI()
    app.exec()
    
if __name__ == "__main__":
    launch()
