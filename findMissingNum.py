# 5. Find the Missing Number
# Problem: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example:

# Copy code
# Input: nums = [3, 0, 1]
# Output: 2

def findMissing(nums):
	setNums = set(nums)
	for num in range(len(nums) + 1):
		if num not in setNums:
			return num
 

print(findMissing([3, 0, 1]))