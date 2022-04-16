from collections import deque
import sys

read = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, read().split())

# 세로 : n, 가로 : m

graph = [list(map(int, read().strip())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]


def bfs():
    q = deque()
    # q에 넣고
    q.append((0, 0))
    # 0, 0에서 시작한다. (q에 0, 0과 0을 넣는다.)
    # dist[0][0] = 0 시작 점은 한 번에 가니 상관없다.
    dist[0][0] = 0

    # q while 문
    while q:
        # x, y 좌표 점을 발급 받는다.
        x, y = q.popleft()
        # 상하좌우 돈다.
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # 범위 안일 때
            # 아직 방문하지 않은 곳이라면
            # 만약 현재 그래프상 데이터 값이 0이라면
            # 큐에 그냥 삽입한다. (대신에 가장 먼저 넣어야 한다.)
            # 아니라면
            # 큐에 삽입할 때, + 1을 한다.
            if 0 <= next_x < n and 0 <= next_y < m and dist[next_x][next_y] == -1:
                if not graph[next_x][next_y]:
                    dist[next_x][next_y] = dist[x][y]
                    q.appendleft((next_x, next_y))
                else:
                    dist[next_x][next_y] = dist[x][y] + 1
                    q.append((next_x, next_y))


bfs()

print(dist[n - 1][m - 1])
