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
	
	def display_client(self):
		print('Nome: {}\nCPF: {}'.format(self._name + ' ' + self._surname, self._cpf))
