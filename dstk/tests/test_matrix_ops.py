import pytest
from dstk.matrix_ops import *
import numpy as np

def test_oneHotEncode():
	data = ['hello', 'goodbye', 'hello', 'later']
	matrix = np.matrix([[False, True, False, False], [True, False, True, False], [False, False, False, True]])
	assert np.array_equal(one_hot_encode(data), matrix)

def test_isRowEchelon():
	matrix1 = np.matrix([[3.,-9,12,-9,6,15], [0,1,-2,2,1,-3], [0,0,0,0,1,4]])
	matrix2 = np.matrix([[3.,14,4,-9,6,15], [0,0,0,0,0,0], [0,1,-2,2,1,-3], [0,0,0,0,1,4]])
	matrix3 = np.matrix([[3.,-9,9,-9,2,7], [0,0,0,0,1,3], [0,1,-2,5,1,-3]])

	assert(is_row_echelon(matrix1))
	assert(not is_row_echelon(matrix2))
	assert(not is_row_echelon(matrix3))

def test_rowEchelon():
	matrix1 = np.matrix([[1., 3, 1, 9], [1, 1, -1, 1], [3, 11, 5, 35]])
	assert (is_row_echelon(row_echelon_form(matrix1)))

def test_isReducedRowEchelon():
	matrix1 = np.matrix([[3.,-9,12,-9,6,15], [0,2,-2,2,1,-3], [0,0,0,0,1,4]])
	matrix2 = np.matrix([[1.,-3,6,-9,6,15], [0,1,-2,5,1,-3], [0,0,0,0,1,4]])

	assert(not is_reduced_row_echelon(matrix1))
	assert(is_reduced_row_echelon(matrix2))

def test_reducedRowEchelon():
	matrix = np.matrix([[2., 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]])
	m1 = reduced_row_echelon(matrix)
	assert(is_reduced_row_echelon(m1))

def test_solveSystem():
	eq1 = '2x + y - z = 8'
	eq2 = '-3x - y + 2z = -11'
	eq3 = '-2x + y + 2z = -3'
	ans = {}
	ans['x'] = 2
	ans['y'] = 3
	ans['z'] = -1
	assert(np.isclose(solve_system([eq1,eq2,eq3]), ans))