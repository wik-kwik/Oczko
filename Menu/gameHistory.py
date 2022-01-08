from PyQt5 import QtCore, QtGui, QtWidgets

import menu


class historyForm(object):
    def __init__(self, language):
        self.language = language

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 601)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundLabel = QtWidgets.QLabel(Form)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.gamesComboBox = QtWidgets.QComboBox(Form)
        self.gamesComboBox.setGeometry(QtCore.QRect(290, 320, 311, 31))
        self.gamesComboBox.setStyleSheet("color: rgb(255, 170, 0);\n"
"selection-background-color: rgb(62, 121, 84);\n"
"background-color: rgb(48, 94, 66);")
        self.gamesComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.gamesComboBox.setObjectName("gamesComboBox")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(390, 400, 131, 131))
        self.playButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(880, 0, 18, 24))
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # Obsługa przycisków
        self.closeButton.clicked.connect(self.returnToMenu)

        # Obsługa języków
        if self.language == 1:
            self.backgroundLabel.setStyleSheet("image: url(:/images/historyBackground.png);")
        if self.language == 2:
            self.backgroundLabel.setStyleSheet("image: url(:/images/historyBackgroundPL.png);")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Games history"))
        self.gamesComboBox.setItemText(0, _translate("Form", "CHUJ"))
        self.gamesComboBox.setItemText(1, _translate("Form", "CUHJ2"))

    def returnToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()
