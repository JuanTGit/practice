import time

def find_duplicate(arr):
	slow = 0
	fast = 0

	while True:
		slow = arr[slow]
		fast = arr[arr[fast]]

		if slow == fast:
			break
	
	slow = 0
	while slow != fast:
		slow = arr[slow]
		fast = arr[fast]
	return slow

print(find_duplicate([4,3,7,8,6,9,2,1,5,2]))
# 				idx:  0,1,2,3,4,5,6,7,8,9



import time

def find_duplicate(arr):
	slow = 0
	fast = 0

	

	while True:
		time.sleep(3)
		slow = arr[slow]
		print(f"Current Slow: {slow}.")
		fast = arr[arr[fast]]
		print(f"Current Fast: {fast}.\n")

		if slow == fast:
			time.sleep(5)
			print(f'Slow: {slow} | Fast: {fast}')
			break
	
	slow = 0
	while slow != fast:
		time.sleep(2)
		slow = arr[slow]
		print(f'Slow has seen fast. Current Slow: {fast}')
		fast = arr[fast]
		print(f'Slow has seen fast. Current Fast: {fast}')
	return slow

print(find_duplicate([4,3,7,8,6,9,2,1,5,2]))