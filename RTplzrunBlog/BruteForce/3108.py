import sys
from collections import deque

maxSize = 2001

read = sys.stdin.readline

sys.setrecursionlimit(2 ** 8)

n = int(read())

arr = [[0] * maxSize for _ in range(maxSize)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

in_queue = deque()

for _ in range(n):
    x1, y1, x2, y2 = map(int, read().split())

    x1 = (x1 + 500) * 2
    y1 = (y1 + 500) * 2
    x2 = (x2 + 500) * 2
    y2 = (y2 + 500) * 2

    for i in range(x1, x2 + 1):
        arr[y1][i] = 1
        arr[y2][i] = 1

    for i in range(y1, y2 + 1):
        arr[i][x1] = 1
        arr[i][x2] = 1
    in_queue.append((y1, x1))  # 시작점

in_queue.append((1000, 1000))

visited = [[False] * maxSize for _ in range(maxSize)]
Pu_Cnt = 0

for q in in_queue:
    if visited[q[0]][q[1]]:
        continue

    Pu_Cnt += 1
    queue = deque()
    queue.append(q)

    while queue:
        qY, qX = queue.popleft()

        if visited[qY][qX]:
            continue
        visited[qY][qX] = True

        for i in range(4):
            next_x = qX + dx[i]
            next_y = qY + dy[i]

            if 0 <= next_x <= 2000 and 0 <= next_y <= 2000:
                if arr[next_y][next_x] and not visited[next_y][next_x]:
                    queue.append((next_y, next_x))

print(Pu_Cnt - 1)
