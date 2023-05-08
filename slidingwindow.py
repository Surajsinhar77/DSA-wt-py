# def slidingwindo(arr, n, x):
#     i = 0
#     while(i<n-2):
#         if(arr[i]+arr[i+1] == x):
#             print("true : ", i,i+1)
#             break
#         i+=1


# import array as ary
# A = ary.array('i', [1, 3, 4, 6, 8, 9, 10])     # 10

# slidingwindo(A, len(A), 10)

# import array as ary
# A = ary.array('i', [1, 3, 4, 6, 8, 9, 10])     # 10

# def max_min(num):
#     a=num[0]
#     b=num[0]
#     for i in num:
#         if i>a:
#             a=i
#         elif (i < b):
#             b=i
#     print("max num",a)
#     print("min munber",b)  
#     # return (a, b)    

# num = [38,-2,3,10,-4,5]
# max_min(num)

# def defmx(nums):
#     max = nums[0]
#     for i in range(len(nums)):
#         if(max < nums[i]):
#             max = nums[i]
#     return max

# def defmix(nums):
#     min = nums[0]
#     for i in range(len(nums)):
#         if(min > nums[i]):
#             min = nums[i]
#     return min


# import array as ary
# A = ary.array('i', [17, 31, 4, 6, 18, 92, 10])     # 10

# print(defmx(A))
# print(defmix(A))


# def max_min(num):
#     a=num[0]
#     b=num[0]
    
#     for i in num:
#         if i>a:
#             a=i
#         for i in range(len(num)):
#             if num[i] >b and num[i] < a:
#                 b=num[i]
#     return b

# num=[1,27,3,10,8,0,2]
# a = max_min(num)
# print(a)

# import array as ary

# x = ary.array('i', [5, 2, 3, 1, 4])  # n =5  1 2 3 4 5 n2

# 2 5 3 1 4
# 2 3 5 1 4
# 2 3 1 5 4
# 2 3 1 4 5 

# 6, 2, 11, 1, 4
# 2 6 11 1 4
# 2 6 11 1 4
# 2 6 1 11 4

# 2 6 1 4 11
# 2 6 1 4 
# 2 1 6 4
# 2 1 4 6

# max = x[0]
# new = 0

# for i in range(len(x)):
#     if max < x[i]:
#         max = x[i]

# for j in range(len(x)):
#     if new < x[j] < max:
#         new = x[j]

# print(new)

# Sorting