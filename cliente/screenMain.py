'''
Classe Main, utilizado a fim de receber e enviar dados para o servidor

'''

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QPlainTextEdit
from PyQt5.QtCore import QCoreApplication

from screenTelas import ScreenTelas
from clientHost import ClientHost


class Main(ScreenTelas):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		'''
		DESCRIPTION:
			utilizado a fim de receber e enviar dados para o servidor e conectar os botão as tela			
		'''
		self.cpf = ''
		self.number = ''
		self.setupUI(self)
		self.clientHost = ClientHost()
		self.clientHost.connectClient()
		
		# Tela Inicial
		self.screenInitial.pushButtonLogin.clicked.connect(self.buttonLogin) # Botão da tela inicial
		self.screenInitial.pushButtonCreateAccount.clicked.connect(self.openScreenRegister) # Botão da tela inicial
		self.screenInitial.pushButtonExit.clicked.connect(self.exitApp) # Botão da tela inicial

		# Tela Registro
		self.screenRegister.pushButtonRegister.clicked.connect(self.buttonRegister) # Botão da tela Registro
		self.screenRegister.pushButtonComeBack.clicked.connect(self.comeBackLogin) # Botão da tela Registro

		# Tela Menu
		self.screenMenu.pushButtonWithdraw.clicked.connect(self.menuWithdraw) # Botão da tela Menu
		self.screenMenu.pushButtonDeposit.clicked.connect(self.menuDeposit) # Botão da tela Menu
		self.screenMenu.pushButtonTransfer.clicked.connect(self.menuTransfer) # Botão da tela Menu
		self.screenMenu.pushButtonExtract.clicked.connect(self.menuExtract) # Botão da tela Menu
		self.screenMenu.pushButtonExit.clicked.connect(self.comeBackLogin) # Botão da tela Menu

		# Tela saque
		self.screenWithdraw.pushButtonWithdrawWithdraw.clicked.connect(self.withdraw) # Botão da tela saque
		self.screenWithdraw.pushButtonComeBack.clicked.connect(self.comeBack) # Botão da tela saque

		# Tela deposito
		self.screenDeposit.pushButtonDepositDeposit.clicked.connect(self.deposit) # Botão da tela deposito
		self.screenDeposit.pushButtonComeBack.clicked.connect(self.comeBack) # Botão da tela deposito

		# Tela tranferencia
		self.screenTransfer.pushButtonTransferTransfer.clicked.connect(self.transfer) # Botão da tela tranferencia
		self.screenTransfer.pushButtonComeBack.clicked.connect(self.comeBack) # Botão da tela tranferencia

		# Tela Extrato
		self.screenExtract.pushButtonComeBack.clicked.connect(self.comeBack) # Botão da tela extrato

	
	def buttonLogin(self): #   Tela Inicial
		cpf = self.screenInitial.lineEditLoginCPF.text()
		password = self.screenInitial.lineEditLoginPassword.text()
		if not (cpf == '' or password == ''):
			push = '{}π∛{}π∛{}'.format('authenticated', cpf, password)  # enviar
			pull = self.clientHost.submit(push)  # receber
			if pull == 'True':
				self.cpf = cpf
				QMessageBox.information(None, 'Evollutte Bank', 'Login realizado com sucesso!')
				self.screenInitial.lineEditLoginCPF.setText('')
				self.screenInitial.lineEditLoginPassword.setText('')
				self.screenMenu.lineEditMenuBalance.setText('saldo')
				self.screenMenu.lineEditMenuName.setText('nome')
				self.menu()
				self.QtStack.setCurrentIndex(2)
		else:
			QMessageBox.information(None, 'Evollutte Bank', 'Todos os valores devem ser preenchidos!')

	def openScreenRegister(self): #	chama a tela de registro do cliente
		# Não mostrar nenhum campo preenchidos
		self.screenRegister.lineEditRegisterName.setText('')
		self.screenRegister.lineEditRegisterSurname.setText('')
		self.screenRegister.lineEditRegisterCPF.setText('')
		self.screenRegister.lineEditRegisterAccountNumber.setText('')
		self.screenRegister.lineEditRegisterAccountBalance.setText('')
		self.screenRegister.lineEditRegisterAccountPassword.setText('')
		self.QtStack.setCurrentIndex(1)

	
	def exitApp(self):	#	saida da aplicação	
		# client_socket.close()
		QMessageBox.information(None, 'Evollutte Bank', 'Programa Finalizado')
		sys.exit(app.exec_())

	def buttonRegister(self): # Tela de Registro
		name = self.screenRegister.lineEditRegisterName.text()
		surname = self.screenRegister.lineEditRegisterSurname.text()
		cpf = self.screenRegister.lineEditRegisterCPF.text()
		number = self.screenRegister.lineEditRegisterAccountNumber.text()
		value = self.screenRegister.lineEditRegisterAccountBalance.text()
		password = self.screenRegister.lineEditRegisterAccountPassword.text()
		
		if not (name == '' or surname == '' or cpf == '' or number == '' or value == '' or password == ''):
			push = '{}π∛{}π∛{}π∛{}π∛{}π∛{}π∛{}'.format('add_client', name, surname, cpf, number, value, password)
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

			elif pull == 'False1':
				QMessageBox.information(None, 'Evollutte Bank', 'Número de Conta Em Uso!')

			elif pull == 'False2':
				QMessageBox.information(None, 'Evollutte Bank', 'CPF Em Uso!')
		else:
			QMessageBox.information(None, 'Evollutte Bank', 'Todos os valores devem ser preenchidos!')

	def menu(self): # Tela Menu
		push = '{}'.format('menuName')
		pull = self.clientHost.submit(push)
		self.screenMenu.lineEditMenuName.setText(pull)
		push = '{}'.format('menuBalance')
		pull = self.clientHost.submit(push)
		self.screenMenu.lineEditMenuBalance.setText(pull)

	def menuWithdraw(self): #	chama a tela de saque
		self.screenWithdraw.lineEditWithdrawValue.setText('')
		self.QtStack.setCurrentIndex(3)

	def menuDeposit(self): #	chama a tela de deposito
		self.screenDeposit.lineEditDepositValue.setText('')
		self.QtStack.setCurrentIndex(4)
	
	def menuTransfer(self): #	chama a tela de transferencia
		self.screenTransfer.lineEditTransferAccountNumber.setText('')
		self.screenTransfer.lineEditTransferValue.setText('')
		self.QtStack.setCurrentIndex(5)

	def menuExtract(self): #	onde é mostrado o extrato do cliente
		push = '{}'.format('extract')
		pull = self.clientHost.submit(push)
		self.screenExtract.plainTextEdit.setPlainText(pull)
		self.QtStack.setCurrentIndex(6)

	def withdraw(self): # Tela Saque
		value = self.screenWithdraw.lineEditWithdrawValue.text()
		if not(value == ''):
			push = '{}π∛{}'.format('withdraw', value)
			pull = self.clientHost.submit(push)
			if pull == 'True':
				self.screenWithdraw.lineEditWithdrawValue.setText('')
				QMessageBox.information(None, 'Evollutte Bank', value)
				self.menu()
				self.QtStack.setCurrentIndex(2)
			else:
				QMessageBox.information(None, 'Evollutte Bank', "Valor invalido")

	def deposit(self): # Tela Deposito
		value = self.screenDeposit.lineEditDepositValue.text()
		if not (value == ''):
			push = '{}π∛{}'.format('deposit', value)
			pull = self.clientHost.submit(push)
			if pull == 'True':
				self.screenDeposit.lineEditDepositValue.setText('')
				QMessageBox.information(None, 'Evollutte Bank', value)
				self.menu()
				self.QtStack.setCurrentIndex(2)
		else:
			QMessageBox.information(None, 'Evollutte Bank', "Valor invalido")

	def transfer(self): # Tela Tranferência
		number = self.screenTransfer.lineEditTransferAccountNumber.text()
		value = self.screenTransfer.lineEditTransferValue.text()
		push = '{}π∛{}π∛{}'.format('transfer', number, value)
		pull = self.clientHost.submit(push)
		if pull == 'True':
			QMessageBox.information(None, 'Evollutte Bank', 'Transferência Realizada Com Sucesso!')
			self.screenTransfer.lineEditTransferAccountNumber.setText('')
			self.screenTransfer.lineEditTransferValue.setText('')
			self.menu()
			self.QtStack.setCurrentIndex(2)
		elif pull == 'False':
			QMessageBox.information(None, 'Evollutte Bank', 'Número de Conta Não Encontrado')
			self.screenTransfer.lineEditTransferAccountNumber.setText('')

	def comeBackLogin(self): # Botao para voltar a tela de login
		push = '{}'.format('backLogin')
		pull = self.clientHost.submit(push)
		self.screenInitial.lineEditLoginCPF.setText('')
		self.screenInitial.lineEditLoginPassword.setText('')
		self.QtStack.setCurrentIndex(0)

	def comeBack(self): #	Botao para voltar a tela principal
		self.QtStack.setCurrentIndex(2)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	show_main = Main()
	sys.exit(app.exec_())
