import sys

read = sys.stdin.readline

n, k = map(int, read().split())

arr = list(map(int, read().split()))

s = [0] * (n + 1)

for i in range(n - 1):
    s[i] = arr[i + 1] - arr[i]

s.sort(reverse=True)

answer = 0

for i in range(k - 1, n):
    answer += s[i]

print(answer)
