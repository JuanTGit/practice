# 104. Maximum Depth of Binary Tree
# Easy

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:

# Input: root = [1,null,2]
# Output: 2


# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion
class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Iterative BFS
class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0

        # Check how many levels we have gone down
        level = 0
        # Create a Queue with our input
        q = deque([root])

        # While our Queue is not empty
        while q:

            # Iterate through the len of our Queue at each level
            for i in range(len(q)):
                # 
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

# Iterative DFS
class Solution:
    def maxDepth(self, root: TreeNode):
        # Node and depth
        stack = [[root, 1]]
        res = 0
        while stack:
            # When popping from the stack you get the node and the depth
            node, depth = stack.pop()

            # If our node is not empty
            if node:
                # Updating our result
                res = max(res, depth)
                # Adding to our stack 
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res




