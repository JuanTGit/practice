# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
# return the shortest distance between these two words in the list.

# Example 1:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3

# Example 2:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1


def shortestWords(words, w1, w2):

    idx1 = None
    idx2 = None
    pointer = 0
    distance = len(words)
    while pointer < len(words):
        if words[pointer] == w1:
            idx1 = pointer
            if idx2 != None:
                distance = min(distance, abs(idx1 - idx2))
        elif words[pointer] == w2:
            idx2 = pointer
            if idx1 != None:
                distance = min(distance, abs(idx1 - idx2))
        pointer += 1
    return distance
        

print(shortestWords(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice'))
