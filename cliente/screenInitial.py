# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attscreenInitial.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ScreenInitial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
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
        font.setFamily("Fira Code")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 800, 520))
        self.frame_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_2.setStyleSheet("background-color: rgb(211, 243, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEditLoginCPF = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditLoginCPF.setGeometry(QtCore.QRect(270, 160, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditLoginCPF.setFont(font)
        self.lineEditLoginCPF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditLoginCPF.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditLoginCPF.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditLoginCPF.setMaxLength(11)
        self.lineEditLoginCPF.setDragEnabled(False)
        self.lineEditLoginCPF.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditLoginCPF.setClearButtonEnabled(False)
        self.lineEditLoginCPF.setObjectName("lineEditLoginCPF")
        self.lineEditLoginPassword = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditLoginPassword.setGeometry(QtCore.QRect(270, 210, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditLoginPassword.setFont(font)
        self.lineEditLoginPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditLoginPassword.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditLoginPassword.setMaxLength(32)
        self.lineEditLoginPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditLoginPassword.setDragEnabled(False)
        self.lineEditLoginPassword.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditLoginPassword.setClearButtonEnabled(False)
        self.lineEditLoginPassword.setObjectName("lineEditLoginPassword")
        self.pushButtonLogin = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonLogin.setGeometry(QtCore.QRect(310, 275, 80, 36))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonLogin.setStyleSheet("QPushButton {\n"
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
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.pushButtonCreateAccount = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonCreateAccount.setGeometry(QtCore.QRect(340, 400, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCreateAccount.setFont(font)
        self.pushButtonCreateAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonCreateAccount.setStyleSheet("QPushButton {\n"
"    color: rgb(0, 55, 104);\n"
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
        self.pushButtonCreateAccount.setObjectName("pushButtonCreateAccount")
        self.pushButtonExit = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonExit.setGeometry(QtCore.QRect(410, 275, 80, 36))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Evollute Bank"))
        self.label.setText(_translate("MainWindow", "Evollutte Bank"))
        self.lineEditLoginCPF.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.lineEditLoginPassword.setPlaceholderText(_translate("MainWindow", "Senha"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Login"))
        self.pushButtonCreateAccount.setText(_translate("MainWindow", "Criar Conta"))
        self.pushButtonExit.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ScreenInitial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
