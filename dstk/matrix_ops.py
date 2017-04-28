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

def row_echelon_form(matrix):
	'''returns row echelon form matrix'''
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
		for i in range(k+1, m):
			print(matrix[i, k])
			print(matrix[k, k])
			f = matrix[i, k] / matrix[k, k]
			for j in range(k+1, n):
				matrix[i,j] = matrix[i,j] - (matrix[k,j]*f)
			matrix[i,k] = 0
			print(matrix)
	return matrix

def is_row_echelon(matrix):
	'''returns true if matrix is in row echelon form, else False'''
	m, n = matrix.shape
	zeros_flag = False
	#check all zeros rows at bottom
	for row in range(m):
		print(matrix[row,:])
		print(np.array_equal(matrix[row,:], np.zeros(n)))
		if (not np.array_equal(matrix[row,:], np.zeros(n))): 
			if zeros_flag: return False
		else:
			zeros_flag = True

	#check leading coefficients of lower rows much be strictly to the right of leading coefficients of higher rows
	i = -1
	for row in range(m):
		for col in range(n):
			if (matrix[row,col] != 0):
				if(col < i): return False
				i = col
				break
	return True

