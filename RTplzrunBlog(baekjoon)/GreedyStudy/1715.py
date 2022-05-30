import heapq
import sys

read = sys.stdin.readline

n = int(read())

arr = []

for _ in range(n):
    heapq.heappush(arr, int(read()))

if n == 1:
    print(0)
else:
    answer = 0
    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        heapq.heappush(arr, first + second)
        answer += (first + second)

    print(answer)
