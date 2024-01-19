def missing_number(nums):
    hashset = set(nums)
    for num in range(len(nums) + 1):
        if num not in hashset:
            return num

print(missing_number([3, 0, 1, 4, 6, 2]))