import array as ary
x = ary.array('i', [5, 2, 3, 1, 4])

minIndex = -1

for i in range(len(x)):
    min =  2147483647
    for j in  range(i, len(x)):
        if(min > x[j]):
            min = x[j]
            minIndex = j
    if(minIndex != i):
        temp = x[i]
        x[i] = x[minIndex]
        x[minIndex] = temp

print(x)