'''
Class Extract: Essa classe é utilizada para o extrato da conta
'''

import datetime


class Extract:
	__slots__ = ['_open_date', '_extract']

	def __init__(self):
		self._open_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S') # armazena o data e hora que a conta foi criada
		self._extract = []

	@property
	def openDate(self):
		return self._open_date

	def add_extract(self, str):
		'''
		DESCRIPTION:
			adiciona uma transição na lista
		'''

		self._extract.append(str)

	def display_extract(self, cpf):
		'''
		DESCRIPTION:
			Informa todas as operações realizadas na conta
		'''
		text = ''
		text += 'Data de abertura {}\n'.format(self._open_date)
		text += 'Transações: \n'
		for t in self._extract:
			text += ' ' + t
		return text
