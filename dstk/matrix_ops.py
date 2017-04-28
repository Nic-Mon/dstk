import numpy as np

def one_hot_encode(data):
	'''takes list of data, returns data one hot encoded into a numpy matrix'''
	unique_elements = reversed(list(set(data)))
	print(unique_elements)
	matrix = []
	for item in unique_elements:
		line = []
		for d in data:
			line.append(item == d)
		matrix.append(line)
	return np.matrix(matrix)

