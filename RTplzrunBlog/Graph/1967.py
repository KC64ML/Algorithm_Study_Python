import sys

sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]

# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())

    graph[a].append([b, c])  # 부모에서 자식
    graph[b].append([a, c])  # 자식에서 부모


def dfs(num, wei):
    for i in graph[num]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 찾은 노드에서 가장 먼 노드를 찾는다.(인덱스 반환)
first_result = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[first_result] = 0
dfs(first_result, 0)

print(max(distance))
