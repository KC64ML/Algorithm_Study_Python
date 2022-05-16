import sys

read = sys.stdin.readline

n = int(read())

village = []

for _ in range(n):
    a, b = map(int, read().split())
    village.append((a, b))

village.sort()

start = 0
end = n

answer = float(1e9)

while start <= end:
    mid = (start + end) // 2
    left = 0
    right = 0

    for i in range(0, mid+1):
        left += village[i][1]

    for i in range(mid + 1, n):
        right += village[i][1]

    if left < right:
        start = mid + 1
    else:
        end = mid - 1
        answer = min(answer, village[mid][0])

print(answer)
