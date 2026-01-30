# Rotate Array
# Medium
# Company Tags
# You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7,8], k = 4

# Output: [5,6,7,8,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [8,1,2,3,4,5,6,7]
# rotate 2 steps to the right: [7,8,1,2,3,4,5,6]
# rotate 3 steps to the right: [6,7,8,1,2,3,4,5]
# rotate 4 steps to the right: [5,6,7,8,1,2,3,4]

# Example 2:

# Input: nums = [1000,2,4,-3], k = 2

# Output: [4,-3,1000,2]
# Explanation:
# rotate 1 steps to the right: [-3,1000,2,4]
# rotate 2 steps to the right: [4,-3,1000,2]

# Constraints:

# 1 <= nums.length <= 100,000
# -(2^31) <= nums[i] <= ((2^31)-1)
# 0 <= k <= 100,000
# Follow up: Could you do it in-place with O(1) extra space?

# Test Cases
nums = [1,3,5,7,9]; k = 4


def rotate(nums, k):
	k = k % len(nums)
	nums.reverse()

	l, r = 0, k-1
	l2, r2 = k, len(nums) - 1

	while r > l:
		nums[l], nums[r] = nums[r], nums[l]
		l += 1
		r -= 1
	
	while r2 > l2:
		nums[l2], nums[r2] = nums[r2], nums[l2]
		l2 += 1
		r2 -= 1

	return nums


# print(rotate(nums, k))

nums = [1,2,3,4,5,6,7]; k = 3

def rotate5(nums, k):
	def twoPointer(l, r):
		while r > l:
			nums[l], nums[r] = nums[r], nums[l]
			l, r = l + 1, r - 1

	twoPointer(0, k - 1)

	twoPointer(k, len(nums) - 1)

	return nums

print(rotate5(nums, k))