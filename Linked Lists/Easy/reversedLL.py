# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) ->   ListNode:
        prev = None

        # While our head is not empty
        while head:
            # Store our head as a temporary variable so we don't lose it
            temp = head
            # Move our head to the next node
            head = head.next
            # Set our temp next variable as our previous value
            temp.next = prev
            # Set our prev value as the temporary value to point backwards
            prev = temp
        return prev

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

