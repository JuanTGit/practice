# Define a funtion

def binarySearch(arr, target):
    # Binary search finds a target by dividing the array in half
	# Create variable indices
	l = 0
	r = len(arr) - 1

	# While loop continues until conditions are true
	while l <= r:
		m = (l + r) // 2

		if arr[m] == target:
			return f'Target found idx: {m}'
		elif target < arr[m]:
			r = m - 1
		else:
			l = m + 1
	return -1


print(binarySearch([2, 4, 5, 19, 24, 99, 120, 348], 5))