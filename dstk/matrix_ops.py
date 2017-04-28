import numpy as np

def one_hot_encode(data):
	'''takes list of data, returns data one hot encoded into a numpy matrix'''
	unique_elements = list(sorted(set(data)))
	print(unique_elements)
	matrix = []
	for item in unique_elements:
		line = []
		for d in data:
			line.append(item == d)
		matrix.append(line)
	return np.matrix(matrix)

def row_reduce(matrix):
	'''returns row reduced matrix'''
	m, n = matrix.shape
	for k in range(min(m,n)):
		print(k)
		print(matrix[k:,k])
		i_max  = np.argmax (abs(matrix[k:,k]))
		print(i_max)
		print(i_max is None)
		i_max = k+i_max
		matrix[[k, i_max]] = matrix[[i_max, k]]
		print(matrix)
		for i in range(k, m):
			f = matrix[i, k] / matrix[k, k]
			for j in range(k, n):
				matrix[i,j] = matrix[i,j] - matrix[k,j]*f
			matrix[i,k] = 0
	return matrix