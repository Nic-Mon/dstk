import pytest
from dstk.matrix_ops import one_hot_encode
import numpy as np

def test_oneHotEncode():
	data = ['hello', 'goodbye', 'hello', 'later']
	matrix = np.matrix([[False, True, False, False], [True, False, True, False], [False, False, False, True]])
	assert np.array_equal(one_hot_encode(data), matrix)