from sys import stdin as s
from collections import deque


def bfs(start, graph, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        if visited[node]:
            return False



t = int(s.readline())

for _ in range(t):
    n = int(s.readline())
    visited = [False] * (n + 1)
    graph = list(map(int, s.readline().split()))

    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i, graph, visited)