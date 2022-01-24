n = int(input())
INF = 10007

dp = [[0] * 10 for _ in range(n + 1)]

dp[n] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


for i in range(n-1, -1, -1):
    for j in range(0, 10):
        cur_data = 0
        for z in range(j, 10):
            cur_data += dp[i+1][z]
            cur_data %= INF
        dp[i][j] = cur_data


print(dp[0][0])


# 참고 https://www.acmicpc.net/source/16076606