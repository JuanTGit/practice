def pivotIdx(arr):
    pivIdx = 0

    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i


alist = [1,7,3,6,5,6]

print(pivotIdx(alist))









