def valid_parentheses(string):

    total = []

    for s in string:
        if s == '(':
            total.append(s)
        elif s == ')':
            total.pop()
    if len(total) > 0:
        return False
    return True