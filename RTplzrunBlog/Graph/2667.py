# import sys
# from collections import deque
#
#
# x_coordinate = [-1 , 0 , 1, 0]
# y_coordinate = [0, 1, 0, -1]
#
# def bfs(x, y):
#     queue = deque()
#     # print("현재 좌표 : ", x, y)
#     queue.append((x, y))
#     visited[x][y] = True
#     result = 1
#     while queue:
#         x_out, y_out = queue.popleft()
#
#         for i in range(4):
#             next_x = x_out + x_coordinate[i]
#             next_y = y_out + y_coordinate[i]
#
#             if next_x < 1 or next_x > n or next_y < 1 or next_y > n:
#                 continue
#             if visited[next_x][next_y]:
#                 continue
#             if graph[next_x][next_y] == 0:
#                 continue
#             visited[next_x][next_y] = True
#             result += 1
#             queue.append((next_x, next_y))
#     return result
#
# n = int(sys.stdin.readline())
#
# graph = [0]
# visited = [[False] * (n+1) for _ in range(n+1)]
#
# total_list = []
#
# for idx in range(n):
#     in_graph = list(sys.stdin.readline().strip())
#     graph.append([0] + list(map(int, in_graph)))
#
# # print(graph)
#
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         if not visited[i][j] and graph[i][j] == 1:
#             result = bfs(i, j)
#             total_list.append(result)
#
# total_list.sort()
#
# print(len(total_list))
# print('\n'.join(map(str, total_list)))


import sys

sys.setrecursionlimit(111111)

x_coordinate = [-1 , 0 , 1, 0]
y_coordinate = [0, 1, 0, -1]



def dfs(x, y):
    global result
    result += 1
    visited[x][y] = True

    for i in range(4):
        next_x = x_coordinate[i] + x
        next_y = y_coordinate[i] + y

        if 1<= next_x <= n and 1 <= next_y <=n:
            if visited[next_x][next_y] or graph[next_x][next_y] == 0:
                continue

            dfs(next_x, next_y)


n = int(sys.stdin.readline())

graph = [0]
visited = [[False] * (n+1) for _ in range(n+1)]

total_list = []

for idx in range(n):
    in_graph = list(sys.stdin.readline().strip())
    graph.append([0] + list(map(int, in_graph)))

for i in range(1,n+1):
    for j in range(1, n+1):
        if not visited[i][j] and graph[i][j] == 1:
            result = 0
            dfs(i, j)
            total_list.append(result)

total_list.sort()
print(len(total_list))
print('\n'.join(map(str, total_list)))
