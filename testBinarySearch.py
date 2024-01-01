nums = [0, 1, 1, 4, 5, 6, 9, 24, 55, 92, 149]


def binarySearch(nums, search):
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (high + low) // 2
        if nums[middle] == search:
            return f'{search} found at {middle} idx.'
        
        elif nums[middle] > search:
            high = middle - 1
        
        else:
            low = middle + 1


print(binarySearch(nums, 149))