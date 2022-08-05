"""
https://www.bigocheatsheet.com/

constant - O(1)
logarithmic - O(log n)
linear - O(n)
linear logarithmic - O(n log n)
quadratic - O(n^2)
cubic - O(n^3)
polynomial - N^O(1)
exponential - 2^O(n)
"""


# Array
from ctypes.wintypes import tagRECT
from re import X


array = [23, 4, 6, 15, 5, 7]

indexing = array[1] # Constant Time and Space - O(1)

# Searching through an array
# Linear Time - O(n) Constant Space - O(1)
for x in array: 
    print(x)

# Copying an array
# Linear Time - O(n) AND Linear Space - O(n)
copy_array = array[:]

# Setting an index in an array
# Constant Time AND Constant Space - O(1)
array[2] = 100


# Calculating a function Time and Space Complexity

def some_func(nums):
    for n in nums: # Quadratic Operation - O(n^2) - Because we have nested for loops
        for x in nums: # Linear Operation - O(n)
            print(X) # Constant Operation - O(1)
        for y in nums: # Linear Operation - O(n)
            print(y) # Constant Operation - O(1)
    nums[2] = 100 # Constant Operation - O(1)
    return nums # Constant Operation - O(1)

print(some_func([1, 2, 3]))
# O(n^2) + 2 O(n) + 4 O(1)
# O(n^2) - The constant and linear time look ups are negligible

"""
Stacks and Queues
Last In First Out (LIFO)
First In First Out (FIFO)
"""
# *STACKS* Last In First Out (LIFO) - Stack of pancakes start from the top and go down

# Searching through a stack will be Linear Time  O(n) - Constant Space O(1)
# Selecting the first item will be done in Linear Time O(n) - Constant Space O(1)
# Selecting the last item will be done in Constant Time O(1) - Constant Space O(1)
# Adding to the stack should take Constant Time O(1) - Constant Space O(1)

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack: ")
while stack:
    grab_item = stack.pop()
    print(grab_item)

"""
Output: Last In First Out
3
2
1
"""

# *QUEUES* First In First Out (FIFO) - Line at a sale. First to go in first to go out.

# Searching through a queue will be Linear Time O(n) - Constant Space O(1)
# Selecting the first item will be done in Constant Time - O(1) - Constant Space O(1)
# Selecting the last item will be done in Linear Time O(n) - Constant Space O(1)
# Adding to the queue should take Constant Time O(1) - Constant Space O(1)

queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print("Queue: ")
while queue:
    grab_item = queue.pop(0)
    print(grab_item)

"""
Output: First In First Out
1
2
3
"""

from collections import deque

stack = deque([1, 2, 3])
print('STACK: ')
while stack:
    print(stack.pop())

queue = deque([1, 2, 3])
print('QUEUE: ')
while queue:
    print(queue.popleft())


"""
Linked List(Data Structure)

A Linked list is created by a node class. We create a Node object and create another class
to use this node object. We pass the appropriate values through the node object to point
to the next data elements.

Advantages - Linked lists can save memory because they can be flexible with memory management
Disadvantages - Finding or adding to the list requires traversing the entire list.
"""

class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

    def traverse_list(self):
        node = self
        while node != None:
            print(node.value)
            node = node.next

node1 = LinkedListNode('Monday')
node2 = LinkedListNode('Tuesday')
node3 = LinkedListNode('Wednesday')

node1.next = node2
node2.next = node3

node1.traverse_list()


# Full Implementation
# 2 Classes - Node Class + LinkedList Class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node to the front of the Linked List
    def push_on(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
    
    # Add a new node to the end of the Linked List
    def append(self, new_value):
        new_node = Node(new_value)

        # check if the linked list is empty, set the head to our new node.
        if self.head is None:
            self.head = new_node
        # If the linked list is not empty, traverse to the end and set the end node to our new node.
        else:
            last = self.head

            # Continue to get the next node until "node.next" is None meaning we are at the end.
            while last.next:
                last = last.next

            last.next = new_node

    # Add a new node after a node in the linked list (middle of the list)
    def insert_after(self, prev_node,  new_value):
        # Check if previous node even exists
        if prev_node is None:
            print('The given previous node must not be empty!')
            return

        new_node = Node(new_value)
        # Point the new node's next to the previous node's (soon-to-be) former next
        new_node.next = prev_node.next
        # Point the previous node to the new node
        prev_node.next = new_node
    
    def traverse(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
        


weekday_links = LinkedList()
weekday_links.push_on('Monday')
weekday_links.append('Tuesday')
weekday_links.append('Thursday')
weekday_links.insert_after(weekday_links.head.next, 'Wednesday')
weekday_links.push_on('Sunday')
weekday_links.traverse()


"""
Binary Search Tree
Data structure for storing data in a certain way
Node in BST has 3 attributes - Root, Left, Right = None
"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert method to add a value onto the tree
    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = BST(new_value) # Each node is it's own BST.
            else:
                self.left.insert(new_value)
        else:
            if self.right is None:
                self.right = BST(new_value)
            else:
                self.right.insert(new_value)

    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            return True

    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()

    def get_max_value(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max_value()

    def remove(self, value_to_remove, parent=None):
        if value_to_remove < self.value:
            if self.left is not None:
                self.left.remove(value_to_remove, self)
        elif value_to_remove > self.value:
            if self.right is not None:
                self.right.remove(value_to_remove, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.get_min_value()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.right = self.right.right
                    self.left = self.right.left
                else:
                    self.value = None
            elif parent.left == self:
                # if self.left is not None:
                #     parent.left = self.left
                # else:
                #     parent.left = self.right
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right



my_tree = BST(50)
my_tree.insert(25)
my_tree.insert(10)
my_tree.contains(10)