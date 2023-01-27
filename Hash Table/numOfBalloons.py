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

text = "loonbalxballpon"

def numOfBalloons(text):

    hashMap = {}

    for i in text:
        hashMap[i] = hashMap.get(i, 0) + 1

    balloons = {
        'b': 1,
        'a' : 1,
        'l' : 2,
        'o' : 2,
        'n' : 1,
    }
    
    minCount = float('inf')

    for key in balloons:
        if key not in hashMap:
            return 0
        minCount = min(minCount, hashMap[key] // balloons[key])

    return minCount
    


# print(numOfBalloons(text))

from collections import Counter

def maxNumBalloon(text):
    counter = Counter(text)
    balloonCount = Counter('balloon')

    return counter
    


print(maxNumBalloon(text))
