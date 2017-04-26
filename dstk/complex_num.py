from math import sqrt

class complex_num():

	def __init__(self, r, i):
		self.real = r
		self.imaginary = i

	def absolute_val(self):
		return sqrt(self.real*self.real + self.imaginary*self.imaginary)

