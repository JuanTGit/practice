# Create a bubble sort algorithim

def bubble_sort(arr):
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False

unsorted = [6, 2, 59, 13, 1, 19]
bubble_sort(unsorted)
print(unsorted)


# Create an insertion sort algorithim

def insertion_sort(arr):
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
unsortedlist = [83, 19, 338, 29, 1, 3, 6, 10]
insertion_sort(unsortedlist)
print(unsortedlist)


# Create a binary search algorithim

def binary_search(arr, target):
    high = len(arr) - 1
    low = 0

    while low <= high:
        middle = (low + high) // 2
        if target == arr[middle]:
            return f'Your number has been found: {target} at {middle}.'
        elif target <= arr[middle]:
            high = middle-1
        else:
            low = middle+1
    return -1

print(binary_search(unsortedlist, 29))







# Bubble Sort

def bubble_sort(arr):
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False