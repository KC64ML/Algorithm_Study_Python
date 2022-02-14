from sys import stdin as s

n, k = map(int, s.readline().split())

tree = [0] * 400005


def init(node, s, e):
    if s == e:
        tree[node] = 1
        return tree[node]

    mid = (s + e) >> 1
    tree[node] = init(2 * node, s, mid) + init(2 * node + 1, mid + 1, e)
    return tree[node]


def query(node, s, e, k):
    tree[node] -= 1
    if s == e:
        return s
    mid = (s + e) >> 1
    if tree[2 * node] >= k:
        return query(2 * node, s, mid, k)
    else:
        return query(2 * node + 1, mid + 1, e, k - tree[2 * node])


init(1, 1, n)
x = k
print("<", end="")
for idx in range(0, n - 1):
    print("%d, " % query(1, 1, n, x), end="")
    x += k - 1
    if x % tree[1] == 0:
        x = tree[1]
    else:
        x %= tree[1]

print("%d" % query(1, 1, n, x), end="")
print(">")
