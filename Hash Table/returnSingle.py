def singleNumber(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1
    for k, v in count.items():
        if v == 1:
            return k

print(singleNumber([1, 1, 3, 4, 4, 7, 7, 8, 8]))