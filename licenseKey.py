def licenseKeyFormatting(s, k):
    res = ""
    s = s.replace("-", "").upper()
    n = len(s)
    print(n % k)
    for i in range(n):
        if i > 0 and (n - i) % k == 0:
            res += "-"
        res += s[i]
    return res

print(licenseKeyFormatting("5F3Z-2e-9-w", 4))