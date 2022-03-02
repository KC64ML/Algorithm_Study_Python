from collections import deque
import sys

n = int(sys.stdin.readline())

graph = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

x_coordinate = [-1, 0, 1, 0]
y_coordinate = [0, 1, 0, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            nx = x_coordinate[i] + cur_x
            ny = y_coordinate[i] + cur_y

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] or (not graph[nx][ny]):
                    continue

                visited[nx][ny] = True
                island[len(island) - 1].append((nx, ny))
                queue.append((nx, ny))


def bfs2(cur_idx):
    # 방문한지 안한지 확인하기 위해
    visited2 = [[False] * n for _ in range(n)]
    queue2 = deque()
    global result

    for idx in range(len(island[cur_idx])):
        (x, y) = island[cur_idx][idx]
        visited2[x][y] = True
        queue2.append((x, y, 0))

    while queue2:
        cur_x, cur_y, cur_len = queue2.popleft()

        for i in range(4):
            nx = x_coordinate[i] + cur_x
            ny = y_coordinate[i] + cur_y

            if 0 <= nx < n and 0 <= ny < n:
                if not visited2[nx][ny] and graph[nx][ny]:
                    result = min(result, cur_len)
                elif not visited2[nx][ny] and not graph[nx][ny]:
                    visited2[nx][ny] = True
                    queue2.append((nx, ny, cur_len + 1))
    return result
    # 현재 해당 좌표안이라면
    # 만약 좌표값이 0이고, 방문한 곳이 아니라면 큐에 삽입한다.
    # 만약 좌표값이 1일 때는 가장 작은 값을 찾는다.


island = []

for i in range(n):
    for j in range(n):
        if graph[i][j] and (not visited[i][j]):
            island.append(deque())
            island[len(island) - 1].append((i, j))
            bfs(i, j)

result = sys.maxsize

# 해당 구간만 확인하기
for i in range(len(island)):
    bfs2(i)

print(result)



# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# # 섬을 구분해주는 bfs
# def bfs1(i, j):
#     global count
#     q = deque()
#     q.append([i, j])
#     vis[i][j] = True
#     arr[i][j] = count
#
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not vis[nx][ny]:
#                 vis[nx][ny] = True
#                 arr[nx][ny] = count
#                 q.append([nx, ny])
#
# # 바다를 건너며 가장 짧은 거리를 구한다.
# def bfs2(z):
#     global answer
#     dist = [[-1] * n for _ in range(n)] # 거리가 저장될 배열
#     q = deque()
#
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == z:
#                 q.append([i, j])
#                 dist[i][j] = 0
#
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 갈 수 없는 곳이면 continue
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
#             if arr[nx][ny] > 0 and arr[nx][ny] != z:
#                 answer = min(answer, dist[x][y])
#                 return
#             # 바다를 만나면 dist를 1씩 늘린다.
#             if arr[nx][ny] == 0 and dist[nx][ny] == -1:
#                 dist[nx][ny] = dist[x][y] + 1
#                 q.append([nx, ny])
#
#
# n = int(input())
#
# arr = [list(map(int, input().split())) for _ in range(n)]
# vis = [[False] * n for _ in range(n)]
# count = 1
# answer = sys.maxsize
#
# for i in range(n):
#     for j in range(n):
#         if not vis[i][j] and arr[i][j] == 1:
#             bfs1(i, j)
#             count += 1
#
# # print(arr)
#
# for i in range(1, count):
#     bfs2(i)
#
# print(answer)

# 참고 : https://kyun2da.github.io/2021/04/22/makeBridge/