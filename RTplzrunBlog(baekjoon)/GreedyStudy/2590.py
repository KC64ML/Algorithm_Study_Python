import sys

read = sys.stdin.readline

arr = [0] * 7

for i in range(1, 7):
    arr[i] = int(read())

answer = 0

# (1) 길이가 6인 정사각형 필요 갯수
answer += arr[6]

# (2) 길이가 5인 정사각형 필요 갯수
while arr[5]:
    res = 36 - (5 * 5)
    arr[5] -= 1
    arr[1] = max(arr[1]-res, 0)
    answer += 1

# (3) 길이가 4인 정사각형 필요 갯수
while arr[4]:
    res = 36 - (4 * 4)
    res -= min(arr[2], 5) * 4
    arr[2] = max(arr[2]-5, 0)
    arr[1] = max(arr[1] - res, 0)
    arr[4] -= 1
    answer += 1

# (4) 길이가 3인 정사각형 필요 갯수
while arr[3]:
    res = 36 - 9 * min(arr[3], 4)

    if arr[3] >= 4:
        res = 0
        arr[3] -= 4
    elif arr[3] == 3:
        res -= min(arr[2], 1) * 4
        arr[3] -= 3
        arr[2] = max(arr[2]-1,0)
    elif arr[3] == 2:
        res -= min(arr[2], 3) * 4
        arr[3] -= 2
        arr[2] = max(arr[2] - 3, 0)
    else:
        res -= min(arr[2], 5) * 4
        arr[3] -= 1
        arr[2] = max(arr[2] - 5, 0)

    arr[1] = max(arr[1] - res, 0)
    answer += 1

# (5) 길이가 2인 정사각형 필요 갯수
while arr[2]:
    res = 36 - 4 * min(arr[2], 9)
    arr[2] = max(arr[2] - 9, 0)
    arr[1] = max(arr[1] - res, 0)
    answer += 1

# (6) 길이가 1인 정사각형 필요 갯수
while arr[1]:
    arr[1] = max(0, arr[1] - 36)
    answer += 1

print(answer)
