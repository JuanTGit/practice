"""
The Binary Search algorithim works by finding the number in the middle of a given
array and comparing it to the target. Given that the array is sorted.
https://www.cs.usfca.edu/~galles/visualization/Search.html
Higher or Lower

Worst case run time: O(log(n)) - Logarithmic
"""

def binary_search(array, target):
    # Index pointers
    high = len(array) - 1
    low = 0
    print(high)
    while low <= high:
        # Continues to decrease until middle is found
        middle = (low + high) // 2
        print(middle)
        if target == array[middle]:
            return f'The index for {target} is {middle}'
        # If our target is less then our middle we update our high to the middle - 1
        elif target < array[middle]:
            high = middle - 1
        # If higher update low to middle + 1
        else:
            low = middle + 1
    # If target is not found return -1
    return -1

ordered_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12]

print(binary_search(ordered_list, 6))