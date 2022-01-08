
def find_def(parent, data):
    if parent[data] != data:
        parent[data] = find_def(parent, parent[data])
    return parent[data]


def union_def(parent, a, b):
    a = find_def(parent, a)
    b = find_def(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)
graph = []

for idx in range(1, n + 1):
    parent[idx] = idx

for idx in range(0, m):
    num, a, b = map(int, input().split())

    if num == 0:
        union_def(parent, a, b)
    else:
        if find_def(parent, a) == find_def(parent, b):
            print("YES")
        else:
            print("NO")