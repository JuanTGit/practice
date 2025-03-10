def insertion_sort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array

nums = [4, 672, 53, 72, 3, 267, 99, 2, 7]
insertion_sort(nums)
print(nums)