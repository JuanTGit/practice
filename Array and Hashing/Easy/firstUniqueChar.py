# 387. First Unique Character in a String
# Easy
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

def firstUniqChar(s):
	charCount = {}

	for letter in s:
		charCount[letter] = charCount.get(letter, 0) + 1

	for i, letter in enumerate(s):
		if charCount[letter] == 1:
			return i
	return -1

print(firstUniqChar("aabb"))