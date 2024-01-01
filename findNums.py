# 448. Find All Numbers Disappeared in an Array
# Easy

# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]

nums = [4,3,2,7,8,2,3,1]
nums2 = [1, 1]

def findDisappearedNumbers(nums):
    numSort = sorted(nums)
    res = []
    for i in range(1, numSort[-1] + 1):
        if i not in nums:
            res.append(i)
    return res

print(findDisappearedNumbers(nums2))