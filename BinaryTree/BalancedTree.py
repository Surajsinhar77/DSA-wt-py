from BinaryNode import BinaryNode, Binaryfunctions

def heightOfTree(root):
    if(root == None):
        return 0

    return max(heightOfTree(root.left)+1, heightOfTree(root.right)+1)


def isBalancedTree(root):
    if(root == None):
        return True

    leftAns = isBalancedTree(root.left)
    rightAns = isBalancedTree(root.right)

    if(leftAns and rightAns){
        if(abs(heightOfTree(root.left) - heightOfTree(root.right) <= 1)){
            return True
        }else{
            return False
        }
    }
    return False


ob = Binaryfunctions()
root = ob.createBinaryTree()

print(isBalancedTree(root))

ob.dispaybinaryTree(root)