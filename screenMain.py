import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from screenBalance import ScreenBalance
from screenDeposit import ScreenDeposit
from screenExtract import ScreenExtract
from screenInitial import ScreenInitial
from screenMenu import ScreenMenu
from screenMyDice import ScreenMyDice
from screenRegister import ScreenRegister
from screenTransfer import ScreenTransfer
from screenWithdraw import ScreenWithdraw
from screenChat import ScreenChat
from account import Account
from client import Client
from historic import Historic
from bank import Bank
import datetime
import socket

ip = "localhost"
port = 8000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

class ScreenMain(QtWidgets.QWidget):
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

		self.screenBalance = ScreenBalance()
		self.screenBalance.setupUi(self.stack6)

		self.screenMyDice = ScreenMyDice()
		self.screenMyDice.setupUi(self.stack7)

		self.screenExtract = ScreenExtract()
		self.screenExtract.setupUi(self.stack8)

		self.screenChat = ScreenChat()
		self.screenChat.setupUi(self.stack9)

		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		self.QtStack.addWidget(self.stack3)
		self.QtStack.addWidget(self.stack4)
		self.QtStack.addWidget(self.stack5)
		self.QtStack.addWidget(self.stack6)
		self.QtStack.addWidget(self.stack7)
		self.QtStack.addWidget(self.stack8)
		self.QtStack.addWidget(self.stack9)


class Main(QMainWindow, ScreenMain):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.setupUI(self)
		self.bank = Bank()
		self.cpf = ''
		# Tela Inicial
		self.screenInitial.pushButtonLogin.clicked.connect(self.buttonLogin)
		self.screenInitial.pushButtonCreateAccount.clicked.connect(self.openScreenRegister)
		self.screenInitial.pushButtonExit.clicked.connect(self.exitApp)

		# Tela Registro
		self.screenRegister.pushButtonRegister.clicked.connect(self.buttonRegister)
		self.screenRegister.pushButtonComeBack.clicked.connect(self.comeBackLogin)

		# Tela Menu
		self.screenMenu.pushButtonWithdraw.clicked.connect(self.menuWithdraw)
		self.screenMenu.pushButtonDeposit.clicked.connect(self.menuDeposit)
		self.screenMenu.pushButtonTransfer.clicked.connect(self.menuTransfer)
		self.screenMenu.pushButtonBalance.clicked.connect(self.menuBalance)
		self.screenMenu.pushButtonMyDice.clicked.connect(self.menuMyDice)
		self.screenMenu.pushButtonExtract.clicked.connect(self.menuExtract)
		self.screenMenu.pushButtonExit.clicked.connect(self.comeBackLogin)
		self.screenMenu.pushButtonChat.clicked.connect(self.menuChat)

		# Tela saque
		self.screenWithdraw.pushButtonWithdrawWithdraw.clicked.connect(self.withdraw)
		self.screenWithdraw.pushButtonComeBack.clicked.connect(self.comeBack)

		# Tela deposito
		self.screenDeposit.pushButtonDepositDeposit.clicked.connect(self.deposit)
		self.screenDeposit.pushButtonComeBack.clicked.connect(self.comeBack)

		# Tela tranferencia
		self.screenTransfer.pushButtonTransferTransfer.clicked.connect(self.transfer)
		self.screenTransfer.pushButtonComeBack.clicked.connect(self.comeBack)

		# Tela saldo
		self.screenBalance.pushButtonComeBack.clicked.connect(self.comeBack)

		# Tela Meus Dados
		self.screenMyDice.pushButtonComeBack.clicked.connect(self.comeBack)

		# Tela Extrato
		self.screenExtract.pushButtonComeBack.clicked.connect(self.comeBack)

		# Tela Chat
		self.screenChat.pushButtonChatSubmit.clicked.connect(self.buttonChatSubmit)
		self.screenChat.pushButtonComeBack.clicked.connect(self.comeBack)

	#   Tela Inicial
	def buttonLogin(self):
		cpf = self.screenInitial.lineEditLoginCPF.text()
		password = self.screenInitial.lineEditLoginPassword.text()
		if not (cpf == '' or password == ''):
			if self.bank.login(cpf, password):
				self.cpf = cpf
				QMessageBox.information(None, 'Evollutte Bank', 'Login realizado com sucesso!')
				self.screenInitial.lineEditLoginCPF.setText('')
				self.screenInitial.lineEditLoginPassword.setText('')
				self.QtStack.setCurrentIndex(2)
			else:
				QMessageBox.information(None, 'Evollutte Bank', 'Dados inseridos incorretos!')
		else:
			QMessageBox.information(None, 'Evollutte Bank', 'Todos os valores devem ser preenchidos!')

	def openScreenRegister(self):
		#Não mostrar nenhum campo preenchidos
		self.screenRegister.lineEditRegisterName.setText('')
		self.screenRegister.lineEditRegisterSurname.setText('')
		self.screenRegister.lineEditRegisterCPF.setText('')
		self.screenRegister.lineEditRegisterAccountNumber.setText('')
		self.screenRegister.lineEditRegisterAccountBalance.setText('')
		self.screenRegister.lineEditRegisterAccountPassword.setText('')
		self.QtStack.setCurrentIndex(1)

	def exitApp(self):
		client_socket.close()
		QMessageBox.information(None, 'Evollutte Bank', 'Programa Finalizado')
		sys.exit(app.exec_())

	# Tela de Registro
	def buttonRegister(self):
		name = self.screenRegister.lineEditRegisterName.text()
		surname = self.screenRegister.lineEditRegisterSurname.text()
		cpf = self.screenRegister.lineEditRegisterCPF.text()
		number = self.screenRegister.lineEditRegisterAccountNumber.text()
		value = self.screenRegister.lineEditRegisterAccountBalance.text()
		password = self.screenRegister.lineEditRegisterAccountPassword.text()

		if not (name == '' or surname == '' or cpf == '' or number == '' or value == '' or password == ''):
			p = Client(name, surname, cpf)
			if not self.bank.get_client(p.cpf):
				balance = float(value)
				a = Account(number, p, balance, password, 1000.0)
				if not self.bank.get_account(a.number):
					self.bank.add_client(p)
					self.bank.add_account(a)
					QMessageBox.information(None, 'Evollutte Bank', 'Cadastro realizado com sucesso!')
					self.screenRegister.lineEditRegisterName.setText('')
					self.screenRegister.lineEditRegisterSurname.setText('')
					self.screenRegister.lineEditRegisterCPF.setText('')
					self.screenRegister.lineEditRegisterAccountNumber.setText('')
					self.screenRegister.lineEditRegisterAccountBalance.setText('')
					self.screenRegister.lineEditRegisterAccountPassword.setText('')
					self.QtStack.setCurrentIndex(0)
				else:
					QMessageBox.information(None, 'Evollutte Bank', 'o Número informado já está cadastrado na base de dados!')
			else:
				QMessageBox.information(None, 'Evollutte Bank', 'o CPF informado já está cadastrado na base de dados!')
		else:
			QMessageBox.information(None, 'Evollutte Bank', 'Todos os valores devem ser preenchidos!')

	# Tela Menu
	def menuWithdraw(self):
		self.screenWithdraw.lineEditWithdrawValue.setText('')
		self.QtStack.setCurrentIndex(3)

	def menuDeposit(self):
		self.screenDeposit.lineEditDepositValue.setText('')
		self.QtStack.setCurrentIndex(4)

	def menuTransfer(self):
		self.screenTransfer.lineEditTransferAccountNumber.setText('')
		self.screenTransfer.lineEditTransferValue.setText('')
		self.QtStack.setCurrentIndex(5)

	def menuChat(self):
		self.screenChat.lineEditChat.setText('')
		self.QtStack.setCurrentIndex(9)

	def menuBalance(self):
		account = self.bank.get_account_2()
		self.screenBalance.lineEditBalanceValue.setText(str(account.balance))
		self.QtStack.setCurrentIndex(6)

	def menuMyDice(self):
		account = self.bank.get_account_2()
		self.screenMyDice.lineEditMyDiceName.setText(account.holder.name)
		self.screenMyDice.lineEditMyDiceSurname.setText(account.holder.surname)
		self.screenMyDice.lineEditMyDiceCPF.setText(account.holder.cpf)
		self.screenMyDice.lineEditMyDiceAccountNumber.setText(account.number)
		self.screenMyDice.lineEditMyDiceAccountHolder.setText(account.holder.name)
		self.screenMyDice.lineEditMyDiceAccountBalance.setText(str(account.balance))
		self.screenMyDice.lineEditMyDiceAccountLimit.setText(str(account.limit))
		self.QtStack.setCurrentIndex(7)

	def menuExtract(self):
		account = self.bank.get_account_2()
		date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
		self.screenExtract.plainTextEdit.setPlainText(
			'Número: {}  Saldo: {:.2f}\nData abertura: {}\nTransações: \n{} - Tirou extrato - saldo de {:.2f} em {}'
				.format(account.number, account.balance, account.historic.openDate, account.extract(), account.balance, date)
		)
		self.QtStack.setCurrentIndex(8)

	# Tela Saque
	def withdraw(self):
		account = self.bank.get_account_2()
		value = self.screenWithdraw.lineEditWithdrawValue.text()
		message = account.withdraw(float(value))
		QMessageBox.information(None, 'Evollutte Bank', message)
		self.screenWithdraw.lineEditWithdrawValue.setText('')
		self.QtStack.setCurrentIndex(2)

	# Tela Deposito
	def deposit(self):
		account = self.bank.get_account_2()
		value = self.screenDeposit.lineEditDepositValue.text()
		message = account.deposit(float(value))
		QMessageBox.information(None, 'Evollutte Bank', message)
		self.screenDeposit.lineEditDepositValue.setText('')
		self.QtStack.setCurrentIndex(2)

	# Tela Tranferência
	def transfer(self):
		account_origin = self.bank.get_account_2()
		number = self.screenTransfer.lineEditTransferAccountNumber.text()
		account_destiny = self.bank.get_account(number)
		if account_destiny:
			value = self.screenTransfer.lineEditTransferValue.text()
			message = account_origin.transfer(account_destiny, float(value))
			QMessageBox.information(None, 'Evollutte Bank', message)
			self.screenTransfer.lineEditTransferAccountNumber.setText('')
			self.screenTransfer.lineEditTransferValue.setText('')
			self.QtStack.setCurrentIndex(2)
		else:
			self.screenTransfer.lineEditTransferAccountNumber.setText('')
			QMessageBox.information(None, 'Evollutte Bank', 'Número de conta não encontrado!')

	# Tela Chat
	def buttonChatSubmit(self):
		mensagem = self.screenChat.lineEditChat.text()
		if not(mensagem == ""):
			client_socket.send(mensagem.encode())
			self.screenChat.plainTextEditChat.insertPlainText('Cliente: {}\n'.format(mensagem))
			self.screenChat.plainTextEditChat.insertPlainText('Servidor: {}\n'.format(client_socket.recv(1024).decode()))
			self.screenChat.lineEditChat.setText('')
		else:
			QMessageBox.information(None, 'Evollutte Bank', 'Nenhuma pergunta foi enviada')

	# Padrão
	def comeBackLogin(self):
		self.screenChat.plainTextEditChat.setPlainText('')
		self.screenInitial.lineEditLoginCPF.setText('')
		self.screenInitial.lineEditLoginPassword.setText('')
		self.QtStack.setCurrentIndex(0)

	def comeBack(self):
		self.QtStack.setCurrentIndex(2)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	show_main = Main()
	sys.exit(app.exec_())
