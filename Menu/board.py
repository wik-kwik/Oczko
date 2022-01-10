from PyQt5 import QtCore, QtGui, QtWidgets
from boardLabels import BoardLabels
from frontendLogic import FrontendLogic
import menu, playUsers
import sqlite3 as sql
from Game_Logic.player import Player
from frontendLogic import FrontendLogic
import time
from PyQt5.QtCore import QTimer
import playerChange
from boardLabels import BoardLabels
import summary


class boardForm(object):
    def __init__(self, language, playersNumber, computersNumber, betting, numberOfPlayer, gameLevel, computerOneLevel, computerTwoLevel, computerThreeLevel, computerFourLevel, input):
        self.language = language
        self.playersNumber = playersNumber
        self.computersNumber = computersNumber
        self.betting = betting
        self.numberOfPlayer = numberOfPlayer
        self.gameLevel = gameLevel
        self.computerOneLevel = computerOneLevel
        self.computerTwoLevel = computerTwoLevel
        self.computerThreeLevel = computerThreeLevel
        self.computerFourLevel = computerFourLevel
        self.input = input
        db = sql.connect('database.db')  # łączymy się do bazy
        c = db.cursor()  # dodajemy kursor
        query = "SELECT skin from settings"
        c.execute(query)
        db.commit()
        result = c.fetchone()
        self.skin = result[0]
        if self.skin == 2:
            self.path = "image: url(:/images/cardBackTwo.png);"

        else:
            self.path = "image: url(:/images/cardBackOne.png);"

        if gameLevel == 1:
            self.time = 15

        elif gameLevel == 2:
            self.time = 10

        elif gameLevel == 3:
            self.time = 5

    def setupUi(self, boardForm):
        boardForm.setObjectName("boardForm")
        boardForm.resize(1838, 1025)
        boardForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        boardForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundDark = QtWidgets.QLabel(boardForm)
        self.backgroundDark.setGeometry(QtCore.QRect(0, 0, 1850, 940))
        self.backgroundDark.setStyleSheet("background-color: rgb(24, 47, 38);")
        self.backgroundDark.setText("")
        self.backgroundDark.setObjectName("backgroundDark")
        self.standButton = QtWidgets.QPushButton(boardForm)
        self.standButton.setGeometry(QtCore.QRect(1510, 520, 161, 61))
        self.standButton.setText("")
        self.standButton.setObjectName("standButton")
        self.timeLeftIcon = QtWidgets.QLabel(boardForm)
        self.timeLeftIcon.setText("")
        self.timeLeftIcon.setObjectName("timeLeftIcon")
        self.hitButton = QtWidgets.QPushButton(boardForm)
        self.hitButton.setGeometry(QtCore.QRect(1510, 430, 161, 61))
        self.hitButton.setText("")
        self.hitButton.setObjectName("hitButton")
        self.playerOneCard_1 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_1.setGeometry(QtCore.QRect(320, 160, 131, 171))
        self.playerOneCard_1.setStyleSheet(self.path)
        self.playerOneCard_1.setText("")
        self.playerOneCard_1.setObjectName("playerOneCard_1")
        self.playerOneLabel = QtWidgets.QLabel(boardForm)
        self.playerOneLabel.setGeometry(QtCore.QRect(330, 100, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.playerOneLabel.setFont(font)
        self.playerOneLabel.setStyleSheet("color: rgb(255, 85, 0);")
        self.playerOneLabel.setText("")
        self.playerOneLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerOneLabel.setObjectName("playerOneLabel")
        self.coinsIcon = QtWidgets.QLabel(boardForm)
        self.coinsIcon.setGeometry(QtCore.QRect(710, 750, 71, 81))
        self.coinsIcon.setStyleSheet("image: url(:/images/coins.png);")
        self.coinsIcon.setText("")
        self.coinsIcon.setObjectName("coinsIcon")
        self.walletIcon = QtWidgets.QLabel(boardForm)
        self.walletIcon.setGeometry(QtCore.QRect(1490, 820, 51, 51))
        self.walletIcon.setStyleSheet("image: url(:/images/wallet.png);")
        self.walletIcon.setText("")
        self.walletIcon.setObjectName("walletIcon")
        self.menuStripe = QtWidgets.QLabel(boardForm)
        self.menuStripe.setGeometry(QtCore.QRect(1470, 0, 251, 941))
        self.menuStripe.setStyleSheet("background-color:rgba(0, 0, 0, 100);")
        self.menuStripe.setText("")
        self.menuStripe.setObjectName("menuStripe")
        self.logoLabel = QtWidgets.QLabel(boardForm)
        self.logoLabel.setGeometry(QtCore.QRect(1560, 30, 81, 91))
        self.logoLabel.setStyleSheet("image: url(:/images/logoCards.png);")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.balanceText = QtWidgets.QLabel(boardForm)
        self.balanceText.setGeometry(QtCore.QRect(1540, 830, 161, 41))
        self.balanceText.setText("")
        self.balanceText.setObjectName("balanceText")
        self.toWinLabel = QtWidgets.QLabel(boardForm)
        self.toWinLabel.setGeometry(QtCore.QRect(650, 824, 191, 81))
        self.toWinLabel.setText("")
        self.toWinLabel.setObjectName("toWinLabel")
        self.balanceLabel = QtWidgets.QLabel(boardForm)
        self.balanceLabel.setGeometry(QtCore.QRect(1470, 880, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.balanceLabel.setFont(font)
        self.balanceLabel.setStyleSheet("color: rgb(223, 175, 0);")
        self.balanceLabel.setText("")
        self.balanceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.balanceLabel.setObjectName("balanceLabel")
        self.timerLabel = QtWidgets.QLabel(boardForm)
        self.timerLabel.setGeometry(QtCore.QRect(1480, 230, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        self.timerLabel.setFont(font)
        self.timerLabel.setStyleSheet("color: rgb(255, 170, 0);")
        self.timerLabel.setText("")
        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLabel.setObjectName("timerLabel")
        self.prizeLabel = QtWidgets.QLabel(boardForm)
        self.prizeLabel.setGeometry(QtCore.QRect(650, 860, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.prizeLabel.setFont(font)
        self.prizeLabel.setStyleSheet("color: rgb(255, 60, 11);")
        self.prizeLabel.setText("")
        self.prizeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.prizeLabel.setObjectName("prizeLabel")
        self.playerTwoLabel = QtWidgets.QLabel(boardForm)
        self.playerTwoLabel.setGeometry(QtCore.QRect(330, 430, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.playerTwoLabel.setFont(font)
        self.playerTwoLabel.setStyleSheet("color: rgb(255, 85, 0);")
        self.playerTwoLabel.setText("")
        self.playerTwoLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerTwoLabel.setObjectName("playerTwoLabel")
        self.playerThreeCard_1 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_1.setGeometry(QtCore.QRect(830, 160, 131, 171))
        self.playerThreeCard_1.setStyleSheet(self.path)
        self.playerThreeCard_1.setText("")
        self.playerThreeCard_1.setObjectName("playerThreeCard_1")
        self.playerThreeLabel = QtWidgets.QLabel(boardForm)
        self.playerThreeLabel.setGeometry(QtCore.QRect(840, 100, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.playerThreeLabel.setFont(font)
        self.playerThreeLabel.setStyleSheet("color: rgb(255, 85, 0);")
        self.playerThreeLabel.setText("")
        self.playerThreeLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerThreeLabel.setObjectName("playerThreeLabel")
        self.playerFourLabel = QtWidgets.QLabel(boardForm)
        self.playerFourLabel.setGeometry(QtCore.QRect(840, 430, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.playerFourLabel.setFont(font)
        self.playerFourLabel.setStyleSheet("color: rgb(255, 85, 0);")
        self.playerFourLabel.setText("")
        self.playerFourLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerFourLabel.setObjectName("playerFourLabel")
        self.playerTwoCard_1 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_1.setGeometry(QtCore.QRect(320, 490, 131, 171))
        self.playerTwoCard_1.setStyleSheet(self.path)
        self.playerTwoCard_1.setText("")
        self.playerTwoCard_1.setObjectName("playerTwoCard_1")
        self.playerOneCard_2 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_2.setGeometry(QtCore.QRect(350, 160, 131, 171))
        self.playerOneCard_2.setStyleSheet(self.path)
        self.playerOneCard_2.setText("")
        self.playerOneCard_2.setObjectName("playerOneCard_2")
        self.playerOneCard_3 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_3.setGeometry(QtCore.QRect(380, 160, 131, 171))
        self.playerOneCard_3.setStyleSheet("")
        self.playerOneCard_3.setText("")
        self.playerOneCard_3.setObjectName("playerOneCard_3")
        self.playerOneCard_4 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_4.setGeometry(QtCore.QRect(410, 160, 131, 171))
        self.playerOneCard_4.setStyleSheet("")
        self.playerOneCard_4.setText("")
        self.playerOneCard_4.setObjectName("playerOneCard_4")
        self.playerOneCard_5 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_5.setGeometry(QtCore.QRect(440, 160, 131, 171))
        self.playerOneCard_5.setStyleSheet("")
        self.playerOneCard_5.setText("")
        self.playerOneCard_5.setObjectName("playerOneCard_5")
        self.playerOneCard_6 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_6.setGeometry(QtCore.QRect(470, 160, 131, 171))
        self.playerOneCard_6.setStyleSheet("")
        self.playerOneCard_6.setText("")
        self.playerOneCard_6.setObjectName("playerOneCard_6")
        self.playerOneCard_7 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_7.setGeometry(QtCore.QRect(500, 160, 131, 171))
        self.playerOneCard_7.setStyleSheet("")
        self.playerOneCard_7.setText("")
        self.playerOneCard_7.setObjectName("playerOneCard_7")
        self.playerOneCard_8 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_8.setGeometry(QtCore.QRect(530, 160, 131, 171))
        self.playerOneCard_8.setStyleSheet("")
        self.playerOneCard_8.setText("")
        self.playerOneCard_8.setObjectName("playerOneCard_8")
        self.playerOneCard_9 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_9.setGeometry(QtCore.QRect(560, 160, 131, 171))
        self.playerOneCard_9.setStyleSheet("")
        self.playerOneCard_9.setText("")
        self.playerOneCard_9.setObjectName("playerOneCard_9")
        self.playerOneCard_10 = QtWidgets.QLabel(boardForm)
        self.playerOneCard_10.setGeometry(QtCore.QRect(590, 160, 131, 171))
        self.playerOneCard_10.setStyleSheet("")
        self.playerOneCard_10.setText("")
        self.playerOneCard_10.setObjectName("playerOneCard_10")
        self.playerTwoCard_2 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_2.setGeometry(QtCore.QRect(350, 490, 131, 171))
        self.playerTwoCard_2.setStyleSheet(self.path)
        self.playerTwoCard_2.setText("")
        self.playerTwoCard_2.setObjectName("playerTwoCard_2")
        self.playerTwoCard_3 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_3.setGeometry(QtCore.QRect(380, 490, 131, 171))
        self.playerTwoCard_3.setStyleSheet("")
        self.playerTwoCard_3.setText("")
        self.playerTwoCard_3.setObjectName("playerTwoCard_3")
        self.playerTwoCard_4 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_4.setGeometry(QtCore.QRect(410, 490, 131, 171))
        self.playerTwoCard_4.setStyleSheet("")
        self.playerTwoCard_4.setText("")
        self.playerTwoCard_4.setObjectName("playerTwoCard_4")
        self.playerTwoCard_5 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_5.setGeometry(QtCore.QRect(440, 490, 131, 171))
        self.playerTwoCard_5.setStyleSheet("")
        self.playerTwoCard_5.setText("")
        self.playerTwoCard_5.setObjectName("playerTwoCard_5")
        self.playerTwoCard_6 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_6.setGeometry(QtCore.QRect(470, 490, 131, 171))
        self.playerTwoCard_6.setStyleSheet("")
        self.playerTwoCard_6.setText("")
        self.playerTwoCard_6.setObjectName("playerTwoCard_6")
        self.playerTwoCard_7 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_7.setGeometry(QtCore.QRect(500, 490, 131, 171))
        self.playerTwoCard_7.setStyleSheet("")
        self.playerTwoCard_7.setText("")
        self.playerTwoCard_7.setObjectName("playerTwoCard_7")
        self.playerTwoCard_8 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_8.setGeometry(QtCore.QRect(530, 490, 131, 171))
        self.playerTwoCard_8.setStyleSheet("")
        self.playerTwoCard_8.setText("")
        self.playerTwoCard_8.setObjectName("playerTwoCard_8")
        self.playerTwoCard_9 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_9.setGeometry(QtCore.QRect(560, 490, 131, 171))
        self.playerTwoCard_9.setStyleSheet("")
        self.playerTwoCard_9.setText("")
        self.playerTwoCard_9.setObjectName("playerTwoCard_9")
        self.playerTwoCard_10 = QtWidgets.QLabel(boardForm)
        self.playerTwoCard_10.setGeometry(QtCore.QRect(590, 490, 131, 171))
        self.playerTwoCard_10.setStyleSheet("")
        self.playerTwoCard_10.setText("")
        self.playerTwoCard_10.setObjectName("playerTwoCard_10")
        self.playerThreeCard_2 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_2.setGeometry(QtCore.QRect(860, 160, 131, 171))
        self.playerThreeCard_2.setStyleSheet(self.path)
        self.playerThreeCard_2.setText("")
        self.playerThreeCard_2.setObjectName("playerThreeCard_2")
        self.playerThreeCard_3 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_3.setGeometry(QtCore.QRect(890, 160, 131, 171))
        self.playerThreeCard_3.setStyleSheet("")
        self.playerThreeCard_3.setText("")
        self.playerThreeCard_3.setObjectName("playerThreeCard_3")
        self.playerThreeCard_4 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_4.setGeometry(QtCore.QRect(920, 160, 131, 171))
        self.playerThreeCard_4.setStyleSheet("")
        self.playerThreeCard_4.setText("")
        self.playerThreeCard_4.setObjectName("playerThreeCard_4")
        self.playerThreeCard_5 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_5.setGeometry(QtCore.QRect(950, 160, 131, 171))
        self.playerThreeCard_5.setStyleSheet("image: url(:/images/6_of_clubs.png);")
        self.playerThreeCard_5.setText("")
        self.playerThreeCard_5.setObjectName("playerThreeCard_5")
        self.playerThreeCard_6 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_6.setGeometry(QtCore.QRect(980, 160, 131, 171))
        self.playerThreeCard_6.setStyleSheet("")
        self.playerThreeCard_6.setText("")
        self.playerThreeCard_6.setObjectName("playerThreeCard_6")
        self.playerThreeCard_7 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_7.setGeometry(QtCore.QRect(1010, 160, 131, 171))
        self.playerThreeCard_7.setStyleSheet("")
        self.playerThreeCard_7.setText("")
        self.playerThreeCard_7.setObjectName("playerThreeCard_7")
        self.playerThreeCard_8 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_8.setGeometry(QtCore.QRect(1040, 160, 131, 171))
        self.playerThreeCard_8.setStyleSheet("")
        self.playerThreeCard_8.setText("")
        self.playerThreeCard_8.setObjectName("playerThreeCard_8")
        self.playerThreeCard_9 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_9.setGeometry(QtCore.QRect(1070, 160, 131, 171))
        self.playerThreeCard_9.setStyleSheet("")
        self.playerThreeCard_9.setText("")
        self.playerThreeCard_9.setObjectName("playerThreeCard_9")
        self.playerThreeCard_10 = QtWidgets.QLabel(boardForm)
        self.playerThreeCard_10.setGeometry(QtCore.QRect(1100, 160, 131, 171))
        self.playerThreeCard_10.setStyleSheet("")
        self.playerThreeCard_10.setText("")
        self.playerThreeCard_10.setObjectName("playerThreeCard_10")
        self.playerFourCard_1 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_1.setGeometry(QtCore.QRect(830, 490, 131, 171))
        self.playerFourCard_1.setStyleSheet(self.path)
        self.playerFourCard_1.setText("")
        self.playerFourCard_1.setObjectName("playerFourCard_1")
        self.playerFourCard_2 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_2.setGeometry(QtCore.QRect(860, 490, 131, 171))
        self.playerFourCard_2.setStyleSheet(self.path)
        self.playerFourCard_2.setText("")
        self.playerFourCard_2.setObjectName("playerFourCard_2")
        self.playerFourCard_3 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_3.setGeometry(QtCore.QRect(890, 490, 131, 171))
        self.playerFourCard_3.setStyleSheet("")
        self.playerFourCard_3.setText("")
        self.playerFourCard_3.setObjectName("playerFourCard_3")
        self.playerFourCard_4 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_4.setGeometry(QtCore.QRect(920, 490, 131, 171))
        self.playerFourCard_4.setStyleSheet("")
        self.playerFourCard_4.setText("")
        self.playerFourCard_4.setObjectName("playerFourCard_4")
        self.playerFourCard_5 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_5.setGeometry(QtCore.QRect(950, 490, 131, 171))
        self.playerFourCard_5.setStyleSheet("")
        self.playerFourCard_5.setText("")
        self.playerFourCard_5.setObjectName("playerFourCard_5")
        self.playerFourCard_6 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_6.setGeometry(QtCore.QRect(980, 490, 131, 171))
        self.playerFourCard_6.setStyleSheet("")
        self.playerFourCard_6.setText("")
        self.playerFourCard_6.setObjectName("playerFourCard_6")
        self.playerFourCard_7 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_7.setGeometry(QtCore.QRect(1010, 490, 131, 171))
        self.playerFourCard_7.setStyleSheet("")
        self.playerFourCard_7.setText("")
        self.playerFourCard_7.setObjectName("playerFourCard_7")
        self.playerFourCard_8 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_8.setGeometry(QtCore.QRect(1040, 490, 131, 171))
        self.playerFourCard_8.setStyleSheet("")
        self.playerFourCard_8.setText("")
        self.playerFourCard_8.setObjectName("playerFourCard_8")
        self.playerFourCard_9 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_9.setGeometry(QtCore.QRect(1070, 490, 131, 171))
        self.playerFourCard_9.setStyleSheet("")
        self.playerFourCard_9.setText("")
        self.playerFourCard_9.setObjectName("playerFourCard_9")
        self.playerFourCard_10 = QtWidgets.QLabel(boardForm)
        self.playerFourCard_10.setGeometry(QtCore.QRect(1100, 490, 131, 171))
        self.playerFourCard_10.setStyleSheet("")
        self.playerFourCard_10.setText("")
        self.playerFourCard_10.setObjectName("playerFourCard_10")
        self.returnIcon = QtWidgets.QLabel(boardForm)
        self.returnIcon.setGeometry(QtCore.QRect(50, 10, 31, 31))
        self.returnIcon.setStyleSheet("border-image: url(:/images/return.png);")
        self.returnIcon.setText("")
        self.returnIcon.setObjectName("returnIcon")
        self.returnButton = QtWidgets.QPushButton(boardForm)
        self.returnButton.setGeometry(QtCore.QRect(50, 10, 31, 31))
        self.returnButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.returnButton.setText("")
        self.returnButton.setObjectName("returnButton")
        self.closeLabel = QtWidgets.QLabel(boardForm)
        self.closeLabel.setGeometry(QtCore.QRect(20, 4, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.closeLabel.setFont(font)
        self.closeLabel.setStyleSheet("color: rgb(255, 170, 0);")
        self.closeLabel.setObjectName("closeLabel")
        self.closeButton = QtWidgets.QPushButton(boardForm)
        self.closeButton.setGeometry(QtCore.QRect(20, 10, 21, 31))
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.playerOnePoints = QtWidgets.QLabel(boardForm)
        self.playerOnePoints.setGeometry(QtCore.QRect(330, 70, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.playerOnePoints.setFont(font)
        self.playerOnePoints.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerOnePoints.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerOnePoints.setObjectName("playerOnePoints")
        self.playerTwoPoints = QtWidgets.QLabel(boardForm)
        self.playerTwoPoints.setGeometry(QtCore.QRect(330, 400, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.playerTwoPoints.setFont(font)
        self.playerTwoPoints.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerTwoPoints.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerTwoPoints.setObjectName("playerTwoPoints")
        self.playerThreePoints = QtWidgets.QLabel(boardForm)
        self.playerThreePoints.setGeometry(QtCore.QRect(840, 70, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.playerThreePoints.setFont(font)
        self.playerThreePoints.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerThreePoints.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerThreePoints.setObjectName("playerThreePoints")
        self.playerFourPoints = QtWidgets.QLabel(boardForm)
        self.playerFourPoints.setGeometry(QtCore.QRect(840, 400, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.playerFourPoints.setFont(font)
        self.playerFourPoints.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerFourPoints.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.playerFourPoints.setObjectName("playerTwoPoints_2")

        # Obsługa języków

        if self.language == 1:
            self.standButton.setStyleSheet("image: url(:/images/stand.png);\n"
                                           "border: 0px;")
            self.hitButton.setStyleSheet("image: url(:/images/hit.png);\n"
                                         "border: 0px;")
            self.timeLeftIcon.setStyleSheet("image: url(:/images/timeLeft.png);")
            self.balanceText.setStyleSheet("image: url(:/images/balance.png);")
            self.toWinLabel.setStyleSheet("image: url(:/images/PRAJZ.png);")
            self.timeLeftIcon.setGeometry(QtCore.QRect(1500, 160, 201, 71))
        if self.language == 2:
            self.standButton.setStyleSheet("image: url(:/images/standPL.png);\n"
                                           "border: 0px;")
            self.hitButton.setStyleSheet("image: url(:/images/hitPL.png);\n"
                                         "border: 0px;")
            self.timeLeftIcon.setStyleSheet("image: url(:/images/timeLeftPL.png);")
            self.balanceText.setStyleSheet("image: url(:/images/balancePL.png);")
            self.toWinLabel.setStyleSheet("image: url(:/images/totalBetPL.jpg);")
            self.timeLeftIcon.setGeometry(QtCore.QRect(1492, 160, 201, 71))

        self.backgroundDark.raise_()
        self.playerOneCard_1.raise_()
        self.playerOneLabel.raise_()
        self.menuStripe.raise_()
        self.timeLeftIcon.raise_()
        self.hitButton.raise_()
        self.standButton.raise_()
        self.walletIcon.raise_()
        self.logoLabel.raise_()
        self.balanceText.raise_()
        self.balanceLabel.raise_()
        self.timerLabel.raise_()
        self.toWinLabel.raise_()
        self.coinsIcon.raise_()
        self.prizeLabel.raise_()

        self.playerTwoLabel.raise_()
        self.playerThreeCard_1.raise_()
        self.playerThreeLabel.raise_()
        self.playerFourLabel.raise_()

        self.playerOneCard_1.raise_()
        self.playerOneCard_2.raise_()
        self.playerOneCard_3.raise_()
        self.playerOneCard_4.raise_()
        self.playerOneCard_5.raise_()
        self.playerOneCard_6.raise_()
        self.playerOneCard_7.raise_()
        self.playerOneCard_8.raise_()
        self.playerOneCard_9.raise_()
        self.playerOneCard_10.raise_()

        self.playerTwoCard_1.raise_()
        self.playerTwoCard_2.raise_()
        self.playerTwoCard_3.raise_()
        self.playerTwoCard_4.raise_()
        self.playerTwoCard_5.raise_()
        self.playerTwoCard_6.raise_()
        self.playerTwoCard_7.raise_()
        self.playerTwoCard_8.raise_()
        self.playerTwoCard_9.raise_()
        self.playerTwoCard_10.raise_()

        self.playerThreeCard_2.raise_()
        self.playerThreeCard_3.raise_()
        self.playerThreeCard_4.raise_()
        self.playerThreeCard_5.raise_()
        self.playerThreeCard_6.raise_()
        self.playerThreeCard_7.raise_()
        self.playerThreeCard_8.raise_()
        self.playerThreeCard_9.raise_()
        self.playerThreeCard_10.raise_()

        self.playerFourCard_1.raise_()
        self.playerFourCard_2.raise_()
        self.playerFourCard_3.raise_()
        self.playerFourCard_4.raise_()
        self.playerFourCard_5.raise_()
        self.playerFourCard_6.raise_()
        self.playerFourCard_7.raise_()
        self.playerFourCard_8.raise_()
        self.playerFourCard_9.raise_()
        self.playerFourCard_10.raise_()
        self.returnIcon.raise_()
        self.returnButton.raise_()
        self.closeLabel.raise_()
        self.closeButton.raise_()

        self.playerOnePoints.raise_()
        self.playerTwoPoints.raise_()
        self.playerThreePoints.raise_()
        self.playerFourPoints.raise_()

        self.retranslateUi(boardForm)
        QtCore.QMetaObject.connectSlotsByName(boardForm)

        self.closeButton.clicked.connect(boardForm.close)
        self.closeButton.clicked.connect(self.returnToMenu)

        self.returnButton.clicked.connect(boardForm.close)
        self.returnButton.clicked.connect(self.returnToUsers)
        self.hitButton.clicked.connect(self.hit)
        self.standButton.clicked.connect(self.stand)

        self.board = boardForm

        if self.betting == 0:
            self.prizeLabel.setVisible(False)
            self.toWinLabel.setVisible(False)
            self.coinsIcon.setVisible(False)
            self.prizeLabel.setVisible(False)
            self.walletIcon.setVisible(False)
            self.balanceText.setVisible(False)
            self.balanceLabel.setVisible(False)
        elif self.betting == 1:
            total_bet = int(self.input * len(self.numberOfPlayer))
            self.prizeLabel.setText(str(total_bet))

        player_number_aux = 0
        self.boardLabels = BoardLabels(self)
        self.players = []

        for i in range(1, self.playersNumber + 1):
            self.get_player_label(i).setText(self.set_username(i))
            self.players.append(Player(self.set_username(i), "player", i, self.boardLabels.labels[player_number_aux]))
            player_number_aux += 1

        for i in range(1, self.computersNumber + 1):
            name, type = self.set_computer_data(self.get_computer_level(i))
            self.get_player_label(self.playersNumber + i).setText(name)
            self.players.append(Player(name, type, self.playersNumber + i, self.boardLabels.labels[player_number_aux]))
            player_number_aux += 1


        # if (1 in self.numberOfPlayer) is True:
        #     self.playerOneLabel.setText(self.set_username(1))
        #     self.players.append(Player(self.set_username(1), "player", 1, self.boardLabels.labels[player_number_aux]))
        #     player_number_aux += 1
        #     # self.playerOneWallet.setText(str(self.set_wallet(1)))
        # if (2 in self.numberOfPlayer) is True:
        #     self.playerTwoLabel.setText(self.set_username(2))
        #     self.players.append(Player(self.set_username(2), "player", 2, self.boardLabels.labels[player_number_aux]))
        #     player_number_aux += 1
        #     # self.playerTwoWallet.setText(str(self.set_wallet(2)))
        # if (3 in self.numberOfPlayer) is True:
        #     self.playerThreeLabel.setText(self.set_username(3))
        #     self.players.append(Player(self.set_username(3), "player", 3, self.boardLabels.labels[player_number_aux]))
        #     player_number_aux += 1
        #     # self.playerThreeWallet.setText(str(self.set_wallet(3)))
        # if (4 in self.numberOfPlayer) is True:
        #     self.playerFourLabel.setText(self.set_username(4))
        #     self.players.append(Player(self.set_username(4), "player", 4, self.boardLabels.labels[player_number_aux]))
        #     player_number_aux += 1
        #     # self.playerFourWallet.setText(str(self.set_wallet(4)))

        # if (1 in self.computersNumber) is True:
        #     name, type = self.set_computer_data()
        #     self.playerOneLabel.setText(name)
        #     self.players.append(Player(name, type, self.playersNumber + 1, self.boardLabels.labels[player_number_aux]))
        #     player_number_aux += 1
        # if (2 in self.computersNumber) is True:
        #     name, type = self.set_computer_data()
        #     self.playerTwoLabel.setText(name)
        #     self.players.append(Player(name, type, self.playersNumber + 2, self.boardLabels.labels[player_number_aux]))
        #     player_number_aux += 1
        # if (3 in self.computersNumber) is True:
        #     name, type = self.set_computer_data()
        #     self.playerThreeLabel.setText(name)
        #     self.players.append(Player(name, type, self.playersNumber + 3, self.boardLabels.labels[player_number_aux]))
        #     player_number_aux += 1
        # if (4 in self.computersNumber) is True:
        #     name, type = self.set_computer_data()
        #     self.playerFourLabel.setText(name)
        #     self.players.append(Player(name, type, self.playersNumber + 4, self.boardLabels.labels[player_number_aux]))
        #     player_number_aux += 1

        self.frontend_logic = FrontendLogic(self)
        self.frontend_logic.start_game()

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_time)  # execute `display_time`
        self.timer.start()
        self.timer.setInterval(200)
        self.start_time = time.time()

        self.closeButton.clicked.connect(self.timer.stop)
        self.returnButton.clicked.connect(self.timer.stop)

        # # dodanie graczy do planszy
        # # players.append(Player("*name*", "*type*", *player_number*)) type reference in ..Blackjack.player Player class
        # player = Player ("XXD", "XXD ", 1)


        # Ustawianie kart w zaleznosci od ilosci graczy
        if self.playersNumber + self.computersNumber == 2:

            self.playerOneLabel.setGeometry(QtCore.QRect(680, 100, 271, 31))
            self.playerOneCard_1.setGeometry(QtCore.QRect(670, 160, 131, 171))
            self.playerOneCard_2.setGeometry(QtCore.QRect(700, 160, 131, 171))
            self.playerOneCard_3.setGeometry(QtCore.QRect(730, 160, 131, 171))
            self.playerOneCard_4.setGeometry(QtCore.QRect(760, 160, 131, 171))
            self.playerOneCard_5.setGeometry(QtCore.QRect(790, 160, 131, 171))
            self.playerOneCard_6.setGeometry(QtCore.QRect(820, 160, 131, 171))
            self.playerOneCard_7.setGeometry(QtCore.QRect(850, 160, 131, 171))
            self.playerOneCard_8.setGeometry(QtCore.QRect(880, 160, 131, 171))
            self.playerOneCard_9.setGeometry(QtCore.QRect(910, 160, 131, 171))
            self.playerOneCard_10.setGeometry(QtCore.QRect(940, 160, 131, 171))
            self.playerOnePoints.setGeometry(QtCore.QRect(680, 70, 271, 31))

            self.playerTwoLabel.setGeometry(QtCore.QRect(680, 430, 271, 31))
            self.playerTwoCard_1.setGeometry(QtCore.QRect(670, 490, 131, 171))
            self.playerTwoCard_2.setGeometry(QtCore.QRect(700, 490, 131, 171))
            self.playerTwoCard_3.setGeometry(QtCore.QRect(730, 490, 131, 171))
            self.playerTwoCard_4.setGeometry(QtCore.QRect(760, 490, 131, 171))
            self.playerTwoCard_5.setGeometry(QtCore.QRect(790, 490, 131, 171))
            self.playerTwoCard_6.setGeometry(QtCore.QRect(820, 490, 131, 171))
            self.playerTwoCard_7.setGeometry(QtCore.QRect(850, 490, 131, 171))
            self.playerTwoCard_8.setGeometry(QtCore.QRect(880, 490, 131, 171))
            self.playerTwoCard_9.setGeometry(QtCore.QRect(910, 490, 131, 171))
            self.playerTwoCard_10.setGeometry(QtCore.QRect(940, 490, 131, 171))
            self.playerTwoPoints.setGeometry(QtCore.QRect(680, 400, 271, 31))

            self.playerThreeCard_1.setStyleSheet("")
            self.playerThreeCard_2.setStyleSheet("")
            self.playerThreeCard_3.setStyleSheet("")
            self.playerThreeCard_4.setStyleSheet("")
            self.playerThreeCard_5.setStyleSheet("")
            self.playerThreeCard_6.setStyleSheet("")
            self.playerThreeCard_7.setStyleSheet("")
            self.playerThreeCard_8.setStyleSheet("")
            self.playerThreeCard_9.setStyleSheet("")
            self.playerThreeCard_10.setStyleSheet("")

            self.playerFourCard_1.setStyleSheet("")
            self.playerFourCard_2.setStyleSheet("")
            self.playerFourCard_3.setStyleSheet("")
            self.playerFourCard_4.setStyleSheet("")
            self.playerFourCard_5.setStyleSheet("")
            self.playerFourCard_6.setStyleSheet("")
            self.playerFourCard_7.setStyleSheet("")
            self.playerFourCard_8.setStyleSheet("")
            self.playerFourCard_9.setStyleSheet("")
            self.playerFourCard_10.setStyleSheet("")

        elif self.playersNumber + self.computersNumber == 3:
            self.playerFourCard_1.setStyleSheet("")
            self.playerFourCard_2.setStyleSheet("")
            self.playerFourCard_3.setStyleSheet("")
            self.playerFourCard_4.setStyleSheet("")
            self.playerFourCard_5.setStyleSheet("")
            self.playerFourCard_6.setStyleSheet("")
            self.playerFourCard_7.setStyleSheet("")
            self.playerFourCard_8.setStyleSheet("")
            self.playerFourCard_9.setStyleSheet("")
            self.playerFourCard_10.setStyleSheet("")

    def display_time(self):
        if self.frontend_logic.current_player.type != "player":
            self.timer.stop()
            self.hitButton.setEnabled(False)
            self.standButton.setEnabled(False)
            QtCore.QTimer.singleShot(1000, self.frontend_logic.decision_ai)

        else:
            if int(time.time() - self.start_time) <= self.time:
                self.current_time = int(time.time() - self.start_time)
                self.timerLabel.setText(str(self.time - self.current_time))

            else:
                self.frontend_logic.clicked_stand()

    def change_player(self):
        self.timer.stop()
        self.hitButton.setEnabled(False)
        self.standButton.setEnabled(False)
        self.window = QtWidgets.QMainWindow()
        self.ui = playerChange.changeForm(self)
        self.ui.setupUi(self.window)
        self.window.show()
        if self.frontend_logic.current_player.type != "player":
            QtCore.QTimer.singleShot(1500, self.close_window_for_ai)

    def close_window_for_ai(self):
        self.window.close()
        self.reset_timer()
        self.timer.start()
        self.show_user_points()

    def reset_timer(self):
        self.start_time = time.time()

    def hit(self):
        self.hitButton.setEnabled(False)
        self.standButton.setEnabled(False)
        self.frontend_logic.clicked_hit()

    def stand(self):
        self.hitButton.setEnabled(False)
        self.standButton.setEnabled(False)
        self.frontend_logic.clicked_stand()

    def enable_buttons(self):
        self.hitButton.setEnabled(True)
        self.standButton.setEnabled(True)

    def round_over(self):
        print("round over")
        self.game_ends()

    def game_ends(self):
        self.timer.stop()
        self.window = QtWidgets.QMainWindow()
        self.ui = summary.summaryForm(self)
        self.ui.setupUi(self.window)
        self.window.show()
        self.board.close()

    def show_user_points(self):
        if self.frontend_logic.current_player_index == 0:
            self.playerOnePoints.setText(str(self.frontend_logic.current_player.hand.value))
            self.playerTwoPoints.setText("")
            self.playerThreePoints.setText("")
            self.playerOnePoints.setText("")

        elif self.frontend_logic.current_player_index == 1:
            self.playerOnePoints.setText("")
            self.playerTwoPoints.setText(str(self.frontend_logic.current_player.hand.value))
            self.playerThreePoints.setText("")
            self.playerOnePoints.setText("")


        elif self.frontend_logic.current_player_index == 2:
            self.playerOnePoints.setText("")
            self.playerTwoPoints.setText("")
            self.playerThreePoints.setText(str(self.frontend_logic.current_player.hand.value))
            self.playerOnePoints.setText("")


        elif self.frontend_logic.current_player_index == 3:
            self.playerOnePoints.setText("")
            self.playerTwoPoints.setText("")
            self.playerThreePoints.setText("")
            self.playerOnePoints.setText(str(self.frontend_logic.current_player.hand.value))

    def get_player_label(self, player_number):
        if player_number == 1:
            return self.playerOneLabel

        elif player_number == 2:
            return self.playerTwoLabel

        elif player_number == 3:
            return self.playerThreeLabel

        elif player_number == 4:
            return self.playerFourLabel

    def get_computer_level(self, computerNumber):
        if computerNumber == 1:
            return self.computerOneLevel

        elif computerNumber == 2:
            return self.computerTwoLevel

        elif computerNumber == 3:
            return self.computerThreeLevel

        elif computerNumber == 4:
            return self.computerFourLevel

    def set_computer_data(self, level):
        if level == 1:
            name = "Computer Easy"
            type = "ceasy"

        elif level == 2:
            name = "Computer Medium"
            type = "cmedium"

        elif level == 3:
            name = "Computer Hard"
            type = "chard"

        return name, type

    def set_username(self, user_id):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "SELECT id, username, coins from logged_users where id = {}".format(user_id)
            c.execute(query)
            db.commit()
            result = c.fetchone()
            print(result[1])
            return result[1]

        except sql.Error as e:
            print("huj")

    def returnToMenu(self):
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
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    def returnToUsers(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = playUsers.usersForm(self.language, self.playersNumber, self.computersNumber, self.betting)
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, boardForm):
        _translate = QtCore.QCoreApplication.translate
        boardForm.setWindowTitle(_translate("boardForm", "Board"))
        self.closeLabel.setText(_translate("boardForm", "X"))
