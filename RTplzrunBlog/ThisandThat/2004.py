from itertools import combinations
from sys import stdin as s

n, m = map(int, s.readline().split())

cb = list(combinations(range(1, n + 1), m))

cb_size = len(cb)

result = 0

while cb_size:
    if cb_size % 10 != 0:
        break

    result += 1
    cb_size //= 10

print(result)




