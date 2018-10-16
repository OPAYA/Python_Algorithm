import random

def insertSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val


List = [1, 3, 5, 4, 2]
insertSort(List)
print(List)