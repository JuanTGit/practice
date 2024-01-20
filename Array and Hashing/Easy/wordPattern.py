# 290. Word Pattern
# Easy

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

def wordPattern(p, s):
    word = s.split(' ')
    word_to_p = {}

    if len(p) != len(word): return False
    if len(set(p)) != len(set(word)): return False

    for i in range(len(word)):
        if word[i] not in word_to_p:
            word_to_p[word[i]] = p[i]
        elif word_to_p[word[i]] != p[i]:
            return False
    return True


# print(wordPattern('aaaa', 'dog cat cat dog'))

def checkPractice(pattern, s):
    word = s.split(' ')
    wordMap = {}

    if len(pattern) != len(word): return False
    if len(set(pattern)) != len(set(word)): return False

    for i in range(len(word)):
        if word[i] not in wordMap:
            wordMap[word[i]] = pattern[i]
        elif wordMap[word[i]] != pattern[i]:
            return False
    return True



print(checkPractice('baab', 'dog cat cat dog'))