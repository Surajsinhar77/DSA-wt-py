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
    
    def display(self, head):
        if(head == None):
            return

        print(head.data," ", end=" ")
        self.display(head.next)