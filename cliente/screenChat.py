# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screenChat.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ScreenChat(object):
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(239, 10, 322, 60))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
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
        self.pushButtonComeBack = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonComeBack.setGeometry(QtCore.QRect(345, 410, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonComeBack.setFont(font)
        self.pushButtonComeBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonComeBack.setStyleSheet("QPushButton {\n"
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
        self.pushButtonComeBack.setObjectName("pushButtonComeBack")
        self.plainTextEditChat = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEditChat.setEnabled(True)
        self.plainTextEditChat.setGeometry(QtCore.QRect(64, 140, 672, 231))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEditChat.setFont(font)
        self.plainTextEditChat.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 55, 104);\n"
"border-radius: 5px;")
        self.plainTextEditChat.setMidLineWidth(0)
        self.plainTextEditChat.setReadOnly(True)
        self.plainTextEditChat.setBackgroundVisible(False)
        self.plainTextEditChat.setCenterOnScroll(False)
        self.plainTextEditChat.setObjectName("plainTextEditChat")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(240, 30, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 55, 104);\n"
"border-radius: 5px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEditChat = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditChat.setGeometry(QtCore.QRect(64, 90, 550, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditChat.setFont(font)
        self.lineEditChat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditChat.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditChat.setMaxLength(200)
        self.lineEditChat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditChat.setDragEnabled(False)
        self.lineEditChat.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditChat.setClearButtonEnabled(False)
        self.lineEditChat.setObjectName("lineEditChat")
        self.pushButtonChatSubmit = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonChatSubmit.setGeometry(QtCore.QRect(630, 90, 100, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonChatSubmit.setFont(font)
        self.pushButtonChatSubmit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonChatSubmit.setStyleSheet("QPushButton {\n"
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
        self.pushButtonChatSubmit.setObjectName("pushButtonChatSubmit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat Cliente"))
        self.label_2.setText(_translate("MainWindow", "Evollutte Bank"))
        self.pushButtonComeBack.setText(_translate("MainWindow", "Voltar"))
        self.label.setText(_translate("MainWindow", "Chat"))
        self.lineEditChat.setPlaceholderText(_translate("MainWindow", " Informe sua duvida"))
        self.pushButtonChatSubmit.setText(_translate("MainWindow", "Enviar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ScreenChat()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
