import pytest
from dstk.xnary import binary

def test_canInstantiateBinary():
	binary_num = xnary(2, 42)

def test_canInstantiate5nary():
	fivenary = xnary(5,234)

def test_binaryToString():
	binary_fifty = xnary(2,50)
	assert(str(binary_fifty) == '110010')

def test_4narytoString():
	fournary_fortytwo = xnary(4,242)
	assert(str(fournary_fortytwo) == '3302')
