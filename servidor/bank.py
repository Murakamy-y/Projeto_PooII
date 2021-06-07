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
import psycopg2 as db
import datetime
from hashlib import md5


class Config:
	def __init__(self) -> None:
		self.config = {
			'postgres': {
				'user': 'postgres',
				'password': 'root',
				'host': '127.0.0.1',
				'port': '5432',
				'database': 'Evollutte_bank'
			}
		}


class Connection(Config):
	def __init__(self):
		Config.__init__(self)
		try:
			self.cnx = db.connect(**self.config['postgres'])
			self.cur = self.cnx.cursor()
		except Exception as error:
			print('Erro na conexão!', error)
			exit(1)

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.commit()
		self.connection.close()

	@property
	def connection(self):
		return self.cnx

	@property
	def cursor(self):
		return self.cur

	def commit(self):
		self.connection.commit()

	def fetchall(self):
		return self.cursor.fetchall()

	def execute(self, sql, params=None):
		self.cursor.execute(sql, params or ())

	def query(self, sql, params=None):
		self.cursor.execute(sql, params or ())
		return self.fetchall()

	def add_clients(self, sql, client):
		self.cursor.execute(sql, (int(client.cpf), client.name, client.surname))

	def add_accounts(self, sql, account):
		self.cursor.execute(sql, (int(account.number), account.holder.name, account.holder.surname, int(account.holder.cpf), float(account.balance), md5(account.password.encode('utf-8')).hexdigest(), float(account.limit)))


class Bank(Connection):
	def __init__(self):
		self.logCPF = None
		self.logNumber = None
		self.extract = []
		self.add = []
		Connection.__init__(self)
		sql = 'create table if not exists db_client (CPF integer primary key, Name varchar(45) not null, Surname varchar(45) not null)'
		self.execute(sql)
		self.commit()
		sql = 'create table if not exists db_account (Number integer primary key, Name varchar(45) not null, Surname varchar(45) not null, CPF integer, Balance real not null, Password varchar(45) not null, Limits real not null)'
		self.execute(sql)
		self.commit()

	def add_client(self, client):
		'''
		DESCRIPTION:
			Essa função serve para adicionar cliente no banco e salvar num dicionario com o seu cpf
		'''
		try:
			sql = 'insert into db_client (CPF, Name, Surname) VALUES (%s, %s, %s)'
			self.add_clients(sql, client)
		except Exception as error:
			print('Erro ao Inserir', error)
		else:
			self.commit()

	def get_client(self, cpf):
		'''
		DESCRIPTION:
			Verificar se já existe algum cliente utilizando o cpf informado
		'''
		sql = 'select * from db_client'
		self.execute(sql)
		for i in self.cursor:
			if cpf == str(i[0]):
				return True
		return False
		
	def add_account(self, account):
		'''
		DESCRIPTION:
			adiciona uma conta no dicionario e já a vincula em um cliente
		'''
		
		try:
			sql = 'insert into db_account (Number,Name, Surname, CPF, Balance, Password, Limits) VALUES (%s, %s, %s, %s, %s, %s, %s)'
			self.add_accounts(sql, account)
		except Exception as error:
			print('Erro ao Inserir', error)
		else:
			self.commit()
		
	def login(self, cpf, password):
		'''
		DESCRIPTION:
			verifica se a senha e o cpf está vinculada ao banco
		'''
		sql = f'select Password from db_account where CPF = {cpf}'
		self.execute(sql)
		bd_password = self.fetchall()
		if md5(password.encode('utf-8')).hexdigest() == str(bd_password[0][0]):
			self.logCPF = int(cpf)
			sql = f'select Number from db_account where CPF = {cpf}'
			self.execute(sql)
			bd_number = self.fetchall()
			self.logNumber = bd_number[0][0]
			return True
		else:
			return False


	def get_account(self, number):
		'''
		DESCRIPTION:
			verifica se o numero da conta já está sendo utilizado
		'''

		sql = 'select * from db_account'
		self.execute(sql)
		for i in self.cursor:		
			if int(number) == i[0]:
				return True
		return False
	
	def nameAndSurname(self):
		sql = f'select Name from db_account where CPF = {self.logCPF}'
		self.execute(sql)
		name = self.fetchall()
		sql = f'select Surname FROM db_account where CPF = {self.logCPF}'
		self.execute(sql)
		surname = self.fetchall()
		fullname = name[0][0].capitalize() + ' ' + surname[0][0].capitalize()
		return fullname

	def menuBalance(self):
		sql = f'select Balance from db_account where CPF = {self.logCPF}'
		self.execute(sql)
		balance = self.fetchall()
		balance = balance[0][0]
		return balance

	def withdraw(self, value):
		sql = f'select Balance from db_account where CPF = {self.logCPF}'
		self.execute(sql)
		balance = self.fetchall()
		balance = balance[0][0]

		sql = f'select Limits from db_account where CPF = {self.logCPF}'
		self.execute(sql)
		limits_account = self.fetchall()
		limits_account = limits_account[0][0]
		if float(value) < 0:
			return 'Valor sacado não pode ser negativo!'
		elif float(value) > balance + limits_account:
			return 'Valor indisponível para saque!'
		else:
			date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
			balance -= float(value)
			self.extract.append(' - Sacou {} em {}\n'.format(value, date))
			sql = f'UPDATE db_account set Balance = {balance} WHERE CPF = {self.logCPF}'
			self.execute(sql)
			self.commit()
			return f'Saque realizado com sucesso!\nSaldo restante = {balance}'

	def deposit(self, value):
		sql = f'select Balance from db_account where CPF = {self.logCPF}'
		self.execute(sql)
		balance = self.fetchall()
		balance = balance[0][0]

		sql = f'select Limits from db_account where CPF = {self.logCPF}'
		self.execute(sql)
		limits_account = self.fetchall()
		limits_account = limits_account[0][0]
		if float(value) < 0:
			return 'Valor sacado não pode ser negativo!'
		else:
			date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
			balance += float(value)
			self.extract.append(' - Depositou {} em {}\n'.format(value, date))
			sql = f'update db_account set Balance = {balance} where CPF = {self.logCPF}'
			self.execute(sql)
			self.commit()
			return f'Saque realizado com sucesso!\nSaldo restante = {balance}'
	
	def transfer(self, number, value):
		account = self.get_account(int(number))
		if account == True:
			sql = f'select Balance FROM db_account where CPF = {self.logCPF}'
			self.execute(sql)
			balance_origin = self.fetchall()
			balance_origin = balance_origin[0][0]
			if float(value) < balance_origin or float(value) > 0:
				balance_origin -= float(value)
				sql = f'update db_account set Balance = {balance_origin} where CPF = {self.logCPF}'
				self.execute(sql)
				self.commit()
				
				sql = f'select Balance from db_account where Number = {int(number)}'
				self.execute(sql)
				balance_destiny = self.fetchall()
				balance_destiny = balance_destiny[0][0]
				balance_destiny += float(value)
				sql = f'UPDATE db_account set Balance = {balance_destiny} where Number = {int(number)}'
				self.execute(sql)
				self.commit()
				return 'Transferência realizada com sucesso!'
			else:
				return 'Dinheiro insuficiente!'
		else:
			return 'Conta não encontrada!'
	
	def sairApp(self):
		self.commit()
		# cnx.close()
