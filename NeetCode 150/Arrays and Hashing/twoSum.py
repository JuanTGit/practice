def twoSum(nums, target):
	hashSet = {}

	for i in range(len(nums)):

		if target - nums[i] in hashSet:
			return [i, hashSet[target - nums[i]]]
		
		hashSet[nums[i]] = i
		