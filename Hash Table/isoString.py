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
    return sorted(dicS.values()) == sorted(dicT.values())


print(isIsomorphic('egg', 'add'))


def isomorphicString(s, t):
    # Create a hashtable for each of our strings.
    dictST, dictTS = {}, {}

    # Compare each character in both strings
    for c1, c2 in zip(s, t):
        if (c1 in dictST and dictST[c1] != c2) or (c2 in dictTS and dictST[c2] != c1):
            return False
        dictST[c1] = c2
        dictTS[c2] = c1
    return True


s1 = 'egg'
s2 = 'add'