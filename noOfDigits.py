def noOfdigits(num):
    if((num//10) == 0):
        return 1

    ans = noOfdigits(num//10)
    return ans+1

num = int(input("Enter any number : "))
print(noOfdigits(num))
# print("1")
# print("2")
# print("3")
# print("4")