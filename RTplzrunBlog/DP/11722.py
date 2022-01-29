import sys

n = int(sys.stdin.readline())

dp = [1] * n

arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(i+1):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
