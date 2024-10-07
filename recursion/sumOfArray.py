# Problem: Sum of an Array
# Write a recursive function that calculates the sum of all elements in an array.

# Example:
# Input: [1, 2, 3, 4, 5]
# Output: 15 (since 1 + 2 + 3 + 4 + 5 = 15)

def sumArr(nums):
	if len(nums) == 0:
		return 0
	
	return nums[0] + sumArr(nums[1:])
