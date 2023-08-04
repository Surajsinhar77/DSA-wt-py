class BinaryNode:
    data = 0
    left = None
    right = None
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binaryfunctions:
    
    def createBinaryTree(self,inputArray):
        root = None
        data = inputArray.pop()
        if(data == -1):
            return root
        newTreeNode = BinaryNode(data)
        root = newTreeNode

        root.left = self.createBinaryTree(inputArray)
        root.right = self.createBinaryTree(inputArray)
        return root

    def dispaybinaryTree(self, root):
        if(root == None):
            return
        print(root.data , end=' ')
        self.dispaybinaryTree(root.left)
        self.dispaybinaryTree(root.right)

# ob = Binaryfunctions()
# root = ob.createBinaryTree()
# ob.dispaybinaryTree(root)