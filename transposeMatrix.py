matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = [
	[1, 4],
	[2, 5],
	[3, 6]
]

def transposeMatrix(matrix):
	res = [[] for _ in matrix[0]]

	for row in matrix:
		for col in range(len(row)):
			res[col].append(row[col])
			

	return res



print(transposeMatrix(matrix))