from sys import stdin
from collections import deque

read = stdin.readline

v = int(read())

graph = [[] for _ in range(v + 1)]

for _ in range(v):
    c = list(map(int, read().split()))

    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))


def bfs(start):
    visited = [-1] * (v + 1)
    queue = deque()
    queue.append(start)
    visited[start] = 0

    # 거리, 노드
    _max = [0, 0]

    while queue:
        c = queue.popleft()

        # e: 노드, wei : 거리
        for e, wei in graph[c]:
            if visited[e] == -1:
                visited[e] = visited[c] + wei  # 현재 c를 기준, 시작 노드에서 c까지 거리 + (노드 c에서 노드 d까지 거리)
                queue.append(e) # 현재 노드 저장

                # 방문한 노드라면, 길이를 잰다.
                if _max[0] < visited[e]:
                    _max = visited[e], e

    return _max


distance, node = bfs(1)
distance, node = bfs(node)

print(distance)
