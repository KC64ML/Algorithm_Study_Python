# import sys
#
# sys.setrecursionlimit(111111)
#
# x_coordinate = [-1, -1, 0, 1, 1, 1, 0, -1]
# y_coordinate = [0, 1, 1, 1, 0, -1, -1, -1]
#
#
# def dfs(x, y):
#     visited[x][y] = True
#
#     for i in range(8):
#         next_x = x_coordinate[i] + x
#         next_y = y_coordinate[i] + y
#
#         if 1 <= next_x <= h and 1 <= next_y <= w:
#             if visited[next_x][next_y] or graph[next_x][next_y] == 0:
#                 continue
#             # print("현재 x, y ", next_x, next_y)
#             dfs(next_x, next_y)
#
# while True:
#     w, h = map(int, sys.stdin.readline().split())
#
#     if w == 0 and h == 0:
#         break
#
#     graph = [0]
#     visited = [[False] * (w + 1) for _ in range(h + 1)]
#     result = 0
#     for i in range(1, h + 1):
#         graph.append([0] + list(map(int, sys.stdin.readline().split())))
#
#     # print(w, h)
#     for i in range(1, h + 1):
#         for j in range(1, w + 1):
#             if (not visited[i][j]) and graph[i][j] == 1:
#                 # print("현재 i, j 시작 점 : ", i, j )
#                 dfs(i, j)
#                 # for k in range(len(visited)):
#                 #     print(visited[k])
#
#                 result += 1
#                 # print()
#
#     print(result)


import sys
from collections import deque

sys.setrecursionlimit(111111)

x_coordinate = [-1, -1, 0, 1, 1, 1, 0, -1]
y_coordinate = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cur_x, cur_y = queue.popleft()
        visited[cur_x][cur_y] = True
        # print(cur_x, cur_y)
        for i in range(8):
            next_x = x_coordinate[i] + cur_x
            next_y = y_coordinate[i] + cur_y

            if 1 <= next_x <= h and 1 <= next_y <= w:
                if visited[next_x][next_y] or graph[next_x][next_y] == 0:
                    continue
                # print("현재 x, y ", next_x, next_y)
                graph[next_x][next_y] = 0
                queue.append((next_x, next_y))

while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph = [0]
    visited = [[False] * (w + 1) for _ in range(h + 1)]
    result = 0
    for i in range(1, h + 1):
        graph.append([0] + list(map(int, sys.stdin.readline().split())))

    # print(w, h)
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if (not visited[i][j]) and graph[i][j] == 1:
                # print("현재 i, j 시작 점 : ", i, j )
                bfs(i, j)
                # for k in range(len(visited)):
                #     print(visited[k])

                result += 1
                # print()

    print(result)