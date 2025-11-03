class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode()
node1.next = ListNode(1)
node1.next.next = ListNode(2)


while node1:
    print(node1.val)
    node1 = node1.next