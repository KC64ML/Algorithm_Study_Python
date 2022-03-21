# # 이와 같이 시작점이 정해진 그래프에서는 dfs를 사용하며, 미리 해당 점들을 저장해놓기
#
# import sys
# from collections import deque
#
# m, n = map(int, sys.stdin.readline().split())
# graph = []
#
# x_coordinate = [-1, 0, 1, 0]
# y_coordinate = [0, 1, 0, -1]
#
#
# def bfs():
#     day = 0
#     while queue:
#         # print("길이", len(queue))
#         day += 1
#         # 현재 위치에서 좌우 펼치면서 확인 돌림
#         for _ in range(len(queue)):
#             cur_x, cur_y = queue.popleft()
#             for i in range(4):
#                 next_x = cur_x + x_coordinate[i]
#                 next_y = cur_y + y_coordinate[i]
#
#                 if (0 <= next_x < n) and (0 <= next_y < m) and (graph[next_x][next_y] == 0):
#                     graph[next_x][next_y] = 1
#                     queue.append((next_x, next_y))
#
#     return day
#
# for _ in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
#
# queue = deque()
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             queue.append((i, j))
# day = bfs()
#
# check = False
#
# for dot in graph:
#     if 0 in dot:
#         print(-1)
#         check = True
#         break
# if not check:
#     print(day-1)
#
#
#


# 이와 같이 시작점이 정해진 그래프에서는 dfs를 사용하며, 미리 해당 점들을 저장해놓기

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
graph = []

queue = deque()

x_coordinate = [-1, 0, 1, 0]
y_coordinate = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def bfs():
    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            next_x = cur_x + x_coordinate[i]
            next_y = cur_y + y_coordinate[i]

            if (0 <= next_x < n) and (0 <= next_y < m) and (graph[next_x][next_y] == 0):
                graph[next_x][next_y] = graph[cur_x][cur_y] + 1
                queue.append((next_x, next_y))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))


bfs()

result = -2
isTrue = False

for i in graph:
    for arr_data in i:
        if arr_data == 0:
            isTrue = True

        # print(result, arr_data)
        result = max(result, arr_data)
        # print(result)


if isTrue:
    print(-1)
else:
    print(result - 1)
