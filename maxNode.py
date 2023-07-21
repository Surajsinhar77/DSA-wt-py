from treeNode import treenode, treenodeFunction

def countleafNode(root):  
    if(root == None):
        return 0
    if(len(root.childern) == 1):
        return 1
    ans = 0
    for i in range(len(root.childern)):
        ans+=countleafNode(root.childern[i])
    return ans

ob = treenodeFunction()
root = ob.creatTree()
ob.depthForTraversal(root)
print("Leaf nodes : ",countleafNode(root))