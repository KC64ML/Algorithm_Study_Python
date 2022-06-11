import sys

read = sys.stdin.readline

n = int(read())

arr = []

for i in range(n):
    a, b = map(int, read().split())
    arr.append([a, b])

arr.sort()

answer = float(1e9)
start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    left = 0
    right = 0

    for i in range(mid+1):
        left += arr[i][1]

    for i in range(mid+1, n):
        right += arr[i][1]

    if left < right:
        start = mid + 1
    else:
        end = mid - 1
        answer = min(answer, arr[mid][0])

print(answer)



