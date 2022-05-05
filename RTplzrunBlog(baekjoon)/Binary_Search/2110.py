import sys

INF = 1e9

read = sys.stdin.readline

n, c = map(int, read().split())

arr = []
answer = 0

for _ in range(n):
    arr.append(int(read()))

arr.sort()

start, end = 1, arr[-1] - arr[0]

while start <= end:
    mid = (start + end) // 2

    count = 1
    cur_house = arr[0]  # 시작점
    for i in range(1, n):
        if cur_house + mid <= arr[i]:
            count += 1
            cur_house = arr[i]

    if count >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
