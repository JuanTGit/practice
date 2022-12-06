# Iterables: An object that can be iterated over
# lists, tuples, sets, dictionaries, strings


"""len()"""
# Returns an integer for the length of the iterable
import enum


name = 'Juan T.'
chars = len(name)
print(chars)
# Output: 7

"""range(start, stop, step)"""
# Takes in an integer and returns the range starting from 0
name_rng = range(chars)
print(name_rng)
# Output: range(0, 7)

for i in range(len(name)):
    print(f'{i} = {name[i]}')
# Output:
# 0 = J
# 1 = u
# 2 = a
# 3 = n
# 4 =
# 5 = T
# 6 = .

"""isinstance()"""
# answer = 5 * 8
# user_answer = int(input("What is 5 x 8?"))

# print(isinstance(user_answer, (int, float)))

# print(user_answer)

"""enumerate()"""
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
  
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

# Output:
# Return type: 
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
# [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
#----------------------------------------------
# enumerate function in loops
l3 = ["eat", "sleep", "repeat"]
  
# printing the tuples in object directly
for ele in enumerate(l3):
    print (ele)
  
# changing index and printing separately
for count, ele in enumerate(l3, 100):
    print (count, ele)
  
# getting desired output from tuple
for count, ele in enumerate(l3):
    print(count)
    print(ele)

# Output:
# (0, 'eat')
# (1, 'sleep')
# (2, 'repeat')
# 100 eat
# 101 sleep
# 102 repeat
# 0
# eat
# 1
# sleep
# 2
# repeat


alist = [2,7,11,15]

for i, num in enumerate(alist):
    print(i, num)