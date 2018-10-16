
import random

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def selectionSort(x):
    for size in reversed(range(len(x))):
        max_i = 0
        print(size)
        for i in range(1, 1+size):
            print(i, max_i, numList)
            if x[i] > x[max_i]:
                max_i = i

        swap(x, max_i, size)



#numList = [random.randint(1,100) for _ in range(5)]
numList = [5,7,8,1,2,3]
selectionSort(numList)
print(numList)