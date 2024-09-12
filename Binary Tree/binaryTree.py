class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertValue(self, value):
        # Check if value is < or > root value:
        if value < self.value:
            # check if there is a value attached to root node
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insertValue(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insertValue(value)
    
    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.value)
        if self.right:
            self.right.inOrderTraversal()

    def postOrderTraversal(self):
        print(self.value)
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()


    def numLeafNodes(self):
        def countLeaves(root):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 1
            return countLeaves(root.left) + countLeaves(root.right)
        
        return countLeaves(self)
        
    
    

tree = TreeNode(15)
tree.insertValue(8)
tree.insertValue(19)
tree.insertValue(2)
tree.insertValue(22)
tree.insertValue(10)
tree.insertValue(37)
tree.insertValue(14)

# tree.inOrderTraversal()
print(tree.numLeafNodes())