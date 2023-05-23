import array as ary
a=ary.array('i',[3,2,7,1,4])

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partation(arr, f , l):
    p = arr[f]
    i = f+1
    j = l

    while(i < j):
        while(p > arr[i]):
            i+=1
        while(p < arr[j]):
            j-=1
        if(i<=j):
            swap(arr, i, j)
    swap(arr, f, j)
    return j




print(a)
print(partation(a, 0, len(a)-1))
print(a)
print(partation(a, 0, len(a)-1))
print(a)

print(partation(a, 3, len(a)-1))
print(a)