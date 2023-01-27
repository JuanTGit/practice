def isValid(s):
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for par in s:
        if par in d:  # 1
            stack.append(par)
        elif len(stack) == 0 or d[stack.pop()] != par:  # 2
            return False
    return len(stack) == 0
    


# print(isValid("()[]{}"))



# 20. Valid Parentheses
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

def validPar(s):
    valid = {'(':')', '{':'}','[':']'}

    stack = []

    for i in s:
        if i in valid:
            stack.append(i)
            print(valid[stack[-1]])
        elif len(stack) == 0 or valid[stack.pop()] != i:
            return False
    return len(stack) == 0

print(validPar(s = "()[]{}"))