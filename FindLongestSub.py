# Problem: Find the Longest Substring Without Repeating Characters
# Prompt:
# You are given a string s. Your task is to find the length of the longest substring without repeating characters.

# Example:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The longest substring without repeating characters is "abc", which has a length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The longest substring without repeating characters is "b", which has a length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The longest substring without repeating characters is "wke", which has a length of 3.
# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols, and spaces.
s = "abcbcbb"

def length_of_longest_substring(s):
	if len(s) < 1: return 0
	longestSub = 0
	l = 0

	currentChars = set()

	for r in range(len(s)):
		while s[r] in currentChars:
			currentChars.remove(s[l])
			l += 1
		currentChars.add(s[r])
		
		longestSub = max(longestSub, r - l + 1)

	return longestSub

print(length_of_longest_substring('abcabcbb'))