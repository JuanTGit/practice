array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
array = str(array)

for i in range(len(array)):
	if array[i].isalnum():
		print(array[i])
