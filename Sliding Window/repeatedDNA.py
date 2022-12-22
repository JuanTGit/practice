def findRepeatedDnaSequences(s):
    dnaDict = {}
    l = 0
    r = 10
    res = []
    while r < len(s):
        for i in s:
            if len(s[l:r]) < 10:
                break
            dnaDict[s[l:r]] = dnaDict.get(s[l:r], 0) + 1
            r += 1
            l += 1
    for k, v in dnaDict.items():
        if v > 1:
            res.append(k)
    return res

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))