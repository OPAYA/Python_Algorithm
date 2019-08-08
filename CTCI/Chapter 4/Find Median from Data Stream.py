import heapq


class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
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
medianfinder.addNum(0)
medianfinder.addNum(1)
medianfinder.addNum(0)
medianfinder.addNum(2)
print(medianfinder.findMedian())
medianfinder.addNum(0)
medianfinder.addNum(3)
#medianfinder.addNum(10)
print(medianfinder.findMedian())