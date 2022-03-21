from sys import stdin as s


def dfs(start, graph, visited):
    visited[start] = True
    next = graph[start]
    if not visited[next]:
        dfs(next, graph, visited)


t = int(s.readline())

for _ in range(t):
    n = int(s.readline())
    visited = [False] * (n + 1)
    graph = list(map(int, s.readline().split()))
    graph = [0] + graph
    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, graph, visited)
            cnt += 1

    print(cnt)
