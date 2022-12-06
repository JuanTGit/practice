def isValid(s):
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for par in s:
        if par in d:  # 1
            stack.append(par)
        elif len(stack) == 0 or d[stack.pop()] != par:  # 2
            return False
    return len(stack) == 0
    


print(isValid("()[]{}"))