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
		i_max  = np.argmax (abs(matrix[k:,k]))
		i_max = k+i_max
		matrix[[k, i_max]] = matrix[[i_max, k]]

		for i in range(k+1, m):
			f = matrix[i, k] / matrix[k, k]
			for j in range(k+1, n):
				matrix[i,j] = matrix[i,j] - (matrix[k,j]*f)
			matrix[i,k] = 0
	return matrix

def is_row_echelon(matrix):
	'''returns true if matrix is in row echelon form, else False'''
	m, n = matrix.shape
	zeros_flag = False
	#check all zeros rows at bottom
	for row in range(m):
		if (np.count_nonzero(matrix[row,:]) != 0): 
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

def is_reduced_row_echelon(matrix):
	if(not is_row_echelon(matrix)):
		return False
	m,n = matrix.shape
	leading_coef_col = -1
	for row in range(m):
		for col in range(n):
			if (matrix[row, col] != 0):
				if (matrix[row, col] != 1): return False
				break
	return True

def reduced_row_echelon(matrix):
	mat = row_echelon_form(matrix)
	m,n = mat.shape
	for row in range(m):
		for col in range(n):
			if (mat[row, col] != 0):
				piv = mat[row, col]
				mat[row, :] = mat[row,:]/piv
				prow = mat[row, :]
				for r in range(row):
					mat[r,:] = mat[r,:] - mat[r,col]*prow
				break
	return mat

def read_eq_string(eq_str):
	'''only works with 3 vars x, y, z'''
	var_list = eq.split(' ')
	rm_indexes = []
	for i, item in enumerate(var_list):
		if item == '-':
			var_list[i+1] = '-' + var_list[i+1]
			rm_indexes.append(i)
		elif(item[:2] == '--'):
			item = item[2:]
		elif(item == '+' or item == '='):
			rm_indexes.append(i)
	for i in reversed(rm_indexes):
		del rm_indexes[i]

	arr = np.array([0,0,0,0])
	for item in var_list:
		if item[-1] == 'x':
			arr[0] = float(item[:-1])
		elif item[-1] == 'y':
			arr[1] = float(item[:-1])
		elif item[-1] == 'z':
			arr[2] = float(item[:-1])
	arr[-1] = float(item[-1])
	return arr

def solve_system(eq_list):
	'''solve system of eqs'''
	mat = []
	for eq in eq_list:
		mat.append(read_eq_string(eq))
	matrix = np.matrix(mat)
	matrix = reduced_row_echelon(matrix)
	d = {}
	d['x'] = matrix[0,3]
	d['y'] = matrix[1,3]
	d['z'] = matrix[2,3]
	return d