# import sys
# import heapq
#
# read = sys.stdin.readline
#
# n = int(read())
#
# dist = {i: [] for i in range(10001)}
#
# max_day = 0
#
# for i in range(n):
#     p, d = map(int, read().split())
#     dist[d].append(p)
#
#     if max_day < d:
#         max_day = d
#
# dist = list(dist.items())
# dist.sort(key=lambda x: (x[0], x[1].sort(reverse=True)))
# dist = dict(dist)
# queue = [0]
#
# for i in range(1, max_day + 1):
#     cur_day = min(i, len(dist[i]))
#
#     for j in range(cur_day):
#         if dist[i][j] > queue[0] or len(queue) < i:
#             if len(queue) == i:
#                 heapq.heappop(queue)
#             heapq.heappush(queue, dist[i][j])
# print(sum(queue))

import heapq
import sys

read = sys.stdin.readline

n = int(read().strip("\n"))

lectures = []

for _ in range(n):
    p, d = map(int, read().split())
    lectures.append([p, d])

lectures.sort(key = lambda x: x[1])

queue = []

for pay, day in lectures:
    heapq.heappush(queue, pay)

    if day < len(queue):
        heapq.heappop(queue)

print(sum(queue))
