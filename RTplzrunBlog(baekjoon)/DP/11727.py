n = int(input())

dp = [0] * (n + 1)

for idx in range(1, n + 1):
    if idx == 1:
        dp[idx] = 1
    elif idx == 2:
        dp[idx] = 3
    else:
        dp[idx] = (dp[idx -1] % 10007 + dp[idx - 2] * 2 % 10007) % 10007

print(dp[n])