t = int(input())

while t > 0:
    n = int(input())
    dp = [0] * (n + 1)

    for idx in range(1, n+1):
        if idx == 1:
            dp[idx] = 1
        elif idx == 2:
            dp[idx] = 2
        elif idx == 3:
            dp[idx] = 4
        else:
            dp[idx] = dp[idx - 1] + dp[idx - 2] + dp[idx - 3]

    t -= 1
    print(dp[n])


