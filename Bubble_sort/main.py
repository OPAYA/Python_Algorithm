import random

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubblesort(x):
    for size in reversed(range(len(x))):

        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)


numList = [random.randint(1,100) for _ in range(10)]
bubblesort(numList)
print(numList)