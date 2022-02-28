import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = [[-1] * (m + 1)]

x_coordinate = [-1, 0, 1, 0]
y_coordinate = [0, 1, 0, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y, 1))

    while queue:
        cur_x, cur_y, cur_date = queue.popleft()
        graph[cur_x][cur_y] = cur_date

        visited_minus_cnt = 0

        for i in range(4):
            next_x = cur_x + x_coordinate[i]
            next_y = cur_y + y_coordinate[i]

            if 1 <= next_x <= n and 1 <= next_y <= m:
                if graph[next_x][next_y] == 1:
                    continue
                if graph[next_x][next_y] == -1:
                    visited_minus_cnt += 1
                    continue
                if graph[next_x][next_y] <= (cur_date + 1):
                    continue

                queue.append((next_x, next_y, cur_date + 1))

        if visited_minus_cnt == 4:
            return False

    return True


for _ in range(n):
    graph.append([-1] + list(map(int, sys.stdin.readline().split())))

check = True

for i in range(1, n + 1):
    check = True
    for j in range(1, m + 1):
        if graph[i][j] == 1:
            if not bfs(i, j):
                print(-1)
                check = False
                break

    if not check:
        break

if check:
    print(graph)
