from collections import deque

t = int(input())

list_array = []
n = 0
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    array_sum = list_array[0][0]
    q = deque([])
    q.append((0, 0, array_sum))
    # total_data = array_sum
    total_list = [[INF] * n for _ in range(n)]

    while q:
        cur_q = q.popleft()

        for idx in range(4):
            x_cordinate = dx[idx] + cur_q[0]
            y_cordinate = dy[idx] + cur_q[1]

            if x_cordinate < 0 or x_cordinate >= n or y_cordinate < 0 or y_cordinate >= n:
                continue

            cur_sum = list_array[x_cordinate][y_cordinate] + cur_q[2]

            if total_list[x_cordinate][y_cordinate] <= cur_sum:
                continue

            total_list[x_cordinate][y_cordinate] = cur_sum

            q.append((x_cordinate, y_cordinate, cur_sum))

    return total_list[n-1][n-1]


for _ in range(t):
    n = int(input())
    list_array = []

    for _ in range(n):
        list_array.append(list(map(int, input().split())))

    print(bfs())
