import heapq


class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        num1 = -heapq.heappushpop(large, num)
        heapq.heappush(small, num1)
        print('-------------')
        print('num1', num1)
        print('num:',num)
        print('add small', small)
        print('add large', large)
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))
            print('len small', small)
            print('len large', large)

    def findMedian(self):
        small, large = self.heaps
        print('small', small)
        print('large', large)
        if len(large) > len(small):
            return float(large[0])
        
        return (large[0] - small[0]) / 2.0


medianfinder = MedianFinder()
medianfinder.addNum(1)
medianfinder.addNum(3)
medianfinder.addNum(5)
medianfinder.addNum(7)
print(medianfinder.findMedian())
medianfinder.addNum(0)
medianfinder.addNum(3)
medianfinder.addNum(10)
print(medianfinder.findMedian())