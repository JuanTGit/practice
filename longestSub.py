# 6. Longest Substring Without Repeating Characters
# Problem: Given a string s, find the length of the longest substring without repeating characters.

# Example:

# vbnet
# Copy code
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with a length of 3.

s = "abcabcbbabcdefg"

def longestsub(s):
	hashSet = set()
	l = 0
	maxLen = 0
	for r in range(len(s)):
		while s[r] in hashSet:
			hashSet.remove(s[l])
			l += 1
		hashSet.add(s[r])
		maxLen = max(maxLen, r - l + 1)

	return maxLen

print(longestsub(s))


		
