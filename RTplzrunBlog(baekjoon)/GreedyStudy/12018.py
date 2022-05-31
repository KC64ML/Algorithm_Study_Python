import sys
import heapq

read = sys.stdin.readline

n, m = map(int, read().split())
heap = []

for i in range(n):
    p, l = map(int, read().split())

    people = list(map(int, read().split()))
    people.sort(reverse=True)

    mil = people[-1]

    if l > p:
        heapq.heappush(heap, 1)
    else:
        heapq.heappush(heap, people[l-1])


res = 0
answer = 0

while heap and m - heap[0] >= 0:
    find_data = heapq.heappop(heap)
    m -= find_data
    answer += 1

print(answer)
