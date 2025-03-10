# Return maximum number of consecutive 1's in the array
# input: [1,1,0,1,1,1]
# output: 3


def max_ones(arr):
	cur_max = 0
	l, r = 0, 0

	while r < len(arr):
		if arr[r] == 0:
			cur_max = max(cur_max, r - l)
			l = r + 1
		r += 1
	cur_max = max(cur_max, r - l)
	return cur_max


print(max_ones([1,1,0,1,1,1]))