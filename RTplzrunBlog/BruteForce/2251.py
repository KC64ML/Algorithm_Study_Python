from collections import deque
import sys

read = sys.stdin.readline

aBucket, bBucket, cBucket = map(int, read().split())


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0] * 210 for _ in range(210)]
    result = []

    while q:
        a, b = q.popleft()
        c = cBucket - a - b
        if visited[a][b]:
            continue
        visited[a][b] = 1
        if a == 0:
            result.append(c)

        # 1 ~ 6가지
        # (1) a->b
        water = min(a, bBucket - b)
        q.append((a - water, b + water))
        # (2) a->c
        water = min(a, cBucket - c)
        q.append((a - water, b))
        # (3) b->a
        water = min(b, aBucket - a)
        q.append((a + water, b - water))
        # (4) b->c
        water = min(b, cBucket - c)
        q.append((a, b - water))
        # (5) c->a
        water = min(c, aBucket - a)
        q.append((a + water, b))
        # (6) c->b
        water = min(c, bBucket - b)
        q.append((a, b + water))

    return sorted(result)


print(' '.join(map(str, bfs())))
