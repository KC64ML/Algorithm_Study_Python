import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def bfs():
    queue = deque()
    queue.append(1)

    while queue:
        node = queue.popleft()

        for alc_node in tree[node]:
            if parent[alc_node] == 0:
                parent[alc_node] = node
                queue.append(alc_node)


bfs()

for cur_node in parent[2:]:
    print(cur_node)




import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(num):
    for i in tree[num]:
        if parent[i] == 0:
            parent[i] = num
            dfs(i)

dfs(1)

for cur_node in parent[2:]:
    print(cur_node)

