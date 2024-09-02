# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_detailsUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import authenticator
import messages

class Ui_MainWindow(object):
    g_username = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, -1, 791, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.gridLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pwfUsername = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pwfUsername.setObjectName("pwfUsername")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pwfUsername)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pwfConfirmUsername = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pwfConfirmUsername.setObjectName("pwfConfirmUsername")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pwfConfirmUsername)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pwfPassword = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pwfPassword.setObjectName("pwfPassword")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pwfPassword)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pwfConfirmPassword = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pwfConfirmPassword.setObjectName("pwfConfirmPassword")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pwfConfirmPassword)
        self.radCreateNewUser = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radCreateNewUser.setObjectName("radCreateNewUser")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.radCreateNewUser)
        self.btnUpdate = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnUpdate.setObjectName("btnUpdate")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.btnUpdate)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain_Menu = QtWidgets.QMenu(self.menubar)
        self.menuMain_Menu.setObjectName("menuMain_Menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMain_Menu = QtWidgets.QAction(MainWindow)
        self.actionMain_Menu.setObjectName("actionMain_Menu")
        self.menuMain_Menu.addAction(self.actionMain_Menu)
        self.menubar.addAction(self.menuMain_Menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #stuff added by me 
        self.getDetails()
        self.pwfPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnUpdate.clicked.connect(self.updateUserDetails)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Confirm New Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Confirm New Password"))
        self.radCreateNewUser.setText(_translate("MainWindow", "Create new login profile"))
        self.btnUpdate.setText(_translate("MainWindow", "Update"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.menuMain_Menu.setTitle(_translate("MainWindow", "Menu"))
        self.actionMain_Menu.setText(_translate("MainWindow", "Main Menu"))

    def updateUserDetails(self):
        username = self.pwfUsername.text()
        username_confirmation = self.pwfConfirmUsername.text()
        password = self.pwfPassword.text()
        password_confirmation =  self.pwfConfirmPassword.text()
                
        if username == username_confirmation and password == password_confirmation and username is not None and password is not None:
            authenticator.update_user(old_username= self.g_username, new_password=password, new_username=username)
            f = open("current session.txt", 'w')
            f.write(username)
            f.close()
            self.g_username = username
            messages.display_message("the Log in details were updated successfully \n Make sure to remember them", messages.SUCCESSFUL_OPERATION)
            
        else:
            messages.display_message("Check if all the fields have been filled with the correct information", messages.ERROR_MSG)
            
    def getDetails(self):
        f = open("current session.txt", 'r')
        self.g_username = f.read()#the username of the currently logged in person. I know I probably should not be doing it like this but this is what I can do for now
        f.close()
        username, password = authenticator.getUserDetails(self.g_username)
        self.pwfUsername.setText(username)
        self.pwfPassword.setText(password)
        
def launch():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch()