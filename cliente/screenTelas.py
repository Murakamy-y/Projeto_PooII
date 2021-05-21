from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStackedLayout

from screenBalance import ScreenBalance
from screenDeposit import ScreenDeposit
from screenExtract import ScreenExtract
from screenInitial import ScreenInitial
from screenMenu import ScreenMenu
from screenRegister import ScreenRegister
from screenTransfer import ScreenTransfer
from screenWithdraw import ScreenWithdraw

class ScreenTelas(QtWidgets.QWidget):
	def setupUI(self, Main):
		Main.setObjectName('Main')
		Main.resize(800, 600)

		self.QtStack = QtWidgets.QStackedLayout()

		self.stack0 = QtWidgets.QMainWindow()
		self.stack1 = QtWidgets.QMainWindow()
		self.stack2 = QtWidgets.QMainWindow()
		self.stack3 = QtWidgets.QMainWindow()
		self.stack4 = QtWidgets.QMainWindow()
		self.stack5 = QtWidgets.QMainWindow()
		self.stack6 = QtWidgets.QMainWindow()
		self.stack7 = QtWidgets.QMainWindow()
		self.stack8 = QtWidgets.QMainWindow()
		self.stack9 = QtWidgets.QMainWindow()

		self.screenInitial = ScreenInitial()
		self.screenInitial.setupUi(self.stack0)

		self.screenRegister = ScreenRegister()
		self.screenRegister.setupUi(self.stack1)

		self.screenMenu = ScreenMenu()
		self.screenMenu.setupUi(self.stack2)

		self.screenWithdraw = ScreenWithdraw()
		self.screenWithdraw.setupUi(self.stack3)

		self.screenDeposit = ScreenDeposit()
		self.screenDeposit.setupUi(self.stack4)

		self.screenTransfer = ScreenTransfer()
		self.screenTransfer.setupUi(self.stack5)

		self.screenExtract = ScreenExtract()
		self.screenExtract.setupUi(self.stack6)

		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		self.QtStack.addWidget(self.stack3)
		self.QtStack.addWidget(self.stack4)
		self.QtStack.addWidget(self.stack5)
		self.QtStack.addWidget(self.stack6)

