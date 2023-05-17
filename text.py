
#  1 2 3 4 5 6 8 9 10 14 16 19 22 23 25 26 27 29 31 34 35 36 38 39 40 45 46 48 50 51 52 57 59 60 61 63 67 68 69 71 75 76 77 79 81 82 83 86 87 88 90 92 93 94 95 96 98 99 100
#  93

def binaryS(arr, lb, ub, k):
        if(lb<ub):   # 3 == 3
            mid = int((lb+ub)/2)
            if(k == arr[mid]):
                return mid
            elif(arr[mid] > k):
                return binaryS(arr, lb, mid-1, k)
            else:
                return binaryS(arr, mid+1, ub, k)
        else:
            return -1




import array as ar
arr = ar.array('i', [])


size = int(input())

print(arr)

for i in range(0,size):
    a = int(input())
    if(a == -1):
        break
    arr.append(a)

item = int(input("item to find : "))

print( binaryS(arr, 0, len(arr)-1, item))