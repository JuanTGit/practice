# 383. Ransom Note
# Easy
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
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

def canConstruct(ransomNote, magazine):
	note = {}
	mag = {}

	for i in ransomNote:
		note[i] = note.get(i, 0) + 1
	for i in magazine:
		mag[i] = mag.get(i, 0) + 1

	for letter in note:
		if letter not in mag or mag[letter] < note[letter]:
			return False
	return True


print(canConstruct("aca", "aab"))