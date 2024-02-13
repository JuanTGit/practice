# 209. Minimum Size Subarray Sum
# Medium

# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Brute Force
def minSub(nums, target):
	res = float('inf')
	total = 0

	for n in range(len(nums)):
		for j in range(n, len(nums)):
			total += nums[j]
			if total >= target:
				res = min(res, j - n + 1)
				break
		total = 0
	return res if res != float('inf') else 0

# Sliding Window
def minSubArrayLength(t, nums):
    res = float('inf')
    l = 0
    total = 0

    for i in range(len(nums)):
        total += nums[i]
        while total >= t:
            res = min(res, i - l + 1)
            total -= nums[l]
            l += 1
    return res if res != float('inf') else 0
# print(minSubArrayLength(7, [2,3,1,2,4,3]))

def minSubArrayLen(t, nums):
    res = float('inf')
    left = 0
    total = 0

    for i in range(len(nums)):
        total += nums[i]
        while total >= t:
            res = min(res, i - left + 1)
            total -= nums[left]
            left += 1
    return res




print(minSubArrayLen(7, [2,3,1,2,4,3]))