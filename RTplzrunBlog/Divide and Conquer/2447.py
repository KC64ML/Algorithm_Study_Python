import sys

sys.setrecursionlimit(2 ** 8)

read = sys.stdin.readline

n = int(read())

# 빈 배열을 생성한다.
# 초기 값은 빈 공간으로 준다.
pattern = [[' '] * n for _ in range(n)]


# 시작 점 (0, 0, n)을 준다.
# -- recursion 함수 --
# 매개변수 (x, y, multiple)
# multiple : 3의 배수
def recursion(cur_x, cur_y, cur_n):
    # 만약, multiple가 1이라면 현재 위치는 *를 찍는 공간이다.
    if cur_n == 1:
        pattern[cur_x][cur_y] = "*"
        return

    # 아니라면, 다음 차례를 위해 multiple을 3으로 나누어 다음 차례 3의 배수 값을 얻는다.
    cur_n //= 3

    # 이제 for문을 돌리는데 패턴 구간을 돌린다. x, y좌표로 문제에 나와있는 패턴 처럼
    # i : 0 ~ 2까지, j : 0 ~ 2까지
    # 만약 (1, 1)은 비워야 하는 점이기에 패스하고 나머지는 재귀함수를 돌린다.
    # 재귀 (x + (i * 3으로 나눈 muliple), y + (j * 3으로 나눈 muliple), 3으로 나눈 multiple)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                recursion(cur_x + (i * cur_n), cur_y + (j * cur_n), cur_n)


# -- recursion 함수 --
recursion(0, 0, n)

# 이제 출력을 한다.행렬로 출력을 한다.
for in_pattern in pattern:
    print(''.join(map(str, in_pattern)))
