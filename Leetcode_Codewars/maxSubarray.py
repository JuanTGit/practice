# 53. Maximum Subarray
# Medium

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:

# Input: nums = [1]
# Output: 1

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

def maxSubarray(nums):
    maxCount = lastSum  = nums[0]

    for num in nums[1: ]:
        if lastSum >= 0:
            lastSum += num
        else:
            lastSum = num 

        maxCount = max(maxCount, lastSum)

    return maxCount

def maxSub(nums):
    maximum = nums[0]
    currSum = 0

    for num in nums:
        if currSum < 0:
            currSum = 0
        currSum += num
        maximum = max(maximum, currSum)
    return maximum