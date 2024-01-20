# 424. Longest Repeating Character Replacement
# Medium

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

def characterReplacement(s, k):
    count = {}
    res = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        # Checking if the least characters in our window are greater than k. e.g. "AABAK" 5 - 3 = 2 > k?. 5 being window size; 3 being max values("A"). 2 being our least characters.
        while (r - l + 1) - max(count.values()) > k:
            # Decriment the position value of our left pointer in our dictionary. and move it forward one in our array.
            count[s[l]] -= 1
            l += 1
        # If the above condition isn't True, update our max result.
        res = max(res, r - l + 1)
    
    return res

print(characterReplacement('AABABBA', 1))