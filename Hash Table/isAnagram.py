# 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

s = "anagram"; t = "nagaram"

def isAnagram(s, t):
    if len(s) != len(t): return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1
    
    return countS == countT

print(isAnagram(s, t))