
import array as ary
# --------------------------------------------

def mergeingTwoArray(ary1, ary2):
    i = 0
    j = 0
    n1 = len(ary1)-1
    n2 = len(ary2)-1
    ans = []
    while(i<=n1 and j<=n2):
        if(ary1[i] < ary2[j]):
            ans.append(ary1[i])
            i+=1
        elif(ary1[i] == ary2[j]):
            ans.append(ary1[i])
            ans.append(ary2[j])
            i+=1
            j+=1
        else:
            ans.append(ary2[j])
            j+=1

    while(i<=n1):
        ans.append(ary1[i])
        i+=1

    while(j<=n2):
        ans.append(ary2[j])
        j+=1

    return ans
# end of function


ary1 = ary.array('i', [])
size = int(input("size of array one : "))

for i in range(size):
    ary1.append(int(input()))

ary2 = ary.array('i', [])
size2 = int(input("size of array one : "))


for i in range(size2):
    ary2.append(int(input()))


ans = ary.array('i', [])

ans =  mergeingTwoArray(ary1, ary2)

print(ans)






