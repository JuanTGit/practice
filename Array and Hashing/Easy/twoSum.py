def twoSum(nums, target):
	hashTable = {}

	for i, num in enumerate(nums):
		if target - num in hashTable:
			return [hashTable[target - num], i]
		hashTable[num] = i
	

print(twoSum([2, 7, 11, 15], 9))