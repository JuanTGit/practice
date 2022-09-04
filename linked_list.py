class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


head = Node(4)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(1)


def traverse(h):
    temp = h
    while temp != None:
        print(temp.value)
        temp = temp.next

# traverse(head)


def reverseLL(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev
# traversing forward
traverse(head)
# traversing iteratively reversed LL
traverse(reverseLL(head))
def recursiveReversal(node, prev=None):
    if not node:
        return prev
    next_node = node.next
    node.next = prev
    return recursiveReversal(next_node, node)
# traverse forward LL
traverse(head)
# traversing recursively reversed LL
traverse(recursiveReversal(head))

# AlgoExpert Starter Code
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

#AlgoExpert Solution to remove dupes
def removeDuplicatesFromLinkedList(LinkedList):
	if not LinkedList:
		return None
    # current node == head of LL
	current = LinkedList
	# while we have a next node
	while current.next:
		print(current.next)
        # compare the two values -- if they are the same, move pointer of current
        # two nodes ahead (AKA, skip the next node since it is the same)
		if current.value == current.next.value:
			current.next = current.next.next
        # if not, move curr to the following node and repeat
		else:
			current = current.next
	return LinkedList

