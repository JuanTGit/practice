# 448. Find All Numbers Disappeared in an Array
# Easy

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:

# Input: nums = [1,1]
# Output: [2]

def findAllDisappeared(nums):
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])
    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i + 1)
    return res



nums = [4,3,2,7,8,2,3,1]
# print(findAllDisappeared(nums))

def findDisappearedN(nums):
    hashset = {}
    output = []
    for i in nums:
        hashset[i] = hashset.get(i, 0) + 1
    for i in range(1, len(nums) + 1):
        if i not in hashset:
            output.append(i)
    
    return output

# print(findDisappearedN(nums))


def findAllDisappeared2(nums):
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])
    
    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i+1)
    return res

print(findAllDisappeared2([1,2,4,4,5]))


def findDisappearedNumbersBF(nums):
    output = []
    for i in range(1, len(nums) + 1):
        if i not in nums:
            output.append(i)
    return output

print(findDisappearedNumbersBF([1,1,1]))


def findDisappearedNumbers(nums):
    numSort = sorted(nums)
    res = []
    for i in range(1, numSort[-1] + 1):
        if i not in nums:
            res.append(i)
    return res

# print(findDisappearedNumbers(nums2))