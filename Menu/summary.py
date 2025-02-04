# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summary.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import board
import replayBoard
import menu
import gameHistory
import sqlite3 as sql


class summaryForm(object):
    def __init__(self, board):
        self.board = board
        self.language = board.language

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 458)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundLabel = QtWidgets.QLabel(Form)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 581, 381))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.winnerNickname = QtWidgets.QLabel(Form)
        self.winnerNickname.setGeometry(QtCore.QRect(50, -30, 471, 141))
        font = QtGui.QFont()
        font.setPointSize(33)
        font.setBold(True)
        self.winnerNickname.setFont(font)
        self.winnerNickname.setStyleSheet("color: rgb(255, 67, 46);")
        self.winnerNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.winnerNickname.setObjectName("winnerNickname")
        self.playerOneNickname = QtWidgets.QLabel(Form)
        self.playerOneNickname.setGeometry(QtCore.QRect(110, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.playerOneNickname.setFont(font)
        self.playerOneNickname.setStyleSheet("color: rgb(48, 94, 66);")
        self.playerOneNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.playerOneNickname.setObjectName("playerOneNickname")
        self.playerThreeNickname = QtWidgets.QLabel(Form)
        self.playerThreeNickname.setGeometry(QtCore.QRect(300, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.playerThreeNickname.setFont(font)
        self.playerThreeNickname.setStyleSheet("color: rgb(48, 94, 66);")
        self.playerThreeNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.playerThreeNickname.setObjectName("playerThreeNickname")
        self.playerTwoNickname = QtWidgets.QLabel(Form)
        self.playerTwoNickname.setGeometry(QtCore.QRect(110, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.playerTwoNickname.setFont(font)
        self.playerTwoNickname.setStyleSheet("color: rgb(48, 94, 66);")
        self.playerTwoNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.playerTwoNickname.setObjectName("playerTwoNickname")
        self.playerFourNickname = QtWidgets.QLabel(Form)
        self.playerFourNickname.setGeometry(QtCore.QRect(300, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.playerFourNickname.setFont(font)
        self.playerFourNickname.setStyleSheet("color: rgb(48, 94, 66);")
        self.playerFourNickname.setAlignment(QtCore.Qt.AlignCenter)
        self.playerFourNickname.setObjectName("playerFourNickname")
        self.playerOnePoints = QtWidgets.QLabel(Form)
        self.playerOnePoints.setGeometry(QtCore.QRect(130, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.playerOnePoints.setFont(font)
        self.playerOnePoints.setStyleSheet("color: rgb(48, 94, 66);")
        self.playerOnePoints.setAlignment(QtCore.Qt.AlignCenter)
        self.playerOnePoints.setObjectName("playerOnePoints")
        self.playerTwoPoints = QtWidgets.QLabel(Form)
        self.playerTwoPoints.setGeometry(QtCore.QRect(130, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.playerTwoPoints.setFont(font)
        self.playerTwoPoints.setStyleSheet("color: rgb(48, 94, 66);")
        self.playerTwoPoints.setAlignment(QtCore.Qt.AlignCenter)
        self.playerTwoPoints.setObjectName("playerTwoPoints")
        self.playerThreePoints = QtWidgets.QLabel(Form)
        self.playerThreePoints.setGeometry(QtCore.QRect(322, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.playerThreePoints.setFont(font)
        self.playerThreePoints.setStyleSheet("color: rgb(48, 94, 66);")
        self.playerThreePoints.setAlignment(QtCore.Qt.AlignCenter)
        self.playerThreePoints.setObjectName("playerThreePoints")
        self.playerFourPoints = QtWidgets.QLabel(Form)
        self.playerFourPoints.setGeometry(QtCore.QRect(320, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.playerFourPoints.setFont(font)
        self.playerFourPoints.setStyleSheet("color: rgb(48, 94, 66);")
        self.playerFourPoints.setAlignment(QtCore.Qt.AlignCenter)
        self.playerFourPoints.setObjectName("playerFourPoints")
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(90, 290, 121, 51))
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
"QPushButton#playButton:pressed{\n"
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
        self.replayButton = QtWidgets.QPushButton(Form)
        self.replayButton.setGeometry(QtCore.QRect(240, 290, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.replayButton.setFont(font)
        self.replayButton.setStyleSheet("QPushButton#replayButton{\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 104, 3);\n"
"    border-radius: 45px;\n"
"}\n"
"\n"
"QPushButton#replayButton:pressed{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"    background-color: rgb(255, 206, 12);\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"\n"
"QPushButton#replayButton:hover{\n"
"    background-color: rgb(255, 206, 12);\n"
"}\n"
"")
        self.replayButton.setObjectName("replayButton")
        self.backButton = QtWidgets.QPushButton(Form)
        self.backButton.setGeometry(QtCore.QRect(390, 290, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("QPushButton#backButton{\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 104, 3);\n"
"    border-radius: 45px;\n"
"}\n"
"\n"
"QPushButton#backButton:pressed{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"    background-color: rgb(255, 206, 12);\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"\n"
"QPushButton#backButton:hover{\n"
"    background-color: rgb(255, 206, 12);\n"
"}\n"
"")
        self.backButton.setObjectName("backButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        if self.board.replay_bool is True:
            self.replayButton.setVisible(False)
            if self.language == 1:
                self.playButton.setText("HISTORY")
            elif self.language == 2:
                self.playButton.setText("HISTORIA")

            self.playButton.clicked.connect(self.play_replay_again)

        else:
            self.playButton.clicked.connect(self.play_again)
            try:
                db = sql.connect('database.db')  # łączymy się do bazy
                c = db.cursor()  # dodajemy kursor

                query = "DELETE FROM logged_users"
                c.execute(query)
                c.execute("UPDATE levels SET level = 0")
                db.commit()

            except sql.Error as e:
                print("error")


        self.playButton.clicked.connect(Form.close)
        self.replayButton.clicked.connect(self.history)
        self.replayButton.clicked.connect(Form.close)
        self.backButton.clicked.connect(self.return_to_menu)
        self.backButton.clicked.connect(Form.close)

        if len(self.board.frontend_logic.winners) > 1 or len(self.board.frontend_logic.winners) == 0:
            self.winnerNickname.setVisible(False)
            if self.language == 1:
                self.backgroundLabel.setStyleSheet("image: url(:/images/summaryTieBackground.png);")
            if self.language == 2:
                self.backgroundLabel.setStyleSheet("image: url(:/images/summaryTieBackgroundPL.png);")

        else:
            self.winnerNickname.setText(self.board.frontend_logic.winners[0].name)
            # Obsługa języków
            if self.language == 1:
                self.backgroundLabel.setStyleSheet("image: url(:/images/summaryBackground.png);")
            if self.language == 2:
                self.backgroundLabel.setStyleSheet("image: url(:/images/summaryBackgroundPL.png);")

        self.number_of_players = len(self.board.players)

        for i in range(1,  + self.number_of_players + 1):
            self.get_player_label(i).setText(self.board.players[i - 1].name)
            self.get_value_label(i).setText(str(self.board.players[i - 1].hand.value))

        # Ustawianie kart w zaleznosci od ilosci graczy
        if self.number_of_players == 2:
            self.playerOneNickname.setGeometry(QtCore.QRect(200, 140, 171, 31))
            self.playerTwoNickname.setGeometry(QtCore.QRect(200, 200, 171, 31))
            self.playerOnePoints.setGeometry(QtCore.QRect(210, 170, 151, 31))
            self.playerTwoPoints.setGeometry(QtCore.QRect(210, 230, 151, 31))
        elif self.number_of_players == 3:
            self.playerOneNickname.setGeometry(QtCore.QRect(110, 140, 171, 31))
            self.playerTwoNickname.setGeometry(QtCore.QRect(210, 200, 171, 31))
            self.playerThreeNickname.setGeometry(QtCore.QRect(310, 140, 171, 31))
            self.playerOnePoints.setGeometry(QtCore.QRect(120, 170, 151, 31))
            self.playerTwoPoints.setGeometry(QtCore.QRect(220, 230, 151, 31))
            self.playerThreePoints.setGeometry(QtCore.QRect(320, 170, 151, 31))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # Obsługa języków
        if self.language == 1:
            self.playButton.setText(_translate("Form", "PLAY AGAIN"))
            self.replayButton.setText(_translate("Form", "REPLAY"))
            self.backButton.setText(_translate("Form", "MENU"))
        if self.language == 2:
            self.playButton.setText(_translate("Form", "GRAJ DALEJ"))
            self.replayButton.setText(_translate("Form", "ODWTÓRZ"))
            self.backButton.setText(_translate("Form", "MENU"))

        self.winnerNickname.setText(_translate("Form", ""))
        self.playerOneNickname.setText(_translate("Form", ""))
        self.playerThreeNickname.setText(_translate("Form", ""))
        self.playerTwoNickname.setText(_translate("Form", ""))
        self.playerFourNickname.setText(_translate("Form", ""))
        self.playerOnePoints.setText(_translate("Form", ""))
        self.playerTwoPoints.setText(_translate("Form", ""))
        self.playerThreePoints.setText(_translate("Form", ""))
        self.playerFourPoints.setText(_translate("Form", ""))

    def play_again(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = board.boardForm(self.board.language, self.board.playersNumber, self.board.computersNumber, self.board.betting,
                                  self.board.numberOfPlayer, self.board.gameLevel, self.board.computerOneLevel, self.board.computerTwoLevel, 
                                  self.board.computerThreeLevel, self.board.computerFourLevel, self.board.input, False)
        self.ui.setupUi(self.window)
        self.window.show()

    def play_replay_again(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = gameHistory.historyForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    def history(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = gameHistory.historyForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    def return_to_menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    def get_player_label(self, player_number):
        if player_number == 1:
            return self.playerOneNickname

        elif player_number == 2:
            return self.playerTwoNickname

        elif player_number == 3:
            return self.playerThreeNickname

        elif player_number == 4:
            return self.playerFourNickname

    def get_value_label(self, player_number):
        if player_number == 1:
            return self.playerOnePoints

        elif player_number == 2:
            return self.playerTwoPoints

        elif player_number == 3:
            return self.playerThreePoints

        elif player_number == 4:
            return self.playerFourPoints
