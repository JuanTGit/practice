# Given a string s, return the length of the longest substring that contains at most two distinct characters.
# Example 1:
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.



def twoDistinct(s):
    # impossible to have more than 2 chars if len(s) < 3
    if len(s) < 3:
        return len(s)
    # sliding window left and right pointers
    left, right = 0, 0
    # hashmap character -> its rightmost position
    # in the sliding window
    d = {}

    max_len = 2

    while right < len(s):
        # when the slidewindow contains less than 3 characters,
        # add the value, idx pair
        d[s[right]] = right
        # keep sliding
        right += 1

        # slidewindow contains 3 characters
        if len(d) == 3:
            # delete the leftmost character
            del_idx = min(d.values())
            del d[s[del_idx]]
            # move left pointer of the slidewindow
            left = del_idx + 1
        # max_len is the greater of itself vs the new substring we found
        max_len = max(max_len, right - left)

    return max_len


s = "eceba"

print(twoDistinct(s))