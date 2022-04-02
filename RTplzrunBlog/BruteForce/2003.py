import sys

read = sys.stdin.readline

n, m = map(int, read().split())

arr = list(map(int, read().split()))

cnt = 0

for i in range(n):
    if arr[i] > m:
        continue
    for j in range(i, n):
        cur_result = sum(arr[i:j+1])

        if cur_result > m:
            break
        elif cur_result == m:
            cnt += 1

print(cnt)