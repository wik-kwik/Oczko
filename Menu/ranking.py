# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ranking.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import menu
import sqlite3 as sql


class rankingForm(object):
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
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(880, 0, 21, 21))
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.playerOneNickname = QtWidgets.QLabel(Form)
        self.playerOneNickname.setGeometry(QtCore.QRect(180, 115, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.playerOneNickname.setFont(font)
        self.playerOneNickname.setStyleSheet("color: rgb(242, 111, 31);")
        self.playerOneNickname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playerOneNickname.setObjectName("playerOneNickname")
        self.playerOneWinrate = QtWidgets.QLabel(Form)
        self.playerOneWinrate.setGeometry(QtCore.QRect(449, 115, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.playerOneWinrate.setFont(font)
        self.playerOneWinrate.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerOneWinrate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerOneWinrate.setObjectName("playerOneWinrate")
        self.playerTwoNickname = QtWidgets.QLabel(Form)
        self.playerTwoNickname.setGeometry(QtCore.QRect(190, 150, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.playerTwoNickname.setFont(font)
        self.playerTwoNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerTwoNickname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playerTwoNickname.setObjectName("playerTwoNickname")
        self.playerTwoWinrate = QtWidgets.QLabel(Form)
        self.playerTwoWinrate.setGeometry(QtCore.QRect(440, 150, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.playerTwoWinrate.setFont(font)
        self.playerTwoWinrate.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerTwoWinrate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerTwoWinrate.setObjectName("playerTwoWinrate")
        self.playerThreeNickname = QtWidgets.QLabel(Form)
        self.playerThreeNickname.setGeometry(QtCore.QRect(190, 176, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.playerThreeNickname.setFont(font)
        self.playerThreeNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerThreeNickname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playerThreeNickname.setObjectName("playerThreeNickname")
        self.playerFourNickname = QtWidgets.QLabel(Form)
        self.playerFourNickname.setGeometry(QtCore.QRect(190, 203, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.playerFourNickname.setFont(font)
        self.playerFourNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerFourNickname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playerFourNickname.setObjectName("playerFourNickname")
        self.playerFiveNickname = QtWidgets.QLabel(Form)
        self.playerFiveNickname.setGeometry(QtCore.QRect(190, 230, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.playerFiveNickname.setFont(font)
        self.playerFiveNickname.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerFiveNickname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.playerFiveNickname.setObjectName("playerFiveNickname")
        self.playerThreeWinrate = QtWidgets.QLabel(Form)
        self.playerThreeWinrate.setGeometry(QtCore.QRect(440, 176, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.playerThreeWinrate.setFont(font)
        self.playerThreeWinrate.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerThreeWinrate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerThreeWinrate.setObjectName("playerThreeWinrate")
        self.playerFourWinrate = QtWidgets.QLabel(Form)
        self.playerFourWinrate.setGeometry(QtCore.QRect(440, 203, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.playerFourWinrate.setFont(font)
        self.playerFourWinrate.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerFourWinrate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerFourWinrate.setObjectName("playerFourWinrate")
        self.playerFiveWinrate = QtWidgets.QLabel(Form)
        self.playerFiveWinrate.setGeometry(QtCore.QRect(440, 230, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.playerFiveWinrate.setFont(font)
        self.playerFiveWinrate.setStyleSheet("color: rgb(255, 170, 0);")
        self.playerFiveWinrate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playerFiveWinrate.setObjectName("playerFiveWinrate")
        self.cardOne = QtWidgets.QLabel(Form)
        self.cardOne.setGeometry(QtCore.QRect(270, 340, 61, 81))
        self.cardOne.setStyleSheet("image: url(:/images/2_of_clubs.png);")
        self.cardOne.setText("")
        self.cardOne.setObjectName("cardOne")
        self.cardTwo = QtWidgets.QLabel(Form)
        self.cardTwo.setGeometry(QtCore.QRect(340, 340, 61, 81))
        self.cardTwo.setStyleSheet("image: url(:/images/2_of_clubs.png);")
        self.cardTwo.setText("")
        self.cardTwo.setObjectName("cardTwo")
        self.cardThree = QtWidgets.QLabel(Form)
        self.cardThree.setGeometry(QtCore.QRect(410, 340, 61, 81))
        self.cardThree.setStyleSheet("image: url(:/images/2_of_clubs.png);")
        self.cardThree.setText("")
        self.cardThree.setObjectName("cardThree")
        self.cardFour = QtWidgets.QLabel(Form)
        self.cardFour.setGeometry(QtCore.QRect(480, 340, 61, 81))
        self.cardFour.setStyleSheet("image: url(:/images/2_of_clubs.png);")
        self.cardFour.setText("")
        self.cardFour.setObjectName("cardFour")
        self.cardFive = QtWidgets.QLabel(Form)
        self.cardFive.setGeometry(QtCore.QRect(550, 340, 61, 81))
        self.cardFive.setStyleSheet("image: url(:/images/2_of_clubs.png);")
        self.cardFive.setText("")
        self.cardFive.setObjectName("cardFive")
        self.easyWinrate = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.easyWinrate.setFont(font)
        self.easyWinrate.setStyleSheet("color: rgb(255, 183, 1);")
        self.easyWinrate.setAlignment(QtCore.Qt.AlignCenter)
        self.easyWinrate.setObjectName("easyWinrate")
        self.mediumWinrate = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.mediumWinrate.setFont(font)
        self.mediumWinrate.setStyleSheet("color: rgb(243, 120, 32);")
        self.mediumWinrate.setAlignment(QtCore.Qt.AlignCenter)
        self.mediumWinrate.setObjectName("mediumWinrate")
        self.hardWinrate = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.hardWinrate.setFont(font)
        self.hardWinrate.setStyleSheet("color: rgb(255, 68, 0);")
        self.hardWinrate.setAlignment(QtCore.Qt.AlignCenter)
        self.hardWinrate.setObjectName("hardWinrate")
        self.cardOneCounter = QtWidgets.QLabel(Form)
        self.cardOneCounter.setGeometry(QtCore.QRect(280, 430, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cardOneCounter.setFont(font)
        self.cardOneCounter.setStyleSheet("color: rgb(255, 170, 0);")
        self.cardOneCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.cardOneCounter.setObjectName("cardOneCounter")
        self.cardTwoCounter = QtWidgets.QLabel(Form)
        self.cardTwoCounter.setGeometry(QtCore.QRect(350, 430, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cardTwoCounter.setFont(font)
        self.cardTwoCounter.setStyleSheet("color: rgb(255, 170, 0);")
        self.cardTwoCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.cardTwoCounter.setObjectName("cardTwoCounter")
        self.cardThreeCounter = QtWidgets.QLabel(Form)
        self.cardThreeCounter.setGeometry(QtCore.QRect(420, 430, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cardThreeCounter.setFont(font)
        self.cardThreeCounter.setStyleSheet("color: rgb(255, 170, 0);")
        self.cardThreeCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.cardThreeCounter.setObjectName("cardThreeCounter")
        self.cardFourCounter = QtWidgets.QLabel(Form)
        self.cardFourCounter.setGeometry(QtCore.QRect(490, 430, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cardFourCounter.setFont(font)
        self.cardFourCounter.setStyleSheet("color: rgb(255, 170, 0);")
        self.cardFourCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.cardFourCounter.setObjectName("cardFourCounter")
        self.cardFiveCounter = QtWidgets.QLabel(Form)
        self.cardFiveCounter.setGeometry(QtCore.QRect(560, 430, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cardFiveCounter.setFont(font)
        self.cardFiveCounter.setStyleSheet("color: rgb(255, 170, 0);")
        self.cardFiveCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.cardFiveCounter.setObjectName("cardFiveCounter")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Obsługa języków
        if self.language == 1:
            self.backgroundLabel.setStyleSheet("image: url(:/images/rankingBackground.png);")
            self.easyWinrate.setGeometry(QtCore.QRect(315, 510, 69, 21))
            self.mediumWinrate.setGeometry(QtCore.QRect(420, 510, 69, 21))
            self.hardWinrate.setGeometry(QtCore.QRect(523, 510, 69, 21))
        if self.language == 2:
            self.backgroundLabel.setStyleSheet("image: url(:/images/rankingBackgroundPL.png);")
            self.easyWinrate.setGeometry(QtCore.QRect(300, 510, 69, 21))
            self.mediumWinrate.setGeometry(QtCore.QRect(410, 510, 69, 21))
            self.hardWinrate.setGeometry(QtCore.QRect(530, 510, 69, 21))

        # Obsługa przycisków
        self.closeButton.clicked.connect(Form.close)
        self.closeButton.clicked.connect(self.returnToMenu)

        #self.siema()

        self.show_data()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


    def show_data(self):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "SELECT sum, path from cards order by sum desc limit 5"
            c.execute(query)
            db.commit()
            sum = c.fetchall()

            self.cardOneCounter.setText(str(sum[0][0]))
            self.cardTwoCounter.setText(str(sum[1][0]))
            self.cardThreeCounter.setText(str(sum[2][0]))
            self.cardFourCounter.setText(str(sum[3][0]))
            self.cardFiveCounter.setText(str(sum[4][0]))



            self.cardOne.setStyleSheet(sum[0][1])
            self.cardTwo.setStyleSheet(sum[1][1])
            self.cardThree.setStyleSheet(sum[2][1])
            self.cardFour.setStyleSheet(sum[3][1])
            self.cardFive.setStyleSheet(sum[4][1])

            query = "SELECT username, win_rate from users order by win_rate desc limit 5"
            c.execute(query)
            db.commit()
            winrate = c.fetchall()

            first_player = winrate[0][0]
            second_player = winrate[1][0]
            third_player = winrate[2][0]
            fourth_player = winrate[3][0]
            fifth_player = winrate[4][0]

            self.playerOneNickname.setText(first_player)
            self.playerTwoNickname.setText(second_player)
            self.playerThreeNickname.setText(third_player)
            self.playerFourNickname.setText(fourth_player)
            self.playerFiveNickname.setText(fifth_player)

            first_player = str(round(winrate[0][1]))
            second_player = str(round(winrate[1][1]))
            third_player = str(round(winrate[2][1]))
            fourth_player = str(round(winrate[3][1]))
            fifth_player = str(round(winrate[4][1]))

            self.playerOneWinrate.setText(first_player + "%")
            self.playerTwoWinrate.setText(second_player + "%")
            self.playerThreeWinrate.setText(third_player + "%")
            self.playerFourWinrate.setText(fourth_player + "%")
            self.playerFiveWinrate.setText(fifth_player + "%")

            query = "SELECT win_rate from games_ai"
            c.execute(query)
            db.commit()
            winrate = c.fetchall()

            self.easyWinrate.setText(str(round(winrate[0][0])) + "%")
            self.mediumWinrate.setText(str(round(winrate[1][0])) + "%")
            self.hardWinrate.setText(str(round(winrate[2][0])) + "%")


        except sql.Error as e:
            print("error")

    def siema(self):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor
            # c.execute("INSERT INTO games_ai (level, games_played, games_won, win_rate) VALUES (?,?,?,?)", (1,0,0,0))
            # c.execute("INSERT INTO games_ai (level, games_played, games_won, win_rate) VALUES (?,?,?,?)", (2, 0, 0, 0))
            # c.execute("INSERT INTO games_ai (level, games_played, games_won, win_rate) VALUES (?,?,?,?)", (3, 0, 0, 0))
            # db.commit()
            #c.execute("INSERT INTO cards (path) VALUES (?) where id = 4", (""))
            c.execute("SELECT path FROM cards WHERE id = 4")
    #          c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (1, "Two of Hearts", 0))
    #         # c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (2, "Two of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (3, "Two of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (4, "Two of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (5, "Three of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (6, "Three of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (7, "Three of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (8, "Three of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (9, "Four of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (10, "Four of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (11, "Four of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (12, "Four of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (13, "Five of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (14, "Five of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (15, "Five of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (16, "Five of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (17, "Six of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (18, "Six of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (19, "Six of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (20, "Six of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (21, "Seven of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (22, "Seven of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (23, "Seven of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (24, "Seven of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (25, "Eight of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (26, "Eight of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (27, "Eight of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (28, "Eight of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (29, "Nine of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (30, "Nine of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (31, "Nine of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (32, "Nine of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (33, "Ten of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (34, "Ten of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (35, "Ten of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (36, "Ten of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (37, "Jack of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (38, "Jack of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (39, "Jack of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (40, "Jack of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (41, "Queen of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (42, "Queen of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (43, "Queen of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (44, "Queen of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (45, "King of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (46, "King of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (47, "King of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (48, "King of Clubs", 0))
    #
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (49, "Ace of Hearts", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (50, "Ace of Diamonds", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (51, "Ace of Spades", 0))
    #         c.execute("INSERT INTO cards (id, name, sum) VALUES (?,?,?)", (52, "Ace of Clubs", 0))
    #
    #
            db.commit()

        except sql.Error as e:
            print("error")

    def returnToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()
