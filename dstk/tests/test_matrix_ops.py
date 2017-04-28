import pytest
from dstk.matrix_ops import one_hot_encode
from dstk.matrix_ops import is_row_echelon
from dstk.matrix_ops import row_echelon_form
import numpy as np

def test_oneHotEncode():
	data = ['hello', 'goodbye', 'hello', 'later']
	matrix = np.matrix([[False, True, False, False], [True, False, True, False], [False, False, False, True]])
	assert np.array_equal(one_hot_encode(data), matrix)

def test_isRowEchelon():
	matrix1 = np.matrix([[3,-9,12,-9,6,15], [0,1,-2,2,1,-3], [0,0,0,0,1,4]])
	matrix2 = np.matrix([[3,14,4,-9,6,15], [0,0,0,0,0,0], [0,1,-2,2,1,-3], [0,0,0,0,1,4]])
	matrix3 = np.matrix([[3,-9,9,-9,2,7], [0,0,0,0,1,3], [0,1,-2,5,1,-3]])

	assert(is_row_echelon(matrix1))
	assert(not is_row_echelon(matrix2))
	assert(not is_row_echelon(matrix3))

def test_rowEchelon():
	matrix1 = np.matrix([[1, 3, 1, 9], [1, 1, -1, 1], [3, 11, 5, 35]])
	assert (is_row_echelon(row_echelon_form(matrix1)))

def test_isReducedRowEchelon():
	matrix1 = np.matrix([[3,-9,12,-9,6,15], [0,2,-2,2,1,-3], [0,0,0,0,1,4]])
	matrix2 = np.matrix([[1,-3,6,-9,6,15], [0,1,-2,5,1,-3], [0,0,0,0,1,4]])

	assert(not is_reduced_row_echelon(matrix1))
	assert(is_reduced_row_echelon(matrix2))