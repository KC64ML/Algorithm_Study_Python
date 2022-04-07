import sys

read = sys.stdin.readline

n = int(read())

board = [list(map(int, read().split())) for _ in range(n)]

array = [0] * 3


def dfs(x, y, n):
    global array

    num_check = board[x][y]
    # 위의 구간 두개의 for문 돌리면서 현재 시작점과 해당 위치 구간 값이 다르다면 재귀호출
    # print()
    # print("현재 x, y, n", x, y, n)
    for i in range(x, x + n):
        for j in range(y, y + n):
            # print("i, j", i, j, "board : ", board[i][j], "num_check: ", num_check, "N : ", n)
            if board[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        # print("i, j 결과", i, j)
                        # print("k, l 결과",k,l)
                        dfs(x + k * n // 3, y + l * n // 3, n // 3)
                        # print("dfs 종료")
                        # 위 반복문 두 개는 이제 해당 구간안에서 9개 구간을 재귀호출한다.
                return

    # 해당 좌표 값이 -1, 0, 1 인 경우

    if num_check == -1:
        array[0] += 1
    elif num_check == 0:
        array[1] += 1
    else:
        array[2] += 1


dfs(0, 0, n)

print("\n".join(map(str, array)))
