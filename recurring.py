# find the first recurring character in a string.
# Example:
# s = "ABFCBC"
# Output: B
# Explanation: B is the first recurring character in the string.

def recurring(s):
    seen = {}

    for i in s:
        seen[i] = seen.get(i, 0) + 1
        if seen[i] >= 2:
            return i
    return 'None'



s = "ACABFCBC"
print(recurring(s))