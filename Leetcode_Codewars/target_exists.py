# Here is another challenge for today to make up for yesterday! This one is a little easier.
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If targetexists, then return its index. Otherwise, return -1.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

def targetExists(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
    return -1

nums = [-1,0,3,5,9,12]
target = 9

print(targetExists(nums, target))
