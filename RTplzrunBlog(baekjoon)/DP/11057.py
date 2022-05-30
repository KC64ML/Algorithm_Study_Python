# n = int(input())
# INF = 10007
#
# dp = [[0] * 10 for _ in range(n + 1)]
#
# dp[n] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#
#
# for i in range(n-1, -1, -1):
#     for j in range(0, 10):
#         cur_data = 0
#         for z in range(j, 10):
#             cur_data += dp[i+1][z]
#             cur_data %= INF
#         dp[i][j] = cur_data
#
#
# print(dp[0][0])


# 참고 https://www.acmicpc.net/source/16076606


n = int(input())

arr = [[0] * 10 for _ in range(n + 2)]

# n + 1번째의 0번째 값이 이전 n 번째까지 구한 총합이 된다.
for i in range(0, n + 2):
    arr[i][9] = 1

for i in range(1, n + 2):
    for j in range(8, -1, -1):
        arr[i][j] = arr[i][j + 1] + arr[i - 1][j]

print(arr[n + 1][0] % 10007)

