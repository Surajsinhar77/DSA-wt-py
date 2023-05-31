# def shiftingTheStr(A, s, e):

# def removetheX(A, s, e):
#     if(s>e):
#         return
#     if(A[s] == 'x'):
#         shiftingTheStr(A,s,e)


# A = input("Enter the String: ")
# removetheX(A, 0, len(A)-1)



# A[0] = 'a'

# print(A)

def shiftingValue(str, s, l):
    i = s
    while(i-1<l):
        str[i] = str[i+1]
        i+=1

    str[l] =" "
    print(len(strArr))


def removeXfromStr(str, s , l):
    if(s>l or str[s] ==" "):
        str.remove(" ")
        return
    print(" --> ",s )
    if(str[s] == 'x'):
        shiftingValue(str, s, l)
        if(s+1<l and str[s] == "x"):
            print("is called ")
            removeXfromStr(str,s,l)
    removeXfromStr(str, s+1, l)



str = input("enter string: ")
strA = list(str)

strArr = []

for i in range(len(str)):
    if(str[i] == ' '):
        continue
    strArr.append(str[i])

print(len(strArr))
removeXfromStr(strArr,0,len(strArr)-1)


# shiftingValue(strArr, 0, len(strArr)-1)
print(len(strArr))

print(strArr)
print(strA)

