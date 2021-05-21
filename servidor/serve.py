import socket

from account import Account
from client import Client
from historic import Historic
from bank import Bank

host = 'localhost'
port = 8000


class conectServ():
	def __init__(self):
		self.bank = Bank()
		self.addr = None
		self.servSocket = None
		self.connection = None

	def connectionServ(self):
		self.addr = (host, port)
		self.servSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.servSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.servSocket.bind(self.addr)
		self.servSocket.listen(10)
		print('Aguardando conexão...')

		self.connection, _ = self.servSocket.accept()
		print('Conectado!')

	def communication(self):
		dados = self.connection.recv(1024).decode()
		message = dados.split('*')
		if message[0] == 'add_client':
			c = Client(message[1], message[2], message[3])
			if not self.bank.get_client(message[3]):
				a = Account(message[4], c, float(message[5]), message[6])
				if not self.bank.get_account(message[4]):
					self.bank.add_client(c)
					self.bank.add_account(a)
					print('Conta Criada Com Sucesso!')
					self.connection.send('True'.encode())
				else:
					print('Número de Conta Em Uso!')
					self.connection.send('False1'.encode())
			else:
				print('CPF Em Uso!')
				self.connection.send('False2'.encode())

		# Logar
		elif message[0] == 'authenticated':
			authenticated = self.bank.login(message[1], message[2])  # pelo numero da conta
			if authenticated:
				print('Login Realizado Sucesso')
				self.connection.send('True'.encode())
			else:
				print('Login Não Realizado!')
				self.connection.send('Conexão inválida!'.encode())

		elif message[0] == 'menuName':
			account = self.bank.get_account_2()
			name = '{}'.format(account.holder.name.capitalize() + ' ' + account.holder.surname.capitalize())
			self.connection.send(name.encode())

		elif message[0] == 'menuBalance':
			account = self.bank.get_account_2()
			balance = '{}'.format(str(account.balance))
			self.connection.send(balance.encode())

		# withdraw
		elif message[0] == 'withdraw':
			account = self.bank.get_account_2()
			if account.withdraw(float(message[1])):
				self.connection.send('True'.encode())
			else: 
				self.connection.send('Erro no saque'.encode())

		# depositar
		elif message[0] == 'deposit':
			account = self.bank.get_account_2()
			account.deposit(float(message[1]))
			self.connection.send('True'.encode())

		# Transferir
		elif message[0] == 'transfer':
			account_origin = self.bank.get_account_2()
			account_destiny = self.bank.get_account(message[1])
			if account_destiny:
				account_origin.transfer(account_destiny, float(message[2]))
				print('Transferência Realizada Com Sucesso!')
				self.connection.send('True'.encode())
			else:
				print('Número de Conta Não Encontrado!')
				self.connection.send('False'.encode())
			# print('ainda não fiz')

		# Extrato
		elif message[0] == 'extract':
			account = self.bank.get_account_2()
			self.connection.send(account.extract().encode())

	def servClose(self):
		self.servSocket.close()
		print("Server finalizado.")


if __name__ == "__main__":
	serv = conectServ()
	serv.connectionServ()
	runing = True
	while runing:
		serv.communication()
	serv.servClose()
