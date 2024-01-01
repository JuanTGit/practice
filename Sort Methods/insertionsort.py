"""
Worst Case: O(n^2) Time - O(1) Space - Quadratic
"""
def insertionSort(array):
    # We start at index 1 because we are checking in reverse. If we start at index 0, we will encounter an error.
    for i in range(1, len(array)):
        # While our index is greater than index 0, and the integer in the current index is less than the integer before it; proceed the following code.
        while i > 0 and array[i] < array[i - 1]:
            # Swap the integers in the indices
            array[i], array[i - 1] = array[i - 1], array[i]
            # Continue to move back through the indices.
            i -= 1
    # Not necessary, generally a good rule of thumb to return your array.
    return array

randArray = [-1, -2, -8, -3, 5]

# for i in range(1, len(randArray)):
#     # if i > 0:
#     print(randArray[i])

print(insertionSort(randArray))