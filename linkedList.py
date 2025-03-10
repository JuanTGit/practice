
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

	def insert_at_beginning(self, value):
		new_node = ListNode(value)
		if self.head == None:
			self.head = new_node
		else:
			temp = self.head
			self.head = new_node
			self.head.next = temp

	def remove_node(self, value):
		current = self.head
		prev = None

		if current.value == value:
			self.head = current.next
			current = None
			return

		while current.value != value:
			prev = current
			current = current.next

		prev.next = current.next
		current = None

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
ll.insert_at_beginning(0)
ll.insert_at_beginning(-1)
ll.display_list()
ll.remove_node(3)
ll.display_list()
ll.remove_node(5)
ll.display_list()