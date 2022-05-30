from sys import stdin as s
from collections import deque

n, m, v = map(int, s.readline().split())

# 2차 행렬 입력
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
visited2 = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, s.readline().split())

    graph[a].append(b)
    graph[b].append(a)

d = deque()
d2 = deque()

for i in range(1, n + 1):
    graph[i].sort()


def dfs(number):
    visited[number] = True
    d.append(number)

    for idx in graph[number]:
        if visited[idx]:
            continue

        dfs(idx)


def bfs(start):
    # 큐(Queue) 구현을 위해 dequeue 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited2[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        d2.append(v)
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True


dfs(v)
bfs(v)

print(' '.join(map(str, d)))
print(' '.join(map(str, d2)))

