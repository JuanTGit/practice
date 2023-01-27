# 205. Isomorphic Strings
# Easy

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"
# Output: true

# Example 2:

# Input: s = "foo", t = "bar"
# Output: false

# Example 3:

# Input: s = "paper", t = "title"
# Output: true


def isIsomorphic(s, t):
    dicS, dicT = {}, {}

    for i, val in enumerate(s):
        dicS[val] = dicS.get(val, []) + [i]
    for i, val in enumerate(t):
        dicT[val] = dicT.get(val, []) + [i]
    print(dicS, dicT)
    print(sorted(dicS.values()), sorted(dicT.values()))


print(isIsomorphic('egg', 'add'))