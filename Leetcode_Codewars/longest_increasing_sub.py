# 300. Longest Increasing Subsequence
# Medium

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1


def longestIncreasingSub(nums):
    # Create a new list of ones at the length of our input. because our longest will atleast be 1.
    LIS = [1] * len(nums)

    # Loop through our list in reverse order.
    for i in range(len(nums) -1, -1, -1):
        # Double loop through our list at index i + 1 to the end of our array.
        for j in range(i + 1, len(nums)):
            # If going in reverse order if our nums[i] < nums[j]:
            if nums[i] < nums[j]:
                # Set the index in our new list LIS to the bigger number, If 1 + LIS[j], we are adding to what we already know. If at LIS[j] has a value greater than 1,
                # we can assume the numbers will be in order because nums[i] < nums[j]
                LIS[i] = max(LIS[i], 1 + LIS[j])
    # Return the maximum in the array.
    return max(LIS)


#===========================================================================================
def longestIncreasingSubsequence(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size