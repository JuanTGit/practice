def isValid(s):
	parMap = { '(':')', '[':']', '{':'}'}
	stack = []
		
	for par in s:
		if par in parMap:
			stack.append(par)
		elif len(stack) == 0 or parMap[stack.pop()] != par:
			return False
	
	return len(stack) == 0
		


par = "(())[][]]["

print(isValid(par))