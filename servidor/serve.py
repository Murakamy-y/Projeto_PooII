'''
Classe Servidor: Para conectar o servidor as tela e informações do cliente

Metodos criados
-----------------
	connectionServ:
		Utilizado para ligar o servidor e aguarda alguma conexão com o cliente para iniciarmos

	communication:
		Serve para enviar e receber dados entre o cliente e servidor

	servClose:
		Utilizado para fechar o servidor

'''
import socket
import pickle

from account import Account
from client import Client
from extract import Extract
from bank import Bank
import sqlite3

host = 'localhost'
port = 8000

#conexao_sql = sqlite3.connect('db_evollutte_bank.sqlite')
#cursor = conexao_sql.cursor()


class conectServ():
	def __init__(self):
		self.bank = Bank()
		self.addr = None
		self.servSocket = None
		self.connection = None
		self.conta_logada = None

	def connectionServ(self):
		'''
			DESCRIPTION:
				função utilizada ligar o servidor e aguarda alguma conexão com o cliente para iniciarmos
		'''
		self.addr = (host, port)
		self.servSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.servSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.servSocket.bind(self.addr)
		self.servSocket.listen(10)
		print('Aguardando conexão...')

		self.connection, _ = self.servSocket.accept()
		print('Conectado!')

	def communication(self):
		'''
		DESCRIPTION:
			função criada para enviar e receber dados entre o cliente e servidor
		'''
		#conta_logada = None

		dados = self.connection.recv(1024).decode()
		message = dados.split('π∛')
		#sql = """CREATE TABLE IF NOT EXISTS db_add_client(cpf integer PRIMARY KEY, nome text NOT NULL, surname text NOT NULL);"""
		#sql = """CREATE TABLE IF NOT EXISTS db_add_account(number integer PRIMARY KEY, value text NOT NULL, password text NOT NULL);"""
		#cursor.execute(sql)
		#sql =  """CREATE TABLE IF NOT EXISTS db_client (Name text NOT NULL, Surname text NOT NULL, CPF integer PRIMARY KEY, Number text NOT NULL, Balance text NOT NULL, Limits text NOT NULL,Password text NOT NULL);"""
		#cursor.execute(sql)
		#conexao_sql.commit()

		if message[0] == 'add_client':
			c = Client(message[1], message[2], message[3])
			
			a = Account(message[4], c, message[5], '1000', message[6])
			
			self.bank.add_client(c)
			self.bank.add_account(a)
			
			#print("aqui0")
			#sql = """CREATE TABLE IF NOT EXISTS db_add_client(cpf integer PRIMARY KEY, nome text NOT NULL, surname text NOT NULL);"""
			#cursor.execute(sql)
			#cursor.execute("INSERT INTO db_add_client(cpf, nome, surname) VALUES (?,?,?)", (message[3], message[1], message[2]))
			#conexao_sql.commit()
			#
			#sql = """CREATE TABLE IF NOT EXISTS db_add_account(number integer PRIMARY KEY, value text NOT NULL, password text NOT NULL);"""
			#cursor.execute(sql)
			#print("aqui1")
			#cursor.execute("INSERT INTO db_add_account(number, value, password) VALUES (?,?,?)", (message[4], message[5], message[6]))
			#conexao_sql.commit()
			#
			print('Conta Criada Com Sucesso!')
			self.connection.send('True'.encode())
				

		elif message[0] == 'authenticated': # Logar
			authenticated = self.bank.login(message[1], message[2])
			if authenticated is True:
				print('Login Realizado Sucesso')
				self.connection.send('True'.encode())
			else:
				print('Login Não Realizado!')
				self.connection.send('Conexão inválida!'.encode())


			#self.connection.send('True'.encode())
			#authenticated = self.bank.login(message[1], message[2])  # pelo numero da conta
			
			
			#if authenticated:
			#	print('Login Realizado Sucesso')
			#	self.connection.send('True'.encode())
			#else:
			#	print('Login Não Realizado!')
			#	self.connection.send('Conexão inválida!'.encode())

		elif message[0] == 'menuName': # Mostrar o nome do usuario na tela de menu
			print("print : test menu {}".format(self.conta_logada))
			cursor.execute('SELECT Name FROM db_client where CPF = {}'.format(self.conta_logada))
			nome_logado = cursor.fetchall()
			cursor.execute('SELECT Surname FROM db_client where CPF = {}'.format(self.conta_logada))
			surname_logado = cursor.fetchall()
			print(nome_logado[0][0]) #depois apagar
			print(surname_logado[0][0]) #depois apagar
			nome_menu = nome_logado[0][0] + ' ' + surname_logado[0][0]
			print("{}".format(nome_menu))
			self.connection.send(nome_menu.encode())

		#	account = self.bank.get_account_2()
		#	name = '{}'.format(account.holder.name.capitalize() + ' ' + account.holder.surname.capitalize())
		#	self.connection.send(name.encode())

		elif message[0] == 'menuBalance': # Depositar
			cursor.execute('SELECT Balance FROM db_client where CPF = {}'.format(self.conta_logada))
			balance_logado = cursor.fetchall()
			print("menu balance")
			print(balance_logado[0][0]) #depois apagar
			balance_menu = balance_logado[0][0]
			self.connection.send(balance_menu.encode())
#
		#	account = self.bank.get_account_2()
		#	balance = '{}'.format(str(account.balance))
		#	self.connection.send(balance.encode())

		elif message[0] == 'withdraw': # Sacar
			account = self.bank.get_account_2()
			if account.withdraw(float(message[1])):
				cursor.execute('SELECT Balance FROM db_client where CPF = {}'.format(self.conta_logada))
				balance_logado = cursor.fetchall()
				test_withdraw = float(balance_logado[0][0])
				balance_withdraw = test_withdraw - float(message[1])
				print("BALANCE")
				print(balance_withdraw)
				cursor.execute('UPDATE db_client set Balance ={} WHERE CPF = {}'.format(balance_withdraw, self.conta_logada))
				print('Saque Realizado Com Sucesso!')
				self.connection.send('True'.encode())
			else:
				print('Erro No Saque!')
				self.connection.send('Erro no saque'.encode())

		elif message[0] == 'deposit': # Depositar
			account = self.bank.get_account_2()
			account.deposit(float(message[1]))
			cursor.execute('SELECT Balance FROM db_client where CPF = {}'.format(self.conta_logada))
			balance_logado = cursor.fetchall()
			test_deposit = float(balance_logado[0][0])
			balance_deposit = test_deposit + float(message[1])
			cursor.execute('UPDATE db_client set Balance ={} WHERE CPF = {}'.format(balance_deposit, self.conta_logada))
			print('Deposito Realizado com Sucesso!')
			self.connection.send('True'.encode())

		elif message[0] == 'transfer': # Transferir
			#account_origin = self.bank.get_account_2()
			#account_destiny = self.bank.get_account(message[1])
			#if account_destiny:
			transfer = float(message[2])
			#account_origin.transfer(account_destiny, float(message[2]))
			
			cursor.execute('SELECT Balance FROM db_client where CPF = {}'.format(self.conta_logada))
			transfer_remove = cursor.fetchall()
			remove = float(transfer_remove[0][0])
			test_remove_transfer = remove - transfer 
			cursor.execute('UPDATE db_client set Balance = {} WHERE CPF = {}'.format(test_remove_transfer, self.conta_logada))
		
			cursor.execute('SELECT Balance FROM db_client where CPF = {}'.format(message[1]))
			transfer_adicionar = cursor.fetchall()
			add_transfer = float(transfer_adicionar[0][0])
			test_add_transfer = add_transfer + transfer
			cursor.execute('UPDATE db_client set Balance = {} WHERE CPF = {}'.format(test_add_transfer, message[1]))
			print('Transferência Realizada Com Sucesso!')
			self.connection.send('True'.encode())
			#else:
			#	print('Número de Conta Não Encontrado!')
			#	self.connection.send('False'.encode())

		elif message[0] == 'extract': # Extrato
			account = self.bank.get_account_2()
			extracts = account.extract.display_extract()
			print('Tirou Extrato!')
			self.connection.send(extracts.encode())
		
		elif message[0] == 'backLogin':
			self.conta_logada = None
			#conexao_sql.commit()
			#conexao_sql.close()
			
	def servClose(self):
		'''
		DESCRIPTION:
			Utilizado para fechar o servidor
		'''
		self.servSocket.close()
		print("Server finalizado.")
		

if __name__ == "__main__":
	serv = conectServ()
	serv.connectionServ()
	runing = True
	while runing:
		serv.communication()
	serv.servClose()
