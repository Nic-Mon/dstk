from math import log

class xnary():
	'class to understand X-nary number representations (i.e. binary, trinary, etc.)'

	def __init__(self, n, value):
		self.n = n
		self.value = value

	def __int__(self):
		return value

	def __str__(self):
		x = self.value
		if x == 0:
			return '0'
		nums = []
		while x:
			x, r = divmod(x, self.n)
			nums.append(str(r))
		return ''.join(reversed(nums))
