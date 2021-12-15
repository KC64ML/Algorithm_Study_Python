import heapq

def heapsort(iterable):
    heap = []
    result = []
    for value in iterable:
        heapq.heappush(heap, value)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

result = heapsort([1,9,0,7,8,6,3,5])
print(result)