import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import menu
import sqlite3 as sql


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        self.language = 1
        super(MainWindow, self).__init__()
        self.initUI()

    def close_window(self):
        self.close()

    def initUI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()
        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    try:
        db = sql.connect('database.db')  # łączymy się do bazy
        c = db.cursor()  # dodajemy kursor

        # c.execute("""CREATE TABLE settings (
        #                 decks integer,
        #                 skin integer
        #                 )""")

        # c.execute("INSERT INTO settings (decks, skin) VALUES (?,?)", (0, 0))
        # db.commit()

        # c.execute("""CREATE TABLE levels (
        #                 id integer,
        #                 level integer
        #                 )""")

        # c.execute("INSERT INTO levels (id, level) VALUES (?,?)", (1, 0))
        # c.execute("INSERT INTO levels (id, level) VALUES (?,?)", (2, 0))
        # c.execute("INSERT INTO levels (id, level) VALUES (?,?)", (3, 0))
        # c.execute("INSERT INTO levels (id, level) VALUES (?,?)", (4, 0))
        # c.execute("INSERT INTO levels (id, level) VALUES (?,?)", (5, 0))
        
        # db.commit()

        # query = "DELETE FROM logged_users"
        # c.execute(query)
        c.execute("UPDATE levels SET level = 0")
        db.commit()

    except sql.Error as e:
        print("xd")

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
