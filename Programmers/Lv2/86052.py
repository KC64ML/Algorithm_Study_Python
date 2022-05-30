def bfs(r, c, k, grid, field):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    row = len(grid)
    col = len(grid[0])

    while True:
        if field[r][c][k]:
            break

        field[r][c][k] = 1
        r = (r + dx[k]) % row
        c = (c + dy[k]) % col

        # 다음 번째 K 값
        # L : 왼쪽이므로 정반대방향이다. (k + 3) % 4
        # R : 오른쪽이므로 정방향이다. (k + 1) % 4
        if grid[r][c] == 'R':
            k = (k + 1) % 4
        else:
            k = (k + 3) % 4
        cnt += 1
    return cnt


def solution(grid):
    answer = []
    row = len(grid)
    col = len(grid[0])
    # 행열 상하좌우
    field = [[[0, 0, 0, 0] for _ in range(col)] for _ in range(row)]

    # 행열 좌표의 상하좌우로 지나가지 않은 곳이 있는지 체크한다.
    for r in range(row):
        for c in range(col):
            for k in range(4):
                # 아직 방문하지 않은 곳이라면
                if not field[r][c][k]:
                    answer.append(bfs(r, c, k, grid, field))

    return answer

solution(["R","R"])