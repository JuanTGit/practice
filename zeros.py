# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]
# Example Output: [11,2,3,4,0,0]

def moveZeros(arr):

    zeros = []
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            zeros.append(arr.pop(i))
    return arr + zeros

# print(moveZeros([11,2,3,4,0,0]))


# Modify list in place

def moveZerosIP(arr):
    left = 0

    for right in range(len(arr)):
        if arr[right] != 0 and arr[left] == 0:
            arr[right], arr[left] = arr[left], arr[right]
        
        if arr[left] != 0:
            left += 1
    
    return arr

print(moveZerosIP([0,1,0,4,6,28]))