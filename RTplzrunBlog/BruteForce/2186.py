import sys
from collections import deque

x_coordinate = [-1, 0, 1, 0]
y_coordinate = [0, 1, 0, -1]

read = sys.stdin.readline

n, m, k = map(int, read().split())

arr = []

for i in range(n):
    arr.append(list(map(str, read().strip())))

find_data = list(map(str, read().strip()))


def dfs(cur_x, cur_y, cur_data_idx):
    # 만약 현재 찾는 인덱스가 문자열 길이보다 클 경우
    if cur_data_idx == len(find_data):
        return 1
    # 현재 방문한 곳이라면 종료
    if arr_result_space[cur_x][cur_y][cur_data_idx] != -1:
        return arr_result_space[cur_x][cur_y][cur_data_idx]

    arr_result_space[cur_x][cur_y][cur_data_idx] = 0
    for i in range(4):
        for k_idx in range(1, k + 1):
            next_x = x_coordinate[i] * k_idx + cur_x
            next_y = y_coordinate[i] * k_idx + cur_y

            if 0 <= next_x < n and 0 <= next_y < m:
                if find_data[cur_data_idx] == arr[next_x][next_y]:
                    arr_result_space[cur_x][cur_y][cur_data_idx] += dfs(next_x, next_y, cur_data_idx + 1)
    return arr_result_space[cur_x][cur_y][cur_data_idx]


result = 0

arr_result_space = [[[-1] * len(find_data) for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == find_data[0]:
            result += dfs(i, j, 1)

print(result)
