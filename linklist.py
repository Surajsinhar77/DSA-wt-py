class node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

class LinklistFunction:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def createLlist(self):
        self.head
        datas = int(input("Enter the data : "))
        while(datas != -1):
            if(self.head == None):
                self.head = node(datas)
                self.tail = self.head
            else:
                newNode = node(datas)
                self.tail.next = newNode
                self.tail = self.tail.next
            datas = int(input("Enter the data : "))
        return self.head
    
    def __display(self, tempHead):
        if(tempHead == None):
            return

        print(tempHead.data," ", end=" ")
        self.__display(tempHead.next)

    def display(self):
        tempHead = self.head
        self.__display(tempHead)

    def deletehead(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            return self.head
        print("LinkList is Empty")
    
    def deleteIndexNode(self, index):
        if(self.head != None):
            temp = self.head
            p = self.head
            count = 0
            if(index == 1):
                self.head = self.deletehead()
                return
            while(count != index-1):
                if(p.next == None):
                    print("This is invalid indexing ")
                    return
                elif(temp.next.next == None and count+1 == index):
                    temp.next = None
                    return
                p = p.next
                temp = temp.next
                count+=1
            p = p.next.next
            temp.next.next = None
            temp = p
