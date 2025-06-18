from collections import defaultdict

def groupAnagrams(strs):

	# Table that holds values of lists

	groupedTable = defaultdict(list)

	for word in strs:
		letterCount = [0]*26

		for letter in word:

			letterCount[ord(letter) - ord('a')] += 1

		groupedTable[str(letterCount)].append(word)


	return list(groupedTable.values())





print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))