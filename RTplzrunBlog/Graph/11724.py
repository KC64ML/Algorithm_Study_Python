from collections import deque
from sys import stdin as s


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        cur_data = queue.popleft()

        for i in range(1, n + 1):
            if graph[cur_data][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)


n, m = map(int, s.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

visited = [False] * (n + 1)

result = 0

for _ in range(m):
    u, v = map(int, s.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i, graph, visited)
        result += 1

print(result)
