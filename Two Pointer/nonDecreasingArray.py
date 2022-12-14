# 665. Non-decreasing Array
# Medium

# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.


def checkPossibility(nums):
    # Check if we've changed an element
    changed = False
    # Iterate through our input
    for i in range(len(nums) - 1):
        # Check if our next element is >= current element(If so continue to the next element).
        if nums[i] <= nums[i + 1]:
            continue
        # Check if we've updated our changed paramater(If so return False possibility).
        if changed:
            return False
        # Change our element = our lowest possible element to keep the array non-decreasing
        if i == 0 or nums[i + 1] >= nums[i - 1]:
            nums[i] = nums[i+1]
        else:
            nums[i+1] = nums[i]
        # Change our paramater to False
        changed = True
    # If we end our iteration we can return True
    return True