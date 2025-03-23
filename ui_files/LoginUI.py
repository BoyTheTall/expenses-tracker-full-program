# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#this is assummes each username is unique

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import backend.authenticator as au
import ui_files.messages as msg
import ui_files.login_detailsUI as login_detailsUI

class LoginUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginUI, self).__init__()
        uic.loadUi('ui_files/Login.ui', self)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.show()
        

        #added by me
        self.btnLogin.clicked.connect(self.login)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Login", "Login"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.lblUsername.setText(_translate("MainWindow", "Username"))
        self.lblPassword.setText(_translate("MainWindow", "Password"))
        self.pwdUsername.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enter Your Username</p></body></html>"))
        
    def login(self):
        username = self.pwdUsername.text()
        password = self.pwdPassword.text()
        login_attempt_status = au.authenticate(username, password)
    
        if login_attempt_status == 0:
            message = "Error, invalid credentials entered"
            title = "Credentials Error >:("
            msg.display_message(message, title, msg.ERROR_MSG)
            
            
        if login_attempt_status == 1:
            message = f"Welcome {username}"
            title = "Hello :)"
            msg.display_message(message, title, msg.INFO_MSG)
            f = open("current session.txt", "w")
            f.write(username)
            f.close()
            login_detailsUI.launch()
            self.close()
            
            
                    
        if login_attempt_status == 2:
            message = "Error duplicate creditials found in database. Guess I did not code this abomination correctly"
            title = "Login Error :("
            msg.display_message(message, title, msg.ERROR_MSG)
            

def launch():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = LoginUI()
    app.exec_()



if __name__ == "__main__":
   launch() 