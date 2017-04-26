import pytest

def test_canCreateComplex():
	two = complex(2, 0)

def test_absFunctionsCorrectlyOnRealOnly():
	four = complex(4,0)
	assert four.abs() == 4

def test_absFunctionsCorrectlyOnImaginaryOnly():
	Ithree = complex(0,3)
	assert 3 == Ithree.abs()

def test_absFunctionsCorrectly():
	num = complex(3,4)
	assert num.abs() == 5