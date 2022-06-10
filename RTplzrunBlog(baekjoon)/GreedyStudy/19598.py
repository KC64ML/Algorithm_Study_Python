import sys
import heapq

read = sys.stdin.readline

n = int(read())

room1 = []

for _ in range(n):
    s, e = map(int, read().split())
    room1.append([s, e])

room1.sort()

answer = []
heapq.heappush(answer, room1[0][1])

for i in range(1, n):
    if room1[i][0] < answer[0]:
        heapq.heappush(answer, room1[i][1])
    else:
        heapq.heappop(answer)
        heapq.heappush(answer, room1[i][1])

print(len(answer))