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
			a = Account(message[4], c, float(message[5]), message[6])
			self.bank.add_client(c)
			self.bank.add_account(a)
			self.connection.send('True'.encode())

		# Logar
		elif message[0] == 'authenticated':
			authenticated = self.bank.login(message[1], message[2])  # pelo numero da conta
			if authenticated:
				print('Acesso permitido')
				self.connection.send('True'.encode())
			else:
				self.connection.send('Conecção invalida'.encode())

		# withdraw = Sacar
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

		# transferir
		elif message[0] == 'transfer':
			print('ainda não fiz')

		# historico
		elif message[0] == 'extract':
			account = self.bank.get_account_2()
			message[1] = account

		# mydice meus dados
		elif message[0] == 'myDice':
			account = self.bank.get_account_2()
			name = account.holder.name
			surname = account.holder.surname
			cpf = account.holder.cpf
			number = account.number
			balance = (str(account.balance))
			limit = (str(account.limit))
			push = '{}*{}*{}*{}*{}*{}'.format(name, surname, cpf, number, balance, limit)
			self.connection.send(push.encode())

		# balance Saldo
		elif message[0] == 'balance':
			account = self.bank.get_account_2()
			valueBalance = '{}'.format(account.balance)
			self.connection.send(valueBalance.encode())

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
