import pytest

def test_canCreateComplex():
	two = complex(2, 0)

def test_absFunctionsCorrectlyOnRealOnly():
	four = complex(4,0)
	assertEquals(four.abs(), 4)

def test_absFunctionsCorrectlyOnImaginaryOnly():
	Ithree = complex(0,3)
	assertEquals(3, Ithree.abs())

def test_absFunctionsCorrectly():
	num = complex(3,4)
	assertEquals(num.abs(), 5)