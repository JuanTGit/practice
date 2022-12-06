# # given an array of n integers construct a product array of the same size such that the ith element of the product array is equal to the product of all
# # of the elements of the original array except for the ith element

# example:

# [1, 2, 3, 4] -> [24, 12, 8, 6]


def prodOfArray(arr):
    n = len(arr)
    output = [1] * n

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                output[i] = output[i] * arr[j]
        

    return output


print(prodOfArray([1, 2, 3, 4]))