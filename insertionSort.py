import array as ary
x = ary.array('i', [5, 2, 3, 1, 4])

for i in range(1, len(x)):
    temp = x[i]
    j = i-1
    while(j >= 0 and x[j] > temp):
        x[j+1] = x[j]
        j-=1
    x[j+1] = temp


print(x)
