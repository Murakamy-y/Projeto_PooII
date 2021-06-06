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

from client import Client
from account import Account
import os
import sqlite3


cnx = sqlite3.connect('db_evollutte_bank.sqlite')
cursor = cnx.cursor()


class Bank:
	def __init__(self):
		# self._clients = {}
		# self._accounts = {}
		self.logCPF = None
		self.logNumber = None

	def add_client(self, client):
		sqlClient = """CREATE TABLE IF NOT EXISTS db_client (Name text NOT NULL, Surname text NOT NULL, CPF integer PRIMARY KEY);"""
		cursor.execute(sqlClient)
		cnx.commit()
		'''
		DESCRIPTION:
			Essa função serve para adicionar cliente no banco e salvar num dicionario com o seu cpf
		'''
		# self._clients[client.cpf] = client
		cursor.execute('INSERT INTO db_client (Name, Surname, CPF) VALUES (?,?,?)', (client.name, client.surname, client.cpf))
		cnx.commit()
		cnx.close()
		
	def get_client(self, cpf):
		'''
		DESCRIPTION:
			Verificar se já existe algum cliente utilizando o cpf informado
		'''
		cursor.execute('SELECT Balance FROM db_client where CPF = {}'.format(self.conta_logada))
		self.logCPF = cursor.fetchall()		
		if cpf in self._clients:
			return self._clients[cpf]
		else:
			return None
	
	def add_account(self, account):
		'''
		DESCRIPTION:
			adiciona uma conta no dicionario e já a vincula em um cliente
		'''
		# self._accounts[account.number] = account
		sqlAccount = """CREATE TABLE IF NOT EXISTS db_account (Number integer PRIMARY KEY, HolderName text NOT NULL, HolderSurname text NOT NULL, HolderCPF integer, Balance text NOT NULL, Limits text NOT NULL, Password text NOT NULL));"""
		cursor.execute(sqlAccount)
		cnx.commit()
		cursor.execute('INSERT INTO db_account (Number, HolderName, HolderSurname, HolderCPF, Balance, Limits, Password) VALUES (?,?,?,?,?,?,?)', (account.number, account.holder.name, account.holder.surname, account.holder.cpf, account.balance, 1000, account.password))
		cnx.commit()
		cnx.close()

	def get_account(self, number):
		'''
		DESCRIPTION:
			verifica se o numero da conta já está sendo utilizado
		'''
		if number in self._accounts:
			return self._accounts[number]
		else:
			return None
	
	def get_account_2(self):
		'''
		DESCRIPTION:
			verifica se o numero da conta já está sendo utilizado
		'''
		if self.logNumber in self._accounts:
			return self._accounts[self.logNumber]
		else:
			return None

	def login(self, cpf, password):
		'''
		DESCRIPTION:
			verifica se a senha e o cpf está vinculada ao banco
		'''
		'''
		for key, a in self._accounts.items():
			if a.holder.cpf == cpf and a.password == password:
				self.logCPF = a.holder.cpf
				self.logNumber = a.number
				return a
		return None
		'''
		cursor.execute('SELECT Password FROM db_account WHERE HolderCPF = {}'.format(cpf))
		bd_password = cursor.fetchall()
		if password == bd_password[0][0]:
			return True
		else:
			return False
	

    	#cons = cursor.execute("SELECT * from Salas WHERE (Bloco = ? AND Numero = ?)",(lista[1],lista[2]))



		
#================================
#Banco de dados
	def verificaCpf(self, cpf):
		print(" ")
		cursor.execute('SELECT * from db_account WHERE HolderCPF = {}'.format(cpf))		
		bd_cpf = cursor.fetchall()
		if bd_cpf[0][0] == cpf:
			return False
		else:
			return True
		
	def nameAndSurname(self, cpf):
		cursor.execute('SELECT Name FROM db_client where CPF = {}'.format(cpf))
		name = cursor.fetchall()
		cursor.execute('SELECT Surname FROM db_client where CPF = {}'.format(cpf))
		surname = cursor.fetchall()
		fullname = name + ' ' + surname
		return fullname


