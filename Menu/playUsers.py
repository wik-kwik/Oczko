from PyQt5 import QtCore, QtGui, QtWidgets
import playOptions, login, register, board, betting
import sqlite3 as sql
from Game_Logic.player import Player
import frontendLogic
import threading


class usersForm(object):
    def __init__(self, language, playersNumber, computersNumber, betting):
        self.language = language
        self.playersNumber = playersNumber
        self.computersNumber = computersNumber
        self.betting = betting
        self.input = ""
        self.gameLevel = 0
        self.computerOneLevel = 0
        self.computerTwoLevel = 0
        self.computerThreeLevel = 0
        self.computerFourLevel = 0
        self.numberOfPlayer = []
        self.popups = []
        self.loggedUsers = []


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 732)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 511, 711))
        self.background.setStyleSheet("background-color: rgb(24, 47, 38);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.returnIcon = QtWidgets.QLabel(Form)
        self.returnIcon.setGeometry(QtCore.QRect(471, 8, 31, 31))
        self.returnIcon.setStyleSheet("border-image: url(:/images/return.png);")
        self.returnIcon.setText("")
        self.returnIcon.setObjectName("returnIcon")
        self.returnButton = QtWidgets.QPushButton(Form)
        self.returnButton.setGeometry(QtCore.QRect(470, 10, 31, 31))
        self.returnButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.returnButton.setText("")
        self.returnButton.setObjectName("returnButton")

        self.backgroundDark = QtWidgets.QLabel(Form)
        self.backgroundDark.setGeometry(QtCore.QRect(40, 20, 431, 671))
        self.backgroundDark.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
                                          "border-radius:10px;\n"
                                          "")
        self.backgroundDark.setText("")
        self.backgroundDark.setObjectName("backgroundDark")

        self.difficultyLabel = QtWidgets.QLabel(Form)
        self.difficultyLabel.setText("")
        self.difficultyLabel.setObjectName("difficultyLabel")
        self.playerOneLabel = QtWidgets.QLabel(Form)
        self.playerOneLabel.setGeometry(QtCore.QRect(100, 181, 151, 31))
        self.playerOneLabel.setText("")
        self.playerOneLabel.setObjectName("playerOneLabel")
        self.playerTwoLabel = QtWidgets.QLabel(Form)
        self.playerTwoLabel.setGeometry(QtCore.QRect(290, 181, 121, 31))
        self.playerTwoLabel.setText("")
        self.playerTwoLabel.setObjectName("playerTwoLabel")
        self.playerThreeLabel = QtWidgets.QLabel(Form)
        self.playerThreeLabel.setText("")
        self.playerThreeLabel.setObjectName("playerThreeLabel")
        self.playerFourLabel = QtWidgets.QLabel(Form)
        self.playerFourLabel.setText("")
        self.playerFourLabel.setObjectName("playerFourLabel")
        self.compOneLabel = QtWidgets.QLabel(Form)
        self.compOneLabel.setGeometry(QtCore.QRect(72, 451, 161, 31))
        self.compOneLabel.setText("")
        self.compOneLabel.setObjectName("compOneLabel")
        self.logoCards = QtWidgets.QLabel(Form)
        self.logoCards.setGeometry(QtCore.QRect(60, 10, 61, 51))
        self.logoCards.setStyleSheet("image: url(:/images/logoCards.png);")
        self.logoCards.setText("")
        self.logoCards.setObjectName("logoCards")

        self.easyGameButton = QtWidgets.QPushButton(Form)
        self.easyGameButton.setGeometry(QtCore.QRect(70, 81, 91, 51))
        self.easyGameButton.setText("")
        self.easyGameButton.setObjectName("easyGameButton")
        self.mediumGameButton = QtWidgets.QPushButton(Form)
        self.mediumGameButton.setGeometry(QtCore.QRect(193, 84, 121, 45))
        self.mediumGameButton.setText("")
        self.mediumGameButton.setObjectName("mediumGameButton")
        self.hardGameButton = QtWidgets.QPushButton(Form)
        self.hardGameButton.setGeometry(QtCore.QRect(343, 81, 91, 51))
        self.hardGameButton.setText("")
        self.hardGameButton.setObjectName("hardGameButton")

        self.compTwoLabel = QtWidgets.QLabel(Form)
        self.compTwoLabel.setGeometry(QtCore.QRect(290, 451, 151, 31))
        self.compTwoLabel.setText("")
        self.compTwoLabel.setObjectName("compTwoLabel")
        self.compThreeLabel = QtWidgets.QLabel(Form)
        self.compThreeLabel.setGeometry(QtCore.QRect(72, 541, 151, 31))
        self.compThreeLabel.setText("")
        self.compThreeLabel.setObjectName("compThreeLabel")
        self.compFourLabel = QtWidgets.QLabel(Form)
        self.compFourLabel.setGeometry(QtCore.QRect(290, 541, 151, 31))
        self.compFourLabel.setText("")
        self.compFourLabel.setObjectName("compFourLabel")

        self.easyLabel = QtWidgets.QLabel(Form)
        self.easyLabel.setGeometry(QtCore.QRect(86, 121, 61, 61))
        self.easyLabel.setText("")
        self.easyLabel.setObjectName("easyLabel")
        self.mediumLabel = QtWidgets.QLabel(Form)
        self.mediumLabel.setGeometry(QtCore.QRect(223, 121, 61, 61))
        self.mediumLabel.setText("")
        self.mediumLabel.setObjectName("mediumLabel")
        self.hardLabel = QtWidgets.QLabel(Form)
        self.hardLabel.setGeometry(QtCore.QRect(358, 121, 61, 61))
        self.hardLabel.setText("")
        self.hardLabel.setObjectName("hardLabel")

        self.compOneEasyButton = QtWidgets.QPushButton(Form)
        self.compOneEasyButton.setGeometry(QtCore.QRect(65, 481, 51, 31))
        self.compOneEasyButton.setText("")
        self.compOneEasyButton.setObjectName("compOneEasyButton")
        self.compOneMediumButton = QtWidgets.QPushButton(Form)
        self.compOneMediumButton.setGeometry(QtCore.QRect(123, 481, 61, 31))
        self.compOneMediumButton.setText("")
        self.compOneMediumButton.setObjectName("compOneMediumButton")
        self.compOneHardButton = QtWidgets.QPushButton(Form)
        self.compOneHardButton.setGeometry(QtCore.QRect(190, 481, 51, 31))
        self.compOneHardButton.setText("")
        self.compOneHardButton.setObjectName("compOneHardButton")
        self.playerOneNickname = QtWidgets.QLabel(Form)
        self.playerOneNickname.setGeometry(QtCore.QRect(97, 220, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.playerOneNickname.setFont(font)
        self.playerOneNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerOneNickname.setText("")
        self.playerOneNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.playerOneNickname.setObjectName("playerOneNickname")
        self.playerTwoNickname = QtWidgets.QLabel(Form)
        self.playerTwoNickname.setGeometry(QtCore.QRect(274, 220, 151, 31))
        self.playerTwoNickname.setFont(font)
        self.playerTwoNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerTwoNickname.setText("")
        self.playerTwoNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.playerTwoNickname.setObjectName("playerTwoNickname")
        self.playerThreeNickname = QtWidgets.QLabel(Form)

        self.playerThreeNickname.setText("")
        self.playerThreeNickname.setFont(font)
        self.playerThreeNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerThreeNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.playerThreeNickname.setObjectName("playerThreeNickname")
        self.playerFourNickname = QtWidgets.QLabel(Form)

        self.playerFourNickname.setStyleSheet("color: rgb(255, 85, 0);")
        self.playerFourNickname.setText("")
        self.playerFourNickname.setFont(font)
        self.playerFourNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerFourNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.playerFourNickname.setObjectName("playerFourNickname")

        self.playerOneLogin = QtWidgets.QPushButton(Form)
        self.playerOneLogin.setText("")
        self.playerOneLogin.setObjectName("playerOneLogin")

        self.playerOneRegister = QtWidgets.QPushButton(Form)
        self.playerOneRegister.setText("")
        self.playerOneRegister.setObjectName("playerOneRegister")

        self.playerOneLogout = QtWidgets.QPushButton(Form)
        self.playerOneLogout.setText("")
        self.playerOneLogout.setObjectName("playerOneLogout")

        self.playerTwoLogin = QtWidgets.QPushButton(Form)
        self.playerTwoLogin.setText("")
        self.playerTwoLogin.setObjectName("playerTwoLogin")

        self.playerTwoRegister = QtWidgets.QPushButton(Form)
        self.playerTwoRegister.setText("")
        self.playerTwoRegister.setObjectName("playerTwoRegister")

        self.playerTwoLogout = QtWidgets.QPushButton(Form)
        self.playerTwoLogout.setText("")
        self.playerTwoLogout.setObjectName("playerTwoLogout")

        self.playerThreeRegister = QtWidgets.QPushButton(Form)
        self.playerThreeRegister.setText("")
        self.playerThreeRegister.setObjectName("playerThreeRegister")

        self.playerThreeLogin = QtWidgets.QPushButton(Form)
        self.playerThreeLogin.setText("")
        self.playerThreeLogin.setObjectName("playerThreeLogin")

        self.playerThreeLogout = QtWidgets.QPushButton(Form)
        self.playerThreeLogout.setText("")
        self.playerThreeLogout.setObjectName("playerThreeLogout")

        self.playerFourRegister = QtWidgets.QPushButton(Form)
        self.playerFourRegister.setText("")
        self.playerFourRegister.setObjectName("playerFourRegister")

        self.playerFourLogin = QtWidgets.QPushButton(Form)

        self.playerFourLogin.setText("")
        self.playerFourLogin.setObjectName("playerFourLogin")

        self.playerFourLogout = QtWidgets.QPushButton(Form)
        self.playerFourLogout.setText("")
        self.playerFourLogout.setObjectName("playerFourLogout")

        self.compTwoMediumButton = QtWidgets.QPushButton(Form)
        self.compTwoMediumButton.setGeometry(QtCore.QRect(333, 481, 61, 31))
        self.compTwoMediumButton.setText("")
        self.compTwoMediumButton.setObjectName("compTwoMediumButton")
        self.compTwoHardButton = QtWidgets.QPushButton(Form)
        self.compTwoHardButton.setGeometry(QtCore.QRect(400, 481, 51, 31))
        self.compTwoHardButton.setText("")
        self.compTwoHardButton.setObjectName("compTwoHardButton")
        self.compTwoEasyButton = QtWidgets.QPushButton(Form)
        self.compTwoEasyButton.setGeometry(QtCore.QRect(275, 481, 51, 31))
        self.compTwoEasyButton.setText("")
        self.compTwoEasyButton.setObjectName("compTwoEasyButton")
        self.compThreeMediumButton = QtWidgets.QPushButton(Form)
        self.compThreeMediumButton.setGeometry(QtCore.QRect(118, 571, 61, 31))
        self.compThreeMediumButton.setText("")
        self.compThreeMediumButton.setObjectName("compThreeMediumButton")
        self.compThreeHardButton = QtWidgets.QPushButton(Form)
        self.compThreeHardButton.setGeometry(QtCore.QRect(185, 571, 51, 31))
        self.compThreeHardButton.setText("")
        self.compThreeHardButton.setObjectName("compThreeHardButton")
        self.compThreeEasyButton = QtWidgets.QPushButton(Form)
        self.compThreeEasyButton.setGeometry(QtCore.QRect(60, 571, 51, 31))
        self.compThreeEasyButton.setText("")
        self.compThreeEasyButton.setObjectName("compThreeEasyButton")
        self.compFourHardButton = QtWidgets.QPushButton(Form)
        self.compFourHardButton.setGeometry(QtCore.QRect(397, 571, 51, 31))
        self.compFourHardButton.setText("")
        self.compFourHardButton.setObjectName("compFourHardButton")
        self.compFourEasyButton = QtWidgets.QPushButton(Form)
        self.compFourEasyButton.setGeometry(QtCore.QRect(272, 571, 51, 31))
        self.compFourEasyButton.setText("")
        self.compFourEasyButton.setObjectName("compFourEasyButton")
        self.compFourMediumButton = QtWidgets.QPushButton(Form)
        self.compFourMediumButton.setGeometry(QtCore.QRect(330, 571, 61, 31))
        self.compFourMediumButton.setText("")
        self.compFourMediumButton.setObjectName("compFourMediumButton")
        self.nextIcon = QtWidgets.QLabel(Form)
        self.nextIcon.setGeometry(QtCore.QRect(128, 590, 251, 111))
        self.nextIcon.setStyleSheet("image: url(:/images/next.png);")
        self.nextIcon.setText("")
        self.nextIcon.setObjectName("nextIcon")
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(212, 620, 81, 51))
        self.nextButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.nextButton.setText("")
        self.nextButton.setObjectName("nextButton")

        self.background.raise_()
        self.backgroundDark.raise_()
        self.difficultyLabel.raise_()
        self.playerOneLabel.raise_()
        self.playerTwoLabel.raise_()
        self.playerThreeLabel.raise_()
        self.playerFourLabel.raise_()
        self.compOneLabel.raise_()
        self.logoCards.raise_()
        self.returnIcon.raise_()
        self.easyGameButton.raise_()
        self.mediumGameButton.raise_()
        self.hardGameButton.raise_()
        self.playerOneNickname.raise_()
        self.playerTwoNickname.raise_()
        self.playerThreeNickname.raise_()
        self.playerFourNickname.raise_()
        self.playerOneLogout.raise_()
        self.playerTwoLogout.raise_()
        self.playerThreeLogout.raise_()
        self.playerFourLogout.raise_()
        self.playerOneLogin.raise_()
        self.playerOneRegister.raise_()
        self.compTwoLabel.raise_()
        self.compThreeLabel.raise_()
        self.compFourLabel.raise_()
        self.easyLabel.raise_()
        self.mediumLabel.raise_()
        self.hardLabel.raise_()
        self.compOneEasyButton.raise_()
        self.compOneMediumButton.raise_()
        self.compOneHardButton.raise_()
        self.playerTwoLogin.raise_()
        self.playerTwoRegister.raise_()
        self.playerThreeRegister.raise_()
        self.playerThreeLogin.raise_()
        self.playerFourRegister.raise_()
        self.playerFourLogin.raise_()
        self.compTwoMediumButton.raise_()
        self.compTwoHardButton.raise_()
        self.compTwoEasyButton.raise_()
        self.compThreeMediumButton.raise_()
        self.compThreeHardButton.raise_()
        self.compThreeEasyButton.raise_()
        self.compFourHardButton.raise_()
        self.compFourEasyButton.raise_()
        self.compFourMediumButton.raise_()
        self.nextIcon.raise_()
        self.nextButton.raise_()
        self.returnButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Obsługa języków
        if self.language == 1:
            self.difficultyLabel.setGeometry(QtCore.QRect(160, 40, 191, 41))
            self.difficultyLabel.setStyleSheet("image: url(:/images/difficulty.png);")

            self.easyGameButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                              "border: 0px;")
            self.mediumGameButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                "border: 0px;")
            self.hardGameButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                              "border: 0px;")

            self.easyLabel.setStyleSheet("image: url(:/images/easyTiming.png);")
            self.mediumLabel.setStyleSheet("image: url(:/images/mediumTiming.png);")
            self.hardLabel.setStyleSheet("image: url(:/images/hardTiming.png);")

            self.playerThreeNickname.setGeometry(QtCore.QRect(96, 341, 151, 31))
            self.playerFourNickname.setGeometry(QtCore.QRect(274, 341, 151, 31))

            self.playerOneLabel.setStyleSheet("image: url(:/images/playerOne.png);")
            self.playerTwoLabel.setStyleSheet("image: url(:/images/playerTwo.png);")
            self.playerThreeLabel.setStyleSheet("image: url(:/images/playerThree.png);")
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFour.png);")
            self.playerThreeLabel.setGeometry(QtCore.QRect(110, 301, 121, 31))
            self.playerFourLabel.setGeometry(QtCore.QRect(260, 301, 181, 31))

            self.playerThreeRegister.setGeometry(QtCore.QRect(120, 381, 101, 31))
            self.playerThreeLogin.setGeometry(QtCore.QRect(110, 341, 121, 31))
            self.playerThreeLogout.setGeometry(QtCore.QRect(120, 381, 101, 31))
            self.playerFourRegister.setGeometry(QtCore.QRect(300, 381, 101, 31))
            self.playerFourLogin.setGeometry(QtCore.QRect(290, 341, 121, 31))
            self.playerFourLogout.setGeometry(QtCore.QRect(300, 381, 101, 31))

            self.playerOneLogin.setGeometry(QtCore.QRect(110, 221, 121, 31))
            self.playerOneLogin.setStyleSheet("image: url(:/images/logIn.png);\n"
                                              "border: 0px;")
            self.playerOneRegister.setGeometry(QtCore.QRect(120, 261, 101, 31))
            self.playerOneRegister.setStyleSheet("image: url(:/images/registerButton.png);\n"
                                                 "border: 0px;")
            self.playerOneLogout.setStyleSheet("image: url(:images/logOut.png);\n"
                                               "border: 0px;")
            self.playerOneLogout.setGeometry(QtCore.QRect(120, 261, 101, 31))

            self.playerTwoLogin.setGeometry(QtCore.QRect(290, 221, 121, 31))
            self.playerTwoRegister.setGeometry(QtCore.QRect(300, 261, 101, 31))
            self.playerTwoLogout.setStyleSheet("image: url(:/images/logOut.png);\n"
                                               "border: 0px;")
            self.playerTwoLogout.setGeometry(QtCore.QRect(300, 261, 101, 31))
            self.playerThreeLogout.setStyleSheet("image: url(:/images/logOut.png);\n"
                                                 "border: 0px;")
            self.playerFourLogout.setStyleSheet("image: url(:/images/logOut.png);\n"
                                                "border: 0px;")
            self.playerTwoLogin.setStyleSheet("image: url(:/images/logIn.png);\n"
                                              "border: 0px;")
            self.playerTwoRegister.setStyleSheet("image: url(:/images/registerButton.png);\n"
                                                 "border: 0px;")
            self.playerThreeRegister.setStyleSheet("image: url(:/images/registerButton.png);\n"
                                                   "border: 0px;")
            self.playerThreeLogin.setStyleSheet("image: url(:/images/logIn.png);\n"
                                                "border: 0px;")
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButton.png);\n"
                                                  "border: 0px;")
            self.playerFourLogin.setStyleSheet("image: url(:/images/logIn.png);\n"
                                               "border: 0px;")

            self.compOneLabel.setStyleSheet("image: url(:/images/computerOne.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwo.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThree.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFour.png);")

            self.compOneEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                 "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                   "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                 "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                   "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                     "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                  "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                    "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.difficultyLabel.setGeometry(QtCore.QRect(141, 33, 231, 51))
            self.difficultyLabel.setStyleSheet("image: url(:/images/difficultyPL.png);")
            self.easyGameButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                              "border: 0px;")
            self.mediumGameButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                "border: 0px;")
            self.hardGameButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                              "border: 0px;")
            self.easyLabel.setStyleSheet("image: url(:/images/easyTimingPL.png);")
            self.mediumLabel.setStyleSheet("image: url(:/images/mediumTimingPL.png);")
            self.hardLabel.setStyleSheet("image: url(:/images/hardTimingPL.png);")

            self.playerThreeNickname.setGeometry(QtCore.QRect(96, 349, 151, 31))
            self.playerFourNickname.setGeometry(QtCore.QRect(274, 349, 151, 31))

            self.playerOneLabel.setStyleSheet("image: url(:/images/playerOnePL.png);")
            self.playerTwoLabel.setStyleSheet("image: url(:/images/playerTwoPL.png);")
            self.playerThreeLabel.setStyleSheet("image: url(:/images/playerThreePL.png);")
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourPL.png);")
            self.playerThreeLabel.setGeometry(QtCore.QRect(110, 314, 121, 31))
            self.playerFourLabel.setGeometry(QtCore.QRect(260, 314, 181, 31))
            self.playerThreeLabel.setStyleSheet("image: url(:/images/playerThreePL.png);")
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourPL.png);")

            self.playerOneLogin.setGeometry(QtCore.QRect(129, 221, 81, 31))
            self.playerOneLogin.setStyleSheet("image: url(:/images/logInButtonPL.png);\n"
                                              "border: 0px;")

            self.playerOneRegister.setStyleSheet("image: url(:/images/registerButtonPL.png);\n"
                                                 "border: 0px;")
            self.playerOneRegister.setGeometry(QtCore.QRect(129, 260, 81, 41))

            self.playerTwoLogin.setStyleSheet("image: url(:/images/logInButtonPL.png);\n"
                                              "border: 0px;")
            self.playerTwoLogin.setGeometry(QtCore.QRect(309, 221, 81, 31))

            self.playerTwoRegister.setStyleSheet("image: url(:/images/registerButtonPL.png);\n"
                                                 "border: 0px;")
            self.playerTwoRegister.setGeometry(QtCore.QRect(309, 260, 81, 41))

            self.playerThreeLogin.setGeometry(QtCore.QRect(129, 351, 81, 31))
            self.playerThreeLogin.setStyleSheet("image: url(:/images/logInButtonPL.png);\n"
                                                "border: 0px;")
            self.playerThreeRegister.setGeometry(QtCore.QRect(129, 390, 81, 41))
            self.playerThreeRegister.setStyleSheet("image: url(:/images/registerButtonPL.png);\n"
                                                   "border: 0px;")
            self.playerFourLogin.setGeometry(QtCore.QRect(309, 351, 81, 31))
            self.playerFourLogin.setStyleSheet("image: url(:/images/logInButtonPL.png);\n"
                                               "border: 0px;")
            self.playerFourRegister.setGeometry(QtCore.QRect(309, 390, 81, 41))
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButtonPL.png);\n"
                                                  "border: 0px;")

            self.playerOneLogout.setGeometry(QtCore.QRect(132, 260, 75, 31))
            self.playerTwoLogout.setGeometry(QtCore.QRect(312, 260, 75, 31))
            self.playerThreeLogout.setGeometry(QtCore.QRect(132, 390, 75, 31))
            self.playerFourLogout.setGeometry(QtCore.QRect(312, 390, 75, 31))

            self.playerOneLogout.setStyleSheet("image: url(:/images/logOutPL.png);\n"
                                               "border: 0px;")
            self.playerTwoLogout.setStyleSheet("image: url(:/images/logOutPL.png);\n"
                                               "border: 0px;")
            self.playerThreeLogout.setStyleSheet("image: url(:/images/logOutPL.png);\n"
                                                 "border: 0px;")
            self.playerFourLogout.setStyleSheet("image: url(:/images/logOutPL.png);\n"
                                                "border: 0px;")

            self.compOneLabel.setStyleSheet("image: url(:/images/computerOnePL.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwoPL.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThreePL.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFourPL.png);")

            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                 "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                   "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                 "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                   "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                     "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                  "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                    "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                  "border: 0px;")



        # Przygotowanie okna w zależności od ilości userów
        if self.playersNumber == 0:
            self.zeroPlayers()
        if self.playersNumber == 1:
            self.onePlayer()
        if self.playersNumber == 2:
            self.twoPlayers()
        if self.playersNumber == 3:
            self.threePlayers()
        if self.playersNumber == 4:
            self.fourPlayers()
        if self.computersNumber == 0:
            self.zeroComputers()
        if self.computersNumber == 1:
            self.oneComputer()
        if self.computersNumber == 2:
            self.twoComputers()
        if self.computersNumber == 3:
            self.threeComputers()
        if self.computersNumber == 4:
            self.fourComputers()

        if self.check_level(5) == 1:
            self.easyLevel()
        if self.check_level(5) == 2:
            self.mediumLevel()
        if self.check_level(5) == 3:
            self.hardLevel()


        # Obsługa przycisków


        self.returnButton.clicked.connect(self.returnToOptions)
        self.returnButton.clicked.connect(Form.close)

        self.easyGameButton.clicked.connect(self.easyLevel)
        self.mediumGameButton.clicked.connect(self.mediumLevel)
        self.hardGameButton.clicked.connect(self.hardLevel)
        self.nextButton.clicked.connect(Form.close)
        self.nextButton.clicked.connect(self.show_betting)



        self.playerOneLogin.clicked.connect(Form.close)
        self.playerTwoLogin.clicked.connect(Form.close)
        self.playerThreeLogin.clicked.connect(Form.close)
        self.playerFourLogin.clicked.connect(Form.close)

        self.playerOneRegister.clicked.connect(Form.close)
        self.playerTwoRegister.clicked.connect(Form.close)
        self.playerThreeRegister.clicked.connect(Form.close)
        self.playerFourRegister.clicked.connect(Form.close)

        self.settings()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Users setup"))

    def returnToOptions(self):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "DELETE FROM logged_users"
            c.execute(query)
            c.execute("UPDATE levels SET level = 0")
            db.commit()

        except sql.Error as e:
            print("xd")

        self.window = QtWidgets.QMainWindow()
        self.ui = playOptions.playOptionsForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    def zeroPlayers(self):

        if self.language == 1:
            self.playerOneLabel.setStyleSheet("image: url(:/images/playerOneInactive.png);")
            self.playerTwoLabel.setStyleSheet("image: url(:/images/playerTwoInactive.png);")
            self.playerThreeLabel.setStyleSheet("image: url(:/images/playerThreeInactive.png);")
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourInactive.png);")

            self.playerOneLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                              "border: 0px;")
            self.playerOneRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                 "border: 0px;")
            self.playerTwoLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                              "border: 0px;")
            self.playerTwoRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                 "border: 0px;")
            self.playerThreeLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                                "border: 0px;")
            self.playerThreeRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                   "border: 0px;")
            self.playerFourLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                               "border: 0px;")
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.playerOneLabel.setStyleSheet("image: url(:/images/playerOneInactivePL.png);")
            self.playerTwoLabel.setStyleSheet("image: url(:/images/playerTwoInactivePL.png);")
            self.playerThreeLabel.setStyleSheet("image: url(:/images/playerThreeInactivePL.png);")
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourInactivePL.png);")
            self.playerOneLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                              "border: 0px;")
            self.playerOneRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                 "border: 0px;")
            self.playerTwoLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                              "border: 0px;")
            self.playerTwoRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                 "border: 0px;")
            self.playerThreeLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                                "border: 0px;")
            self.playerThreeRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                   "border: 0px;")
            self.playerFourLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                               "border: 0px;")
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                  "border: 0px;")

        self.playerOneLogin.setEnabled(False)
        self.playerTwoLogin.setEnabled(False)
        self.playerThreeLogin.setEnabled(False)
        self.playerFourLogin.setEnabled(False)
        self.playerOneRegister.setEnabled(False)
        self.playerTwoRegister.setEnabled(False)
        self.playerThreeRegister.setEnabled(False)
        self.playerFourRegister.setEnabled(False)

    def onePlayer(self):
        self.first_player()

        self.playerOneLogin.clicked.connect(self.first_player)
        self.playerOneLogin.clicked.connect(self.show_login)
        self.playerOneRegister.clicked.connect(self.show_register)
        self.playerOneLogout.clicked.connect(self.logout_one)

        self.playerOneLogin.setEnabled(True)
        self.playerTwoLogin.setEnabled(False)
        self.playerThreeLogin.setEnabled(False)
        self.playerFourLogin.setEnabled(False)
        self.playerOneRegister.setEnabled(True)
        self.playerTwoRegister.setEnabled(False)
        self.playerThreeRegister.setEnabled(False)
        self.playerFourRegister.setEnabled(False)

        if self.language == 1:
            self.playerTwoLabel.setStyleSheet("image: url(:/images/playerTwoInactive.png);")
            self.playerThreeLabel.setStyleSheet("image: url(:/images/playerThreeInactive.png);")
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourInactive.png);")

            self.playerTwoLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                              "border: 0px;")
            self.playerTwoRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                 "border: 0px;")
            self.playerThreeLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                                "border: 0px;")
            self.playerThreeRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                   "border: 0px;")
            self.playerFourLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                               "border: 0px;")
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.playerTwoLabel.setStyleSheet("image: url(:/images/playerTwoInactivePL.png);")
            self.playerThreeLabel.setStyleSheet("image: url(:/images/playerThreeInactivePL.png);")
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourInactivePL.png);")
            self.playerTwoLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                              "border: 0px;")
            self.playerTwoRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                 "border: 0px;")
            self.playerThreeLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                                "border: 0px;")
            self.playerThreeRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                   "border: 0px;")
            self.playerFourLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                               "border: 0px;")
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                  "border: 0px;")

    def twoPlayers(self):
        self.first_player()
        self.second_player()

        self.playerOneLogin.setEnabled(True)
        self.playerTwoLogin.setEnabled(True)
        self.playerThreeLogin.setEnabled(False)
        self.playerFourLogin.setEnabled(False)
        self.playerOneRegister.setEnabled(True)
        self.playerTwoRegister.setEnabled(True)
        self.playerThreeRegister.setEnabled(False)
        self.playerFourRegister.setEnabled(False)

        self.playerOneLogin.clicked.connect(self.first_player)
        self.playerOneLogin.clicked.connect(self.show_login)
        self.playerOneRegister.clicked.connect(self.show_register)
        self.playerOneLogout.clicked.connect(self.logout_one)
        self.playerTwoLogin.clicked.connect(self.second_player)
        self.playerTwoLogin.clicked.connect(self.show_login)
        self.playerTwoRegister.clicked.connect(self.show_register)
        self.playerTwoLogout.clicked.connect(self.logout_two)

        if self.language == 1:
            self.playerThreeLabel.setStyleSheet("image: url(:/images/playerThreeInactive.png);")
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourInactive.png);")

            self.playerThreeLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                                "border: 0px;")
            self.playerThreeRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                   "border: 0px;")
            self.playerFourLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                               "border: 0px;")
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.playerThreeLabel.setStyleSheet("image: url(:/images/playerThreeInactivePL.png);")
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourInactivePL.png);")
            self.playerThreeLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                                "border: 0px;")
            self.playerThreeRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                   "border: 0px;")
            self.playerFourLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                               "border: 0px;")
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                  "border: 0px;")

    def threePlayers(self):
        self.first_player()
        self.second_player()
        self.third_player()

        self.playerOneLogin.setEnabled(True)
        self.playerTwoLogin.setEnabled(True)
        self.playerThreeLogin.setEnabled(True)
        self.playerFourLogin.setEnabled(False)
        self.playerOneRegister.setEnabled(True)
        self.playerTwoRegister.setEnabled(True)
        self.playerThreeRegister.setEnabled(True)
        self.playerFourRegister.setEnabled(False)

        self.playerOneLogin.clicked.connect(self.first_player)
        self.playerOneLogin.clicked.connect(self.show_login)
        self.playerOneRegister.clicked.connect(self.show_register)
        self.playerOneLogout.clicked.connect(self.logout_one)
        self.playerTwoLogin.clicked.connect(self.second_player)
        self.playerTwoLogin.clicked.connect(self.show_login)
        self.playerTwoRegister.clicked.connect(self.show_register)
        self.playerTwoLogout.clicked.connect(self.logout_two)
        self.playerThreeLogin.clicked.connect(self.third_player)
        self.playerThreeLogin.clicked.connect(self.show_login)
        self.playerThreeRegister.clicked.connect(self.show_register)
        self.playerThreeLogout.clicked.connect(self.logout_three)

        if self.language == 1:
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourInactive.png);")

            self.playerFourLogin.setStyleSheet("image: url(:/images/logInInactive.png);\n"
                                               "border: 0px;")
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButtonInactive.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.playerFourLabel.setStyleSheet("image: url(:/images/playerFourInactivePL.png);")
            self.playerFourLogin.setStyleSheet("image: url(:/images/logInInactivePL.png);\n"
                                               "border: 0px;")
            self.playerFourRegister.setStyleSheet("image: url(:/images/registerButtonInactivePL.png);\n"
                                                  "border: 0px;")

    def fourPlayers(self):
        self.first_player()
        self.second_player()
        self.third_player()
        self.fourth_player()

        self.playerOneLogin.setEnabled(True)
        self.playerTwoLogin.setEnabled(True)
        self.playerThreeLogin.setEnabled(True)
        self.playerFourLogin.setEnabled(True)
        self.playerOneRegister.setEnabled(True)
        self.playerTwoRegister.setEnabled(True)
        self.playerThreeRegister.setEnabled(True)
        self.playerFourRegister.setEnabled(True)

        self.playerOneLogin.clicked.connect(self.first_player)
        self.playerOneLogin.clicked.connect(self.show_login)
        self.playerOneRegister.clicked.connect(self.show_register)
        self.playerOneLogout.clicked.connect(self.logout_one)
        self.playerTwoLogin.clicked.connect(self.second_player)
        self.playerTwoLogin.clicked.connect(self.show_login)
        self.playerTwoRegister.clicked.connect(self.show_register)
        self.playerTwoLogout.clicked.connect(self.logout_two)
        self.playerThreeLogin.clicked.connect(self.third_player)
        self.playerThreeLogin.clicked.connect(self.show_login)
        self.playerThreeRegister.clicked.connect(self.show_register)
        self.playerThreeLogout.clicked.connect(self.logout_three)
        self.playerFourLogin.clicked.connect(self.fourth_player)
        self.playerFourLogin.clicked.connect(self.show_login)
        self.playerFourRegister.clicked.connect(self.show_register)
        self.playerFourLogout.clicked.connect(self.logout_four)

    def zeroComputers(self):
        self.compOneEasyButton.setEnabled(False)
        self.compTwoEasyButton.setEnabled(False)
        self.compThreeEasyButton.setEnabled(False)
        self.compFourEasyButton.setEnabled(False)
        self.compOneMediumButton.setEnabled(False)
        self.compTwoMediumButton.setEnabled(False)
        self.compThreeMediumButton.setEnabled(False)
        self.compFourMediumButton.setEnabled(False)
        self.compOneHardButton.setEnabled(False)
        self.compTwoHardButton.setEnabled(False)
        self.compThreeHardButton.setEnabled(False)
        self.compFourHardButton.setEnabled(False)

        if self.language == 1:
            self.compOneLabel.setStyleSheet("image: url(:/images/computerOneInactive.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwoInactive.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThreeInactive.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFourInactive.png);")
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                  "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                   "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                     "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                    "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                 "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                 "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                   "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.compOneLabel.setStyleSheet("image: url(:/images/computerOneInactivePL.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwoInactivePL.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThreeInactivePL.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFourInactivePL.png);")
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                  "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                   "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                     "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                    "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                 "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                 "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                   "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                  "border: 0px;")

    def oneComputer(self):
        self.compOneEasyButton.setEnabled(True)
        self.compTwoEasyButton.setEnabled(False)
        self.compThreeEasyButton.setEnabled(False)
        self.compFourEasyButton.setEnabled(False)
        self.compOneMediumButton.setEnabled(True)
        self.compTwoMediumButton.setEnabled(False)
        self.compThreeMediumButton.setEnabled(False)
        self.compFourMediumButton.setEnabled(False)
        self.compOneHardButton.setEnabled(True)
        self.compTwoHardButton.setEnabled(False)
        self.compThreeHardButton.setEnabled(False)
        self.compFourHardButton.setEnabled(False)

        self.compOneEasyButton.clicked.connect(self.compOneEasyLevel)
        self.compOneMediumButton.clicked.connect(self.compOneMediumLevel)
        self.compOneHardButton.clicked.connect(self.compOneHardLevel)




        if self.language == 1:
            self.compOneLabel.setStyleSheet("image: url(:/images/computerOne.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwoInactive.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThreeInactive.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFourInactive.png);")

            self.compOneEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                  "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                   "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                     "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                    "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                 "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                 "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                   "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                  "border: 0px;")


        if self.language == 2:
            self.compOneLabel.setStyleSheet("image: url(:/images/computerOnePL.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwoInactivePL.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThreeInactivePL.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFourInactivePL.png);")
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                  "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                   "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                     "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                    "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                 "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                 "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                   "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                  "border: 0px;")
        if self.check_level(1) == 1:
            self.compOneEasyLevel()
        elif self.check_level(1) == 2:
            self.compOneMediumLevel()
        elif self.check_level(1) == 3:
            self.compOneHardLevel()

    def twoComputers(self):
        self.compOneEasyButton.setEnabled(True)
        self.compTwoEasyButton.setEnabled(True)
        self.compThreeEasyButton.setEnabled(False)
        self.compFourEasyButton.setEnabled(False)
        self.compOneMediumButton.setEnabled(True)
        self.compTwoMediumButton.setEnabled(True)
        self.compThreeMediumButton.setEnabled(False)
        self.compFourMediumButton.setEnabled(False)
        self.compOneHardButton.setEnabled(True)
        self.compTwoHardButton.setEnabled(True)
        self.compThreeHardButton.setEnabled(False)
        self.compFourHardButton.setEnabled(False)

        self.compOneEasyButton.clicked.connect(self.compOneEasyLevel)
        self.compOneMediumButton.clicked.connect(self.compOneMediumLevel)
        self.compOneHardButton.clicked.connect(self.compOneHardLevel)
        self.compTwoEasyButton.clicked.connect(self.compTwoEasyLevel)
        self.compTwoMediumButton.clicked.connect(self.compTwoMediumLevel)
        self.compTwoHardButton.clicked.connect(self.compTwoHardLevel)

        if self.language == 1:
            self.compOneLabel.setStyleSheet("image: url(:/images/computerOne.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwo.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThreeInactive.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFourInactive.png);")

            self.compOneEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                  "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                   "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                     "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                    "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                 "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                 "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                   "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.compOneLabel.setStyleSheet("image: url(:/images/computerOnePL.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwoPL.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThreeInactivePL.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFourInactivePL.png);")
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                  "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                   "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                     "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                    "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                 "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                 "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                   "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                  "border: 0px;")
        if self.check_level(1) == 1:
            self.compOneEasyLevel()
        elif self.check_level(1) == 2:
            self.compOneMediumLevel()
        elif self.check_level(1) == 3:
            self.compOneHardLevel()
        if self.check_level(2) == 1:
            self.compTwoEasyLevel()
        elif self.check_level(2) == 2:
            self.compTwoMediumLevel()
        elif self.check_level(2) == 3:
            self.compTwoHardLevel()

    def threeComputers(self):
        self.compOneEasyButton.setEnabled(True)
        self.compTwoEasyButton.setEnabled(True)
        self.compThreeEasyButton.setEnabled(True)
        self.compFourEasyButton.setEnabled(False)
        self.compOneMediumButton.setEnabled(True)
        self.compTwoMediumButton.setEnabled(True)
        self.compThreeMediumButton.setEnabled(True)
        self.compFourMediumButton.setEnabled(False)
        self.compOneHardButton.setEnabled(True)
        self.compTwoHardButton.setEnabled(True)
        self.compThreeHardButton.setEnabled(True)
        self.compFourHardButton.setEnabled(False)

        self.compOneEasyButton.clicked.connect(self.compOneEasyLevel)
        self.compOneMediumButton.clicked.connect(self.compOneMediumLevel)
        self.compOneHardButton.clicked.connect(self.compOneHardLevel)
        self.compTwoEasyButton.clicked.connect(self.compTwoEasyLevel)
        self.compTwoMediumButton.clicked.connect(self.compTwoMediumLevel)
        self.compTwoHardButton.clicked.connect(self.compTwoHardLevel)
        self.compThreeEasyButton.clicked.connect(self.compThreeEasyLevel)
        self.compThreeMediumButton.clicked.connect(self.compThreeMediumLevel)
        self.compThreeHardButton.clicked.connect(self.compThreeHardLevel)

        if self.language == 1:
            self.compOneLabel.setStyleSheet("image: url(:/images/computerOne.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwo.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThree.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFourInactive.png);")

            self.compOneEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                  "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                   "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                     "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                    "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                 "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                 "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                   "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.compOneLabel.setStyleSheet("image: url(:/images/computerOnePL.png);")
            self.compTwoLabel.setStyleSheet("image: url(:/images/computerTwoPL.png);")
            self.compThreeLabel.setStyleSheet("image: url(:/images/computerThreePL.png);")
            self.compFourLabel.setStyleSheet("image: url(:/images/computerFourInactivePL.png);")
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                 "border: 0px;")
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                 "border: 0px;")
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                   "border: 0px;")
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                  "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                   "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                     "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                    "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                 "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                 "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                   "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                  "border: 0px;")

        if self.check_level(1) == 1:
            self.compOneEasyLevel()
        elif self.check_level(1) == 2:
            self.compOneMediumLevel()
        elif self.check_level(1) == 3:
            self.compOneHardLevel()
        if self.check_level(2) == 1:
            self.compTwoEasyLevel()
        elif self.check_level(2) == 2:
            self.compTwoMediumLevel()
        elif self.check_level(2) == 3:
            self.compTwoHardLevel()
        if self.check_level(3) == 1:
            self.compThreeEasyLevel()
        elif self.check_level(3) == 2:
            self.compThreeMediumLevel()
        elif self.check_level(3) == 3:
            self.compThreeHardLevel()

    def fourComputers(self):
        self.compOneEasyButton.setEnabled(True)
        self.compTwoEasyButton.setEnabled(True)
        self.compThreeEasyButton.setEnabled(True)
        self.compFourEasyButton.setEnabled(True)
        self.compOneMediumButton.setEnabled(True)
        self.compTwoMediumButton.setEnabled(True)
        self.compThreeMediumButton.setEnabled(True)
        self.compFourMediumButton.setEnabled(True)
        self.compOneHardButton.setEnabled(True)
        self.compTwoHardButton.setEnabled(True)
        self.compThreeHardButton.setEnabled(True)
        self.compFourHardButton.setEnabled(True)

        self.compOneEasyButton.clicked.connect(self.compOneEasyLevel)
        self.compOneMediumButton.clicked.connect(self.compOneMediumLevel)
        self.compOneHardButton.clicked.connect(self.compOneHardLevel)
        self.compTwoEasyButton.clicked.connect(self.compTwoEasyLevel)
        self.compTwoMediumButton.clicked.connect(self.compTwoMediumLevel)
        self.compTwoHardButton.clicked.connect(self.compTwoHardLevel)
        self.compThreeEasyButton.clicked.connect(self.compThreeEasyLevel)
        self.compThreeMediumButton.clicked.connect(self.compThreeMediumLevel)
        self.compThreeHardButton.clicked.connect(self.compThreeHardLevel)
        self.compFourEasyButton.clicked.connect(self.compFourEasyLevel)
        self.compFourMediumButton.clicked.connect(self.compFourMediumLevel)
        self.compFourHardButton.clicked.connect(self.compFourHardLevel)

        if self.check_level(1) == 1:
            self.compOneEasyLevel()
        elif self.check_level(1) == 2:
            self.compOneMediumLevel()
        elif self.check_level(1) == 3:
            self.compOneHardLevel()
        if self.check_level(2) == 1:
            self.compTwoEasyLevel()
        elif self.check_level(2) == 2:
            self.compTwoMediumLevel()
        elif self.check_level(2) == 3:
            self.compTwoHardLevel()
        if self.check_level(3) == 1:
            self.compThreeEasyLevel()
        elif self.check_level(3) == 2:
            self.compThreeMediumLevel()
        elif self.check_level(3) == 3:
            self.compThreeHardLevel()
        if self.check_level(4) == 1:
            self.compFourEasyLevel()
        elif self.check_level(4) == 2:
            self.compFourMediumLevel()
        elif self.check_level(4) == 3:
            self.compFourHardLevel()

    # Wygaszanie nieużywanych opcji + przypisywanie poziomów do zmiennych

    # Poziomy pierwszego komputera

    def compOneEasyLevel(self):
        self.computerOneLevel = 1
        self.update_leveldb(1, 1)
        if self.language == 1:
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                 "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                   "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                 "border: 0px;")
        if self.language == 2:
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                 "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                   "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                 "border: 0px;")

        self.settings()

    def compOneMediumLevel(self):
        self.computerOneLevel = 2
        self.update_leveldb(1, 2)
        if self.language == 1:
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                 "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                   "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                 "border: 0px;")
        if self.language == 2:
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                 "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                   "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                 "border: 0px;")

        self.settings()

    def compOneHardLevel(self):
        self.computerOneLevel = 3
        self.update_leveldb(1, 3)
        if self.language == 1:
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                 "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                   "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                 "border: 0px;")
        if self.language == 2:
            self.compOneEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                 "border: 0px;")
            self.compOneMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                   "border: 0px;")
            self.compOneHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                 "border: 0px;")

        self.settings()

        # Poziomy drugiego komputera

    def compTwoEasyLevel(self):
        self.computerTwoLevel = 1
        self.update_leveldb(2, 1)
        if self.language == 1:
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                 "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                   "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                 "border: 0px;")
        if self.language == 2:
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                 "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                   "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                 "border: 0px;")

        self.settings()

    def compTwoMediumLevel(self):
        self.computerTwoLevel = 2
        self.update_leveldb(2, 2)
        if self.language == 1:
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                 "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                   "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                 "border: 0px;")
        if self.language == 2:
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                 "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                   "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                 "border: 0px;")

        self.settings()

    def compTwoHardLevel(self):
        self.computerTwoLevel = 3
        self.update_leveldb(2, 3)
        if self.language == 1:
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                 "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                   "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                 "border: 0px;")
        if self.language == 2:
            self.compTwoEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                 "border: 0px;")
            self.compTwoMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                   "border: 0px;")
            self.compTwoHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                 "border: 0px;")

        self.settings()

        # Poziomy trzeciego komputera

    def compThreeEasyLevel(self):
        self.computerThreeLevel = 1
        self.update_leveldb(3, 1)
        if self.language == 1:
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                     "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                   "border: 0px;")
        if self.language == 2:
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                     "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                   "border: 0px;")

        self.settings()

    def compThreeMediumLevel(self):
        self.computerThreeLevel = 2
        self.update_leveldb(3, 2)
        if self.language == 1:
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                     "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                   "border: 0px;")
        if self.language == 2:
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                     "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                   "border: 0px;")

        self.settings()

    def compThreeHardLevel(self):
        self.computerThreeLevel = 3
        self.update_leveldb(3, 3)
        if self.language == 1:
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                     "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                   "border: 0px;")
        if self.language == 2:
            self.compThreeEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                   "border: 0px;")
            self.compThreeMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                     "border: 0px;")
            self.compThreeHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                   "border: 0px;")

        self.settings()

        # Poziomy czwartego komputera

    def compFourEasyLevel(self):
        self.computerFourLevel = 1
        self.update_leveldb(4, 1)
        if self.language == 1:
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                                  "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                    "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                                  "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                    "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                  "border: 0px;")

        self.settings()

    def compFourMediumLevel(self):
        self.computerFourLevel = 2
        self.update_leveldb(4, 2)
        if self.language == 1:
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                  "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                    "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                  "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                    "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                                  "border: 0px;")

        self.settings()

    def compFourHardLevel(self):
        self.computerFourLevel = 3
        self.update_leveldb(4, 3)
        if self.language == 1:
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                                  "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                    "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                                  "border: 0px;")
        if self.language == 2:
            self.compFourEasyButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                                  "border: 0px;")
            self.compFourMediumButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                    "border: 0px;")
            self.compFourHardButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                                  "border: 0px;")

        self.settings()

        # Wygaszanie poziomu gry

    def easyLevel(self):
        self.gameLevel = 1
        self.update_leveldb(5,1)

        if self.language == 1:
            self.easyGameButton.setStyleSheet("image: url(:/images/easy.png);\n"
                                              "border: 0px;")
            self.easyLabel.setStyleSheet("image: url(:/images/easyTiming.png);")
            self.mediumLabel.setStyleSheet("image: url(:/images/mediumTimingInactive.png);")
            self.mediumGameButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                "border: 0px;")
            self.hardLabel.setStyleSheet("image: url(:/images/hardTimingInactive.png);")
            self.hardGameButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                              "border: 0px;")
        if self.language == 2:
            self.easyGameButton.setStyleSheet("image: url(:/images/easyPL.png);\n"
                                              "border: 0px;")
            self.easyLabel.setStyleSheet("image: url(:/images/easyTimingPL.png);")
            self.mediumLabel.setStyleSheet("image: url(:/images/mediumTimingInactivePL.png);")
            self.mediumGameButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                "border: 0px;")
            self.hardLabel.setStyleSheet("image: url(:/images/hardTimingInactivePL.png);")
            self.hardGameButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                              "border: 0px;")

        self.settings()



    def mediumLevel(self):
        self.gameLevel = 2
        self.update_leveldb(5, 2)
        if self.language == 1:
            self.mediumGameButton.setStyleSheet("image: url(:/images/medium.png);\n"
                                                "border: 0px;")
            self.mediumLabel.setStyleSheet("image: url(:/images/mediumTiming.png);")
            self.easyLabel.setStyleSheet("image: url(:/images/easyTimingInactive.png);")
            self.easyGameButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                              "border: 0px;")
            self.hardLabel.setStyleSheet("image: url(:/images/hardTimingInactive.png);")
            self.hardGameButton.setStyleSheet("image: url(:/images/hardInactive.png);\n"
                                              "border: 0px;")
        if self.language == 2:
            self.mediumGameButton.setStyleSheet("image: url(:/images/mediumPL.png);\n"
                                                "border: 0px;")
            self.mediumLabel.setStyleSheet("image: url(:/images/mediumTimingPL.png);")
            self.easyLabel.setStyleSheet("image: url(:/images/easyTimingInactivePL.png);")
            self.easyGameButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                              "border: 0px;")
            self.hardLabel.setStyleSheet("image: url(:/images/hardTimingInactivePL.png);")
            self.hardGameButton.setStyleSheet("image: url(:/images/hardInactivePL.png);\n"
                                              "border: 0px;")

        self.settings()

    def hardLevel(self):
        self.gameLevel = 3
        self.update_leveldb(5, 3)
        if self.language == 1:
            self.hardLabel.setStyleSheet("image: url(:/images/hardTiming.png);")
            self.hardGameButton.setStyleSheet("image: url(:/images/hard.png);\n"
                                              "border: 0px;")
            self.easyLabel.setStyleSheet("image: url(:/images/easyTimingInactive.png);")
            self.easyGameButton.setStyleSheet("image: url(:/images/easyInactive.png);\n"
                                              "border: 0px;")

            self.mediumLabel.setStyleSheet("image: url(:/images/mediumTimingInactive.png);")
            self.mediumGameButton.setStyleSheet("image: url(:/images/mediumInactive.png);\n"
                                                "border: 0px;")
        if self.language == 2:
            self.hardLabel.setStyleSheet("image: url(:/images/hardTimingPL.png);")
            self.hardGameButton.setStyleSheet("image: url(:/images/hardPL.png);\n"
                                              "border: 0px;")
            self.easyLabel.setStyleSheet("image: url(:/images/easyTimingInactivePL.png);")
            self.easyGameButton.setStyleSheet("image: url(:/images/easyInactivePL.png);\n"
                                              "border: 0px;")

            self.mediumLabel.setStyleSheet("image: url(:/images/mediumTimingInactivePL.png);")
            self.mediumGameButton.setStyleSheet("image: url(:/images/mediumInactivePL.png);\n"
                                                "border: 0px;")
        self.settings()

    def first_player(self):

        result = self.assign_player(1)

        print("1")
        self.numberOfPlayer.append(1)
        print(self.numberOfPlayer)

        if result is not None:
            self.loggedUsers.append(1)
            self.playerOneLogin.setVisible(False)
            self.playerOneRegister.setVisible(False)
            self.playerOneLogout.setVisible(True)

            self.playerOneNickname.setText(self.set_username(1))

        else:
            print("xd")

    def second_player(self):
        result = self.assign_player(2)

        print("2")
        self.numberOfPlayer.append(2)
        print(self.numberOfPlayer)

        if result is not None:
            self.loggedUsers.append(2)
            self.playerTwoLogin.setVisible(False)
            self.playerTwoRegister.setVisible(False)

            self.playerTwoNickname.setText(self.set_username(2))
        else:
            print("xd")

    def third_player(self):
        result = self.assign_player(3)
        print("3")
        self.numberOfPlayer.append(3)
        print(self.numberOfPlayer)

        if result is not None:
            self.loggedUsers.append(3)
            self.playerThreeLogin.setVisible(False)
            self.playerThreeRegister.setVisible(False)

            self.playerThreeNickname.setText(self.set_username(3))

        else:
            print("xd")

    def fourth_player(self):
        result = self.assign_player(4)

        print("4")
        self.numberOfPlayer.append(4)
        print(self.numberOfPlayer)

        if result is not None:
            self.loggedUsers.append(4)
            self.playerFourLogin.setVisible(False)
            self.playerFourRegister.setVisible(False)

            self.playerFourNickname.setText(self.set_username(4))

        else:
            print("xd")

    # Nadanie użytkownikowi nazwy po zalogowaniu
    def set_username(self, user_id):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "SELECT id, username, coins from logged_users where id = {}".format(user_id)
            c.execute(query)
            db.commit()
            result = c.fetchone()

            if result is not None:
                return result[1]
            else:
                return "-"

        except sql.Error as e:
            print("xd")

    def assign_player(self, user_id):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "SELECT id, username, coins from logged_users where id = {}".format(user_id)
            c.execute(query)
            db.commit()
            result = c.fetchone()
            return result

        except sql.Error as e:
            print("xd")

    def update_leveldb(self, level_id, level):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            c.execute(
                "UPDATE levels SET level = {} WHERE id = {}".format(level, level_id))
            # "INSERT INTO logged_users (id,username,password) VALUES (?,?,?)", (0, self.username, self.password))
            db.commit()
        except sql.Error as e:
            print("Error")

    def check_level(self, level_id):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "SELECT level from levels where id = {}".format(level_id)
            c.execute(query)
            db.commit()
            result = c.fetchone()
            print(result)
            return result[0]


        except sql.Error as e:
            print("xd")


    def settings(self):
        if self.playersNumber == 1 and len(self.loggedUsers) != 1:
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
        elif self.playersNumber == 2 and len(self.loggedUsers) != 2:
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
        elif self.playersNumber == 3 and len(self.loggedUsers) != 3:
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
        elif self.playersNumber == 4 and len(self.loggedUsers) != 4:
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
        elif self.computersNumber == 1 and self.check_level(1) == 0:
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
        elif self.computersNumber == 2 and (self.check_level(1) == 0 or self.check_level(2) == 0):
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
        elif self.computersNumber == 3 and (self.check_level(1) == 0 or self.check_level(2) == 0 or self.check_level(3) == 0):
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
        elif self.computersNumber == 4 and (self.check_level(1) == 0 or self.check_level(2) == 0 or self.check_level(3) == 0 or self.check_level(4) == 0):
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
        elif self.gameLevel == 0 and self.check_level(5) == 0:
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
        else:
            self.nextIcon.setStyleSheet("image: url(:/images/next.png);")
            self.nextButton.setVisible(True)

    def show_register(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = register.registerForm(self.language, self.numberOfPlayer, self.playersNumber, self.computersNumber,
                                        self.betting)
        self.ui.setupUi(self.window)
        self.window.show()

    def show_login(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = login.loginForm(self.language, self.numberOfPlayer, self.playersNumber, self.computersNumber,
                                  self.betting)
        self.ui.setupUi(self.window)
        self.window.show()

    def openBoard(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = board.boardForm(self.language, self.playersNumber, self.computersNumber, self.betting,
                                  self.numberOfPlayer, self.gameLevel, self.computerOneLevel, self.computerTwoLevel, self.computerThreeLevel, self.computerFourLevel, self.input)
        self.ui.setupUi(self.window)
        self.window.show()
        # boardLabels = BoardLabels(self)
        # self.popups.append(self.window)

    def show_betting(self):
        if self.betting == 1:
            # self.openBoard()
            self.window = QtWidgets.QMainWindow()
            self.ui = betting.bettingForm(self.language, self.playersNumber, self.computersNumber, self.betting,
                                  self.numberOfPlayer, self.gameLevel, self.computerOneLevel, self.computerTwoLevel, self.computerThreeLevel, self.computerFourLevel)
            self.ui.setupUi(self.window)
            self.window.show()



        elif self.betting == 0:
            self.openBoard()

    # Wylogowywanie poszczególnych graczy
    def logout_one(self):
        print("siema")

        self.numberOfPlayer.remove(1)
        self.loggedUsers.remove(1)
        print(self.numberOfPlayer)
        self.delete_user(1)

        self.playerOneRegister.setVisible(True)
        self.playerOneLogin.setVisible(True)
        self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
        self.nextButton.setVisible(False)

    def logout_two(self):
        print("siema")

        self.numberOfPlayer.remove(2)
        self.loggedUsers.remove(2)
        print(self.numberOfPlayer)
        self.delete_user(2)

        self.playerTwoRegister.setVisible(True)
        self.playerTwoLogin.setVisible(True)
        self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
        self.nextButton.setVisible(False)

    def logout_three(self):
        print("siema")

        self.numberOfPlayer.remove(3)
        self.loggedUsers.remove(3)
        print(self.numberOfPlayer)
        self.delete_user(3)

        self.playerThreeRegister.setVisible(True)
        self.playerThreeLogin.setVisible(True)
        self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
        self.nextButton.setVisible(False)

    def logout_four(self):
        print("siema")

        self.numberOfPlayer.remove(4)
        self.loggedUsers.remove(4)
        print(self.numberOfPlayer)
        self.delete_user(4)

        self.playerFourRegister.setVisible(True)
        self.playerFourLogin.setVisible(True)
        self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
        self.nextButton.setVisible(False)

    def delete_user(self, user_id):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "DELETE FROM logged_users where id = {}".format(user_id)
            c.execute(query)
            db.commit()

        except sql.Error as e:
            print("xd")
