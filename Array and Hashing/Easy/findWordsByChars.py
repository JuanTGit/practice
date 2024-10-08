# 1160. Find Words That Can Be Formed by Characters
# Easy
# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
words = ["hello","world","leetcode"]; chars = "welldonehoneyr"

def countCharacters(words, chars):
	res = 0
	charsDict = {}

	for char in chars:
		charsDict[char] = charsDict.get(char, 0) + 1
	
	for word in words:
		wordDict = {}
		valid = True
		for char in word:
			wordDict[char] = wordDict.get(char, 0) + 1
			if not (char in charsDict and wordDict[char] <= charsDict[char]):
				valid = False
				break
		if valid:
			res += len(word)
		
	return res

print(countCharacters(words, chars))