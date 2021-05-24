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


class Bank:
	def __init__(self):
		self._clients = {}
		self._accounts = {}
		self.logCPF = None
		self.logNumber = None

	def add_client(self, client):
		'''
		DESCRIPTION:
			Essa função serve para adicionar cliente no banco e salvar num dicionario com o seu cpf
		'''
		self._clients[client.cpf] = client

	def get_client(self, cpf):
		'''
		DESCRIPTION:
			Verificar se já existe algum cliente utilizando o cpf informado
		'''
		if cpf in self._clients:
			return self._clients[cpf]
		else:
			return None
	
	def add_account(self, account):
		'''
		DESCRIPTION:
			adiciona uma conta no dicionario e já a vincula em um cliente
		'''
		self._accounts[account.number] = account

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
		for key, a in self._accounts.items():
			if a.holder.cpf == cpf and a.password == password:
				self.logCPF = a.holder.cpf
				self.logNumber = a.number
				return a
		return None
