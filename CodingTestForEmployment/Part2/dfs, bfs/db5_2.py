from collections import deque

n, m = map(int,input().split())

graph = []
# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    q = deque()
    q.append((x, y))

    
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                print("nx, ny", nx, ny, "x, y" , x, y , "graph", graph[x][y])
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))