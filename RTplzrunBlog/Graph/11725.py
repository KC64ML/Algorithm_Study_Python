import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]


def bfs(idx):
    queue = deque()
    queue.append((idx, idx))

    while queue:
        cur_node, parent = queue.popleft()

        if tree[cur_node][0] != parent:
            for idx in range(len(tree[cur_node])):
                if tree[cur_node][idx] == parent:
                    tree[cur_node][idx], tree[cur_node][0] = tree[cur_node][0], tree[cur_node][idx]
                    break

        # [0] 부모노드 저장

        for i in range(1, len(tree[cur_node])):
            queue.append((tree[cur_node][i], cur_node))


for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


bfs(1)

for idx in range(2, n + 1):
    print(tree[idx][0])

#
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# graph = [[] for _ in range(n + 1)]
# parent = [0 for _ in range(n + 1)]
#
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# def bfs():
#     q = deque()
#     q.append(1)
#     while q:
#         node = q.popleft()
#         for i in graph[node]:
#             if parent[i] == 0:
#                 parent[i] = node
#                 q.append(i)
#
#     return parent
#
# bfs()
#
# for i in parent[2:]:
#     print(i)