# [1,2,3,4,5] --> [1,5]
# [2334454,5] --> [5,2334454]
# [1]         --> [1,1]

def highlow(arr):
    return [min(arr), max(arr)]


print(highlow([1,2,3,4,5]))