'''
Class Extract: Essa classe é utilizada para o extrato da conta
'''

import datetime

class Extract:
	__slots__ = ['_open_date', '_extract']

	def __init__(self):
		self._open_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
		self._extract = []

	@property
	def openDate(self):
		return self._open_date

	# adiciona uma transição na lista
	def add_extract(self, str):
		self._extract.append(str)

	# Informa todas as operações realizadas na conta
	def display_extract(self):
		text = ''
		text += 'Data de abertura {}\n'.format(self._open_date)
		text += 'Transações: \n'
		for t in self._extract:
			text += ' ' + t
		return text
