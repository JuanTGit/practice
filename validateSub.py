def isValidSubsequence(array, sequence):
    l = 0
    for l2 in range(len(array)):
        if sequence[l] == array[l2]:
            if l == len(seq):
                return True
            else:
                l += 1
    return False

array = [5, 1, 22, 25, 6, -1, 8, 10],
sequence = [1, 6, -1, 10]

print(isValidSubsequence(array, sequence))