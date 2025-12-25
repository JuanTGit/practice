array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]



def spiralTraverse(array):
	right = True
	left = False
	up = False
	down = False

	seen = set()

	for r in range(len(array)):
		# print(f"Row: {r}")

		for c in range(len(array[r])):
			if c == colLen:
				pass

			# if (r,c) in seen:

			# seen.add((r,c))


print(spiralTraverse(array))