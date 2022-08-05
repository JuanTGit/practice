"""
Most Optimal approach to a bubble sort is Quadratic
Worst Case: O(N^2) Time - O(1) Constant Space - Quadratic
Best Case: O(n) Linear Time - O(1) Constant Space - Linear
"""

def bubbleSort(arr):
    # Set sorted Variable == False to run through the loop at least once. Assume array is not sorted.
    isSorted = False
    # While isSorted is = to False
    while not isSorted:
        # Immediately assume the array is sorted to break the while loop once finished.
        isSorted = True
        # Loop through every index[i] in the 
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = False
