import itertools

class Student:
	id_counter = itertools.count(1)
	def __init__(self, name, group):
		self.__studentID = next(self.id_counter)
		self.__name = name
		self.__group = group

	def get_studentID(self):
		return self.__studentID

	def get_name(self):
		return self.__name

	def get_group(self):
		return self.__group

	def set_name(self, value):
		if value == '':
			raise ValueError('invalid data')
		self.__name = value

	def set_group(self, value):
		if value == '':
			raise ValueError('invalid data')
		self.__group = value

	def __str__(self):
		string = f'>ID:{self.get_studentID()} Name:{self.get_name()} Group:{self.get_group()}<'
		return string
