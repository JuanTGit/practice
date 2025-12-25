# 1408. String Matching in an Array
# Easy
# Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.


# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.


# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique.

words = ["leetcode","et","code"]


def stringMatching(words):
	res = []

	for i in range(len(words)):
		curWord = words[i]
		for j in range(len(words)):
			subString = len(words[j])
			if subString < len(curWord):
				left, right = 0, subString

				while right < len(curWord) + 1:
					if curWord[left:right] == words[j] and words[j] not in res:
						res.append(words[j])
					left += 1
					right += 1
	return res
				
print(stringMatching(words))