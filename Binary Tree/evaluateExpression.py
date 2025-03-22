from tree import TreeNode

root = TreeNode(-1)
node2 = TreeNode(-2)
node3 = TreeNode(-3)
node4 = TreeNode(-4)
node5 = TreeNode(2)
node6 = TreeNode(8)
node7 = TreeNode(3)
node8 = TreeNode(2)
node9 = TreeNode(3)


root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9

"""
-1: Addition
-2: Subtraction right from left
-3: Division left by right
-4: Multiplication
"""


def evaluateTree(tree):
    if tree.val >= 0:
        return tree.val

    leftValue = evaluateTree(tree.left)
    rightValue = evaluateTree(tree.right)

    if tree.val == -1:
        return leftValue + rightValue
    if tree.val == -2:
        return leftValue - rightValue
    if tree.val == -3:
        return int(leftValue / rightValue)
    return leftValue * rightValue
		
