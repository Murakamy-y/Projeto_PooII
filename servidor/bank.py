from client import Client
from account import Account
import os


class Bank:
	def __init__(self):
		self._clients = {}
		self._accounts = {}
		self.logCPF = None
		self.logNumber = None

	#   Cliente --------------------------------------------------------------------------------------------------------

	def add_client(self, client):
		self._clients[client.cpf] = client

	def get_client(self, cpf):
		if cpf in self._clients:
			return self._clients[cpf]
		else:
			return None
	
	# 	Conta ----------------------------------------------------------------------------------------------------------

	def add_account(self, account):
		self._accounts[account.number] = account

	def display_accounts(self):
		for key, item in self._accounts.items():
			item.display_account()

	def get_account(self, number):
		if number in self._accounts:
			return self._accounts[number]
		else:
			return None
	
	def get_account_2(self):
		if self.logNumber in self._accounts:
			return self._accounts[self.logNumber]
		else:
			return None

	def get_account_client(self, cpf, number):
		c = self.get_account(cpf)
		if c is not None and c.number == number:
			return c
		else:
			return None

	def get_account_client_2(self):
		c = self.get_account(self.logNumber)
		if c is not None and c.holder.cpf == self.logCPF:
			return c
		else:
			return None

	def login(self, cpf, password):
		for key, a in self._accounts.items():
			if a.holder.cpf == cpf and a.password == password:
				self.logCPF = a.holder.cpf
				self.logNumber = a.number
				return a
		return None
