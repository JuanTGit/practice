# 1624. Largest Substring Between Two Equal Characters
# Easy
# Topics
# Companies
# Hint
# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.

from collections import defaultdict

def maxLengthBetweenEqualCharacters(s):
	charCount = defaultdict(list)
	maxCount = -1

	for letter in range(len(s)):
		if s[letter] in charCount:
			maxCount = max(maxCount, letter - charCount[s[letter]][0] - 1)
		charCount[s[letter]] += [letter]

	return maxCount


print(maxLengthBetweenEqualCharacters("cc"))