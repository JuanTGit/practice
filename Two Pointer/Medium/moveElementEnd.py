def moveElementToEnd(array, toMove):
    right = len(array)-1

    for i in range(len(array)-1):
        if array[i] == toMove:
            while array[right] == toMove and right > i:
                right -= 1
            if array[right] != toMove:
                array[i], array[right] = array[right], array[i]
    return array
            

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))