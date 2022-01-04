from PyQt5 import QtCore, QtGui, QtWidgets
import menu

class rulesForm(object):
    def __init__(self, language):
        self.language = language

    def setupUi(self, rulesForm):
        rulesForm.setObjectName("rulesForm")
        rulesForm.resize(901, 616)
        rulesForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        rulesForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(rulesForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 901, 616))

        self.label.setText("")
        self.label.setObjectName("label")
        self.closeButton = QtWidgets.QPushButton(rulesForm)
        self.closeButton.setGeometry(QtCore.QRect(880, 0, 16, 27))
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(rulesForm)
        QtCore.QMetaObject.connectSlotsByName(rulesForm)

        self.closeButton.clicked.connect(rulesForm.close)
        self.closeButton.clicked.connect(self.returnToMenu)

        if self.language == 1:
            self.label.setStyleSheet("image: url(:/images/rulesText.png);")
        if self.language == 2:
            self.label.setStyleSheet("image: url(:/images/rulesTextPL.png);")

    def retranslateUi(self, rulesForm):
        _translate = QtCore.QCoreApplication.translate
        rulesForm.setWindowTitle(_translate("rulesForm", "Form"))

    def returnToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

