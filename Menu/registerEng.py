# UI rejestracji, wersja angielska

from PyQt5 import QtCore, QtGui, QtWidgets
import menu
import sqlite3 as sql

class registerEngForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(535, 802)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(30, 20, 401, 551))
        font = QtGui.QFont()
        font.setBold(False)
        self.background.setFont(font)
        self.background.setStyleSheet("background-color: rgb(16, 31, 25);\n"
"border-color: 3 px rgb(255, 170, 0);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.backgroundLight = QtWidgets.QLabel(Form)
        self.backgroundLight.setGeometry(QtCore.QRect(70, 50, 329, 491))
        self.backgroundLight.setStyleSheet("background-color: rgb(24, 47, 38);\n"
"background-color: rgb(24, 47, 38);\n"
"border-radius:10px;\n"
"")
        self.backgroundLight.setText("")
        self.backgroundLight.setObjectName("backgroundLight")
        self.registerLabel = QtWidgets.QLabel(Form)
        self.registerLabel.setGeometry(QtCore.QRect(131, 100, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(36)
        font.setBold(False)
        self.registerLabel.setFont(font)
        self.registerLabel.setStyleSheet("color: rgb(255, 170, 0);")
        self.registerLabel.setObjectName("registerLabel")
        self.usernameLine = QtWidgets.QLineEdit(Form)
        self.usernameLine.setGeometry(QtCore.QRect(131, 200, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.usernameLine.setFont(font)
        self.usernameLine.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(255, 170, 0);\n"
"color: rgb(80, 93, 94);\n"
"padding-bottom: 7px;")
        self.usernameLine.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLine.setObjectName("usernameLine")
        self.passwordLine = QtWidgets.QLineEdit(Form)
        self.passwordLine.setGeometry(QtCore.QRect(131, 260, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        self.passwordLine.setFont(font)
        self.passwordLine.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(255, 170, 0);\n"
"color: rgb(80, 93, 94);\n"
"padding-bottom: 7px;")
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLine.setDragEnabled(False)
        self.passwordLine.setObjectName("passwordLine")
        self.confirmLine = QtWidgets.QLineEdit(Form)
        self.confirmLine.setGeometry(QtCore.QRect(131, 320, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.confirmLine.setFont(font)
        self.confirmLine.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(255, 170, 0);\n"
"color: rgb(80, 93, 94);\n"
"padding-bottom: 7px;")
        self.confirmLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmLine.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmLine.setDragEnabled(False)
        self.confirmLine.setObjectName("confirmLine")
        self.createButton = QtWidgets.QPushButton(Form)
        self.createButton.setGeometry(QtCore.QRect(153, 420, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(False)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("QPushButton#createButton{\n"
"    background-color: rgb(255, 170, 0);\n"
"    color: rgb(255, 104, 3);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#createButton:pressed{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"    background-color: rgb(255, 206, 12);\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"\n"
"QPushButton#createButton:hover{\n"
"    background-color: rgb(255, 206, 12);\n"
"}\n"
"")
        self.createButton.setObjectName("createButton")
        self.createButton.clicked.connect(self.new_user)
        self.statusLabel = QtWidgets.QLabel(Form)
        self.statusLabel.setGeometry(QtCore.QRect(100, 380, 271, 20))
        font = QtGui.QFont()
        font.setBold(False)
        self.statusLabel.setFont(font)
        self.statusLabel.setStyleSheet("color: rgb(255, 46, 56);")
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.closeLabel = QtWidgets.QLabel(Form)
        self.closeLabel.setGeometry(QtCore.QRect(410, 20, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.closeLabel.setFont(font)
        self.closeLabel.setStyleSheet("color: rgb(255, 170, 0);")
        self.closeLabel.setObjectName("closeLabel")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(410, 27, 14, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(15)
        font.setBold(True)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.registerLabel.setText(_translate("Form", "REGISTER"))
        self.usernameLine.setPlaceholderText(_translate("Form", "USERNAME"))
        self.passwordLine.setPlaceholderText(_translate("Form", "PASSWORD"))
        self.confirmLine.setPlaceholderText(_translate("Form", "CONFIRM PASSWORD"))
        self.createButton.setText(_translate("Form", "CREATE ACCOUNT"))
        self.closeLabel.setText(_translate("Form", "X"))

    def new_user(self):
        try:
            db = sql.connect('siema.db')  # łączymy się do bazy

            c = db.cursor()  # dodajemy kursor

            # c.execute("""CREATE TABLE users (
            #                user_id integer PRIMARY KEY,
            #                username text UNIQUE,
            #                password text,
            #                games_played integer,
            #                win_rate real,
            #                time_spent integer,
            #                coins integer
            #                )""")


            username = self.usernameLine.text()
            password = self.passwordLine.text()
            confirm = self.confirmLine.text()

            games_played = 0
            win_rate = 0
            time_spent = 0
            coins = 1000
            data = [
                (username, password, games_played,
                 win_rate, time_spent, coins)
            ]

            if username == "" or password == "" or confirm == "":
                self.statusLabel.setText("Please fill in all the required fields")

            elif password == confirm:
                try:
                    c.executemany(
                        "INSERT INTO users (username,password,games_played,win_rate,time_spent,coins) VALUES (?,?,?,?,?,?)",
                        data)
                    db.commit()
                    print("Data has been inserted")
                    self.statusLabel.setStyleSheet("color: rgb(51, 204, 51);")
                    self.statusLabel.setText("You have been registered!")
                    self.createButton.setEnabled(False)

                    c.execute("SELECT * FROM users")

                    print(c.fetchall())
                    db.commit()
                    db.close()

                except sql.IntegrityError as e:
                    self.statusLabel.setText("This nickname is not available")

            else:
                self.statusLabel.setText("Passwords don't match")

        except sql.Error as e:
            self.statusLabel.setText("Error")

    def returnToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm()
        self.ui.setupUi(self.window)
        self.window.show()
