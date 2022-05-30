import sys

read = sys.stdin.readline

t = int(read())

arr = []

for _ in range(t):
    arr.append(int(read()))

dp = [0] * (max(arr) + 1)

for idx in range(1, max(arr)+1):
    if idx == 1:
        dp[idx] = 1
    elif idx == 2:
        dp[idx] = 2
    elif idx == 3:
        dp[idx] = 4
    else:
        dp[idx] = dp[idx - 1] + dp[idx - 2] + dp[idx - 3]

for num in arr:
    print(dp[num])



