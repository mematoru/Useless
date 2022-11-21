from Domain.student import Student
import itertools

class RepoStudents:
	def __init__(self):
		self._students = []

	def size(self):
		return len(self._students)

	def get_students(self):
		return self._students

	def find_student(self, student):
		for stud in self._students:
			if stud.get_name() == student.get_name() and stud.get_group() == student.get_group():
				return True
		raise ValueError('student not found')

	def add_student(self, student):
		self._students.append(student)

	def delete_student(self, student):
		if self.find_student(student):
			for indx, stud in enumerate(self._students):
				if stud.get_name() == student.get_name() and stud.get_group() == student.get_group():
					self._students.pop(indx)
					if not self.size():
						Student.id_counter = itertools.count(1)
					break

	def modify_student(self, student, new_student):
		if self.find_student(student):
			for stud in self._students:
				if stud.get_name() == student.get_name() and stud.get_group() == student.get_group():
					stud.set_name(new_student.get_name())
					stud.set_group(new_student.get_group())
					break