import sys

read = sys.stdin.readline

n = int(read())

answer = 0
dp = [0] * 100001
if n == 1:
    print(-1)
else:
    if n % 5 == 0:
        answer = n // 5
    else:
        dp[1] = -1
        dp[2] = 1
        dp[3] = -1
        dp[4] = 2
        dp[5] = 1
        dp[6] = 3
        dp[7] = 2
        dp[8] = 4
        for i in range(9, n+1):
            dp[i] = min(dp[i-2], dp[i-5]) + 1

        answer = dp[n]
    print(answer)
