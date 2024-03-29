# 238. Product of Array Except Self
# Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

nums = [4, 5, 3, 6]
#      [0, 1, 2, 3]
def productArray(nums):
    res = [1] * (len(nums)) 
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


print(productArray(nums))


def prodOfArray2(arr):
    n = len(arr)
    output = [1] * n

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                output[i] = output[i] * arr[j]
        

    return output


print(prodOfArray2([1, 2, 3, 4]))