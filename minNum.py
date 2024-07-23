def findMin(array):
	res = float('inf')

	for num in array:
		if num < res:
			res = num
	return res

print(findMin([2,1,0]))