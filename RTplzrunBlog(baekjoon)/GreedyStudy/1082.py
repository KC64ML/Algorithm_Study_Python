# 참고 사이트 : https://comdolidol-i.tistory.com/284


import sys

read = sys.stdin.readline

n = int(read())

room = list(map(int, read().split()))
m = int(read())

dp = [-sys.maxsize] * (m + 1)

for i in range(n - 1, -1, -1):
    x = room[i]
    for j in range(x, m + 1):
        # dp[j - x] * 10, 이전에 구한 dp 값 [j-x] * 10
        # i는 방번호
        # dp[j] : 이전에 구한 dp 값
        dp[j] = max(dp[j - x] * 10 + i, i, dp[j])

print(dp[m])
