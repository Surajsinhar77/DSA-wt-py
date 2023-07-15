from collections import deque
from queue import Queue

class treenode:
    data = 0
    childern = []

    def __init__(self, data):
        self.childern = []
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
                    front.childern.append(newNode)
                    pendingNode.put(newNode)
        return root

    # def DisplayLevel(self, root):
    #     if(root == None):
    #         return
        
    #     print("Root Data : ",root.data)
    #     pendingNode = Queue() 
    #     pendingNode.put(root)

    #     while(pendingNode.qsize() > 0):
    #         front = pendingNode.get()
    #         print(len(front.children))
    #         for i in range(0, len(front.children)):
    #             print("Children of :",front.data," ",front.children[i].data, end=" ")
    #             pendingNode.put(front.children[i])
    #         print()

    # def display(self, root):
    #     if root is None:
    #         return
    #     print("Root data:", root.data)
    #     pendingQueue = Queue()
    #     pendingQueue.put(root)

    #     while pendingQueue.qsize() > 0:
    #         front = pendingQueue.get()
    #         for i in range(len(front.childern)):
    #             print("childern of:", front.data, ":", front.childern[i].data, end=" | ")
    #             pendingQueue.put(front.childern[i])
    #         print()

ob = treenodeFunction()
root = ob.creatTree()
ob.display(root)



