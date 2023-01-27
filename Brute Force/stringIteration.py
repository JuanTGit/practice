myString = 'Jupiter'

def stringPractice(s):
    strDict = {}

    for first in range(len(s)):
        for second in range(len(s) - first):
            substring = s[first:second+first]
            print(substring)
    print(substring)
        
    # print(strDict)


# print(stringPractice(myString))

# range(start, stop, step)


"""
for length in range(1, len(S) + 1):
    # Iterate over all substrings of the input string that have the current length
    for i in range(len(S) - length + 1):
        substring = S[i:i+length]
"""

for i in range(1, len(myString) + 1):
    for j in range(len(myString) - i + 1):
        # print(myString[j:j+i])
        pass

print(myString[0:1])