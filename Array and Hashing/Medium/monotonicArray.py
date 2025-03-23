def isMonotonic(array):
    if len(array) <= 2: return True
    increasing = True
    decreasing = True

    for i in range(len(array)-1):
        if array[i] > array[i + 1]:
            decreasing = False
        elif array[i] < array[i + 1]:
            increasing = False
    if not increasing and not decreasing:
        return False
    return True