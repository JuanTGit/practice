def targetIdx(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
        
nums = [1, 3, 5, 7, 9, 13, 18]
target = 0

print(targetIdx(nums, target))
