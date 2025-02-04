

def selectionSort(array):

	for i in range(len(array) - 1):
		smallest = [float("inf"), float('inf')]
		for j in range(i+1, len(array)):
			if array[j] < smallest[0]:
				smallest[0], smallest[1] = array[j], j
				
		if array[i] > smallest[0]:
			array[i], array[smallest[1]] = array[smallest[1]], array[i]

