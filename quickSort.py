def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(array,f,l):
    p=array[f]
    i=f+1
    j=l
    
    while(i<=j):
        while(i<=j  and p >= array[i]):
            i+=1
        while(i<=j and p <= array[j] ):
            j-=1
        if(i<=j):
            swap(array , i ,j)
    swap(array,f,j)
    return j

def quick_sort(array,f,l):
    if(f<=l):
        key=partition(array,f,l)
        quick_sort(array,f,key-1)
        quick_sort(array,key+1,l)

import array as ary
A=ary.array('i', [3,2,7,1,4])

print("before : ", A)

quick_sort(A, 0, len(A)-1)

print(A)

