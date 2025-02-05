matrix = [
    [0, -1, -2, -3],
    [4, 5, 6, 7],
    [2, 3, -2, -3],
    [42, 100, 30, -42]
]


def transposeMatrix(matrix):
    
	res = [[] for _ in range(len(matrix[0]))]
	print(res)

	# for row in matrix:
	# 	print(row)
	# 	for col in row:
	# 		print(col)
	# 	print('----------')


print(transposeMatrix(matrix))