# "Check if Number and its double exists
# Given an array arr of integers, check if there exists two integers N and M

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5, that is, 10 = 2 * 5.

# Example 2:
# Input: arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7, that is, 14 = 2 * 7.

# /Example 3:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M."

def checkDub(arr):
    double = {}

    for num in arr:
        if num * 2 in double or num / 2 in double and num != 0:
            return True
        double[num] = double.get(num, 0) + 1
    for k, v in double.items():
        if k == 0 and v > 1:
            return True
    return False

print(checkDub([5,2,3,0,0]))