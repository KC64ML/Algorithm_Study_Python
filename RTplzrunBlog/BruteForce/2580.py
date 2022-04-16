import sys

# 경우의 수 : 상하 좌우, 현재위치부터 3x3방면
# 현재 0인 위치를 찾고, 백트래킹을 적용한다.


read = sys.stdin.readline

# 먼저 배열을 입력받는다.
# 입력받고 나서 만약 위치가 0인 것들의 위치를 저장한다.
sku_arr = [list(map(int, read().split())) for _ in range(9)]
zero_arr = [(i, j) for i in range(9) for j in range(9) if sku_arr[i][j] == 0]


# get_reference 함수
# (1) row_zero 행을 기준으로 0의 위치를 찾는다.
# (2) col_zero 열을 기준으로 0의 위치를 찾는다.
# (1) - (2) 로 공통적이지 않는 곳을 찾는다.
# (3) 3 x 3 으로 0의 위치를 찾는다.
# (1) - (2) - (3) 으로 공통적이지 않는 숫자를 찾는다.
# 결과를 return 한다.

def get_loc_value(r, c):
    possible = set(range(1, 10))
    possible -= set(sku_arr[r])

    col_zero = set()

    for i in range(9):
        col_zero.add(sku_arr[i][c])

    possible -= col_zero

    in_zero = set()
    # 3 x 3
    for i in range(r // 3 * 3, r // 3 * 3 + 3):
        for j in range(c // 3 * 3, c // 3 * 3 + 3):
            in_zero.add(sku_arr[i][j])
    possible -= in_zero

    return tuple(possible)


# 해결책 함수 0의 개수 0개부터 시작한다.
# 만약 갯수가 총 0의 개수일 때는 출력하고 종료한다.
# 0의 개수로 0인 것들의 배열로 부터 데이터를 받는다. r, c
# get_reference 함수를 호출한다.
# 결과를 받아서
# 반복문을 돌린다.
# 그래프 r, c 좌표에 결과를 저장하며
# 다시, 해결책 함수에 현재 개수 + 1을 한다.
# 해결책 함수 종료될 시 r, c 좌표 값은 0으로 바꾼다.

def solve(cnt):
    if cnt == len(zero_arr):
        [print(*row) for row in sku_arr]
        sys.exit()
    r, c = zero_arr[cnt]
    permission = get_loc_value(r, c)

    for cur_data in permission:
        sku_arr[r][c] = cur_data
        solve(cnt + 1)
        sku_arr[r][c] = 0


solve(0)
