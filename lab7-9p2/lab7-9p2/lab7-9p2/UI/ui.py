from UI.console import Console
from Service.service_students import ServiceStudents
from Service.service_problems import ServiceProblems
from Errors.errors import ValidationError

class UI:
	def __init__(self, console: Console, service_students: ServiceStudents, service_problems: ServiceProblems):
		self.__console = console
		self.__service_students = service_students
		self.__service_problems = service_problems

		console.register_function(self.show_students, 'shows', 'show list of students')
		console.register_function(self.show_problems, 'showp', 'show list of problems')
		console.register_function(self.add_student, 'adds', 'add student in list')
		console.register_function(self.add_problem, 'addp', 'add problem in list')
		console.register_function(self.delete_student, 'dels', 'delete student from list')
		console.register_function(self.modify_student, 'mods', 'modify student from list')

	def start(self):
		self.__console.start()

	def show_students(self, param: list):
		for stud in self.__service_students.get_students():
			print(stud)

	def show_problems(self, param: list):
		for prob in self.__service_problems.get_problems():
			print(prob)

	def add_student(self, param: list):
		try:
			name = input('enter name: ')
			group = input('enter group: ')
			self.__service_students.add_student(name, group)
		except ValidationError as e:
			print(str(e))

	def delete_student(self, param: list):
		try:
			name = input('enter name to delete: ')
			group = input('enter group to delete: ')
			self.__service_students.delete_student(name, group)
		except ValidationError as e:
			print(str(e))

	def modify_student(self, param: list):
		try:
			name = input('enter name to modify: ')
			group = input('enter group to modify: ')
			new_name = input('enter new name: ')
			new_group = input('enter new group: ')
			self.__service_students.modify_student(name, group, new_name, new_group)
		except ValidationError as e:
			print(str(e))

	def add_problem(self, param: list):
		try:
			lab_nr = int(input('enter lab number: '))
			desc = input('enter description: ')
			deadline = int(input('enter deadline: '))
			self.__service_problems.add_problem(lab_nr, desc, deadline)
		except ValidationError as e:
			print(str(e))

	def delete_problem(self, param: list):
		try:
			name = input('enter name to delete: ')
			group = input('enter group to delete: ')
			self.__service_students.delete_student(name, group)
		except ValidationError as e:
			print(str(e))
