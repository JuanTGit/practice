# 169. Majority Element
# Easy
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

nums = [2,2,1,1,1,2,2,]
def majorityElement(nums):
    count = {}

    for n in nums:
        count[n] = count.get(n, 0) + 1
        if count[n] > len(nums) //2:
            return n
 

print(majorityElement(nums))


def majorityEl(nums):
    res, count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += (1 if res == n else -1)
    return res

print(majorityEl(nums))