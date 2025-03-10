# A binary search is checking whether a number is higher or lower in an array

def binarySearch(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = (low + high) // 2
        if target == array[middle]: # We want to check if our target is in the array at index middle because middle will stay the same.
            return f'Your target has been found at index {middle}.'
        elif target < array[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return - 1



search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(binarySearch(search, 13))