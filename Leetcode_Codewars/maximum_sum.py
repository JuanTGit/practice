# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def maxSequence(arr):
    maxl = 0
    maxg = 0
    for n in arr:
        maxl = max(0, maxl + n)
        maxg = max(maxg, maxl)
    return maxg



arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSequence(arr1))


# procedure maxSequence(arr)
# 1. set maxSeq and currSeq to 0 // since we should return only positive numbers or 0
# 2. for each element in arr
# A. if 0 < element + currSeq: then currSeq = element + currSeq
# B. if currSeq > maxSeq: then maxSeq = currSeq
# 3. return maxSeq