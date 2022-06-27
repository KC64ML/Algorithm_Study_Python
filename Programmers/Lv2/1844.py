from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(col, row, maps):
    queue = deque()
    queue.append((0, 0, 1))
    res = 1e9

    while queue:
        x, y, cnt = queue.popleft()

        if x == row - 1 and y == col - 1:
            if res > cnt:
                res = cnt
        else:
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]

                if 0 <= next_x < row and 0 <= next_y < col:
                    if maps[next_x][next_y] == 1:
                        maps[next_x][next_y] = 0
                        queue.append((next_x, next_y, cnt + 1))

    if res == 1e9:
        res = -1

    return res


def solution(maps):
    answer = 0
    col = len(maps[0])
    row = len(maps)

    if maps[0][0] == 0:
        answer = -1
    else:
        answer = dfs(col, row, maps)

    print(answer)

    return answer
