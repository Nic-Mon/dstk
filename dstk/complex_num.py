from math import sqrt

class complex_num():
	'class to understand complex numbers'

	def __init__(self, r, i):
		self.real = r
		self.imaginary = i

	def absolute_val(self):
		return sqrt(self.real*self.real + self.imaginary*self.imaginary)

	def add(self, other_complex):
		self.real += other_complex.real
		self.imaginary += other_complex.imaginary

	def subtract(self, other_complex):
		self.real -= other_complex.real
		self.imaginary -= other_complex.imaginary