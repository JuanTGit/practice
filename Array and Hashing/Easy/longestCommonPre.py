# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    res = []
    i = 0
    shortest = len(min(strs))
    while i < shortest:
        for word in strs:
            if strs[0][i] != word[i]:
                return ''.join(res)
        res.append(strs[0][i])
        i += 1
    return ''.join(res)

def commented(strs):
    # array to build the output string
    res = []
    # start at idx 0 to iterate over each idx of each word
    i = 0
    # use length of shortest word (a common prefix cannot be longer than
    # the shortest word in the list)
    shortest = len(min(strs))
    # iterate over each index of each word
    while i < shortest:
        for word in strs:
            # make sure the idx matches the first word.
            # if ANY of them are different, this is uncommon and we can return the current
            # prefix
            if strs[0][i] != word[i]:
                return ''.join(res)
        # if all idxs hold the same value, add this char to the common prefix
        res.append(strs[0][i])
        # on to the next letter
        i += 1
    # if we make it through the whole shortest word, return res
    return ''.join(res)


strs = ["flower","flow","flight"]

print(commented(strs))


def longestCommonPre(strs):
    res = ''

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or strs[0][i] != s[i]:
                return res
        res += strs[0][i]

print(longestCommonPre(strs))