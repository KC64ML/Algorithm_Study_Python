import sys
from collections import deque

read = sys.stdin.readline

t = int(read())


def bfs():
    q = deque()
    q.append((a, ''))
    visited = [False] * 10000

    while q:
        next_data, path = q.popleft()

        if next_data == b:
            print(path)
            break

        num = (next_data * 2) % 10000
        if not visited[num]:
            visited[num] = True
            q.append((num, path + 'D'))

        num = (next_data - 1) % 10000
        if not visited[num]:
            visited[num] = True
            q.append((num, path + 'S'))

        num = (next_data // 1000 + (next_data % 1000) * 10) % 10000
        if not visited[num]:
            visited[num] = True
            q.append((num, path + 'L'))

        num = ((next_data % 10) * 1000 + next_data // 10) % 10000
        if not visited[num]:
            visited[num] = True
            q.append((num, path + 'R'))


while t > 0:
    a, b = map(int, read().split())

    bfs()

    t -= 1
