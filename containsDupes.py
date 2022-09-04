# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def containsDupes(num):
    dupes = {}
    for i in num:
        dupes[i] = dupes.get(i, 0) + 1
    for j in dupes:
        if dupes[j] > 1:
            return True
    return False


nums1 = [1,1,1,3,3,4,3,2,4,2]
nums2 = [1,2,3,4]

print(containsDupes(nums1))

def contains_dupes(arr):
    hashset = set()

    for n in arr:
        if n in hashset:
            return True
        hashset.add(n)
    return False