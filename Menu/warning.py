from PyQt5 import QtCore, QtGui, QtWidgets
import playOptions

class warningForm(object):
    def __init__(self, language, warningType):
        self.language = language
        self.warningType=warningType

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(415, 307)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.orangeBackground = QtWidgets.QLabel(Form)
        self.orangeBackground.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.orangeBackground.setStyleSheet("image: url(:/images/warningBackground.jpg);")
        self.orangeBackground.setText("")
        self.orangeBackground.setObjectName("orangeBackground")
        self.warningIcon = QtWidgets.QLabel(Form)
        self.warningIcon.setGeometry(QtCore.QRect(155, 50, 91, 81))
        self.warningIcon.setStyleSheet("image: url(:/images/warning.png);")
        self.warningIcon.setText("")
        self.warningIcon.setObjectName("warningIcon")
        self.warningText = QtWidgets.QLabel(Form)
        self.warningText.setGeometry(QtCore.QRect(50, 140, 301, 121))
        self.warningText.setStyleSheet("image: url(:/images/warningType1.png);")
        self.warningText.setText("")
        self.warningText.setObjectName("warningText")

        if self.warningType==1:
            if self.language==1:
                self.warningText.setStyleSheet("image: url(:/images/warningType1.png);")
            if self.language==2:
                self.warningText.setStyleSheet("image: url(:/images/warningType1PL.png);")
        # Po zmianie koncepcji - nieużywane warningi, nieprzetłumaczone
        if self.warningType==2:
            self.warningText.setStyleSheet("image: url(:/images/warningType2.png);")

        if self.warningType==3:
            self.warningText.setStyleSheet("image: url(:/images/warningType3.png);")

        if self.warningType==4:
            self.warningText.setStyleSheet("image: url(:/images/warningType4.png);")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #     self.show_playOptions()
    #
    # def show_playOptions(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = playOptions.playOptionsForm(self.language)
    #     self.ui.setupUi(self.window)
    #     QtCore.QTimer.singleShot(3000, self.window.show)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Warning"))

