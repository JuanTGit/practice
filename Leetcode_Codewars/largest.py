# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

# Example 1:
# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.

# Example 2:
# Input: nums = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.

def isLargest(nums):
    numDict = {}

    for i in nums:
        numDict[i] = numDict.get(i, 0) + 1
    ones = [k for k in numDict if numDict[k] == 1]
    return max(ones) if ones else -1

nums = [5,7,3,9,4,9,8,3,1]

print(isLargest(nums))
#=======================================================
def largestUniqueNumber(arr):
        unique = set()
        dup = set()
        for i in arr:
            if i not in unique:
                unique.add(i)
            else:
                dup.add(i)  
        res = unique - dup
        if res:
            return max(res)
        return -1