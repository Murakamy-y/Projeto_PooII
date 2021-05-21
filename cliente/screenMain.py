import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from screenTelas import ScreenTelas
from clientHost import ClientHost

import datetime
import socket


class Main(ScreenTelas):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.cpf = ''
		self.number = ''
		self.setupUI(self)
		self.clientHost = ClientHost()
		self.clientHost.connectClient()
		
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
			push = '{}*{}*{}'.format('authenticated', cpf, password)#enviar
			pull = self.clientHost.submit(push)#receber
			if pull == 'True':
				self.cpf = cpf
				QMessageBox.information(None, 'Evollutte Bank', 'Login realizado com sucesso!')
				self.screenInitial.lineEditLoginCPF.setText('')
				self.screenInitial.lineEditLoginPassword.setText('')
				self.QtStack.setCurrentIndex(2)
		else:
			QMessageBox.information(None, 'Evollutte Bank', 'Todos os valores devem ser preenchidos!')

	def openScreenRegister(self):
		# Não mostrar nenhum campo preenchidos
		self.screenRegister.lineEditRegisterName.setText('')
		self.screenRegister.lineEditRegisterSurname.setText('')
		self.screenRegister.lineEditRegisterCPF.setText('')
		self.screenRegister.lineEditRegisterAccountNumber.setText('')
		self.screenRegister.lineEditRegisterAccountBalance.setText('')
		self.screenRegister.lineEditRegisterAccountPassword.setText('')
		self.QtStack.setCurrentIndex(1)

	def exitApp(self):
		# client_socket.close()
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
			push = '{}*{}*{}*{}*{}*{}*{}'.format('add_client', name, surname, cpf, number, value, password)
			pull = self.clientHost.submit(push)
			if pull == 'True':
				QMessageBox.information(None, 'Evollutte Bank', 'Cadastro realizado com sucesso!')
				self.screenRegister.lineEditRegisterName.setText('')
				self.screenRegister.lineEditRegisterSurname.setText('')
				self.screenRegister.lineEditRegisterCPF.setText('')
				self.screenRegister.lineEditRegisterAccountNumber.setText('')
				self.screenRegister.lineEditRegisterAccountBalance.setText('')
				self.screenRegister.lineEditRegisterAccountPassword.setText('')
				self.QtStack.setCurrentIndex(0)
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
		push = '{}'.format('balance')
		pull = self.clientHost.submit(push)
		self.screenBalance.lineEditBalanceValue.setText(pull)
		self.QtStack.setCurrentIndex(6)

	def menuMyDice(self):
		push = '{}'.format('myDice')
		pull = self.clientHost.submit(push)
		message = pull.split('*')
		self.screenMyDice.lineEditMyDiceName.setText(message[0])
		self.screenMyDice.lineEditMyDiceSurname.setText(message[1])
		self.screenMyDice.lineEditMyDiceCPF.setText(message[2])
		self.screenMyDice.lineEditMyDiceAccountNumber.setText(message[3])
		self.screenMyDice.lineEditMyDiceAccountHolder.setText(message[4])
		self.screenMyDice.lineEditMyDiceAccountBalance.setText(message[5])
		self.screenMyDice.lineEditMyDiceAccountLimit.setText(message[6])
		self.QtStack.setCurrentIndex(7)

	def menuExtract(self):
		push = "{}".format('extract')
		pull = self.clientHost.submit(push)
		
		self.self.screenExtract.plainTextEdit.setPlainText(pull)
		self.QtStack.setCurrentIndex(8)

	# Tela Saque
	def withdraw(self):
		value = self.screenWithdraw.lineEditWithdrawValue.text()
		if not(value == ''):
			push = '{}*{}'.format('withdraw', value)
			pull = self.clientHost.submit(push)
			if pull == 'True':
				self.screenWithdraw.lineEditWithdrawValue.setText('')
				QMessageBox.information(None, 'Evollutte Bank', value)
				self.QtStack.setCurrentIndex(2)
			else:
				QMessageBox.information(None, 'Evollutte Bank', "Valor invalido")

	# Tela Deposito
	def deposit(self):
		value = self.screenDeposit.lineEditDepositValue.text()
		if not(value == ''):
			
			push = '{}*{}'.format('deposit', value)
			pull = self.clientHost.submit(push)
			
			if pull == 'True':
				self.screenDeposit.lineEditDepositValue.setText('')
				QMessageBox.information(None, 'Evollutte Bank', value)
				self.QtStack.setCurrentIndex(2)
		else:
			QMessageBox.information(None, 'Evollutte Bank', "Valor invalido")

	# Tela Tranferência
	def transfer(self):
		#account_origin = self.bank.get_account_2()
		#number = self.screenTransfer.lineEditTransferAccountNumber.text()
		#account_destiny = self.bank.get_account(number)
		#if account_destiny:
		#	value = self.screenTransfer.lineEditTransferValue.text()
		#	message = account_origin.transfer(account_destiny, float(value))
		#	QMessageBox.information(None, 'Evollutte Bank', message)
		#	self.screenTransfer.lineEditTransferAccountNumber.setText('')
		#	self.screenTransfer.lineEditTransferValue.setText('')
		#	self.QtStack.setCurrentIndex(2)
		#else:
		#	self.screenTransfer.lineEditTransferAccountNumber.setText('')
		QMessageBox.information(None, 'Evollutte Bank', 'Número de conta não encontrado!')

	# Tela Chat
	def buttonChatSubmit(self):
		mensagem = self.screenChat.lineEditChat.text()
		if not(mensagem == ""):
			#client_socket.send(mensagem.encode())
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
