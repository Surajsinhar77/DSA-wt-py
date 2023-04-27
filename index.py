# print("hellow world")


# # logical operator

# # and ,  or , not ,  ^ 

# # 5 =  8421
#     # 0101
#     # 1000


# # print(2^2^3^3^4);

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)


# print("\n")

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)


# print("\n")

# print( not True)
# print( not False)


# int 4bit
# float 8bit

# char  1bit
# boolen 1bit


# if , else, elif 

# if (False):
#     print("statement one ")
# elif(True):
#     print("statement mid")
# else:
#     print("statement 2")


# loop

# i = 1
# while(i<10):
#     print("looping", end=" ")
#     i+=1

#  Array 

# import numpy

# arr = []
# arry = numpy.array(arr)
# print(type(arry))

# arr 1: newarry2

arr = []

arr.append(4)
arr.append(5)
arr.append(6)
arr.append(7)

print(arr[0])
print(arr[3])
arr[2] = 8
arr.insert(3, 9)
print(arr)

# arr.pop()
# arr.pop()
print(arr)



n = len(arr)
i = 0
sum =0

while(i <= n-1):
    if(arr[i] == 8):
        # print('sajhkajd')
        i+=1
        continue
    sum+=arr[i] # sum = sum + arr[i]
    i+=1

print(sum)







