# 1422. Maximum Score After Splitting a String
# Easy
# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

# Example 1:

# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
# Example 2:

# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
# Example 3:

# Input: s = "1111"
# Output: 3

s = "01001"

def maxScore(s):
	left = [int(s[0])]
	right = [int(num) for num in s[1:]]
	maxTotal = left.count(0) + right.count(1)
	
	for num in range(len(right) - 1):
		left.append(right.pop(0))
		maxTotal = max(left.count(0) + right.count(1), maxTotal)

	return maxTotal

print(maxScore(s))

def maxScore2(s):
	ones = 0
	zeros = 0
	best = float("inf")

	for i in range(len(s) - 1):
		if s[i] == "1":
			ones += 1
		else:
			zeros += 1
		
		best = max(best, zeros - ones)
		
	if s[-1] == "1":
		ones += 1
	
	return best + ones