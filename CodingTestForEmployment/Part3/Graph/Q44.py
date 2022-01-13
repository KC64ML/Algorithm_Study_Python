
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

list_array = [[0]]

edges = []
parent = [0] * (n + 1)
result = 0




for idx in range(1, n+1):
    parent[idx] = idx

for _ in range(n):
    list_array.append(list(map(int, input().split())))

for i in range(1, n):
    list_in_array = []

    for j in range(i + 1, n + 1):
        cost = min(abs(list_array[i][0] - list_array[j][0])
                       , abs(list_array[i][1] - list_array[j][1]),
                       abs(list_array[i][2] - list_array[j][2]))
        edges.append((cost, i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
