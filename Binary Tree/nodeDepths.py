from tree import TreeNode
from collections import deque

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9


def dfs(root):
	if not root: return None
	sumOfDepths = 0

	stack = [(root, 0)]

	while stack:
		current = stack.pop()
		# print(current.val)
		sumOfDepths += current[1]
		if current[0].right:
			stack.append(current[0].right, current[1] + 1)
		if current[0].left:
			stack.append(current[0].left, current[1] + 1)
	
	return sumOfDepths


dfs(root)

def bfs(root):
	if not root: return None

	q = deque()
	q.append(root)

	while q:
		current = q.popleft()
		print(current.val)

		if current.left:
			q.append(current.left)
		if current.right:
			q.append(current.right)


# bfs(root)