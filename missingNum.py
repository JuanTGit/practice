def missing_number(nums):
    hashset = set(nums)
    for num in range(len(nums) + 1):
        if num not in hashset:
            return num

print(missing_number([3, 0, 1, 4, 6, 2]))


nums = {
    0: 1,
    1: 1,
    2: 1
}

nums.pop(0)

if 1 in nums.keys():
    print('good')


strs = ['flowers', 'flow', 'flight']
res = ''

smallest = len(min(strs))
        
print(smallest)