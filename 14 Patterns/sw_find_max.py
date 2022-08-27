# Find the maximum sum in k amount:

# Example:

# arr = [2, 3, 5, 7, 10, 1, 4] k = 3
# output = 22


# Bubble sort grab last 3
def bubbleMax(arr, k):
    if k < 1:
        return ''

    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False
    return sum(arr[k+1:])


arr1 = [2, 3, 5, 7, 10, 1, 4]

# print(bubbleMax(arr1, 3))

# ============================================================
# Sliding Window
def slidingMax(arr, k):
    output = []
    l = 0
    r = 0
    total = 0
    while r < len(arr):
        for i in range(len(arr[:k])):
            total += arr[i]
            r += 1
            l += 1
    return total

print(slidingMax(arr1, 3))