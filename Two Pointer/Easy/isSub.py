# 392. Is Subsequence
# Easy

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

s = "abc"; t = "ahbgdc"

def isSub(s, t):
    sPointer = 0
    tPointer = 0
    count_s = 0

    while sPointer < len(s) and tPointer < len(t):
        if s[sPointer] == t[tPointer]:
            count_s += 1
            sPointer += 1
        tPointer += 1
    return len(s) == count_s

print(isSub(s, t))