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

# root == None
# both child == None
# left child == None
# right child == None
# both child != None

def delNode(root, key):
    if root == None:
        return None
    
    if(root.data > key):
        root.left = delNode(root.left, key)
        return root
    elif(root.data < key):
        root.right = delNode(root.right, key)
        return root
    else:
        if(root.left == None and root.right == None):
            del root
            return None
        elif(root.left == None):
            temp = root.right
            del root
            return temp
        elif(root.right == None):
            temp = root.left
            del root
            return temp
        else:
            temp = root.right
            print("returnning data : ",temp.data)

            minNode = root.right
            root.right = None

            while(minNode.left != None):
                minNode = minNode.left

            minNode.left = root.left
            del root
            print("returnning data : ",temp.data)
            return temp


ob = Binaryfunctions()
# paste your Full input element in the Array 
inputArray = [5, 3 , 1 , 0 , -1 , -1 , 2,-1 ,- 1, 4 , -1 , -1 , 13 , 11, -1, -1 , 15 , 14, 12, -1, -1 , -1, 16, -1, -1]
inputArray.reverse()
print("reversing Node ", inputArray)
root = ob.createBinaryTree(inputArray)

# root = insertingElementInBST(root,5)
key = int(input("Enter the element to delete :"))
root = delNode(root, key)
print(root.data)
ob.dispaybinaryTree(root)
