from email import charset


def nonRepeating(s):
    longest = 0
    left = 0
    seen = {}
    for i in range(len(s)):
        if s[i] in seen:
            left = max(seen[s[i]], left)
        longest = max(longest, i - left + 1)
        seen[s[i]] = i + 1
    return longest

print(nonRepeating('abcabcbb'))


def nonRepeat(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

