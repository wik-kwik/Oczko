from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql

import account
import menu
import playUsers
import playOptions

class loginForm(object):
    def __init__(self, language, numberOfPlayer, playersNumber, computersNumber, betting):
        self.language = language
        self.numberOfPlayer = numberOfPlayer
        self.playersNumber = playersNumber
        self.computersNumber = computersNumber
        self.betting = betting
        self.playerNickname = ''

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 574)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.gradientBackground = QtWidgets.QLabel(Form)
        self.gradientBackground.setGeometry(QtCore.QRect(50, 90, 291, 361))
        font = QtGui.QFont()
        font.setBold(False)
        self.gradientBackground.setFont(font)
        self.gradientBackground.setText("")
        self.gradientBackground.setObjectName("gradientBackground")
        self.usernameLine = QtWidgets.QLineEdit(Form)
        self.usernameLine.setGeometry(QtCore.QRect(127, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usernameLine.setFont(font)
        self.usernameLine.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                        "border:2px solid rgba(0, 0, 0, 0);\n"
                                        "border-bottom-color: rgb(24, 47, 38);\n"
                                        "color: rgb(80, 93, 94);\n"
                                        "padding-bottom: 7px;")
        self.usernameLine.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLine.setObjectName("usernameLine")
        self.passwordLine = QtWidgets.QLineEdit(Form)
        self.passwordLine.setGeometry(QtCore.QRect(127, 270, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwordLine.setFont(font)
        self.passwordLine.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                        "border:2px solid rgba(0, 0, 0, 0);\n"
                                        "border-bottom-color: rgb(24, 47, 38);\n"
                                        "color: rgb(80, 93, 94);\n"
                                        "padding-bottom: 7px;")
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLine.setDragEnabled(False)
        self.passwordLine.setObjectName("passwordLine")
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(130, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton#loginButton{\n"
                                       "    background-color: rgb(24, 47, 38);\n"
                                       "    color: rgb(255, 183, 16);\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#loginButton:pressed{\n"
                                       "    padding-left:3px;\n"
                                       "    padding-top:3px;\n"
                                       "    \n"
                                       "    background-color: rgb(48, 94, 66);\n"
                                       "    background-position:calc(100%-10px)center;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#pushButton:hover{\n"
                                       "    background-color: rgb(255, 206, 12);\n"
                                       "}\n"
                                       "")
        self.loginButton.setObjectName("loginButton")
        self.statusLabel = QtWidgets.QLabel(Form)
        self.statusLabel.setGeometry(QtCore.QRect(95, 163, 201, 51))
        font = QtGui.QFont()
        font.setBold(False)
        self.statusLabel.setFont(font)
        self.statusLabel.setStyleSheet("color: rgb(255, 46, 56);")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.closeLabel = QtWidgets.QLabel(Form)
        self.closeLabel.setGeometry(QtCore.QRect(324, 90, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.closeLabel.setFont(font)
        self.closeLabel.setStyleSheet("color: rgb(24, 47, 38);")
        self.closeLabel.setObjectName("closeLabel")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(322, 95, 14, 17))
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")

        self.gradientBackground.raise_()
        self.closeLabel.raise_()
        self.closeButton.raise_()
        self.loginButton.raise_()
        self.passwordLine.raise_()
        self.usernameLine.raise_()
        self.statusLabel.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        if (1 in self.numberOfPlayer) == True:
            self.update_db(1)
        if (2 in self.numberOfPlayer) == True:
            self.update_db(2)
        if (3 in self.numberOfPlayer) == True:
            self.update_db(3)
        if (4 in self.numberOfPlayer) == True:
            self.update_db(4)


        # Obsługa przycisków
        self.loginButton.clicked.connect(self.login)
        self.closeButton.clicked.connect(Form.close)
        # Jeśli ktoś otwiera logowanie z menu, zamknięcie okna powoduje powrót do playUsers
        self.closeButton.clicked.connect(self.returnToUsers)
        # Jeśli ktoś otwiera logowanie z menu, zamknięcie okna powoduje powrót do menu
        if self.betting == 3:
            self.closeButton.clicked.connect(Form.close)
            self.closeButton.clicked.connect(self.returnToMenu)

        # Obsługa języków
        if self.language == 1:
            self.gradientBackground.setStyleSheet("image: url(:/images/loginENG.png);")
        if self.language == 2:
            self.gradientBackground.setStyleSheet("image: url(:/images/loginPL.png);")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.closeLabel.setText(_translate("Form", "x"))
        # Obsługa języków
        if self.language == 1:
            self.usernameLine.setPlaceholderText(_translate("Form", "USERNAME"))
            self.passwordLine.setPlaceholderText(_translate("Form", "PASSWORD"))
            self.loginButton.setText(_translate("Form", "LOG IN"))
        if self.language == 2:
            self.usernameLine.setPlaceholderText(_translate("Form", "LOGIN"))
            self.passwordLine.setPlaceholderText(_translate("Form", "HASŁO"))
            self.loginButton.setText(_translate("Form", "ZALOGUJ SIĘ"))



    def login(self):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            # c.execute("""CREATE TABLE logged_users (
            #                 id integer,
            #                 username text UNIQUE,
            #                 coins integer,
            #                 games_played integer,
            #                 win_rate integer,
            #                 time_spent integer,
            #                 cards_used integer
            #                 )""")

            username = self.usernameLine.text()
            password = self.passwordLine.text()

            query = "SELECT username, password, coins, games_played, win_rate, time_spent, cards_used from users where username = '" + username + "'and password = '" + password + "'"
            c.execute(query)
            db.commit()

            result = c.fetchone()



            if username == "" or password == "":
                if self.language == 1:
                    self.statusLabel.setText("Please fill in all the required fields")
                if self.language == 2:
                    self.statusLabel.setText("Wypełnij wszystkie pola")
            elif result == None:
                if self.language == 1:
                    self.statusLabel.setText("Incorrect username or password")
                if self.language == 2:
                    self.statusLabel.setText("Niepoprawna nazwa lub hasło")
            else:
                self.playerNickname = username
                # playUsers.usersForm.loginInfo(self.loginStatus, self.playerNickname)
                self.statusLabel.setStyleSheet("color: rgb(51, 204, 51);")
                if self.language == 1:
                    self.statusLabel.setText("You are logged in")
                if self.language == 2:
                    self.statusLabel.setText("Zalogowano")
                self.loginButton.setEnabled(False)


                try:
                    coins = result[2]
                    games_played = result[3]
                    win_rate = result[4]
                    time_spent = result[5]
                    cards_used = result[6]
                    c.execute(
                        "INSERT INTO logged_users (id,username,coins, games_played, win_rate, time_spent, cards_used) VALUES (?,?,?,?,?,?,?)", (0, username, coins, games_played, win_rate, time_spent, cards_used))
                    db.commit()

                    if self.betting != 3:
                        self.update_db(self.numberOfPlayer[-1])
                    else:
                        self.update_db(5)
                        self.closeButton.clicked.connect(self.account)

                except sql.Error as e:
                    self.statusLabel.setStyleSheet("color: rgb(255, 46, 56);")
                    self.loginButton.setEnabled(True)
                    if self.language == 1:
                        self.statusLabel.setText("This user is already logged in")
                    if self.language == 2:
                        self.statusLabel.setText("Ten użytkownik jest już zalogowany")


        except sql.Error as e:
            self.statusLabel.setStyleSheet("color: rgb(255, 46, 56);")
            self.statusLabel.setText("Error")

    def update_db(self, user_id):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            c.execute(
                "UPDATE logged_users SET id = {} WHERE id = 0".format(user_id))
            db.commit()

        except sql.Error as e:
            print("Error")

    def returnToUsers(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = playUsers.usersForm(self.language, self.playersNumber, self.computersNumber, self.betting)
        self.ui.setupUi(self.window)
        self.window.show()

    def returnToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    def account(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = account.accountForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()