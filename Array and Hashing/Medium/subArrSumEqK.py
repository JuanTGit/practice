# 560. Subarray Sum Equals K
# Medium
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# O(n^2)

def subarraySum(nums, k):
    res = 0
    total = 0

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                res += 1
    return res

print(subarraySum([1,1,1], 2))


def subarrSum(nums, k):
    res = 0
    curSum = 0
    prefixSums = { 0 : 1 }

    for n in nums:
        curSum += n
        diff = curSum - k

        res += prefixSums.get(diff, 0)
        prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

    return res

print(subarrSum([1,1,1], 2))
