def topKFrequent(nums, k):
	count = {}
	res = [[] for i in range(len(nums) + 1)]
	for num in nums:
		count[num] = count.get(num, 0) + 1

	print(count)
	
	for key, v in count.items():
		res[v].append(key)
	
	result = []
	print(res)
	for i in range(len(res) -1, -1, -1):
		for num in res[i]:
			result.append(num)
			if len(result) == k:
				return result

	return result

		
	
	



print(topKFrequent([1,2], 2))