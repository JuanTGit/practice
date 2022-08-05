# Complete the solution so that the function will break up camel casing, using a space between words.
# Examples:
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# "breakCamelCase"  =>  "break Camel Case"



# Create a function that takes in a string
def breakCamel(words):
    output = ''
# Check through string, for every capital letter put a space before capital
    for i in words:
        if i == i.upper():
            output += ' '
        output += i
    return output
# Return new string

# print(breakCamel('checkMeOut'))


def breakCamel(s):
	res = ""
	for char in s:
		if char.isupper():
			res += ' '
		res += char
	return res
# commented version
def breakCamel(s):
	# create empty string to add onto
	res = ""
	# loop over every character
	for char in s:
		# if character is uppercase
		if char.isupper():
			# add a space to res
			res += ' '
		# regardless of the casing, add the character, too
		res += char
	# return res
	return res



# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

# Create a function the takes in an array of strings
def repeatString(words):
# Create an empty array to append repeating characters
    res = []
# Check through all strings to find characters
    for word in words:
        for i, j in word:
            print(i[j])
        
# Add the repeating character as a string to the empty array

# Return the array
    return res
words = ["bella","label","roller"]
# print(repeatString(words))



# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
# Example 1:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Example 2:
# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1


def distance(s, w1, w2):
     
    if w1 == w2 :
       return 0
 
    # get individual words in a list
    words = s.split(" ")
 
    # assume total length of the string as
    # minimum distance
    min_dist = len(words)+1
 
    # traverse through the entire string
    for index in range(len(words)):
 
        if words[index] == w1:
            for search in range(len(words)):
 
                if words[search] == w2:
 
                    # the distance between the words is
                    # the index of the first word - the
                    # current word index
                    curr = abs(index - search) - 1
 
                    # comparing current distance with
                    # the previously assumed distance
                    if curr < min_dist:
                       min_dist = curr
 
    # w1 and w2 are same and adjacent
    return min_dist

# Driver code
s = "geeks for geeks contribute practice"
w1 = "geeks"
w2 = "practice"
print(distance(s, w1, w2))