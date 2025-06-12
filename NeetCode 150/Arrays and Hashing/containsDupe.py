def containsDuplicate(nums):
	seen = set()

	for num in nums:
		if num in seen:
			return False
		seen.add(num)
	return True


# time: O(N), space: O(N)