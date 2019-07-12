def Rotate(matrix):
	"""Return the roattion matrix of matrix
	>>> Rotate([[1,2,3], [2,2,2], [3,4,5]])
	[[3, 2, 5], [2, 2, 4], [1, 2, 3]]
	"""
	return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1, -1,-1)]

if __name__ == '__main__':
	import doctest
	doctest.testmod()
