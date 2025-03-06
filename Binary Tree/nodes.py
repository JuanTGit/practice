from tree import TreeNode

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


def searchTree(root):
	if not root:
		return 0
	# Preorder Traversal
		# Visit node - Traverse Left - Traverse Right
	print(f'value: {root.val}')

	return 1 + searchTree(root.left) + searchTree(root.right)



# print(searchTree(root))

def iterativeTree(root):
	if not root:
		return 0
	
	count = 0

	stack = [root]

	while stack:
		current = stack.pop()
		print(current.val)

		count += 1

		if current.right:
			stack.append(current.right)
		if current.left:
			stack.append(current.left)

	return count

print(iterativeTree(root))

