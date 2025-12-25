
# O(n) time / O(n) space
def firstDuplicateValue(array):
    seen = set()

    for i in range(len(array)):
        if array[i] in seen:
            return array[i]
        seen.add(array[i])

    return -1


# O(n) time / O(1) space
def firstDuplicateValue(array):
    
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1
