# Majority Element II
# Medium
# You are given an integer array nums of size n, find all elements that appear more than ⌊ n/3 ⌋ times. You can return the result in any order.

# Example 1:

# Input: nums = [5,2,3,2,2,2,2,5,5,5]

# Output: [2,5]
# Example 2:

# Input: nums = [4,4,4,4,4]

# Output: [4]
# Example 3:

# Input: nums = [1,2,3]

# Output: []
# Constraints:

# 1 <= nums.length <= 50,000.
# -1,000,000,000 <= nums[i] <= 1,000,000,000
# Follow up: Could you solve the problem in linear time and in O(1) space?

def majorityElement(nums):
	res, minimum = [], len(nums)//3
	ignoreList = set()
	
	seen = {}

	for num in nums:
		seen[num] = seen.get(num, 0) + 1

		if seen[num] > minimum and num not in ignoreList:
			res.append(num)
			ignoreList.add(num)

	return res

print(majorityElement([1,2,3]))


# Time/space = O(n) Linear. Use Boyer-Moore Voting Algorithm to get O(1) Space and O(n) time
