

def calculateMod(num, mod):

    return num % mod


# print(calculateMod(24, 6))


# Circular Array Access (Index-Level Modulo)
"""
Problem

Youre given an array nums of length n.
For each index i, you want to read the element k steps to the right, wrapping around if needed.

Return kth number from idx.
"""
nums = [10,20,30,40]; k = 6

def circleArray(nums, idx, k):
	k = idx + k % len(nums)
    
	return nums[k]

# print(circleArray(nums, 1, k))


# Rotate String (Global Modulo)
"""
Problem

Rotate a string s to the right by k positions.
"""
s = 'abcdef'; k = 20
def rotateString(s, k):
	res = ['' for letter in s]

	for i in range(len(s)):
		print(f'idx:{i}')
		placement = (i + k) % len(s)
		print(f'placement:{placement}')
		res[placement] = s[i]

	print(res)


print(rotateString(s, 20))


s = 'abcdef'; k = 20
def rotateStringTwoPointer(s, k):

	def twoPointer(l, r):
		while l < r:
			s[l], s[r] = s[r], s[l]
			l, r = l + 1, r - 1

	k = k % len(s)

	twoPointer(0, len(s) - 1)

	twoPointer(0, k - 1)

	twoPointer(k, len(s) - 1)

	return s

print(rotateStringTwoPointer(s, k))

	