from sys import stdin as s

import sys

sys.setrecursionlimit(111111)
# 파이썬은 기본적으로 재귀 깊이 제한이 매우 낮기 때문에 늘려줘야 한다.

t = int(s.readline())


def dfs(start):
    global result
    visited[start] = True
    cycle.append(start)
    next = graph[start]

    if visited[next]:
        if next in cycle:
            result += cycle[cycle.index(next):]  # next가 시작 점 : 문제에서 보면 4 -> 7 -> 6에서 4가 시작점이라면, 시작점 인덱스 시작부터 끝까지(사이클)
        return
    else:
        dfs(next)


for _ in range(t):
    n = int(s.readline())
    graph = [0] + list(map(int, s.readline().split()))
    visited = [True] + [False] * n
    result = []
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))