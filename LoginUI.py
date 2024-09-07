# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#this is assummes each username is unique

from PyQt5 import QtCore, QtGui, QtWidgets
import authenticator as au
import messages as msg
import login_detailsUI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 376)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(250, 230, 171, 51))
        self.btnLogin.setObjectName("btnLogin")
        self.lblUsername = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername.setGeometry(QtCore.QRect(80, 80, 111, 41))
        self.lblUsername.setObjectName("lblUsername")
        self.lblPassword = QtWidgets.QLabel(self.centralwidget)
        self.lblPassword.setGeometry(QtCore.QRect(80, 150, 111, 41))
        self.lblPassword.setObjectName("lblPassword")
        self.pwdUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.pwdUsername.setGeometry(QtCore.QRect(180, 90, 331, 31))
        self.pwdUsername.setObjectName("pwdUsername")
        self.pwdPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.pwdPassword.setGeometry(QtCore.QRect(180, 160, 331, 31))
        self.pwdPassword.setObjectName("pwdPassword")
        self.pwdPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
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
            
                    
        if login_attempt_status == 2:
            message = "Error duplicate creditials found in database. Guess I did not code this abomination correctly"
            title = "Login Error :("
            msg.display_message(message, title, msg.ERROR_MSG)
            

def launch():
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
   launch() 