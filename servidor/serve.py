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
import threading

from account import Account
from client import Client
from extract import Extract
from bank import Bank

# self.sinc.acquire()
# apenas para um exec
# self.sinc.release()
# libera a thread para outro usar

class ClientThread(threading.Thread):
	def __init__(self, clientAddress, clientsocket):
		threading.Thread.__init__(self)
		self.csocket = clientsocket
		print("nova conexao: ", clientAddress)
		self.sinc = threading.Lock()
		self.bank = Bank()

	def run(self):
		print("Connected de :", clientAddress)
		print('run')
		'''
		DESCRIPTION:
			função criada para enviar e receber dados entre o cliente e servidor
		'''
		test = 1

		while (test != 0):

			dados = self.csocket.recv(1024).decode()
			message = dados.split('π∛')

			if message[0] == 'add_client':
				c = Client(message[1], message[2], message[3])
				if self.bank.get_client(message[3]) is False:
					a = Account(message[4], c, message[5], message[6], '1000')
					if self.bank.get_account(message[4]) is False:
						self.bank.add_client(c)
						self.bank.add_account(a)

						print('Conta Criada Com Sucesso!')
						self.csocket.send('True'.encode())
					else:
						print('Número de Conta Em Uso!')
						self.csocket.send('False1'.encode())
				else:
					print('CPF Em Uso!')
					self.csocket.send('False2'.encode())

			elif message[0] == 'authenticated':  # Logar
				authenticated = self.bank.login(message[1], message[2])
				if authenticated is True:
					print('Login Realizado Sucesso')
					self.csocket.send('True'.encode())
				else:
					print('Login Não Realizado!')
					self.csocket.send('False'.encode())

			elif message[0] == 'menuName':  # Mostrar o nome do usuario na tela de menu
				self.csocket.send(str(self.bank.nameAndSurname()).encode())

			elif message[0] == 'menuBalance':  # Mostrar o saldo do usuario na tela de menu
				self.csocket.send(str(self.bank.menuBalance()).encode())

			elif message[0] == 'withdraw':  # Sacar
				self.sinc.acquire()
				account = self.bank.withdraw(message[1])
				if account == 'True':
					self.csocket.send('True'.encode())
					self.sinc.release()
				elif account == 'Negativo':
					self.csocket.send('Negativo'.encode())
					self.sinc.release()
				elif account == 'Indisponível':
					self.csocket.send('Indisponível'.encode())
					self.sinc.release()

			elif message[0] == 'deposit':  # Depositar
				self.sinc.acquire()
				account = self.bank.deposit(message[1])
				if account == 'True':
					self.csocket.send('True'.encode())
					self.sinc.release()
				elif account == 'Negativo':
					self.csocket.send('Negativo'.encode())
					self.sinc.release()

			elif message[0] == 'transfer': # Transferir
				self.sinc.acquire()
				account = self.bank.transfer(message[1], message[2])
				if account == 'True':
					self.csocket.send('True'.encode())
					self.sinc.release()
				elif account == 'False':
					self.csocket.send('False'.encode())
					self.sinc.release()
				elif account == 'Negativo':
					self.csocket.send('Negativo'.encode())
					self.sinc.release()
				elif account == 'Inválido':
					self.csocket.send('Inválido'.encode())
					self.sinc.release()

			elif message[0] == 'extract':  # Extrato
				# account = self.bank.get_account_2()
				# extracts = account.extract.display_extract()
				# print('Tirou Extrato!')
				self.csocket.send(''.encode())

			elif message[0] == 'backLogin':
				self.bank.sairApp()
				self.csocket.send('True'.encode())

	def servClose(self):
		'''
		DESCRIPTION:
			Utilizado para fechar o servidor
		'''

		self.servSocket.close()
		print("Server finalizado.")
		

if __name__ == "__main__":
	host = 'localhost'
	port = 8000
	addr = (host, port)
	servSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	servSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	servSocket.bind(addr)
	print("Servidor iniciado!")
	print("Aguardando nova conexao...")
	while True:
		servSocket.listen(1)
		clientsock, clientAddress = servSocket.accept()
		newthread = ClientThread(clientAddress, clientsock)
		newthread.start()

