from sys import stdin as s
from collections import deque


def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()

        for cur_data in graph[node]:
            if cur_data != start and visited[cur_data]:
                print(cur_data)
                return False
            elif not visited[cur_data]:
                queue.append(cur_data)
                visited[cur_data] = True

    return True


k = int(s.readline())

for _ in range(k):
    v, e = map(int, s.readline().split())
    visited = [False] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for idx in range(e):
        a, b = map(int, s.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for idx in range(e):
        if not visited[idx]:
            result = bfs(idx, visited, graph)

            if result == False:
                print("NO")
                break

    if result == True:
        print("YES")
