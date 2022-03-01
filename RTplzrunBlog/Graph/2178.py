from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = []

visited = [[False] * m for _ in range(n)]

x_coordinate = [-1, 0, 1, 0]
y_coordinate = [0, 1, 0, -1]

# 한 줄로 입력될 때는 strip()을 사용한다.

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))


def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    result = n * m
    visited[0][0] = True

    while queue:
        x, y, cnt = queue.popleft()
        # print("x, y : ", x,y)

        if x == (n - 1) and y == (m - 1):
            if result > cnt:
                result = cnt

        for i in range(4):
            next_x = x + x_coordinate[i]
            next_y = y + y_coordinate[i]

            if 0 <= next_x < n and 0 <= next_y < m and (not visited[next_x][next_y])\
                    and graph[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, cnt + 1))

    return result


print(bfs())
