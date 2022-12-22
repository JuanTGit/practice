nums = [1, 4, 2, 9]

def plusOne(nums):
    # Iterate through in reverse
    for i in range(len(nums)-1, -1, -1):
        # Check if nums < 9
        if nums[i] != 9:
            # Increase by one, and break.
            nums[i] += 1
            break
        else:
            nums[i] = 0
    # Check for case we only have a 9 in our input
    if nums[0] == 0:
        nums.insert(0, 1)
    return nums


print(plusOne(nums))
