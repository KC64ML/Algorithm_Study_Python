n = int(input())

dp = [0] * (n + 1)

dp[1] = 1

if n >= 2:
    dp[2] = 1

    for idx in range(3, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]

print(dp[n])