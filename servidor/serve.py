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
		self.addr = ((host, port))
		self.servSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.servSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.servSocket.bind(self.addr)
		self.servSocket.listen(10)
		print("Aguardando conexão...")

		self.connection, _ = self.servSocket.accept()
		print("Conectado!")
		print("Aguardando solicitações...")

	def communication(self):
		dados = self.connection.recv(1024).decode()
		message = dados.split('*')
		#Account._total_accounts += 1
		#adicionar cliente Nome / sobrenome / cpf // conta / saldo / senha
		if message[0] == 'add_client':
			c = Client(message[1],message[2],message[3])
			a = Account(message[4],flaot(message[5]),message[6])
			#account = account((self.bank._total_accounts +1))
			#a = Account(number, p, balance, password, 1000.0)
			if not (b.add_client(c) and b.add_account(a)):
				con.send('True'.encode())
			else:
				con.send('Erro no cadastro'.encode())

		#withdraw = Sacar
		elif message[0] == 'withdraw':
			account = self.banco.get_account_2(message[1])
			if account.withdraw(float(message[2])):
				self.connectionServ.send('True'.encode())
			else: 
				self.connectionServ.send('Erro no saque'.encode())

		#depositar
		elif message[0] == 'deposit':
			account = self.bank.get_account_2(message[1])
			account.deposit(float(message[2]))
			self.connectionServ.send("True".encode())

		#transferir
		elif message[0] == 'transfer':
			print("ainda n")

		#historico
		elif message[0] == 'extract':
			account = self.bank.get_account_2()
			message[1] = account

		#Logar
		elif message[0] == 'autenctic':
			authenticated = self.bank.login(message[1],message[2])  #pelo numero da conta
			if (authenticated):
				print('Acesso permitido')
				self.connectionServ.send('True'.encode())
			else: 
				self.connectionServ.send('Conecção invalida'.encode())

		#mydice meus dados
		elif message[0] == 'myDice':
			account = self.bank.get_account_2()
			message[1] = account.holder.name
			message[2] = account.holder.surname
			message[3] = account.holder.cpf
			message[4] = account.holder.number
			message[5] = (str(account.balance))
			message[6] = (str(account.limit))

		#balance Saldo
		elif message[0] == 'balance':
			account = self.bank.get_account_2()
			valueBalance = '{}'.format(account.balance)
			self.connectionServ.send(valueBalance.encode())

	def servClose(self):
		self.servSocket.close()
		print("Server finalizado.")


if __name__ == "__main__":
	serv = conectServ()
	serv.connectionServ()
	runing = True
	while(runing):
		serv.communication()
	serv.servClose()



"""
class Serve:
	def __init__(self):
		self.host = 'localhost'
		self.port = 8000
		self.addr = (self.host, self.port)
		self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.b = Bank()

	def run(self):
		self.serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.serv_socket.bind(self.addr)
		self.serv_socket.listen(10)
		print("aguardando conexao")
		self.start()

	def start(self):
		con, client = self.serv_socket.accept()
		print("Conectando")
		print("Aguardando mensagem")
		startTrue = True
		while(startTrue):
			recebe = con.recv(1024)
			print("Cliente: " + recebe.decode())
			if (recebe.decode() == ''):
				startTrue = False
			elif (recebe.decode() == 'add cliente'):
				name = recebe.decode()
				surname = recebe.decode()
				cpf = recebe.decode()
				number = recebe.decode()
				value = recebe.decode()
				password = recebe.decode()
				p = Client(name, surname, cpf)
				if not self.bank.get_client(p.cpf):
					balance = float(value)
					a = Account(number, p, balance, password, 1000.0)
				if not self.bank.get_account(a.number):
					self.bank.add_client(p)
					self.bank.add_account(a)

serv = Serve()
serv.run()
#enviar = None
#
#while enviar != '':
#	recebe = con.recv(1024)
#	if (recebe.decode() != ''):
#		enviar = input("Enviar Mensagem:")
#		con.send(enviar.encode())
#	else:
#		print('fim...')
#		serv_socket.close()
#		break
#
#"""