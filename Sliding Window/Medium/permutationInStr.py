# 567. Permutation in String
# Medium
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

s1 = "aidi"
s2 = "eiidaooo"

def checkInclusion(s1, s2):
    l = 0
    hash1, hash2 = {}, {}

    for i in range(len(s1)):
        hash1[s1[i]] = hash1.get(s1[i], 0) + 1
        hash2[s2[i]] = hash2.get(s2[i], 0) + 1
    
    for r in range(len(s1)-1, len(s2)-1):
        if hash1 == hash2:
            return True
        
        else:
            hash2[s2[l]] -= 1
            if hash2[s2[l]] < 1: 
                hash2.pop(s2[l])
            l += 1
            hash2[s2[r+1]] = hash2.get(s2[r+1], 0) + 1
    return False
        

print(checkInclusion(s1, s2))