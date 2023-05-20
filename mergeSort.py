import array as ary

def merge(arr, f , mid , l):
    i = f
    j = mid+1
    n1 = mid
    n2 = l
    ans = []

    print("i: ",i," j:", j , " n1 : ",n1 , " n2: ",n2, " ans : ",ans)
    while(i<=n1 and j<=n2):
        if(arr[i] < arr[j]):
            ans.append(arr[i])
            print(ans)
            i+=1
        else:
            ans.append(arr[j])
            j+=1

    while(i<=n1):
        ans.append(arr[i])
        i+=1

    while(j<=n2):
        ans.append(arr[j])
        j+=1

    k = 0
    for i in range(f, l+1):
        arr[i] = ans[k]
        k+=1


def mergeSort(arr, f , l):
    if(f >= l):
        return

    print("ansdka")
    mid = int((f+l)/2)
    print(mid)
    mergeSort(arr, f ,mid)
    mergeSort(arr, mid+1, l)
    merge(arr, f , mid , l)
    print(arr)


ary1 = ary.array('i', [])
size = int(input("size of array one : "))

for i in range(size):
    ary1.append(int(input()))


mergeSort(ary1, 0, size-1)
print(ary1)