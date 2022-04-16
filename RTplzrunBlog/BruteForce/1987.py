# import sys
#
# sys.setrecursionlimit(2 ** 8)
#
# read = sys.stdin.readline
#
# r, c = map(int, read().split())
#
# board_card = []
#
# for _ in range(r):
#     board_card.append(list(map(str, read().strip())))
#
# result = 0
# check = [False] * 26
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# def dfs(x, y, cnt):
#     # print("현재 x, y", x, y, cnt)
#     # print("방문 한 곳 : ", visited)
#     global result
#     result = max(result, cnt)
#
#     for i in range(4):
#         next_x = dx[i] + x
#         next_y = dy[i] + y
#
#         if 0 <= next_x < r and 0 <= next_y < c:
#             check_idx = ord(board_card[next_x][next_y]) - 65
#             if not check[check_idx]:
#                 check[check_idx] = True
#                 dfs(next_x, next_y, cnt + 1)
#                 check[check_idx] = False
#
#
# check[ord(board_card[0][0]) - 65] = True
# dfs(0, 0, 1)
#
# print(result)


import sys

read = sys.stdin.readline
R, C = map(int, read().split())
graph = [read().strip() for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(a, b):
    q = {(a, b, graph[a][b])}
    check = [['' for _ in range(C)] for _ in range(R)]
    check[a][b] = graph[a][b]
    result = 1
    while q:
        x, y, track = q.pop()
        result = max(result, len(track))
        if result == 26:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 좌표 nx, ny을 기준으로 (현재 위치에 저장되어 있는 결과 와 이전 결과 + graph 현재 위치) 가 다르다면
            # check nx, ny에 결과를 저장한다.
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in track and check[nx][ny] != track + graph[nx][ny]:
                check[nx][ny] = track + graph[nx][ny]
                q.add((nx, ny, check[nx][ny]))
    return result


print(bfs(0, 0))
