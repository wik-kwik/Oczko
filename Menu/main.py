import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import menu

class MyWindow(QtWidgets.QMainWindow, menu.menuForm):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def close_window(self):
        self.close()


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())

