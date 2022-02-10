# https://hongjw1938.tistory.com/63

import sys

n, k = map(int, sys.stdin.readline().split())

INF = 1e9

dp = [[0] * (n + 1) for _ in range(k + 1)]


for k_idx in range(1, k + 1):
    for n_idx in range(n + 1):
        if k_idx == 1:
            dp[k_idx][n_idx] = 1
        else:
            # print("k_idx - 1 : ", k_idx - 1, " n_idx + 1 : ", n_idx + 1)
            dp[k_idx][n_idx] += sum(dp[k_idx - 1][:n_idx + 1])

print(dp[k][n] % 1000000000)
