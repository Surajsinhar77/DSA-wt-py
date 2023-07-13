from collections import deque
from queue import Queue

class treenode:
    data = 0
    children = []
    def __init__(self, data):
        self.data = data

class treenodeFunction:
    def creatTree(self):
        root = None
        data = int(input("Enter the Root data : ")) # 3\ 

        if(-1 != data):
            newNode = treenode(data)
            root = newNode
        else:
            return root
        
        pendingNode = Queue() #  3 
        pendingNode.put(root)

        while(pendingNode.qsize() > 0):
            front = pendingNode.get() #   
            n = int(input(f"how many Child do u want to enter : {front.data} : "))
            if(n > 0):
                for i in range(0,n):
                    data = int(input(f'Enter the {front.data} childrens data : '))
                    newNode = treenode(data)
                    front.children.append(newNode)
                    pendingNode.put(newNode)
        return root

ob = treenodeFunction()
root = ob.creatTree()


