
def difference(nums):
    if len(nums) < 2: return 0

    return max(nums) - min(nums)

list1 = [2, 4, 41, 18, 12, 8]

print(difference(list1))