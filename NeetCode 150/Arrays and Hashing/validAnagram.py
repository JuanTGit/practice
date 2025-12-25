def isAnagram(s, t):

	if len(s) != len(t): return False
	sHash, tHash = {}, {}

	for letter in range(len(s)):
		sHash[s[letter]] = sHash.get(s[letter], 0) + 1
		tHash[t[letter]] = tHash.get(t[letter], 0) + 1

	return sHash == tHash


# time: O(N), space: O(N)