# 659. Encode and Decode Strings
# Medium
# Description
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is 
# decoded back to the original list of strings.

# Example

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"

# Example 2

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"


"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    # write your code here
    res = ''

    for s in strs:
        res += str(len(s)) + '#' + s
    return res

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode(str):
    res, i = [], 0

    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
        length = int(str[i:j])
        res.append(str[j + 1 : j + 1 + length])
        i = j + 1 + length
    
    return res



print(encode(["lint","code","love","you"]))
print(decode('4#lint4#code4#love3#you'))