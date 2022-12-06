# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

def ransomNote(note, magazine):
    noteDict = {}
    magDict = {}
    for letter in note:
        noteDict[letter] = noteDict.get(letter, 0) + 1
    for letter in magazine:
        magDict[letter] = magDict.get(letter, 0) + 1
    for key in noteDict:
        if key not in magDict or noteDict[key]>magDict[key]:
            return False
    return True
rn = "aa"; magazine = "ab"

print(ransomNote(rn, magazine))