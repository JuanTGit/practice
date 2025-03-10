# given a string s, find whether or not all characters are unique

word = 'seashell'

def uniqueString(w):
    if len(w) == len(set(w)):
        return True
    return False


def unique_string(w):
    return len(w) == len(set(w))

word2 = 'seab'
# print(uniqueString(word2))



# Given a string s, compress the string using the following format...
s = 'aaabbccc2'
# Ouput == '3a2b3c12'
s2 = 'aaaaaaaaaaaabbccaa' # -> 9a3a2b2c


def compressString(s):
    count = 1
    prev_letter = s[0]
    output = []

    for i in range(1, len(s)):
        if s[i] == prev_letter:
            if count == 9:
                output.append(f'{count}{prev_letter}')
                count = 1
            else:
                count += 1
        else:
            output.append(f'{count}{prev_letter}')
            count = 1
            prev_letter = s[i]
    output.append(f'{count}{prev_letter}')
    return ''.join(output)

print(compressString(s2))