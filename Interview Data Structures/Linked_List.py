"""
Operation   Time Complexity
---------------------------
Insert End  O(1)
Remove End  O(1)
Insert Mid  O(1)
Remove Mid  O(1)

DownSide:
Can't randomly access an idx in O(1) Time like an Array. Have to start at the beginning.

Linked Lists use pointers instead of indices.

Use cases:
    implement other data structures: Stacks, Queues, Hash Tables
    Dynamic memory allocation
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, target): # O(n)
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None
    
    def insert(self, node): # O(1)
        node.next = self.head
        if self.head:
            self.head.prev = node
        
        self.head = node
        node.prev = None
    
    def delete(self, node): # O(1)
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.prev = node.prev