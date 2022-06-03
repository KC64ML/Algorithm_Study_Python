import sys

read = sys.stdin.readline

n, m = map(int, read().split())

man = list(map(int, read().split()))
woman = list(map(int, read().split()))

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j-1] + abs(man[i-1] - woman[j-1])
        if i > j:
            dp[i][j] = min(dp[i-1][j], dp[i][j])
        elif i < j:
            dp[i][j] = min(dp[i][j-1], dp[i][j])

print(dp[n][m])
