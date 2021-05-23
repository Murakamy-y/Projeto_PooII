import datetime


class Extract:
	__slots__ = ['_open_date', '_extract']

	def __init__(self):
		self._open_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
		self._extract = []

	@property
	def openDate(self):
		return self._open_date

	def add_extract(self, str):
		self._extract.append(str)

	def display_extract(self):
		text = ''
		text += 'Data de abertura {}\n'.format(self._open_date)
		text += 'Transações: \n'
		for t in self._extract:
			text += ' ' + t
		return text
