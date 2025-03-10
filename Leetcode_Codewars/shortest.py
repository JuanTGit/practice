# Simple question to start off the week!
# Given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
# Added challenge: do this in O(1) space (without making another data structure)
# Example 1:
# s = "Hello World JavaScript!"
# output: 5
# explained: "Hello" and "World" both have 5 characters
# Example 2:
# s = "We built a nest and tested it."
# output: 1
# explained: "a" is the shortest word with a length of 1


def shortestWord(s):
    l = 0
    r = 0
    count = float('inf')

    while r < len(s) - 1:
        if s[r] == ' ':
            if count > (r-l):
                count = (r-l)
            l = r + 1
            r = l
        else:
            r += 1
    return count

s = "We're built and nest and tested i."

print(shortestWord(s))