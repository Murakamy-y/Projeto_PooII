from client import Client
from account import Account
import os


class Bank:
	def __init__(self):
		self._clients = {}
		self._accounts = {}
		self._historical = []
	
	#   Cliente --------------------------------------------------------------------------------------------------------

	def add_client(self):
		print('\n\tCadastra Cliente\n')
		name = self.names('Nome: ')
		surname = self.names('Sobrenome: ')
		cpf = self.integer_values('CPF: ')
		while self.get_client(cpf) is not None:
			print('CPF já está cadastrado!')
			cpf = self.integer_values('CPF: ')

		c = Client(name, surname, cpf)
		self._clients[c.cpf] = c
		print('Cliente {} cadastrado com sucesso!'.format(name))
	
	def display_clients(self):
		for key, item in self._clients.items():
			item.display_client()
		
	def get_client(self, cpf):
		if cpf in self._clients:
			return self._clients[cpf]
		else:
			return None
	
	# 	Conta ----------------------------------------------------------------------------------------------------------

	def add_account(self):
		print('\n\tCadastra Conta\n')

		self.display_clients()
		cpf = self.integer_values('Digite o CPF do cliente: ')
		while self.get_account(cpf) is not None:
			print('Esse CPF já tem conta!')
			cpf = self.integer_values('Digite o CPF do cliente: ')
		while self.get_client(cpf) is None:
			print('Não tem cliente com esse CPF!')
			cpf = self.integer_values('Digite o CPF do cliente: ')

		number = self.integer_values('Número: ')
		while self.number_account(number):
			print('Esse número de conta já existe!')
			number = self.integer_values('Número: ')

		balance = self.floating_values('Saldo: ')
		limit = self.floating_values('Limite: ')

		c = Account(number, self.get_client(cpf), balance, limit)
		self._accounts[c.holder.cpf] = c
		print('Contra cadastrada com sucesso!')

	def display_accounts(self):
		for key, item in self._accounts.items():
			item.display_account()
	
	def display_account_client(self, cpf):
		c = self.get_account(cpf)
		if c:
			c.display_account()

	def get_account(self, cpf):
		if cpf in self._accounts:
			return self._accounts[cpf]
		else:
			return None
	
	def get_account_client(self, cpf, number):
		c = self.get_account(cpf)
		if c is not None and c.number == number:
			return c
		else:
			return None

	def transactions(self):
		self.display_clients()
		cpf = self.integer_values('Informe o CPF do cliente: ')
		while self.get_client(cpf) is None:
			print('Não tem cliente com esse CPF!')
			cpf = self.integer_values('Digite o CPF do cliente: ')

		self.display_account_client(cpf)
		number = self.integer_values('Número: ')
		while not self.number_account(number):
			print('Número de conta está errado!')
			number = self.integer_values('Número: ')

		account = self.get_account_client(cpf, number)
		if account:
			return account
		else:
			print('Dados não correspondem!')
			return None

	def withdraw(self):
		account = self.transactions()
		if account:
			value = self.floating_values('Valor: ')
			return account.withdraw(value)

	def deposit(self):
		account = self.transactions()
		if account:
			value = self.floating_values('Valor: ')
			return account.deposit(value)

	def transfer(self):
		account_origin = self.transactions()
		if account_origin:
			account_destiny = self.transactions()
			while account_destiny is None:
				account_destiny = self.transactions()
			if account_destiny:
				value = self.floating_values('Valor: ')
				return account_origin.transfer(account_destiny, value)

	def display_extract(self):
		self.display_clients()
		cpf = self.integer_values('CPF: ')
		c = self.get_account(cpf)
		if c:
			self.clear()
			print('\n\tConta')
			c.extract()

	def display_amount_account(self):
		print('Quantidade de contas {}'.format(Account.get_total_accounts()))

	#   Verifica se está vazio -----------------------------------------------------------------------------------------

	def vazio_cliente(self):
		if any(self._clients):
			return True
		else:
			return False

	def vazio_conta(self):
		if any(self._accounts):
			return True
		else:
			return False

	#   Validações -----------------------------------------------------------------------------------------------------

	def names(self, message):  # Nomes
		while True:
			flag = 0
			name = input(message)
			for i in list(name):
				if (chr(32) < i < chr(65)) or (chr(90) < i < chr(97)) or (chr(122) < i < chr(128)) or i is None:
					flag = 1
			if flag == 0:
				break
			print('Error, entrada não permitida!')
		return name

	def integer_values(self, message):  # valores inteiros
		while True:
			try:
				value = int(input(message))
				while value < 0:
					print('Error, entrada tem que ser maior que zero!')
					value = int(input(message))
			except:
				print('Error, entrada não permitida!')
			else:
				return value

	def floating_values(self, message):  # valores flutuantes
		while True:
			try:
				value = float(input(message))
				while value < 0:
					print('Error, entrada tem que ser maior que zero!')
					value = float(input(message))
			except:
				print('Error, entrada não permitida!')
			else:
				return value

	def number_account(self, number):
		for key, item in self._accounts.items():
			if item.number == number:
				return True
		return False

	#   Enfeite --------------------------------------------------------------------------------------------------------

	def pause(self):  # Pausa
		input('\nPRESSIONE ENTER PARA CONTINUAR.')
		self.clear()

	def clear(self):  # Limpa o Terminal
		os.system('cls' if os.name == 'nt' else 'clear')