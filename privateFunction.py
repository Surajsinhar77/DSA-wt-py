class A:
    def __init__(self):
        pass

    #private functions
    def __Function(self):
        print("private one")


    #public Functions 
    def public(self):
        self.__Function()
        print("public one")


#Object in the A 
ob = A()
ob.public()
# ob.__Function()
