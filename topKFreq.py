
nums = [1, 1, 1, 2, 2, 3]
k = 2

def top_k_frequent(nums, k):
	timesSeen = {}
	freq = [[] for i in range(len(nums))]

	for num in nums:
		timesSeen[num] = timesSeen.get(num, 0) + 1
	
	for n, c in timesSeen.items():
		freq[c-1].append(n)

	res = []

	for item in range(len(freq) -1, -1, -1):
		for n in freq[item]:
			res.append(n)
			if len(res) == k:
				return res


print(top_k_frequent(nums, k))