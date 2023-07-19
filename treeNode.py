from collections import deque
from queue import Queue

class treenode:
    data = 0
    childern = []

    def __init__(self, data):
        self.childern = [None]
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
                front.childern.pop()
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


    #Genric Tree
    def depthForTraversal(self, root):
        if(root == None):
            return
        print("Value : ", root.data, end=" ")
        for i in range(0, len(root.childern)):
            self.depthForTraversal(root.childern[i])

            # 1 2 3 4 5 6 7 8 9 11

    # def __sumofNode(self, root, ans):
        


    def sumOfNode(self , root):
        ans = 0
        if(root == None):
            return 0
        # ans+=root.data
        pendingNode = Queue()
        pendingNode.put(root)

        while(pendingNode.qsize() > 0 ):
            front = pendingNode.get()
            ans += front.data
            if(front.childern[0] == None):
                continue
            for i in range(0, len(front.childern)):
                pendingNode.put(front.childern[i])
        return ans 

        # def sumOfNode2(self , root):
        # ans = 0
        # if(root == None):
        #     return 0
        # ans+=root.data
        # pendingNode = Queue()
        # pendingNode.put(root)

        # while(pendingNode.qsize() > 0 ):
        #     front = pendingNode.get()
        #     if(front.childern[0] == None):
        #         continue
        #     for i in range(0, len(front.childern)):
        #         ans += front.data
        #         pendingNode.put(front.childern[i])
        # return ans 

    def inputByRec(self): #   1 2 4 0 5 0
        root = None
        data = int(input(" Enter Root data : "))
        newNode = treenode(data)
        root = newNode
        n = int(input("enter the no of Childs : "))

        for i in range(n):
            child = self.inputByRec()
            if(root.childern[0] == None):
                root.childern.pop()
            root.childern.append(child)
        return root


ob = treenodeFunction()
root = ob.creatTree()
# ob.depthForTraversal(root)
ans = ob.sumOfNode(root)
print("Ans : ", ans)

# ob.display(root)



