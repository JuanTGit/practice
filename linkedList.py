
class ListNode:
	def __init__(self, value=0, next=None):
		self.value = value
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_end(self, value):
		new_node = ListNode(value)
		if self.head == None:
			self.head = new_node
		else:
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = new_node
	
	def display_list(self):
		current = self.head
		while current is not None:
			print(current.value, end=' -> ')
			current = current.next
		print('None')


ll = LinkedList()

ll.insert_at_end(1)
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.display_list()