# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screenWithdraw.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ScreenWithdraw(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../telas/banco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
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
        self.pushButtonWithdrawWithdraw = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonWithdrawWithdraw.setGeometry(QtCore.QRect(350, 200, 100, 36))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonWithdrawWithdraw.setFont(font)
        self.pushButtonWithdrawWithdraw.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonWithdrawWithdraw.setStyleSheet("QPushButton {\n"
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
        self.pushButtonWithdrawWithdraw.setObjectName("pushButtonWithdrawWithdraw")
        self.lineEditWithdrawValue = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditWithdrawValue.setGeometry(QtCore.QRect(270, 120, 260, 42))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditWithdrawValue.setFont(font)
        self.lineEditWithdrawValue.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEditWithdrawValue.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 55, 104);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.lineEditWithdrawValue.setMaxLength(10)
        self.lineEditWithdrawValue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditWithdrawValue.setDragEnabled(False)
        self.lineEditWithdrawValue.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEditWithdrawValue.setClearButtonEnabled(False)
        self.lineEditWithdrawValue.setObjectName("lineEditWithdrawValue")
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
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.lineEditWithdrawValue, self.pushButtonWithdrawWithdraw)
        mainWindow.setTabOrder(self.pushButtonWithdrawWithdraw, self.pushButtonComeBack)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Saque"))
        self.label_2.setText(_translate("mainWindow", "Evollutte Bank"))
        self.pushButtonWithdrawWithdraw.setText(_translate("mainWindow", "Sacar"))
        self.lineEditWithdrawValue.setPlaceholderText(_translate("mainWindow", "Valor"))
        self.pushButtonComeBack.setText(_translate("mainWindow", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = ScreenWithdraw()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
