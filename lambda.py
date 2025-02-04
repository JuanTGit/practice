# key = lambda x: (-x[0], x[1])
# lst = [(2, 10),(2, 20), (2, 30), (2, 40)]
# print(sorted(lst, key=key))



# syntax: lambda arguments: expression

# Function that adds 2 numbers

def addNums(a, b):
	return a + b

add = lambda a, b: a + b

# Mapping with lambda
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))

# Filter with lambda
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# ====================
# =		PRACTICE	 =
# ====================

# Create squares using map
numbers = [1, 2, 3, 4]
squareNums = list(map(lambda x: x ** 2, numbers))
# print(squareNums)

# Filter Odd nums
numbers = [1, 2, 3, 4, 5, 6]
filterOdds = list(filter(lambda x: x % 2 != 0, numbers))
# print(filterOdds)

# Sort list of tuples based on second value
tuples = [(1, 2), (3, 1), (5, 0)]
sortTuples = sorted(tuples, key=lambda x: x[1])
# print(sortTuples)

# Sort a List of Strings by Length
strings =  ["apple", "banana", "cherry", "date"]
sortStrings = sorted(strings, key=lambda x: len(x))
print(sortStrings)

# Challenge Problem: Sort a List of Dictionaries by a Specific Key
dicts = [{'name': 'Juan', 'age': 25}, {'name': 'Sherley', 'age': 23}]
sortByAge = sorted(dicts, key=lambda k: k['age'])
print(sortByAge)
