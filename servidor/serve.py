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

from account import Account
from client import Client
from extract import Extract
from bank import Bank


host = 'localhost'
port = 8000


class conectServ:
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

		if message[0] == 'add_client':
			c = Client(message[1], message[2], message[3])
			if self.bank.get_client(message[3]) is False:
				a = Account(message[4], c, message[5], message[6], '1000')
				if self.bank.get_account(message[4]) is False:
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

		elif message[0] == 'authenticated':  # Logar
			authenticated = self.bank.login(message[1], message[2])
			if authenticated is True:
				print('Login Realizado Sucesso')
				self.connection.send('True'.encode())
			else:
				print('Login Não Realizado!')
				self.connection.send('False'.encode())

		elif message[0] == 'menuName':  # Mostrar o nome do usuario na tela de menu
			self.connection.send(str(self.bank.nameAndSurname()).encode())

		elif message[0] == 'menuBalance':  # Mostrar o saldo do usuario na tela de menu		
			self.connection.send(str(self.bank.menuBalance()).encode())

		elif message[0] == 'withdraw':  # Sacar
			account = self.bank.withdraw(message[1])
			if account == 'True':
				self.connection.send('True'.encode())
			elif account == 'Negativo':
				self.connection.send('Negativo'.encode())
			elif account == 'Indisponível':
				self.connection.send('Indisponível'.encode())

		elif message[0] == 'deposit':  # Depositar
			account = self.bank.deposit(message[1])
			if account == 'True':
				self.connection.send('True'.encode())
			elif account == 'Negativo':
				self.connection.send('Negativo'.encode())

		elif message[0] == 'transfer': # Transferir
			account = self.bank.transfer(message[1], message[2])
			if account == 'True':
				self.connection.send('True'.encode())
			elif account == 'False':
				self.connection.send('False'.encode())
			elif account == 'Negativo':
				self.connection.send('Negativo'.encode())
			elif account == 'Inválido':
				self.connection.send('Inválido'.encode())

			
		elif message[0] == 'extract':  # Extrato
			# account = self.bank.get_account_2()
			# extracts = account.extract.display_extract()
			# print('Tirou Extrato!')
			self.connection.send(''.encode())
		
		elif message[0] == 'backLogin':
			self.bank.sairApp()
			self.connection.send('True'.encode())
			#self.conta_logada = None
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
