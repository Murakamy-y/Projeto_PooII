'''
Class Bank: local utilizada para armazenar e verificar informação

Metodos criados
-----------------
	add_client:
		adicionar o cliente em um dicionario

	get_client
		verificar se já existe algum cliente utilizando o cpf informado

	add_account
		adiciona uma conta no dicionario e já a vincula em um cliente

	get_account
		verifica se o numero da conta já está sendo utilizado

	get_account_2
		verifica se o numero da conta já está sendo utilizado

	login
		verifica se a senha e o cpf está vinculada ao banco
'''

from Projeto_PooII.servidor.client import Client
from Projeto_PooII.servidor.account import Account
import os
import sqlite3
import datetime
from hashlib import md5

cnx = sqlite3.connect('db_evollutte_bank.sqlite')
cursor = cnx.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS db_client (Name text NOT NULL, Surname text NOT NULL, CPF integer PRIMARY KEY);')
cursor.execute('CREATE TABLE IF NOT EXISTS db_account (Number integer PRIMARY KEY, HolderName text NOT NULL, HolderSurname text NOT NULL, HolderCPF integer, Balance real NOT NULL, Password text NOT NULL, Limits real NOT NULL);')


class Bank:
	def __init__(self):
		self.logCPF = None
		self.logNumber = None
		self.extract = []

	def add_client(self, client):
		'''
		DESCRIPTION:
			Essa função serve para adicionar cliente no banco e salvar num dicionario com o seu cpf
		'''
		cursor.execute('INSERT OR REPLACE INTO db_client (Name, Surname, CPF) VALUES (?,?,?)', (client.name, client.surname, int(client.cpf)))

	def get_client(self, cpf):
		'''
		DESCRIPTION:
			Verificar se já existe algum cliente utilizando o cpf informado
		'''

		cursor.execute('SELECT * FROM db_client')
		for i in cursor:
			if cpf == str(i[2]):
				return True
		return False
		
	def add_account(self, account):
		'''
		DESCRIPTION:
			adiciona uma conta no dicionario e já a vincula em um cliente
		'''

		cursor.execute('INSERT OR REPLACE INTO db_account (Number, HolderName, HolderSurname, HolderCPF, Balance, Password, Limits) VALUES (?,?,?,?,?,?,?)', (int(account.number), account.holder.name, account.holder.surname, int(account.holder.cpf), float(account.balance), md5(account.password.encode('utf-8')).hexdigest(), float(account.limit)))
		cnx.commit()
		
	def login(self, cpf, password):
		'''
		DESCRIPTION:
			verifica se a senha e o cpf está vinculada ao banco
		'''
		
		cursor.execute('SELECT Password FROM db_account WHERE HolderCPF = {}'.format(cpf))
		bd_password = cursor.fetchall()
		if md5(password.encode('utf-8')).hexdigest() == str(bd_password[0][0]):
			self.logCPF = int(cpf)
			cursor.execute('SELECT Number FROM db_account WHERE HolderCPF = {}'.format(cpf))
			bd_number = cursor.fetchall()
			self.logNumber = bd_number[0][0]
			return True
		else:
			return False


	def get_account(self, number):
		'''
		DESCRIPTION:
			verifica se o numero da conta já está sendo utilizado
		'''

		cursor.execute('SELECT * FROM db_account')
		for i in cursor:		
			if number == i[0]:
				return True
		return False
	
	def nameAndSurname(self):
		cursor.execute('SELECT HolderName FROM db_account where HolderCPF = {}'.format(self.logCPF))
		name = cursor.fetchall()
		cursor.execute('SELECT HolderSurname FROM db_account where HolderCPF = {}'.format(self.logCPF))
		surname = cursor.fetchall()
		fullname = name[0][0].capitalize() + ' ' + surname[0][0].capitalize()
		return fullname

	def menuBalance(self):
		cursor.execute('SELECT Balance FROM db_account where HolderCPF = {}'.format(self.logCPF))
		balance = cursor.fetchall()
		balance = balance[0][0]
		return balance

	def withdraw(self, value):
		cursor.execute('SELECT Balance FROM db_account where HolderCPF = {}'.format(self.logCPF))
		balance = cursor.fetchall()
		balance = balance[0][0]

		cursor.execute('SELECT Limits FROM db_account where HolderCPF = {}'.format(self.logCPF))
		limits_account = cursor.fetchall()
		limits_account = limits_account[0][0]
		if float(value) < 0:
			return 'Valor sacado não pode ser negativo!'
		elif float(value) > balance + limits_account:
			return 'Valor indisponível para saque!'
		else:
			date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
			balance -= float(value)
			self.extract.append(' - Sacou {} em {}\n'.format(value, date))
			cursor.execute('UPDATE db_account set Balance = {} WHERE HolderCPF = {}'.format(balance, self.logCPF))
			cnx.commit()
			return 'Saque realizado com sucesso!\nSaldo restante = {:.2f}'.format(balance)

	def deposit(self, value):
		cursor.execute('SELECT Balance FROM db_account where HolderCPF = {}'.format(self.logCPF))
		balance = cursor.fetchall()
		balance = balance[0][0]

		cursor.execute('SELECT Limits FROM db_account where HolderCPF = {}'.format(self.logCPF))
		limits_account = cursor.fetchall()
		limits_account = limits_account[0][0]
		if float(value) < 0:
			return 'Valor sacado não pode ser negativo!'
		else:
			date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
			balance += float(value)
			self.extract.append(' - Depositou {} em {}\n'.format(value, date))
			cursor.execute('UPDATE db_account set Balance = {} WHERE HolderCPF = {}'.format(balance, self.logCPF))
			cnx.commit()
			return 'Saque realizado com sucesso!\nSaldo restante = {:.2f}'.format(balance)
	
	def transfer(self, number, value):
		account = self.get_account(int(number))
		if account == True:
			cursor.execute('SELECT Balance FROM db_account where HolderCPF = {}'.format(self.logCPF))
			balance_origin = cursor.fetchall()
			balance_origin = balance_origin[0][0]
			if float(value) < balance_origin or float(value) > 0:
				balance_origin -= float(value)
				cursor.execute('UPDATE db_account set Balance = {} WHERE HolderCPF = {}'.format(balance_origin, self.logCPF))
				cnx.commit()
				
				cursor.execute('SELECT Balance FROM db_account where Number = {}'.format(int(number)))
				balance_destiny = cursor.fetchall()
				balance_destiny = balance_destiny[0][0]
				balance_destiny += float(value)
				cursor.execute('UPDATE db_account set Balance = {} WHERE Number = {}'.format(balance_destiny, int(number)))
				cnx.commit()
				return 'Transferência realizada com sucesso!'
				
			else:
				return 'Dinheiro insuficiente!'
		else:
			return 'Conta não encontrada'
	
	def sairApp(self):
		cnx.commit()
		cnx.close()