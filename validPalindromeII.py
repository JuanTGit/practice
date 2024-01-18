# 680. Valid Palindrome II
# Easy
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

def validPalindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        return validPalindromeUtil(s, l + 1, r) or validPalindromeUtil(s, l, r - 1)
    return True
        
def validPalindromeUtil(s, l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True


print(validPalindrome('abc'))