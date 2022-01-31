# n = int(input())
#
# arr = []
#
# for _ in range(n):
#     arr.append(int(input()))
#
# dp = [[0] * 2 for _ in range(n)]
#
#
# dp[n-1][0] = arr[n-1]
# dp[n-1][1] = 0
#
# if n >= 2:
#     dp[n-2][0] = 0
#     dp[n-2][1] = dp[n-1][0] + arr[n-2]
#
#     for idx in range(n-3, -1, -1):
#         if idx == (n-3):
#             dp[idx][0] = dp[idx+2][0] + arr[idx]
#             dp[idx][1] = 0
#         else:
#             dp[idx][0] = max(dp[idx+2][0], dp[idx+2][1]) + arr[idx]
#             dp[idx][1] = dp[idx+1][0] + arr[idx]
#
# if n == 1:
#     print(max(dp[0]))
# else:
#     print(max(max(dp[0]), max(dp[1])))



# 참고 소스 : https://www.acmicpc.net/source/26038889

import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)
num = [0] * (n+1)
for i in range(1,n+1):
    num[i] = int(input())


for i in range(1,n+1):
    if i == 1:
        d[i] = num[i]
    elif i == 2:
        d[i] = max(num[i],d[i-1] + num[i])
    else:
        d[i] = max(num[i] + num[i-1] + d[i-3], num[i] + d[i-2])

print(d[n])