# 49. Group Anagrams
# Medium

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

from collections import defaultdict

def groupAnagrams(strs):
    # mapping charCount to list of Anagrams
    res = defaultdict(list)

    for s in strs:
        # a ... z
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        res[tuple(count)].append(s)
    
    return res.values()

