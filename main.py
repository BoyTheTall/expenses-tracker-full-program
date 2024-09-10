from PyQt5 import QtWidgets, uic
import sys

class ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(ui, self).__init__()
        uic.loadUi('TransactionsUI.ui', self)
        self.show()
        
app = QtWidgets.QApplication(sys.argv)
window = ui()
app.exec_()