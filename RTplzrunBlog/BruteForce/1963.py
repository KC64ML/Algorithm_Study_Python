import sys
from collections import deque

read = sys.stdin.readline

t = int(read())

# 소수 구하기

decimal_number = [True] * 10000

def decimal_function():
    for i in range(2, 10000):
        if decimal_number[i]:
            for j in range(i + i, 10000, i):
                decimal_number[j] = False


decimal_function()


def bfs():
    queue = deque()
    queue.append((a, 0))
    visited = [False] * 10010

    while queue:
        now, cnt = queue.popleft()
        strNow = str(now)

        if now == b:
            return cnt

        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i + 1:])

                if not visited[temp] and decimal_number[temp] and temp >= 1000:
                    visited[temp] = True
                    queue.append((temp, cnt + 1))


while t > 0:
    a, b = map(int, read().split())
    result = bfs()
    if not result:
        print(0) # Impossible
    else:
        print(result)

    t -= 1
