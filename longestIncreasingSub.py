# You are given an array of integers arr, return the length of the longest continuous increasing subarray.
# A continuous increasing subarray is defined as 2 or more consecutive indices such that arr[i] < arr[i+1] .

# Case 1:
# Input: arr = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subarray is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subarray, it is not continuous as elements 5 and 7 are separated by element 4.

# Case 2:
# Input: arr = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subarray is [2] with length 1. Note that it must be strictly
# increasing.

def longestIncreasingSub(arr):
    start = 0
    output = 0
    if len(set(arr)) == 1:
        return 1
    for i in range(1, len(arr)):
        if arr[i-1] >= arr[i]:
            start = i
        if i+1-start > output:
            output = i+1-start
    return output

arr = [1,3,5,4,7]

print(longestIncreasingSub(arr))