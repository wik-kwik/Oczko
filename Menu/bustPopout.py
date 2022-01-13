from PyQt5 import QtCore, QtGui, QtWidgets


class bustForm(object):
    def __init__(self, board, name):
        self.board = board
        self.language = board.language
        self.name = name

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1850, 940)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundLabel = QtWidgets.QLabel(Form)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 1850, 940))
        self.backgroundLabel.setStyleSheet("image: url(:/images/bustBackground.png);")
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.nicknameLabel = QtWidgets.QLabel(Form)
        self.nicknameLabel.setGeometry(QtCore.QRect(370, 400, 1091, 141))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        self.nicknameLabel.setFont(font)
        self.nicknameLabel.setStyleSheet("color: rgb(255, 156, 17);")
        self.nicknameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nicknameLabel.setObjectName("nicknameLabel")
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(870, 720, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("QPushButton#playButton{\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 104, 3);\n"
"    border-radius: 45px;\n"
"}\n"
"\n"
"QPushButton#pplayButton:pressed{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"    background-color: rgb(255, 206, 12);\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"\n"
"QPushButton#playButton:hover{\n"
"    background-color: rgb(255, 206, 12);\n"
"}\n"
"")
        self.playButton.setObjectName("playButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        if self.board.frontend_logic.current_player.type != "player":
            self.playButton.setVisible(False)

        else:
            self.playButton.setVisible(True)

        self.playButton.clicked.connect(Form.close)

        # Obsługa języków
        if self.language == 1:
            self.backgroundLabel.setStyleSheet("image: url(:/images/bustBackground.png);")
            self.playButton.setGeometry(QtCore.QRect(870, 720, 91, 91))
        if self.language == 2:
            self.backgroundLabel.setStyleSheet("image: url(:/images/bustBackgroundPL.png);")
            self.playButton.setGeometry(QtCore.QRect(870, 660, 91, 91))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nicknameLabel.setText(_translate("Form", self.name))
        self.playButton.setText(_translate("Form", "OK"))
