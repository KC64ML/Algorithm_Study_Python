# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     list_array = []
#     dp = [[0] * (n) for _ in range(2)]
#
#     for _ in range(2):
#         list_array.append(list(map(int, input().split())))
#
#     dp[0][0] = list_array[0][0]
#     dp[1][0] = list_array[1][0]
#
#     for j in range(1, n):
#         for i in range(2):
#             if i == 1:
#                 cur_i = 0
#             else:
#                 cur_i = 1
#
#             if j == 1:
#                 # print("i, j", i, j, "결과 : ", dp[cur_i][j - 1])
#                 dp[i][j] = dp[cur_i][j - 1] + list_array[i][j]
#             else:
#                 # print("i, j", i, j, "결과 : ", dp[cur_i][j - 2], dp[cur_i][j - 1])
#                 cur_data = max(dp[cur_i][j - 2], dp[cur_i][j - 1]) + list_array[i][j]
#                 if cur_data > dp[i][j]:
#                     dp[i][j] = cur_data
#
#     zero = max(dp[0])
#     one = max(dp[1])
#
#     print(max(zero, one))
#

t = int(input())
for i in range(t):
  s = []
  n = int(input())
  for k in range(2):
    s.append(list(map(int, input().split())))
  for j in range(1, n):
    if j == 1:
      s[0][j] += s[1][j - 1]
      s[1][j] += s[0][j - 1]
    else:
      s[0][j] += max(s[1][j - 1], s[1][j - 2])
      s[1][j] += max(s[0][j - 1], s[0][j - 2])
  print(max(s[0][n - 1], s[1][n - 1]))