# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kthdistinct element.

# Example 1:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

# Example 2:
# Input: matrix = [[-5]], k = 1
# Output: -5


def kthSmallest(arr, k):
    n = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            n.append(arr[i][j])
        n.sort()
        return n[k-1]