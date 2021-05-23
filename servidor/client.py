'''
Class Client: Essa classe é utilizada com o intuito de cadastrar os cliente
'''

class Client:

	__slots__ = ['_name', '_surname', '_cpf']

	def __init__(self, name, surname, cpf):
		self._name = name
		self._surname = surname
		self._cpf = cpf

	@property
	def name(self):
		return self._name

	@property
	def surname(self):
		return self._surname

	@property
	def cpf(self):
		return self._cpf
