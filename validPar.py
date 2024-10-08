

def isValid(s):
	pairs = {
		'(': ')',
		'[': ']',
		'{': '}'
	}

	stack = []

	for par in s:
		if par in pairs:
			stack.append(par)

		elif len(stack) == 0 or par != pairs[stack.pop()]:
			return False
	
	return len(stack) == 0


print(isValid("()"))