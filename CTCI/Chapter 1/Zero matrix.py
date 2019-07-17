def zero_matrix(matrix):
	M = len(matrix)
	N = len(matrix[0])

	rows = []
	columns = []

	for x in range(M):
		for y in range(N):
			if matrix[x][y] == 0:
				rows.append(x)
				columns.append(y)
	for row in rows:
	    for i in range(len(matrix[0])):
        	matrix[row][i] = 0
	for column in columns:
	    for i in range(len(matrix)):
	        matrix[column][i] = 0

	return matrix

matrix = [[1,0,3,4],[2,3,0,5],[1,2,3,5]]
print(zero_matrix(matrix))