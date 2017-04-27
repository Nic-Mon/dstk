import pytest
from dstk.matrix_ops import one_hot_encode
import numpy as np

def test_oneHotEncode():
	data = ['hello', 'goodbye', 'hello', 'later']
	matrix = np.matrix([[True, False, True, False], [False, True, False, False], [False, False, False, True]])
	assert one_hot_encode(data) == matrix