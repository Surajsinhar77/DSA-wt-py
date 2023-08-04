from BSTNode import BinaryNode, Binaryfunctions 


def insertingElementInBST(root, value):
    if(root==None):
        newNode = BinaryNode(value)
        root = newNode
        return root
    
    if(value < root.data):
        root.left = insertingElementInBST(root.left, value)
    else:
        root.right = insertingElementInBST(root.right, value)
    return root

ob = Binaryfunctions()
# paste your Full input element in the Array 
inputArray = [3, 2, -1, -1 , 7, 4 , -1, -1 , 8 , -1 ,-1]
inputArray.reverse()
print("reversing Node ", inputArray)

root = ob.createBinaryTree(inputArray)
print("Tree Creation Done")
root = insertingElementInBST(root,5)

print("Tree Inseting Done ")
ob.dispaybinaryTree(root)
