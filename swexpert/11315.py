t = int(input())

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

for i in range(1, t + 1):
    n = int(input())
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    graph = []
    answer = 'NO'
    for _ in range(n):
        graph.append(list(input().rstrip()))

    for row in range(n):
        for col in range(n):
            if graph[row][col] == 'o':
                for d in range(4):
                    r = row
                    c = col
                    # 각 방향으로 연속적으로 오목이 존재하는가?
                    cnt = 0
                    # 파이썬만 0 <= r <= N-1 허용
                    # 다른 언어는 r >= 0 and r <= N-1
                    while 0 <= r <= n - 1 and 0 <= c <= n - 1 and graph[r][c] == 'o':
                        cnt += 1
                        r += dx[d]
                        c += dy[d]
                    # 각 방향으로 오목이 존재?하는가
                    if cnt >= 5:
                        answer = 'YES'
                        break

            if answer == 'YES':
                break
        if answer == 'YES':
            break

    print("#{} {}".format(i, answer))
