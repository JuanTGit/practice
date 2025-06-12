# 3151. Special Array I
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# An array is considered special if the parity of every pair of adjacent elements is different. In other words, one element in each pair must be even, and the other must be odd.

# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

# Example 1:
# Input: nums = [1]
# Output: true
# Explanation:
# There is only one element. So the answer is true.

# Example 2:
# Input: nums = [2,1,4]
# Output: true
# Explanation:
# There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

# Example 3:
# Input: nums = [4,3,2,5,6]
# Output: false
# Explanation:
# nums[1] and nums[2] are both odd. So the answer is false.


# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def isArraySpecial(nums):
	if len(nums) <= 1: return True
	isEven = False
	if nums[0] % 2 == 0: isEven = True

	for i in range(1, len(nums)):
		if nums[i] % 2 == 0 and isEven:
			return False
		elif nums[i] % 2 != 0 and not isEven:
			return False
		else:
			isEven = not isEven

	return True
		

print(isArraySpecial([4,3,2,5,6,6]))