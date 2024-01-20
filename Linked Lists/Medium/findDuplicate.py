# 287. Find the Duplicate Number
# Medium

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

def findDupe(nums):
    l = 0
    
    while l < len(nums) - 1:
        for r in range(l, len(nums)):
            if nums[l] == nums[r] and l != r:
                return nums[r]
        l += 1

print(findDupe([3,1,3,4,2]))



def findDupe2(nums):
    # First Detect a cycle 
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Next find where the cycle intersects and return the duplicate
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow
        
print(findDupe2([3,1,3,4,2]))




nums = [3,1,3,4,2]