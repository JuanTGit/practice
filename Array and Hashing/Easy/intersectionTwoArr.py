# 349. Intersection of Two Arrays
# Easy
# Given two integer arrays nums1 and nums2, return an array of their 
# intersection
# . Each element in the result must be unique and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

def intersection(nums1, nums2):
	nums1Table = {}
	res = []

	for i in nums1:
		nums1Table[i] = nums1Table.get(i, 0) + 1

	for i in nums2:
		if i in nums1Table and i not in res:
			res.append(i)

	return res

print(intersection([1,2,2,1], [2,2]))