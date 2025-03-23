array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]



def spiralTraverse(array):

	seen = set()

	for r in range(len(array)):
		print(f"Row: {r}")

		for c in range(len(array[r])):
			print(c)


print(spiralTraverse(array))