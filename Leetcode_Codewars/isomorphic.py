# Given two strings s1 and s2, return True if they are isomorphic, or False if they are not.
# Two strings s1 and s2 are isomorphic if the characters in s1 can be replaced to get s2.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Case 1:
# In: s1 = "ott", s2 = "add"
# Out: True
# Explained: all o's can be replaced with 'a' and all t's can be replaces with 'd' (o -> a, t -> d)

# Case 2:
# In: s1 = "foo", s2 = "bar"
# Out: False
# Explained: f can map to b, but o cannot map to two different letters -- o cannot change to be both a and r

# Case 3:
# In: s1 = "paper", s2 = "title"
# Out: True

def isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    dict1 = {}
    dict2 = {}

    for char in s1:
        dict1[char] = dict1.get(char, 0) + 1
    for char in s2:
        dict2[char] = dict2.get(char, 0) + 1
    
    if sorted(dict1.values()) != sorted(dict2.values()):
        return False
    return True

s1 = "ott"; s2 = "add"
s3 = "foo"; s4 = "bar"
s5 = "paper"; s6 = "title"
s7 = "badc"
s8 = "baba"

print(isomorphic(s7, s8))