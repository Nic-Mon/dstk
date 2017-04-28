import pytest
from dstk.matrix_ops import one_hot_encode
from dstk.matrix_ops import row_reduce
import numpy as np

def test_oneHotEncode():
	data = ['hello', 'goodbye', 'hello', 'later']
	matrix = np.matrix([[False, True, False, False], [True, False, True, False], [False, False, False, True]])
	assert np.array_equal(one_hot_encode(data), matrix)

def test_rowReduce():
	matrix1 = np.matrix([[1, 3, 1, 9], [1, 1, -1, 1], [3, 11, 5, 35]])
	matrix2 = np.matrix([[1, 0, -2, -3], [0, 1, 1, 4], [0, 0, 0, 0]])
	assert (row_reduce(matrix1) == matrix2)



