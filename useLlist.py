from linklist import node, LinklistFunction

ob = LinklistFunction()
newHead  = ob.createLlist()
# print(newHead)
ob.display()
# ob.deletehead()

# index = int(input("Enter the index value : "))
# ob.deleteIndexNode(index)
# ob.display()

# data = int(input("Enter the Data value : "))

# print(ob.searchingNode(data))

# ob.insertionAtIndedx(index, data)

# ob.display()


# print("length of the LinkList",ob.getLength())

newReverseList = ob.reverse()
print()
# ob.display(newReverseList)
# ob.display()

def reverse(head):
        if(head == None):
            return { "first" : None, "second": None}
        
        temp = reverse(head.next)
        if(temp['first'] == None):
            temp['first'] = head
            temp['second'] = head
        else:
            head.next = None
            temp['second'].next = head
            temp['second'] = head
        return temp