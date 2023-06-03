
# class class1:
#     a = 0
#     b = 0
#     c = 0
    
#     def __init__(self, j, k ,l):
#         self.a = j
#         self.b = k
#         self.c = l

#     def updateValue(self,newValue):
#         self.c = newValue
#         self.b = newValue
#         # print(c)

#     def destoryElement(self):
#         self.c = -1

#     def display(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)

# object1 = class1(6,7,9)

# # object1.updateValue(6)
# object1.display()
# object1.destoryElement()
# object1.display()



# class StudentInfo:
#     def __init__(self, name, age, branch):
#         self.name = name
#         self.age = age
#         self.branch = branch

#     def print(self):
#         print(f"Name: {self.name}, Age: {self.age}, Branch: {self.branch}")


#     # def update(self):
#     #     self.name = 


# obj = StudentInfo("Adarsh", 18, "ISE")

# obj.print()

# class info:

#     def __init__(self):
#         self.name="pavan"
#         self.course="DSA"
#         self.age=22
#     def updatename(self,nam,ag,cou):
#         self.name=nam
#         self.age=ag
#         self.course=cou
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.course)

# obj = info()
# obj.display()
# obj.updatename("Pavan sai",21,"FSD")
# obj.display()



# class ClassInfo:
#     name = "name"
#     dpt = "dpt"
#     class_course = "classCourse"
#     def __init__(self, name, dpt, class_course):
#         self.name = name
#         self.dpt = dpt
#         self.class_course = class_course
#     def display_info(self):
#         print("Name:", self.name)
#         print("dpt:", self.dpt)
#         print("course:", self.class_course)
        
# s1 = ClassInfo("Husna", "CST", "DSA")
# s1.display_info()


class studentInfo:
    def __init__ (self):
        self.name="pallavi"
        self.class_name="G1"
        self.course="python"

    def changeName(self,Name):
        self.name=Name
    def changeClass(self,Class):
        self.class_name=Class
    def changeCourse(self,Course):
        self.course=Course
    def display(self):
        print("name=",self.name)
        print("class=",self.class_name)
        print("course=",self.course)

obj=studentInfo()
obj.changeName("Husna")
obj.changeCourse("Java")
obj.display()
