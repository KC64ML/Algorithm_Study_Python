import sys
import heapq

read = sys.stdin.readline

n = int(read())

lesson = []

for i in range(n):
    s, t = map(int, read().split())
    lesson.append((s, t))


lesson.sort()

room = []

heapq.heappush(room, lesson[0][1])

for i in range(1, n):
    if room[0] > lesson[i][0]:
        heapq.heappush(room, lesson[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lesson[i][1])

print(len(room))
