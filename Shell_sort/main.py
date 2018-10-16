import random

def gapInsertionSort(x, start, gap):
    for target in range(start-gap, len(x), gap):
        


def shellSort(x):
    gap = len(x) // 2
    while gap > 0:
        for start in range(gap):
            ga