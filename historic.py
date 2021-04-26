import datetime


class Historic:
	def __init__(self):
		self._open_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
		self.extract = []
	
	def add_extract(self, str):
		self.extract.append(str)

	def display_extract(self):
		print('Data abertura: {}'.format(self._open_date))
		print('Transações: ')
		for t in self.extract:
			print('-', t)
