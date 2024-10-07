"""
What is recurrsion?
Recursion occurs when a function calls itself directly or indirectly
"""

"""
you have to have a base case when using recurrsion to avoid a stack overflow.
"""

def getNthFib(n):
    # Formula:
    # f(n) = f(n - 1) + f(n - 2)

	# Base case:
	if n == 2:
		return 1
	if n == 1:
		return 1
	return getNthFib(n - 1) + getNthFib(n - 2)

# print(getNthFib(7))

def iteration(array):
	l = 0
	# -1 because of the index starting at 0
	r = len(array) - 1
	while r > l:
		print(array[r])
		r -= 1
		l += 1

print(iteration([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
