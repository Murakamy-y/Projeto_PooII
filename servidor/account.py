'''
class Account: Essa classe é utilizada a fim de cadastrar a conta que o cliente vai utilizar no banco.
'''

from extract import Extract
import datetime

class Account:

	_total_accounts = 0
	__slots__ = ['_number', '_holder', '_balance', '_limit', '_extract', '_password']

	def __init__(self, number, client, balance, password, limit=1000.0):
		'''
		DESCRIPTION:
			Essa classe é utilizada a fim de cadastrar a conta que o cliente vai utilizar no banco.
		'''
		self._number = number
		self._holder = client
		self._balance = balance
		self._limit = limit
		self._password = password
		self._extract = Extract()
		Account._total_accounts += 1


	@property
	def number(self):
		return self._number
	
	@property
	def holder(self):
		return self._holder

	@property
	def balance(self):
		return self._balance
	
	@property
	def limit(self):
		return self._limit

	@property
	def password(self):
		return self._password

	@property
	def extract(self):
		return self._extract

	def withdraw(self, value):
		'''
		:param value: float
			valor do tipo float
		:raise:
			aceita valores do tipo inteiro e flutuante

		:return:
			informa uma mensagem, avisando que a saque foi um sucesso.
			informa o restante do saldo presente na sua carteira após o termino da operação.
		'''

		if value < 0:
			return 'Valor sacado não pode ser negativo!'
		elif value > self._balance + self._limit:
			return 'Valor indisponível para saque!'
		else:
			self._balance -= value
			date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
			self._extract.add_extract(' - Sacou {} em {}\n'.format(value, date))
			return 'Saque realizado com sucesso!\nSaldo restante = {:.2f}'.format(self._balance)

	def deposit(self, value):
		'''
		:param value: float
			valor do tipo float
		:raise:
			aceita valores do tipo inteiro e flutuante

		:return:
			informa uma mensagem, avisando que o deposito foi um sucesso.
			informa o restante do saldo presente na sua carteira após o termino da operação.
		'''

		if value < 0:
			return 'Valor depositado não pode ser negativo!'
		else:
			self._balance += value
			date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
			self._extract.add_extract(' - Depositou {} em {}\n'.format(value, date))
			return 'Deposito realizado com sucesso!\nSaldo da conta = {:.2f}'.format(self.balance)

	def transfer(self, destiny, value):
		'''
		:param destiny: str
			valor do tipo str
		:param value: float
			valor do tipo float
		:raise:
			aceita valores de tipo str
			aceita valores do tipo inteiro e flutuante

		:return:
			informa uma mensagem, avisando que a transferencia foi um sucesso.
		'''
		
		if value < 0:
			return 'Valor a ser transferido não pode ser negativo!'
		elif value > self._balance + self._limit:
			return 'Valor indisponível para transferencia!'
		else:
			self._balance -= value
			destiny._balance += value
			date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
			# self._extract.add_extract(' - Sacou {} em {}\n'.format(value, date))
			self._extract.add_extract(' - Transferiu {:.2f} para conta {} em {}\n'.format(value, destiny._number, date))
			# destiny._extract.add_extract(' - Depositou {} em {}\n'.format(value, date))
			destiny._extract.add_extract(' - Recebeu {:.2f} por transferência da conta {} em {}\n'.format(value, self._number, date))
			return 'Transferencia realizada com sucesso!'

	#	contar a quantidade de contas
	@staticmethod
	def get_total_accounts():
		return Account._total_accounts
