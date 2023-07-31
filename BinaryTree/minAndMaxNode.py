from BinaryNode import BinaryNode, Binaryfunctions
import math

class pair:
    def __init__(self, first = 0, second = 0):
        self.first = first
        self.second = second


def findMaxAndMinNode(root):
    if(root == None):
        p1 = pair(0,math.inf)
        # p1.first = 0
        # p1.second = math.inf
        return p1
    
    leftAns = findMaxAndMinNode(root.left)
    rightAns = findMaxAndMinNode(root.right)
    Vmax =  max(leftAns.first, rightAns.first, root.data)
    Vmin = min(leftAns.second, rightAns.second, root.data)
    ans = pair(Vmax, Vmin)
    return ans

# 2 1 7 -1 -1 11 -1 -1 3 9 -1 -1 8 -1 -1

ob = Binaryfunctions()
root = ob.createBinaryTree()
ob.dispaybinaryTree(root)
ans = findMaxAndMinNode(root)
print()
print('max and min : ', ans.first," ",ans.second)