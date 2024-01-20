# 1189. Maximum Number of Balloons
# Easy

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:

# Input: text = "nlaebolko"
# Output: 1
# Example 2:

# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0

def maxNumBalloon(text):
    strs = ['b', 'a', 'l', 'o', 'n']
    counts = [0] * 5

    for i in range(5):
        counts[i] = text.count(strs[i])
        
    counts[2] = counts[2] // 2
    counts[3] = counts[3] // 2

    return min(counts)

print(maxNumBalloon("loonbalxballpoon"))



def maximumNumBalloons(text):
    strs = ['b', 'a', 'l', 'o', 'n']
    counts = [0] * 5

    for i in range(5):
        counts[i] = text.count(strs[i])
    
    counts[2] = counts[2] // 2
    counts[3] = counts[3] // 2

    return min(counts)
    