# 283. Move Zeroes
# Easy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]


def moveZeroes(nums):
    l = 0

    for r in range(len(nums)):
        if nums[r] != 0:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1