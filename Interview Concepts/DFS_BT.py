class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    
    def insertNode(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insertNode(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insertNode(val)


Tree = TreeNode('5')

Tree.insertNode('10')
Tree.insertNode('3')
Tree.insertNode('9')
Tree.insertNode('4')
Tree.insertNode('7')

print(Tree.left.val)