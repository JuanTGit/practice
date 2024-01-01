# 75. Sort Colors
# Medium

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

def sortColors(nums):

    for i in range(1, len(nums)):
        while i > 0 and nums[i] < nums[i - 1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
    return nums

print(sortColors([2,0,2,1,1,0]))

def sortC(nums):
    low = 0
    high = len(nums) - 1
    mid = 0

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid +=1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

