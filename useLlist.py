from linklist import node, LinklistFunction

ob = LinklistFunction()
newHead  = ob.createLlist()
# print(newHead)
ob.display()
# ob.deletehead()

index = int(input("Enter the index value : "))
ob.deleteIndexNode(index)
ob.display()
