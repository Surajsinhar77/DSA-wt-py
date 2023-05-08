# import array as ary

# A = ary.array('i', [1, 3, 4, 6, 8, 9])

# i = 0
# end =  7-1
# sum = 0
# while(i<end):
#     sum+=A[i]
#     i+=1


# print(sum)


# import numpy as np

# import array as ary

# ar1 = np.array('i', [])
# ar2 = ary.array('i', [])

# A = np.array('i', [1, 2, 3, 4, 5])

# for i in range(len(A)):
# 	if A[i]%2 == 0:
# 		print("It's Even")
# 	else:
# 		print("Odd")
		
# print(type(ar1))
# print(type(ar2))

# import numpy as np

# A = np.array([1, 2, 3, 4, 5])

# for i in range(len(A)):
# 	print(type(A[i]))
# 	if A[i] % 2 == 0:
# 		print("It's Even")
# 	else:
# 		print("Odd")

# ---------------------------------

# import array as ary

# A = ary.array('', [1, 3, 4, 6, 8, 9])

# import numpy as np
# var = np.array(["striung", "suraj", "any", "askd"])

# print(var)

# import array as ary
# A = ary.array('i', [1, 1, 0, 0, 0,])


# import array as arr
# a = arr.array('i',[1,1,0,0,0])
# print(a[2:]+a[:2])


# print(a)

# import array as arr
# a = arr.array('i',[1,1,0,0,0])
# a = a[2:]+a[:2]
# print(a)


# a=arr.array("i",[1,1,0,0,0])

# onecount=a.count(1)

# for j in range(onecount):
#     a.remove(1)

# for k in range(onecount):
#     a.append(1)
# print(a)

# import array as ary
# A=ary.array('i',[1,1,0,0,0])
# i=0

# for i in range(len(A)-1):
#     if A[i] == 0:
#         a=A[i]
#         A[i]=A[i+1]

# print(A)



# import array as ary
# A = ary.array('i', [1, 1, 0, 0, 0])  # 1 0 0 0 1   # 0  0  0 1 1
# i = 0
# end = len(A)

# while(A[i] != 0):
#     temp = A[i]
#     j = i
#     end2 = end;
#     while(j<end-1):
#         A[j] = A[j+1]
#         j+=1 
#     A[j] = temp


# print(A)

# list = ['suraj', 13, 5.6, True]

# print(list)

# import array as ary
# n = int(input("Enter the size of Array : "))

# arr = ary.array('i', [])

# for i in range(n):
#     data = int(input(" : "))
#     arr.append(data)

# print(arr)


# swap
# a = 4
# b = 3
# c = 0

# c = a
# a = b
# b = c

# print( a , b )
#  5 6 7 8 9 
#  5 6 8 9 

# searching 

# import array as ary
# A = ary.array('i', [1, 3, 4, 6, 8, 9])

# d = int(input("give me the element : "))

# for i in range(len(A)):
#     if(d == A[i]):
#         j = i
#         while(j < len(A)-1):
#             A[j] = A[j+1]
#             j+=1
#         break

# print(A)


# def sum(a , b , y ):
#     print(a+b)

# a = 7
# b = 2.4
# ans = sum(a , b, 1)
# print(ans)


# import array as ary
# A = ary.array('i', [1, 3, 4, 6, 8, 9])

# def arraYSum(B):
#     sum = 0
#     for i in range(len(B)):
#         sum+=B[i]
#     return sum 

# # print(B)

# print(arraYSum(A))

# tow Pointer approach 
# import array as ary
# A = ary.array('i', [1, 3, 4, 6, 8, 9, 10])

# i = 0
# j = len(A)-1

# while(i<=j):
#     print(A[i])
#     print(A[j])
#     i+=1
#     j-=1


#  1 2 3  3 2 1

#  1 2 3 4    4 3 2 1 

import array as ary
A = ary.array('i', [1, 3, 4, 6, 8, 9, 10])

# B = ary.array('i', []) # 10 9 .... 1 

# j = len(A)-1
# while(j >=0):
#     B.append(A[j])
#     j-=1

# print(B)

# i  = 0
# j = len(A)-1

# while(i<j):
#     temp = A[i]
#     A[i] = A[j]
#     A[j] = temp
#     i+=1
#     j-=1


# print(A)


# number = 1234  #  4321

# 1234%10  = 4
# 1234/10  = 123
# 12%10





















