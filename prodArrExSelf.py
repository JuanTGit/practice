nums = [1, 2, 3, 4]

def product_except_self(nums):

	res = [1] * len(nums)

	prefix = 1
	for num in range(len(nums)):
		res[num] = prefix
		prefix *= nums[num]

	postfix = 1
	for num in range(len(nums) -1, -1, -1):
		res[num] *= postfix
		postfix *= nums[num]


	return res

print(product_except_self(nums))
