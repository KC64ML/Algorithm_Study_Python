from collections import deque
import sys

read = sys.stdin.readline

f, s, g, u, d = map(int, read().split())

visited = [False] * (f + 1)

ud = [u, d * -1]


def bfs():
    q = deque()
    q.append((s, 0))
    global result

    visited[s] = True
    while q:
        cur_data, cnt = q.popleft()

        if cur_data == g:
            result = cnt
            return True

        for i in ud:
            next_layer = cur_data + i

            if 1 <= next_layer <= f and not visited[next_layer]:
                visited[next_layer] = True
                q.append((next_layer, cnt + 1))

    return False


result = 0

if bfs():
    print(result)
else:
    print("use the stairs")
