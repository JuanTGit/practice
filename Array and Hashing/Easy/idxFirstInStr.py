# 28. Find the Index of the First Occurrence in a String
# Easy
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
haystack = "sadbutsad"; needle = "but"

def strStr(haystack, needle):
    l = 0
    r = 0

    point = needle[0]

    while l < len(haystack):
        if haystack[l] != point:
            l += 1

        r = l + len(needle)
        if haystack[l:r] == needle:
            return l
        else:
            l += 1
        
    return -1

            

def strStr2(haystack, needle):
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(strStr2(haystack, needle))