import sys
from collections import deque

read = sys.stdin.readline

n, k = map(int, read().split())


# bfs

def bfs():
    queue = deque()
    queue.append((n, 0))
    visited = [False] * 100010
    visited[n] = True

    while queue:
        x, cnt = queue.popleft()

        if x == k:
            # bfs 특징 상 작은 것부터 검색 하니, 나오면 종료하면 된다.
            print(cnt)
            break

        for move_data in (x - 1, x + 1, 2 * x):
            if 0 <= move_data <= 100000 and not visited[move_data]:
                visited[move_data] = True
                queue.append((move_data, cnt + 1))


bfs()
