import pytest
from complex_num import complex_num

def test_canCreateComplex():
	two = complex_num(2, 0)

def test_absFunctionsCorrectlyOnRealOnly():
	four = complex_num(4,0)
	assert four.absolute_val() == 4

def test_absFunctionsCorrectlyOnImaginaryOnly():
	Ithree = complex_num(0,3)
	assert 3 == Ithree.absolute_val()

def test_absFunctionsCorrectly():
	num = complex_num(3,4)
	assert num.absolute_val() == 5