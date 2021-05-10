import datetime


class Historic:
	def __init__(self):
		self._open_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
		self.extract = []

	@property
	def openDate(self):
		return self._open_date

	def add_extract(self, str):
		self.extract.append(str)

	def display_extract(self):
		text = ''
		for t in self.extract:
			text += t
		return text
