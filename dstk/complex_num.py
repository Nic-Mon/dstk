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
		return self

	def subtract(self, other_complex):
		self.real -= other_complex.real
		self.imaginary -= other_complex.imaginary
		return self

	def __eq__(self, other):
		"""Override the default Equals behavior"""
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		return False

	def __ne__(self, other):
		"""Define a non-equality test"""
		return not self.__eq__(other)

