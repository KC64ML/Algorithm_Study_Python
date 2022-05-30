import sys

read = sys.stdin.readline
n = int(read())

mat = [[' '] * 6660 for _ in range(6660)]


def solve(y, x, num):
    if num == 1:
        mat[x][y] = '*'
        return

    div = num // 3

    for i in range(0, 3):
        for j in range(0, 3):
            if i == 1 and j == 1:
                continue
            else:
                solve(y + (i * div), x + (j * div), div)
# i * div란 현재 3의 배수 값에서, 위치만큼 곱해준다.

solve(0, 0, n)

for i in range(n):
    for j in range(n):
        print(mat[i][j], end="")
    print()


# https://study-all-night.tistory.com/5
# 소스 이해하기