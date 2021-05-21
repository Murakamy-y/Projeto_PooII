import socket

host = 'localhost'
port = 8000


class ClientHost(object):
	def __init__(self):
		self.addr = None
		self.clientSocket = None

	def connectClient(self):	
		self.addr = (host, port)  # define a tupla de endereco
		self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que eh TCP/IP
		self.clientSocket.connect(self.addr)
		
	def submit(self, push: str):
		self.clientSocket.send(push.encode())
		push = self.clientSocket.recv(1024).decode()
		return push
	
	def close(self):
		self.clientSocket.close()
