from collections import defaultdict
import heapq

def rearrange(string):
    frequencies = defaultdict(int)
    print(frequencies)
    for letter in string:

        frequencies[letter] += 1

    heap = []
    for char, count in frequencies.items():

        heapq.heappush(heap, (-count, char))
    print(heap)
    count, char = heapq.heappop(heap)
    result = [char]

    while heap:
        last = (count + 1, char)

        count, char = heapq.heappop(heap)
        print(char)
        result.append(char)
        print(result)
        if last[0] < 0 :
            heapq.heappush(heap, last)
    if len(result) == len(string):
        return "".join(result)
    else:
        return ""




a=rearrange('aaabbc')
print(a)