# 557. Reverse Words in a String III
# Easy
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"

def reverseWords(s):
	newWords = list(s)
	l = 0

	for r in range(len(newWords)):
		if newWords[r] == " " or r == len(newWords) - 1:
			tempL, tempR = l, r - 1

			if r == len(newWords) - 1:
				tempR = r

			while tempL < tempR:
				newWords[tempL], newWords[tempR] = newWords[tempR], newWords[tempL]
				tempL += 1
				tempR -=1
			l = r + 1

	return ''.join(newWords)


print(reverseWords("Let's take LeetCode contest"))