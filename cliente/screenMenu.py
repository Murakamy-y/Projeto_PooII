# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screenMenuAtt02.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ScreenMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("banco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 80))
        self.frame.setStyleSheet("background-color: rgb(0, 55, 104);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(239, 10, 322, 60))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 800, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(800, 600))
        self.frame_2.setMaximumSize(QtCore.QSize(800, 600))
        self.frame_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_2.setStyleSheet("background-color: rgb(211, 243, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButtonWithdraw = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonWithdraw.setGeometry(QtCore.QRect(50, 70, 202, 92))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonWithdraw.setFont(font)
        self.pushButtonWithdraw.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonWithdraw.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(134, 127, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButtonWithdraw.setObjectName("pushButtonWithdraw")
        self.pushButtonExit = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonExit.setGeometry(QtCore.QRect(350, 420, 100, 36))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonExit.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(134, 127, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.pushButtonDeposit = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonDeposit.setGeometry(QtCore.QRect(550, 70, 202, 92))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonDeposit.setFont(font)
        self.pushButtonDeposit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonDeposit.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(134, 127, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButtonDeposit.setObjectName("pushButtonDeposit")
        self.pushButtonTransfer = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonTransfer.setGeometry(QtCore.QRect(300, 190, 202, 92))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonTransfer.setFont(font)
        self.pushButtonTransfer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonTransfer.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(134, 127, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButtonTransfer.setObjectName("pushButtonTransfer")
        self.pushButtonExtract = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonExtract.setGeometry(QtCore.QRect(550, 190, 202, 92))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonExtract.setFont(font)
        self.pushButtonExtract.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonExtract.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(134, 127, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButtonExtract.setObjectName("pushButtonExtract")
        self.pushButtonBalance = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonBalance.setGeometry(QtCore.QRect(300, 70, 202, 92))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonBalance.setFont(font)
        self.pushButtonBalance.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonBalance.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(134, 127, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButtonBalance.setObjectName("pushButtonBalance")
        self.pushButtonMyDice = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonMyDice.setGeometry(QtCore.QRect(50, 190, 202, 92))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonMyDice.setFont(font)
        self.pushButtonMyDice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonMyDice.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(134, 127, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButtonMyDice.setObjectName("pushButtonMyDice")
        self.pushButtonChat = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonChat.setGeometry(QtCore.QRect(300, 310, 202, 92))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonChat.setFont(font)
        self.pushButtonChat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonChat.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:rgb(134, 127, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.pushButtonChat.setObjectName("pushButtonChat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButtonWithdraw, self.pushButtonDeposit)
        MainWindow.setTabOrder(self.pushButtonDeposit, self.pushButtonTransfer)
        MainWindow.setTabOrder(self.pushButtonTransfer, self.pushButtonBalance)
        MainWindow.setTabOrder(self.pushButtonBalance, self.pushButtonMyDice)
        MainWindow.setTabOrder(self.pushButtonMyDice, self.pushButtonExtract)
        MainWindow.setTabOrder(self.pushButtonExtract, self.pushButtonExit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "Evollutte Bank"))
        self.pushButtonWithdraw.setText(_translate("MainWindow", "Sacar"))
        self.pushButtonExit.setText(_translate("MainWindow", "Sair"))
        self.pushButtonDeposit.setText(_translate("MainWindow", "Depositar"))
        self.pushButtonTransfer.setText(_translate("MainWindow", "Transferência"))
        self.pushButtonExtract.setText(_translate("MainWindow", "Extrato"))
        self.pushButtonBalance.setText(_translate("MainWindow", "Saldo"))
        self.pushButtonMyDice.setText(_translate("MainWindow", "Meus Dados"))
        self.pushButtonChat.setText(_translate("MainWindow", "Chat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ScreenMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
