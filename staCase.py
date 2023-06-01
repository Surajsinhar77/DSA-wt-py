
def strCase(n):
    if n<0:
        return 0
    
    if n == 0:
        return 1

    return strCase(n-3)+strCase(n-2)+strCase(n-1)


n = int(input("enter the Number : "))
print(strCase(n))


# 5 